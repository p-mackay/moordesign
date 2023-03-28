# Generated with SMOP  0.41-beta
from libsmop import *
# modmoorco.m

    
@function
def modmoorCO(command=None,parameter=None,*args,**kwargs):
    varargin = modmoorCO.varargin
    nargin = modmoorCO.nargin

    # Program to make a GUI for add/modifying clamp-on devices
    
    global U,V,W,z,rho
    global H,B,Cd,ME,moorele,Z
    global HCO,BCO,CdCO,mooreleCO,ZCO,Iobj,Jobj,Pobj
    global floats,wires,chains,acrels,cms,anchors,miscs,format,typelist,type_,list
    global handle_listCO,insertCO,heightCO,val,elenumCO
    global fs
    global Zoo
    if nargin == logical_or(0,command) <= 0:
        if command == logical_or(- 1,isempty(BCO)):
            HCO=[]
# modmoorco.m:14
            BCO=[]
# modmoorco.m:14
            CdCO=[]
# modmoorco.m:14
            mooreleCO='1234567890123456'
# modmoorco.m:15
            handle_listCO=[]
# modmoorco.m:16
        else:
            if command == 0:
                if logical_not(isempty(BCO)):
                    elenumCO=length(BCO) + 1
# modmoorco.m:19
                    deleleCO=0
# modmoorco.m:20
                    heightCO=0
# modmoorco.m:21
        typelist=' '
# modmoorco.m:24
        list=' '
# modmoorco.m:24
        command=0
# modmoorco.m:25
    
    Z=[]
# modmoorco.m:27
    
    Zoo=[]
# modmoorco.m:28
    if logical_not(isempty(handle_listCO)):
        h_edit_elenumCO=handle_listCO(1)
# modmoorco.m:30
        h_edit_deleleCO=handle_listCO(2)
# modmoorco.m:31
        h_menu_typeCO=handle_listCO(3)
# modmoorco.m:32
        h_menu_listCO=handle_listCO(4)
# modmoorco.m:33
        h_edit_heightCO=handle_listCO(5)
# modmoorco.m:34
    
    
    if isempty(floats):
        load('mdcodes')
    
    
    if command == 0:
        elenumCO=length(BCO) + 1
# modmoorco.m:40
        deleleCO=0
# modmoorco.m:41
        heightCO=0
# modmoorco.m:42
        list=copy(floats)
# modmoorco.m:43
        type_=1
# modmoorco.m:44
        me,ne=size(list,nargout=2)
# modmoorco.m:45
        for ii in arange(1,me).reshape(-1):
            typelist[arange((dot((ii - 1),17) + 1),(dot((ii - 1),17) + 17))]=concat([list(ii,arange(1,16)),'|'])
# modmoorco.m:47
        typelist=typelist(arange(1,length(typelist) - 1))
# modmoorco.m:49
        figure(2)
        clf
        set(gcf,'Units','Normalized','Position',concat([0.05,0.05,0.25,0.275]),'Name','Modify Clamp-On Devices','Color',concat([0.8,0.8,0.8]),'tag','modmoorCO')
        telenum=uicontrol('Style','text','String','Element to Clamp-On','FontSize',fs,'Units','normalized','Position',concat([0.1,0.88,0.55,0.1]))
# modmoorco.m:56
        h_edit_elenumCO=uicontrol('Style','edit','Callback','modmoorCO(1)','String',num2str(elenumCO),'FontSize',fs,'Units','Normalized','Position',concat([0.7,0.88,0.2,0.1]))
# modmoorco.m:60
        teleins=uicontrol('Style','text','String','Delete Clamp-On Element','FontSize',fs,'Units','normalized','Position',concat([0.1,0.76,0.55,0.1]))
# modmoorco.m:65
        h_edit_deleleCO=uicontrol('Style','edit','Callback','modmoorCO(2)','String',num2str(deleleCO),'FontSize',fs,'Units','Normalized','Position',concat([0.7,0.76,0.2,0.1]))
# modmoorco.m:69
        h_menu_typeCO=uicontrol('Style','popupmenu','Callback','modmoorCO(3)','FontSize',fs,'String',concat(['Floatation|Current Meter|Misc Instrument']),'Units','Normalized','Position',concat([0.1,0.64,0.8,0.1]))
# modmoorco.m:74
        h_menu_listCO=uicontrol('Style','popupmenu','Callback','modmoorCO(4)','String',typelist,'FontSize',fs,'Units','Normalized','Position',concat([0.1,0.52,0.8,0.1]))
# modmoorco.m:79
        telehght=uicontrol('Style','text','String','Height Above Bottom [m]','FontSize',fs,'Units','normalized','Position',concat([0.1,0.4,0.55,0.1]))
# modmoorco.m:84
        h_edit_heightCO=uicontrol('Style','edit','Callback','modmoorCO(11)','String',num2str(heightCO),'FontSize',fs,'Units','Normalized','Position',concat([0.7,0.4,0.2,0.1]))
# modmoorco.m:88
        h_push_file=uicontrol('Style','pushbutton','Callback','modmoorCO(88)','String','Load Different Database','FontSize',fs,'Units','Normalized','Position',concat([0.25,0.27,0.5,0.1]))
# modmoorco.m:93
        h_push_disp=uicontrol('Style','pushbutton','Callback','dismoor','String','Display Elements','FontSize',fs,'Units','Normalized','Position',concat([0.075,0.15,0.4,0.1]))
# modmoorco.m:98
        h_push_update=uicontrol('Style','Pushbutton','String','Execute Update','FontSize',fs,'Units','normalized','Position',concat([0.525,0.15,0.4,0.1]),'Callback','modmoorCO(5)')
# modmoorco.m:103
        hmaincls=uicontrol('Style','Pushbutton','String','Close','FontSize',fs,'Units','normalized','Position',concat([0.3,0.02,0.4,0.1]),'Callback','modmoorCO(6)')
# modmoorco.m:108
        handle_listCO=concat([h_edit_elenumCO,h_edit_deleleCO,h_menu_typeCO,h_menu_listCO,h_edit_heightCO])
# modmoorco.m:114
        set(gcf,'userdata',handle_listCO)
        insertCO=0
# modmoorco.m:121
    else:
        if command == 88:
            ifile,ipath=uigetfile('*.mat','Load Database File MDCODES.MAT (cancel loads default)',nargout=2)
# modmoorco.m:123
            if logical_and(ischar(ifile),ischar(ipath)):
                if logical_not(strcmp(ifile,'*.mat')):
                    load(concat([ipath,ifile]))
                else:
                    load('mdcodes')
            else:
                if ifile == logical_and(0,ipath) == 0:
                    load('mdcodes')
            clear('ifile','ipath')
            modmoorCO(0)
        else:
            if command == 1:
                insertCO=str2num(get(h_edit_elenumCO,'String'))
# modmoorco.m:136
            else:
                if command == 11:
                    heightCO=str2num(get(h_edit_heightCO,'String'))
# modmoorco.m:138
                else:
                    if command == 2:
                        deleleCO=str2num(get(h_edit_deleleCO,'String'))
# modmoorco.m:140
                        mb=length(BCO)
# modmoorco.m:141
                        if deleleCO <= mb:
                            if deleleCO == 1:
                                if mb > 1:
                                    BCO=BCO(arange(2,mb))
# modmoorco.m:145
                                    HCO=HCO(arange(),arange(2,mb))
# modmoorco.m:146
                                    CdCO=CdCO(arange(2,mb))
# modmoorco.m:147
                                    ZCO=ZCO(arange(2,mb))
# modmoorco.m:148
                                    mooreleCO=mooreleCO(arange(2,mb),arange())
# modmoorco.m:149
                                else:
                                    BCO=[]
# modmoorco.m:151
                                    HCO=[]
# modmoorco.m:151
                                    CdCO=[]
# modmoorco.m:151
                                    ZCO=[]
# modmoorco.m:151
                                    mooreleCO=[]
# modmoorco.m:151
                            else:
                                if deleleCO == mb:
                                    BCO=BCO(arange(1,(mb - 1)))
# modmoorco.m:154
                                    HCO=HCO(arange(),arange(1,(mb - 1)))
# modmoorco.m:155
                                    CdCO=CdCO(arange(1,(mb - 1)))
# modmoorco.m:156
                                    ZCO=ZCO(arange(1,(mb - 1)))
# modmoorco.m:157
                                    mooreleCO=mooreleCO(arange(1,(mb - 1)),arange())
# modmoorco.m:158
                                else:
                                    if deleleCO > logical_and(1,deleleCO) < mb:
                                        inew=concat([arange(1,deleleCO - 1),arange(deleleCO + 1,mb)])
# modmoorco.m:160
                                        BCO=BCO(inew)
# modmoorco.m:161
                                        HCO=HCO(arange(),inew)
# modmoorco.m:162
                                        CdCO=CdCO(inew)
# modmoorco.m:163
                                        ZCO=ZCO(inew)
# modmoorco.m:164
                                        mooreleCO=mooreleCO(inew,arange())
# modmoorco.m:165
                            Iojb=[]
# modmoorco.m:167
                            Jobj=[]
# modmoorco.m:167
                            Pobj=[]
# modmoorco.m:167
                            mmCO=length(BCO)
# modmoorco.m:168
                            mm=length(B)
# modmoorco.m:169
                            for ico in arange(1,mmCO).reshape(-1):
                                for i in arange(1,mm - 1).reshape(-1):
                                    if ZCO(ico) < logical_and(sum(H(1,arange(i,mm))),ZCO(ico)) >= sum(H(1,arange((i + 1),mm))):
                                        Jobj[ico]=i
# modmoorco.m:173
                                        dz=ZCO(ico) - sum(H(1,arange((i + 1),mm)))
# modmoorco.m:174
                                        Pobj[ico]=dz / H(1,i)
# modmoorco.m:175
                                        i=mm - 1
# modmoorco.m:176
                            # re-set the next value to input.
                            elenumCO=length(BCO) + 1
# modmoorco.m:181
                            if elenumCO <= 0:
                                elenumCO=1
# modmoorco.m:182
                            deleleCO=0
# modmoorco.m:183
                            set(h_edit_elenumCO,'String',num2str(elenumCO))
                            set(h_edit_deleleCO,'String',num2str(deleleCO))
                            dismoor
                        insertCO=0
# modmoorco.m:188
                    else:
                        if command == 3:
                            clear('typelist')
                            type_=get(h_menu_typeCO,'Value')
# modmoorco.m:191
                            if type_ == 1:
                                list=copy(floats)
# modmoorco.m:193
                            else:
                                if type_ == 2:
                                    list=copy(cms)
# modmoorco.m:195
                                else:
                                    if type_ == 3:
                                        list=copy(miscs)
# modmoorco.m:197
                            me,ne=size(list,nargout=2)
# modmoorco.m:199
                            for ii in arange(1,me).reshape(-1):
                                typelist[arange((dot((ii - 1),17) + 1),(dot((ii - 1),17) + 17))]=concat([list(ii,arange(1,16)),'|'])
# modmoorco.m:201
                            typelist=typelist(arange(1,length(typelist) - 1))
# modmoorco.m:203
                            set(h_menu_listCO,'Value',1)
                            set(h_menu_listCO,'String',typelist)
                        else:
                            if command == 4:
                                #ZCO=[];
                                val=get(h_menu_listCO,'Value')
# modmoorco.m:208
                                elenumCO=str2num(get(h_edit_elenumCO,'String'))
# modmoorco.m:210
                            else:
                                if command == 5:
                                    if heightCO == logical_and(0,elenumCO) > length(BCO):
                                        disp('You must set the height of the device (>0).')
                                        return
                                    # complete the operation
                                    if insertCO != logical_and(0,elenumCO) <= length(BCO):
                                        mb=length(BCO)
# modmoorco.m:218
                                        bump=concat([arange(insertCO + 1,mb + 1)])
# modmoorco.m:219
                                        mooreleCO[bump,arange()]=mooreleCO(arange(elenumCO,mb),arange())
# modmoorco.m:220
                                        BCO[bump]=BCO(arange(elenumCO,mb))
# modmoorco.m:221
                                        HCO[arange(),bump]=HCO(arange(),arange(elenumCO,mb))
# modmoorco.m:222
                                        CdCO[bump]=CdCO(arange(elenumCO,mb))
# modmoorco.m:223
                                        ZCO[bump]=ZCO(arange(elenumCO,mb))
# modmoorco.m:224
                                    mooreleCO[elenumCO,arange()]=list(val,arange(format(1,1),format(1,2)))
# modmoorco.m:226
                                    BCO[elenumCO]=str2num(list(val,arange(format(2,1),format(2,2))))
# modmoorco.m:227
                                    HCO[1,elenumCO]=str2num(list(val,arange(format(3,1),format(3,2)))) / 100
# modmoorco.m:228
                                    HCO[2,elenumCO]=str2num(list(val,arange(format(4,1),format(4,2)))) / 100
# modmoorco.m:229
                                    HCO[3,elenumCO]=str2num(list(val,arange(format(5,1),format(5,2)))) / 100
# modmoorco.m:230
                                    HCO[4,elenumCO]=0
# modmoorco.m:231
                                    CdCO[elenumCO]=str2num(list(val,arange(format(6,1),format(6,2))))
# modmoorco.m:232
                                    ZCO[elenumCO]=heightCO
# modmoorco.m:233
                                    elenum0=copy(elenumCO)
# modmoorco.m:234
                                    elenumCO=length(BCO) + 1
# modmoorco.m:235
                                    set(h_edit_elenumCO,'String',num2str(elenumCO))
                                    insertCO=0
# modmoorco.m:237
                                    elenumCO=length(BCO) + 1
# modmoorco.m:237
                                    if HCO(1,elenum0) == 0:
                                        set(h_edit_deleleCO,'String',num2str(elenum0))
                                        modmoorCO(2)
                                    mmCO=length(BCO)
# modmoorco.m:242
                                    mm=length(B)
# modmoorco.m:243
                                    for ico in arange(1,mmCO).reshape(-1):
                                        for i in arange(1,mm - 1).reshape(-1):
                                            if ZCO(ico) < logical_and(sum(H(1,arange(i,mm))),ZCO(ico)) >= sum(H(1,arange((i + 1),mm))):
                                                Jobj[ico]=i
# modmoorco.m:247
                                                dz=ZCO(ico) - sum(H(1,arange((i + 1),mm)))
# modmoorco.m:248
                                                Pobj[ico]=dz / H(1,i)
# modmoorco.m:249
                                                i=mm - 1
# modmoorco.m:250
                                    dismoor
                                else:
                                    if command == 6:
                                        close_(2)
                                        moordesign(3)
    
    # fini