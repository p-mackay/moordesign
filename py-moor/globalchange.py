# Generated with SMOP  0.41-beta
from libsmop import *
# globalchange.m

    
@function
def globalchange(command=None,parameter=None,*args,**kwargs):
    varargin = globalchange.varargin
    nargin = globalchange.nargin

    # Program for modifying all of one type of mooring component
    
    global U,V,W,z,rho
    global H,B,Cd,ME,moorele,Z
    global floats,wires,chains,acrels,cms,anchors,miscs,format
    global handle_list2,typelist2,type2,list2,elenum2,complist2
    global change,comp,moortally,components
    global fs
    if isempty(moorele):
        disp('You must have a mooring loaded to modify.')
        return
    
    if command != 0:
        h_menu_elenum2=handle_list2(1)
# globalchange.m:17
        h_menu_type2=handle_list2(2)
# globalchange.m:18
        h_menu_list2=handle_list2(3)
# globalchange.m:19
    
    if command == 0:
        mm,mn=size(moorele,nargout=2)
# globalchange.m:23
        if mm > 1:
            icnt=1
# globalchange.m:25
            moortally[icnt,arange(1,2)]=concat([1,1])
# globalchange.m:26
            components='1234567890123456'
# globalchange.m:27
            comp=copy(components)
# globalchange.m:28
            typelist2=copy(comp)
# globalchange.m:29
            list2=copy(comp)
# globalchange.m:30
            for el in arange(2,mm).reshape(-1):
                icnt0=copy(icnt)
# globalchange.m:32
                ifound=0
# globalchange.m:33
                for j in arange(1,icnt0).reshape(-1):
                    if strcmp(moorele(moortally(j,1),arange()),moorele(el,arange())) == 1:
                        moortally[j,2]=moortally(j,2) + 1
# globalchange.m:36
                        ifound=1
# globalchange.m:37
                if ifound == 0:
                    icnt=icnt + 1
# globalchange.m:41
                    moortally[icnt,arange(1,2)]=concat([el,1])
# globalchange.m:42
            moortally=moortally(arange(1,icnt),arange())
# globalchange.m:45
            mt,nt=size(moortally,nargout=2)
# globalchange.m:46
            for i in arange(1,mt).reshape(-1):
                components[i,arange()]=moorele(moortally(i,1),arange())
# globalchange.m:48
            me,ne=size(components,nargout=2)
# globalchange.m:50
            for ii in arange(1,me).reshape(-1):
                complist[arange((dot((ii - 1),17) + 1),(dot((ii - 1),17) + 17))]=concat([components(ii,arange(1,16)),'|'])
# globalchange.m:52
            complist=complist(arange(1,length(complist) - 1))
# globalchange.m:54
        else:
            disp('There is only one element. Use the Modify Mooring routine.')
            return
    
    
    if command == 0:
        if logical_not(exist('elen')):
            elenum2=1
# globalchange.m:64
            change=0
# globalchange.m:65
        comp=components(elenum2,arange())
# globalchange.m:67
        list2=copy(floats)
# globalchange.m:68
        type2=1
# globalchange.m:69
        me,ne=size(list2,nargout=2)
# globalchange.m:70
        for ii in arange(1,me).reshape(-1):
            typelist2[arange((dot((ii - 1),17) + 1),(dot((ii - 1),17) + 17))]=concat([list2(ii,arange(1,16)),'|'])
# globalchange.m:72
        typelist2=typelist2(arange(1,length(typelist2) - 1))
# globalchange.m:74
        figure(3)
        clf
        set(gcf,'Units','Normalized','Position',concat([0.325,0.05,0.3,0.2]),'Name','Global Change of Component','Color',concat([0.8,0.8,0.8]),'tag','globalchange')
        title1=uicontrol('Style','text','String','Change All','FontSize',fs,'Units','normalized','Position',concat([0.1,0.8,0.35,0.125]))
# globalchange.m:81
        h_menu_elenum2=uicontrol('Style','popupmenu','Callback','globalchange(1)','String',complist,'FontSize',fs,'Units','Normalized','Position',concat([0.5,0.8,0.45,0.125]))
# globalchange.m:85
        titleto=uicontrol('Style','text','String','To','FontSize',fs,'Units','normalized','Position',concat([0.425,0.625,0.1,0.125]))
# globalchange.m:90
        title2=uicontrol('Style','text','String','Type','FontSize',fs,'Units','normalized','Position',concat([0.2,0.5,0.2,0.125]))
# globalchange.m:94
        h_menu_type2=uicontrol('Style','popupmenu','Callback','globalchange(2)','FontSize',fs,'String',concat(['Floatation|Wire|Chain+Shackles|Current Meter|Acoustic Release|Anchor|Misc Instrument']),'Units','Normalized','Position',concat([0.1,0.3,0.35,0.125]))
# globalchange.m:98
        title3=uicontrol('Style','text','String','Component','FontSize',fs,'Units','normalized','Position',concat([0.55,0.5,0.3,0.125]))
# globalchange.m:103
        h_menu_list2=uicontrol('Style','popupmenu','Callback','globalchange(3)','String',typelist2,'FontSize',fs,'Units','Normalized','Position',concat([0.5,0.3,0.45,0.125]))
# globalchange.m:107
        h_push_change=uicontrol('Style','pushbutton','Callback','globalchange(4)','String','Change','FontSize',fs,'Units','Normalized','Position',concat([0.1,0.1,0.2,0.125]))
# globalchange.m:112
        h_push_disp=uicontrol('Style','pushbutton','Callback','dismoor','String','Display Elements','FontSize',fs,'Units','Normalized','Position',concat([0.325,0.1,0.35,0.125]))
# globalchange.m:117
        h_close_change=uicontrol('Style','Pushbutton','String','Close','FontSize',fs,'Units','normalized','Position',concat([0.7,0.1,0.2,0.125]),'Callback','globalchange(6)')
# globalchange.m:122
        set(gcf,'userdata',handle_list2)
    else:
        if command == 1:
            elenum2=get(h_menu_elenum2,'Value')
# globalchange.m:129
            complist2='1234567890123456'
# globalchange.m:130
            complist2=components(elenum2,arange())
# globalchange.m:131
        else:
            if command == 2:
                clear('typelist2')
                type2=get(h_menu_type2,'Value')
# globalchange.m:134
                if type2 == 1:
                    list2=copy(floats)
# globalchange.m:136
                else:
                    if type2 == 2:
                        list2=copy(wires)
# globalchange.m:138
                    else:
                        if type2 == 3:
                            list2=copy(chains)
# globalchange.m:140
                        else:
                            if type2 == 4:
                                list2=copy(cms)
# globalchange.m:142
                            else:
                                if type2 == 5:
                                    list2=copy(acrels)
# globalchange.m:144
                                else:
                                    if type2 == 6:
                                        list2=copy(anchors)
# globalchange.m:146
                                    else:
                                        if type2 == 7:
                                            list2=copy(miscs)
# globalchange.m:148
                me,ne=size(list2,nargout=2)
# globalchange.m:150
                for ii in arange(1,me).reshape(-1):
                    typelist2[arange((dot((ii - 1),17) + 1),(dot((ii - 1),17) + 17))]=concat([list2(ii,arange(1,16)),'|'])
# globalchange.m:152
                typelist2=typelist2(arange(1,length(typelist2)))
# globalchange.m:154
                set(h_menu_list2,'Value',1)
                set(h_menu_list2,'String',typelist2)
            else:
                if command == 3:
                    change=get(h_menu_list2,'Value')
# globalchange.m:158
                else:
                    if command == 4:
                        if change < logical_or(1,strcmp('12345',complist2(arange(1,5)))):
                            disp('You must select an item, even it is the default value displayed.')
                            break
                        # Need to find all element componets to replace, replace them
                        mm,mn=size(moorele,nargout=2)
# globalchange.m:167
                        icnt=0
# globalchange.m:168
                        for iele in arange(1,mm).reshape(-1):
                            if strcmp(complist2,moorele(iele,arange())):
                                icnt=icnt + 1
# globalchange.m:171
                                ele[icnt]=iele
# globalchange.m:172
                        disp(concat([' I will be replaceing ',num2str(icnt),' occurances of ',complist2]))
                        disp(concat([' with ',num2str(icnt),' occurances of ',list2(change,arange(format(1,1),format(1,2)))]))
                        for elen in ele.reshape(-1):
                            moorele[elen,arange()]=list2(change,arange(format(1,1),format(1,2)))
# globalchange.m:178
                            B[elen]=str2num(list2(change,arange(format(2,1),format(2,2))))
# globalchange.m:179
                            Hsave=copy(H)
# globalchange.m:180
                            H[1,elen]=str2num(list2(change,arange(format(3,1),format(3,2)))) / 100
# globalchange.m:181
                            H[2,elen]=str2num(list2(change,arange(format(4,1),format(4,2)))) / 100
# globalchange.m:182
                            H[3,elen]=str2num(list2(change,arange(format(5,1),format(5,2)))) / 100
# globalchange.m:183
                            H[4,elen]=0
# globalchange.m:184
                            ME[elen]=inf
# globalchange.m:185
                            if type2 == logical_or(2,type2) == 3:
                                if H(1,elen) == 1:
                                    H[1,elen]=Hsave(1,elen)
# globalchange.m:188
                                    H[4,elen]=1
# globalchange.m:189
                                    mat=str2num(list2(change,arange(format(7,1),format(7,2))))
# globalchange.m:190
                                    if mat == 1:
                                        ME[elen]=138000000000.0
# globalchange.m:192
                                    else:
                                        if mat == 2:
                                            ME[elen]=345000000.0
# globalchange.m:194
                                        else:
                                            if mat == 3:
                                                ME[elen]=690000000.0
# globalchange.m:196
                                            else:
                                                if mat == 4:
                                                    ME[elen]=345000000.0
# globalchange.m:198
                                                else:
                                                    if mat == 5:
                                                        ME[elen]=690000000.0
# globalchange.m:200
                                                    else:
                                                        if mat == 6:
                                                            ME[elen]=69000000000.0
# globalchange.m:202
                                                        else:
                                                            if mat == 7:
                                                                ME[elen]=76000000000.0
# globalchange.m:204
                                                            else:
                                                                if mat == 8:
                                                                    ME[elen]=100000000000.0
# globalchange.m:206
                                else:
                                    H[4,elen]=2
# globalchange.m:209
                            Cd[elen]=str2num(list2(change,arange(format(6,1),format(6,2))))
# globalchange.m:212
                        disp('Done.')
                        dismoor
                        close_(3)
                        modmoor(0)
                    else:
                        if command == 5:
                            dismoor
                        else:
                            if command == 6:
                                close_(3)
                                modmoor(0)
    
    handle_list2=concat([h_menu_elenum2,h_menu_type2,h_menu_list2])
# globalchange.m:224
    # fini