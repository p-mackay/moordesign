function [R] = getxlname()
    % Demonstrate how to make a custom dialog box which returns information.
    %
    % Example: 
    %          T = getxlname;  % T will be a string.
    %
    % Suggested exercise:  How would you modify this code so that the default
    % answer 'Enter Some Data' CANNOT be returned?
    %
    %
    % Author:  Matt Fig
    % Date:  1/15/2010

    bgcolor='#e8e8e8';
    R = [];  % In case the user closes the GUI.
    S.fh = figure('units','normalized',...
    'menubar','none',...
    'name','getxlname',...
    'numbertitle','off',...
    'Color',bgcolor);clf;axis off;
    ht = text (-.1,.9, '\color{red}*\color{black}Enter Name of New XLSX file: ',...
    'units', 'normalized', 'FontSize',15);    
    S.ed = uicontrol('style','edit',...
    'units','normalized',...
    'position',[.05 .72 .44 .08],...
    'string','.xlsx');
    S.pb = uicontrol('style','pushbutton',...
    'units','normalized',...
    'position',[.5 .72 .22 .08],...
    'string','Enter',...
    'callback',{@pb_call});
    ht1 = text (-.1,.5, '\color{red}*\color{black}Over-Write Existing XLSX file: ',...
    'units', 'normalized', 'FontSize',15);
    S.pb2 = uicontrol('style','pushbutton',...
    'units','normalized',...
    'position',[.05 .4 .22 .08],...
    'string','Browse Files',...
    'callback',{@pb2_call});
    uicontrol(S.ed)  % Make the editbox active.
    uiwait(S.fh)  % Prevent all other processes from starting until closed.

    function [] = pb_call(varargin)
        % Callback for the pushbutton.
        R = get(S.ed,'string');
        close(S.fh);  % Closes the GUI, allows the new R to be returned.
    endfunction
    function [] = pb2_call(varargin)
        [ifile,ipath]=uigetfile({'*.xlsx'},'Create New/Update Excel Data Base');
        R = [ipath ifile];
        close(S.fh);  % Closes the GUI, allows the new R to be returned.
    endfunction
endfunction




%figure(10);clf;drawnow;axis off;
%set(gcf,'menubar','none','Color',bgcolor);
%set(gcf, 'numbertitle','off');
%set(gcf,'name','Create New or Over-Write Data Base');
%
%ht = text (-.1,.9, '\color{red}*\color{black}Enter Name of New XLSX file: ',...
%'units', 'normalized', 'FontSize',15);    
%hu = uicontrol ('style', 'edit','string','', 'units', 'normalized',...
%'position', [.05,.72,.44,.08]);
%
%ht3 = text (.6,.6, '\bfOR ... ',...
%'units', 'normalized', 'FontSize',15);
%
%ht1 = text (-.1,.5, '\color{red}*\color{black}Over-Write Existing XLSX file: ',...
%'units', 'normalized', 'FontSize',15);
%hu1 = uicontrol ('style', 'pushbutton', 'units', 'normalized',...
%'String', 'Browse Files',...
%'FontSize',11,'backgroundcolor',bgcolor,...
%'position', [.05,.4,.44,.08]);
%hu1 = uicontrol ('Style', 'Pushbutton',...
%    %'String', 'Browse Files',...
%        %'FontSize',15,...
%            %'position', [.55,.5,.44,.08], ...
%                %'units','normalized',...
%                    %'backgroundcolor','#222222');
%                        file1 = get(hu, 'String');
%                            printf("%s \n", file1);gg=
























% Below is the exact same program, without the use of nested functions.

% function [R] = getxlname()
% % Get information from a GUI to the command line.
% % How to make a GUI that returns information to caller?
% % How to initialize the string as active in an editbox
% % Suggested exercise:  How would you modify this code so that the default
% % answer 'Enter Some Data' cannot be returned?
% R = [];
% S.fh = figure('units','pixels',...
%               'position',[500 500 200 130],...
%               'menubar','none',...
%               'name','getxlname',...  
%               'numbertitle','off',...
%               'resize','off');
% S.ed = uicontrol('style','edit',...
%                  'units','pix',...
%                 'position',[10 60 180 60],...
%                 'string','Data');
% S.pb = uicontrol('style','pushbutton',...
%                  'units','pix',...
%                 'position',[10 20 180 30],...
%                 'string','Push to Return Data');
% set(S.pb,'callback',{@pb_call,S})            
% waitfor(S.ed)
% 
% if ishandle(S.fh)
%     F = get(S.pb,'callback');
%     R = F{2}.R;
%     close(S.fh)
% end
% 
% 
% function [] = pb_call(varargin)
% S = varargin{3};
% S.R = get(S.ed,'string');
% set(S.pb,'callback',{@pb_call,S});
% delete(S.ed);

