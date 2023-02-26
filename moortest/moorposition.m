function moorposition(command)
% Enter range estimates froman acoustic release and plot/estimate 
% the postion and range of the acoustic release (mooring).

% RKD 9/98

global mpf latranges longranges ranges axislim
global fs

if nargin==0, command=0; end
if command == 0,
   figure(4);clf
   mpf=[];latranges=[];longranges=[];ranges=[];axislim=[];
   set(gcf,'Units', 'Normalized',...
      'Position',[.05 .02 .4 .3],...
      'Name','Mooring Position Rangeing',...
      'Color',[.8 .8 .8],...
      'tag','moorposition');
   h_push_enterran=uicontrol('Style','pushbutton',...
      'Callback','moorposition(1)',...
      'String','Enter/Edit Range Info','FontSize',fs,...
      'Units','normalized',...
      'Position',[.25 .85 .5 .1]);
   if ~isempty(ranges),
     h_push_plotran=uicontrol('Style','pushbutton',...
      'Callback','moorposition(2)','FontSize',fs,...
      'String','Plot/Estimate Mooring Position',...
      'Units','normalized',...
      'Position',[.2 .7 .6 .1]);
     h_push_saveran=uicontrol('Style','pushbutton',...
      'Callback','moorposition(3)',...
      'String','Save Ranges Data to a File','FontSize',fs,...
      'Units','normalized',...
      'Position',[.2 .2 .6 .1]);
   else
     h_push_loadran=uicontrol('Style','pushbutton',...
      'Callback','moorposition(4)',...
      'String','Load Ranges File','FontSize',fs,...
      'Units','normalized',...
      'Position',[.25 .35 .5 .1]);
   end
   h_help=uicontrol('Style','Pushbutton',...
      'String','Help','FontSize',fs,...
      'Units','normalized',...
      'Position',[.15 .03 .2 .125],...
      'Callback','moorposition(10)');
   h_close=uicontrol('Style','Pushbutton',...
      'String','Close','FontSize',fs,...
      'Units','normalized',...
      'Position',[.65 .03 .2 .125],...
      'Callback','moorposition(50)');
end
% plot help and close in all windows
%
if command == 4,
   [ifile,ipath]=uigetfile('*.mat','Load Existing Ranges File');
   if ifile~=0,
      load([ipath ifile]);
   end
   clear ifile ipath
   moorposition(0);
elseif command == 3,
   [ofile,opath]=uiputfile('*.mat','Save Range Data File');
   if ~isempty(ofile) & ~isempty(opath), 
      save([opath ofile],'latranges','longranges','ranges','axislim');
   end
   clear ofile opath
   moorposition(0);
elseif command == 1,
   figure(4);clf;
   h_push_latval=uicontrol('Style','pushbutton',...
           'Callback','moorposition(5)',...
           'String','Enter Latitude Values','FontSize',fs,...
           'Units','normalized',...
           'Position',[.25 .85 .5 .1]);
   h_push_longval=uicontrol('Style','pushbutton',...
           'Callback','moorposition(6)',...
           'String','Enter Longitude Values','FontSize',fs,...
           'Units','normalized',...
           'Position',[.25 .7 .5 .1]);
   h_push_ranval=uicontrol('Style','pushbutton',...
           'Callback','moorposition(7)',...
           'String','Enter Range Values','FontSize',fs,...
           'Units','normalized',...
           'Position',[.25 .55 .5 .1]);
   h_push_ransave=uicontrol('Style','pushbutton',...
           'Callback','moorposition(3)',...
           'String','Save Range Data','FontSize',fs,...
           'Units','normalized',...
           'Position',[.3 .4 .4 .1]);
   h_push_ranreturn=uicontrol('Style','pushbutton',...
           'Callback','moorposition(0)',...
           'String','Finish Data Entry','FontSize',fs,...
           'Units','normalized',...
           'Position',[.3 .25 .4 .1]);
	h_help=uicontrol('Style','Pushbutton',...
      'String','Help','FontSize',fs,...
      'Units','normalized',...
      'Position',[.15 .03 .2 .125],...
      'Callback','moorposition(10)');
	h_close=uicontrol('Style','Pushbutton',...
      'String','Close','FontSize',fs,...
      'Units','normalized',...
      'Position',[.65 .03 .2 .125],...
      'Callback','moorposition(50)');
end
if command==2,
   
   if length(ranges)==length(latranges) & length(ranges)==length(longranges)...
         & length(ranges) > 0, 
      % otherwise, there is insufficient range data
   if isempty(mpf), 
      mpf=figure;
   else
      figure(mpf);
   end
   clf;
%
   set(gca,'Visible','off');
   xlim=get(gca,'XLim');

   if xlim == [0 1],  % no figure yet.
      if isempty(axislim), axislim=[-180 180 -90 90]; end
      xlim=[axislim(1) axislim(2)];
      ylim=[axislim(3) axislim(4)];
   else
      ylim=get(gca,'YLim');
   end
   axislim=[xlim(1) xlim(2) ylim(1) ylim(2)];
   xmid=mean(xlim);ymid=mean(ylim);
   dlat=abs(ylim(2)-ylim(1));
   dlong=abs(xlim(2)-xlim(1));
   
   dsx=gcdist(ymid,xmid,ymid,xmid+1.0)*1000; % m per degree long
   dsy=gcdist(ymid-0.5,xmid,ymid+0.5,xmid)*1000;% km per degree lat
   ratio=abs(dsx*dlong/(dsy*dlat));  % this is the ratio of km in long vs lat.
%
   yoff=0;
   set(gca,'Box','on');
   xneg=1;
   if xlim(1) < 0 & xlim(2) <= 0,
      xlim=abs(xlim);
      axis([xlim(2) xlim(1) ylim(1) ylim(2)]);
      set(gca,'XDir','reverse');
      xneg=-1;
      xylim=[xlim(2) xlim(1) ylim(1) ylim(2)];
   else
      axis([xlim(1) xlim(2) ylim(1) ylim(2)]);
      xylim=[xlim(1) xlim(2) ylim(1) ylim(2)];
   end
%
   if ratio >= 1 % either way, make aspectratiomode manual
      set(gca,'PlotBoxAspectRatio',[1 1/ratio 1]);
   else
      set(gca,'PlotBoxAspectRatio',[ratio 1 1]);
   end
%
   fbox;  % draw nice box around figure
   axis(axis);
   hold on;
% Now restrict plot domain by patch thickness
   tkln=get(gca,'TickLength');
   dy=tkln(1)*abs(xylim(3)-xylim(4));
   dx=tkln(1)*abs(xylim(1)-xylim(2));
% now draw circles/spheres associated with each range estimate   
   nptslength(ranges);
	theta=[0:360];phi=[-90:0];
   for ip=1:npts,
      plot(xneg*longranges(ip),latranges(ip),'ro'),
      X(ip,:,:)=xneg*(longranges(ip)+(ranges(ip)/dsx)*cos(phi)*cos(theta));
      Y(ip,:,:)=latranges(ip)+(ranges(ip)/dsy)*cos(phi)*sin(theta);
      Z(ip,:,:)=ranges(ip)*sin(phi);
      figure;plot3(X,Y,Z);hold on
   end
   if npts > 1, % then find range to/position of intersection
      imin=0;
      for ip=1:npts-1,
         for ipp=ip+1:npts,
            imin=imin+1;
            Xmin(imin)=find(abs(X(ip,:,:))-X(ipp,:,:));
         end
      end
   end

   
   else % insufficient range data yet: must have lat, long and range
      moorposition(1);
   end

%
elseif command == 5,
   clf;
   if ~isempty(latranges),
      [ml,nl]=size(latranges);
      if mu==length(longranges),
         lat=num2str(latranges(:,1)');
      else
         lat=num2str(latranges(1,:));
      end
   end
   h_text_latitudes=uicontrol('Style','text',...
      'String','Enter Latitudes [degrees] at Range Points',...
      'Units','normalized','FontSize',fs,...
      'Position',[.05 .7 .3 .2]);
   h_edit_latitudes=uicontrol('Style','edit',...
      'Callback','moorposition(15)',...
      'String',lat,'FontSize',fs,...
      'Units','Normalized',...
      'Position',[.4 .7 .5 .2]);
   h_ok=uicontrol('Style','Pushbutton',...
      'String','OK','FontSize',fs,...
      'Units','normalized',...
      'Position',[.4 .25 .2 .2],...
      'Callback','moorposition(15)');
   h_help=uicontrol('Style','Pushbutton',...
      'String','Help','FontSize',fs,...
      'Units','normalized',...
      'Position',[.15 .03 .2 .15],...
      'Callback','moorposition(10)');
   h_close=uicontrol('Style','Pushbutton',...
      'String','Close','FontSize',fs,...
      'Units','normalized',...
      'Position',[.65 .03 .2 .15],...
      'Callback','moorposition(50)');
elseif command == 15,
   latranges=str2num(get(h_edit_latitudes,'String'));
   moorposition(1);
elseif command == 6,
   clf;
   if ~isempty(longranges),
      [ml,nl]=size(longranges);
      if mu==length(ranges),
         long=num2str(longranges(:,1)');
      else
         long=num2str(longranges(1,:));
      end
   end
   h_text_longitudes=uicontrol('Style','text',...
      'String','Enter Longitudes [degrees] at Range Points',...
      'Units','normalized','FontSize',fs,...
      'Position',[.05 .7 .3 .2]);
   h_edit_longitudes=uicontrol('Style','edit',...
      'Callback','moorposition(16)',...
      'String',long,'FontSize',fs,...
      'Units','Normalized',...
      'Position',[.4 .7 .5 .2]);
   h_ok=uicontrol('Style','Pushbutton',...
      'String','OK','FontSize',fs,...
      'Units','normalized',...
      'Position',[.4 .25 .2 .2],...
      'Callback','moorposition(16)');
   h_help=uicontrol('Style','Pushbutton',...
      'String','Help','FontSize',fs,...
      'Units','normalized',...
      'Position',[.15 .03 .2 .15],...
      'Callback','moorposition(10)');
   h_close=uicontrol('Style','Pushbutton',...
      'String','Close','FontSize',fs,...
      'Units','normalized',...
      'Position',[.65 .03 .2 .15],...
      'Callback','moorposition(50)');
elseif command == 16,
   longranges=str2num(get(h_edit_longitudes,'String'));
   moorposition(1);
elseif command == 7,
   clf;
   if ~isempty(ranges),
      [ml,nl]=size(ranges);
      if mu==length(latranges),
         range=num2str(ranges(:,1)');
      else
         range=num2str(ranges(1,:));
      end
   end
   h_text_ranges=uicontrol('Style','text',...
      'String','Enter Ranges [m] at Range Points',...
      'Units','normalized','FontSize',fs,...
      'Position',[.05 .7 .3 .2]);
   h_edit_ranges=uicontrol('Style','edit',...
      'Callback','moorposition(17)',...
      'String',range,'FontSize',fs,...
      'Units','Normalized',...
      'Position',[.4 .7 .5 .2]);
   h_ok=uicontrol('Style','Pushbutton',...
      'String','OK','FontSize',fs,...
      'Units','normalized',...
      'Position',[.4 .25 .2 .2],...
      'Callback','moorposition(17)');
   h_help=uicontrol('Style','Pushbutton',...
      'String','Help','FontSize',fs,...
      'Units','normalized',...
      'Position',[.15 .03 .2 .15],...
      'Callback','moorposition(10)');
   h_close=uicontrol('Style','Pushbutton',...
      'String','Close','FontSize',fs,...
      'Units','normalized',...
      'Position',[.65 .03 .2 .15],...
      'Callback','moorposition(50)');
elseif command == 17,
   ranges=str2num(get(h_edit_ranges,'String'));
   moorposition(1);
elseif command == 10,
   load positionhelp.mat
   h_positionhelp=msgbox(positionhelp);
   hpos=get(h_positionhelp,'Position');
   set(h_positionhelp,'Position',[hpos(1) 10 hpos(3) hpos(4)]);
   clear positionhelp
elseif command==50,
   close(4);
   moordesign(0);
end
% fini
