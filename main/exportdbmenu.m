function [] = exportdbmenu()

    bgcolor='#e8e8e8';
    S.fh = figure('units','pixels',...
    'position',[300 300 300 110],...
    'name','exportdbmenu',...
    'numbertitle', 'off',...
    'resize','off');%clf;drawnow;axis off;
    %set(gcf,'menubar','none','Color',bgcolor);
    %set(gcf, 'numbertitle','off');
    %set(gcf,'name','Create New or Over-Write Data Base');

    S.title = text (-.1,.9, '\color{red}*\color{black}Enter Name of New XLSX file: ',...
    'units', 'normalized', 'FontSize',15);    
    %edit1 = uicontrol ('style', 'edit','string','', 'units', 'normalized',...
    %'callback',@exportdbmenu2,...
    %'position', [.05,.72,.44,.08]);
    S.ed = uicontrol ('style', 'edit',...
    'position', [.05,.72,.44,.08]);

    set([S.ed,],{'callback'},{@ed_call,S});

    function [] = ed_call(varargin)
        S = varargin{3};
        E = get(S.ed, 'string');

    

    %ht3 = text (.6,.6, '\bfOR ... ',...
    %'units', 'normalized', 'FontSize',15);

    %ht1 = text (-.1,.5, '\color{red}*\color{black}Over-Write Existing XLSX file: ',...
    %'units', 'normalized', 'FontSize',15);
    %edit2 = uicontrol ('style', 'pushbutton', 'units', 'normalized',...
    %'String', 'Browse Files',...
    %'FontSize',11,'backgroundcolor',bgcolor,...
    %'callback',@exportdbmenu2, ...
    %'position', [.05,.4,.44,.08]);
