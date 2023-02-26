function moordesign(command);
% GUI Program to HELP design and evaluate an oceanographic mooring.
% Use: moordesign
%
% This program will ASSIST in the design and evaluation of oceanographic moorings
% in order to determine 1) wire tensions and anchor requirements, and
% 2) the anticipated depth and horizontal excursions of mooring elements
% forced by currents U(z) [V(z) W(z)], where V and W are optional. 
%
% Time varying currents can be fed to moordyn.m (the engine) by user written MATLAB
% code in order to simulate and even make movies of element positions.
% A preliminary data base of mooring components has been included (c/o C.Darnall of APL UW).
% Advanced users can add and modify the text mooring database (mdcodes.mat), which
% includes the component names, their buoyancy/mass [in kg], their dimensions 
%  (Length/height, Cylinder Width, Sphere Diameter, all in [m]), and Drag
%   Coefficients (0.65-0.95 for spheres, 1.1-1.3 for cylinders).
% The mooring motion/dynamics engine solves the 3-D wire tension problem 
% from the top of the mooring to the bottom (anchor). 
% Simple current profiles can be entered manually, more detailed current 
% profiles should be saved in user mat files: U(z) z [V(z) W(z)].
% Menu lay-out may varying depending on screen resolution/monitor size.
% Additional program help and use is documented in moordyn.txt
%
% No liability is assumed, and users of this code must take full responsability
% for actual mooring design and potential mooring damage and/or loss.
%
% R.Dewey, U.of Victoria, 12/97 

% Please forward improvements/suggestions/bugs to rdewey@uvic.ca
% The latest version of Mooring Dynamics is available at: ftp://canuck.seos.uvic.ca/
% This code has been tested on Windows 95, NT (4.0), and HP-UNIX, but is not idiot proof.

global U V W z rho time uw vw
global Xts Yts Zts Tits psits iobjts M figs   % these are time series variables
global H B Cd ME moorele
global X Y Z Ti iobj jobj psi
global Ht Bt Cdt MEt moorelet Usp Vsp DD
global fs

%
if nargin == 0,% initialize some variables
   H=[];B=[];Cd=[];ME=[];moorele=[];
   U=[];V=[];W=[];z=[];rho=[];time=[];uw=[];vw=[];
   M=[];Xts=[];Yts=[];Zts=[];Tits=[];psits=[];iobjts=[]; figs=[];
   X=[];Y=[];Z=[];Zoo=[];Ti=[];psi=[];iobj=[];jobj=[];
   Ht=[];Bt=[];Cdt=[];MEt=[];moorelet=[];Usp=[];Vsp=[];DD=[];
   command=0;
end
if command==2, % load a new mooring/towed body
   H=[];B=[];Cd=[];ME=[];moorele=[];
   U=[];V=[];W=[];z=[];rho=[];time=[];uw=[];vw=[];
   M=[];Xts=[];Yts=[];Zts=[];Tits=[];psits=[];iobjts=[]; figs=[];
   X=[];Y=[];Z=[];Zoo=[];Ti=[];psi=[];iobj=[];jobj=[];
   Ht=[];Bt=[];Cdt=[];MEt=[];moorelet=[];Usp=[];Vsp=[];DD=[];
end
%
fs=10;  % set the font size for your screen/viewing preferences
ss=get(0,'ScreenSize');
if ss(3) < 1024, fs=10; end
if ss(3) >= 1024, fs=11; end
if ss(3) > 1200, fs=12; end
%
if isempty(uw), uw=0;vw=0; end
%
figure(1);figname=get(1,'Name');
if strcmp(figname,'Mooring Design & Dynamics')==1,
   mmppathfile=which('mmposition.mat'); % Main Menu Position info
   mmp=get(1,'Position');
   save(mmppathfile,'mmp'); % save the main menu position, if the user has modified it.
end
%
mmppathfile=which('mmposition.mat'); % Main Menu Position info
if length(mmppathfile) >= 14,
   blank=0;for i=1:length(mmppathfile), if strcmp(' ',mmppathfile(i)),blank=1;end; end
   if blank==1, % if your path has blanks, load won't work!
      mmppathfile=[pwd,'\mmposition.mat'];
      mmp=[0.05 0.6 0.32 0.33];   
   else
      load(mmppathfile);
   end
else
   mmp=[0.05 0.6 0.32 0.33];
end
%
figure(1);clf;
set(gcf,'Units','Normalized',...
   'Position',mmp,...
   'Name','Mooring Design & Dynamics',...
   'Color',[.2 .6 .9]);
hmain1=uicontrol('Style','Pushbutton',...
   'String','Design New Mooring','FontSize',fs,...
   'Units','normalized',...
   'Position',[.05 .89 .44 .08],...
   'Callback','modmoor(-1)');
hmain11=uicontrol('Style','Pushbutton',...
   'String','Design Towed Body','FontSize',fs,...
   'Units','normalized',...
   'Position',[.51 .89 .44 .08],...
   'Callback','modtow(-1)');
if (~isempty(H) & ~isempty(moorele))|(~isempty(Ht) & ~isempty(moorelet)),
  hmain2=uicontrol('Style','Pushbutton','String',...
   'Load Existing Mooring/Tow','FontSize',fs,...
   'Units','normalized',...
   'Position',[.05 .79 .44 .08],...
   'Callback','moordesign(2)');
  hmain3=uicontrol('Style','Pushbutton','String',...
   'Save Mooring/Towed Body','FontSize',fs,...
   'Units','normalized',...
   'Position',[.51 .79 .44 .08],...
   'Callback','savemd');
  if isempty(Ht),
     hmain4=uicontrol('Style','Pushbutton','String',...
  	'Add/Modify In-Line Elements','FontSize',fs,...
   	'Units','normalized',...
   	'Position',[.05 .68 .44 .08],...
   	'Callback','modmoor(0)');
     hmain44=uicontrol('Style','Pushbutton','String',...
      'Add/Modify Clamp-On Devices','FontSize',fs,...
      'Units','normalized',...
      'Position',[.51 .68 .44 .08],...
      'Callback','modmoorCO(0)');
  else
     hmain4=uicontrol('Style','Pushbutton','String',...
   	'Add/Modify Towed Body','FontSize',fs,...
   	'Units','normalized',...
   	'Position',[.05 .68 .44 .08],...
   	'Callback','modtow(0)');
     hmain44=uicontrol('Style','Pushbutton','String',...
      'Add/Modify Clamp-On Devices','FontSize',fs,...
      'Units','normalized',...
      'Position',[.51 .68 .44 .08],...
      'Callback','modtowCO(0)');
  end
else
  hmain2=uicontrol('Style','Pushbutton','String',...
   'Load Existing Mooring','FontSize',fs,...
   'Units','normalized',...
   'Position',[.05 .79 .44 .08],...
   'Callback','moordesign(2)');
  hmain21=uicontrol('Style','Pushbutton','String',...
   'Load Existing Towed Body','FontSize',fs,...
   'Units','normalized',...
   'Position',[.51 .79 .44 .08],...
   'Callback','moordesign(2)');
end
if ~isempty(U) & ~isempty(z),
  hmain5=uicontrol('Style','Pushbutton','String',...
   'Set/Load Envir. Cond.','FontSize',fs,...
   'Units','normalized',...
   'Position',[.05 .57 .44 .08],...
   'Callback','getvelocity');
  hmain6=uicontrol('Style','Pushbutton','String',...
   'Display Currents/Ship Speed','FontSize',fs,...
   'Units','normalized',...
   'Position',[.51 .57 .44 .08],...
   'Callback','getvelocity(40)');
else
  hmain5=uicontrol('Style','Pushbutton','String',...
   'Set/Load Environmental Conditions','FontSize',fs,...
   'Units','normalized',...
   'Position',[.1 .57 .8 .08],...
   'Callback','getvelocity');
end
if (~isempty(H) & ~isempty(moorele))|(~isempty(Ht) & ~isempty(moorelet)), % once a moorings loaded
   hmain7=uicontrol('Style','Pushbutton','String',...
   'Evaluate and Plot 3-D Mooring/Towed Body','FontSize',fs,...
   'Units','normalized',...
   'Position',[.05 .43 .9 .12],...
   'Callback','mdplot',...
   'FontWeight','bold');
  if ~isempty(Z),
	   hmain8=uicontrol('Style','Pushbutton',...
	   'String','Display Positions & Tensions','FontSize',fs,...
	   'Units','normalized',...
	   'Position',[.025 .32 .475 .08],...
	   'Callback','dismoor(0)');
	   hmain9=uicontrol('Style','Pushbutton',...
	   'String','Print','FontSize',fs,...
	   'Units','normalized',...
	   'Position',[.5 .32 .1 .08],...
	   'Callback','dismoor(1)');
  else
	  hmain8=uicontrol('Style','Pushbutton',...
	   'String','Display Mooring Elements',...
	   'Units','normalized','FontSize',fs,...
	   'Position',[.05 .32 .425 .08],...
	   'Callback','dismoor(0)');
	  hmain9=uicontrol('Style','Pushbutton',...
	   'String','Print','FontSize',fs,...
	   'Units','normalized',...
	   'Position',[.475 .32 .1 .08],...
           'Callback','dismoor(1)');
  end
  if isempty(Ht),  % if this is a mooring, buttons to plot/print it
  		hmain8p=uicontrol('Style','Pushbutton',...
   	'String','Plot Mooring','FontSize',fs,...
   	'Units','normalized',...
   	'Position',[.625 .32 .225 .08],...
   	'Callback','plot_elements(0)');
  		hmain9p=uicontrol('Style','Pushbutton',...
   	'String','Print','FontSize',fs,...
   	'Units','normalized',...
   	'Position',[.85 .32 .1 .08],...
        'Callback','plot_elements(1)');
  else % if this is a towed body, button to find depth
  		hmain8p=uicontrol('Style','Pushbutton',...
   	'String','Enter Desired Depth [m]','FontSize',fs,...
   	'Units','normalized',...
   	'Position',[.625 .32 .325 .08],...
   	'Callback','getvelocity(47)');
  end
end
hmain10=uicontrol('Style','Pushbutton',...
   'String','Add/Examine Elements in Database',...
   'Units','normalized','FontSize',fs,...
   'Position',[.1 .21 .8 .08],...
   'Callback','addelement');
hmainclr=uicontrol('Style','Pushbutton',...
   'String','Clear All','FontSize',fs,...
   'Units','normalized',...
   'Position',[.1 .01 .2 .08],...
   'Callback','moordesign(1)');
hmain_whos=uicontrol('Style','Pushbutton',...
   'String','Whos','FontSize',fs,...
   'Units','normalized',...
   'Position',[.4 .01 .2 .08],...
   'Callback','whos global');
hmaincls=uicontrol('Style','Pushbutton',...
   'String','Close','FontSize',fs,...
   'Units','normalized',...
   'Position',[.7 .01 .2 .08],...
   'Callback','close all');
%
if command==1,
   mmp=get(1,'Position');
   mmppathfile=which('mmposition.mat'); % Main Menu Position info
   save(mmppathfile,'mmp'); % save the main menu position, if the user has modified it.
   clear all;
   close all;
   command=1;
   moordesign(0);
elseif command==2,
   loadmd;
   moordesign(100);
end
%
if command ~= 1,
if ~isempty(U),
   [mu,nu]=size(U);
   [mz,nz]=size(z);
   if mz==nu & nz~=mu,
      U=U';V=V';W=W';
   end
   [mu,nu]=size(U);
   if ~isempty(time),
    if length(time) == nu & nu > 1,
       if exist('M') | exist('Zts'),
          if isempty(M) & isempty(Zts),
              hmain11=uicontrol('Style','Pushbutton',...
                  'String','Make a Time Series','FontSize',fs,...
                  'Units','normalized',...
                  'Position',[.3 .12 .4 .08],...
                  'Callback','makemovie(0)');
          elseif ~isempty(M) | ~isempty(Zts),
              hmain11=uicontrol('Style','Pushbutton',...
                 'String','Make Movie','FontSize',fs,...
                 'Units','normalized',...
                 'Position',[.1 .12 .25 .08],...
                 'Callback','makemovie(0)');
              hmain12=uicontrol('Style','Pushbutton',...
                 'String','Save Movie','FontSize',fs,...
                 'Units','normalized',...
                 'Position',[.37 .12 .26 .08],...
                 'Callback','savemovie');
              if ~isempty(M),
                 hmain13=uicontrol('Style','Pushbutton',...
                     'String','Show Movie','FontSize',fs,...
                     'Units','normalized',...
                     'Position',[.65 .12 .25 .08],...
                     'Callback','makemovie(2)');
              end
          end
       end
    end
   end
else
   if ~isempty(M),
      hmain11=uicontrol('Style','Pushbutton',...
        'String','Load a Movie','FontSize',fs,...
        'Units','normalized',...
        'Position',[.1 .12 .35 .08],...
        'Callback','moordesign(2)'); 
      hmain13=uicontrol('Style','Pushbutton',...
        'String','Show Movie','FontSize',fs,...
        'Units','normalized',...
        'Position',[.55 .12 .35 .08],...
        'Callback','makemovie(2)');
   else
      hmain11=uicontrol('Style','Pushbutton',...
        'String','Load a Movie','FontSize',fs,...
        'Units','normalized',...
        'Position',[.3 .12 .4 .08],...
        'Callback','moordesign(2)'); 
   end
end
end
mmp=get(1,'Position');
mmppathfile=which('mmposition.mat'); % Main Menu Position info
save(mmppathfile,'mmp'); % save the main menu position, if the user has modified it.
% fini