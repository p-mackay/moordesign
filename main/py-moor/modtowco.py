# Generated with SMOP  0.41-beta
from libsmop import *
# modtowco.m

    
@function
def modtowCO(command=None,parameter=None,*args,**kwargs):
    varargin = modtowCO.varargin
    nargin = modtowCO.nargin

    # Program to make a GUI for add/modifying clamp-on devices
    
    global U,V,W,z,rho,uw,vw,Usp,Vsp
    global Ht,Bt,Cdt,MEt,moorelet,Z
    global HCO,BCO,CdCO,mooreleCO,ZCO,Iobj,Jobj,Pobj
    global floats,wires,chains,acrels,cms,anchors,miscs,format,typelist,type_,list
    global handle_listCO,insertCO,heightCO,val,elenumCO
    global fs
    global Zoo
    if nargin == logical_or(0,command) <= 0:
        if command == logical_or(- 1,isempty(BCO)):
            HCO=[]
# modtowco.m:14
            BCO=[]
# modtowco.m:14
            CdCO=[]
# modtowco.m:14
            mooreleCO='1234567890123456'
# modtowco.m:15
            handle_listCO=[]
# modtowco.m:16
        else:
            if command == 0:
                if logical_not(isempty(BCO)):
                    elenumCO=length(BCO) + 1
# modtowco.m:19
                    deleleCO=0
# modtowco.m:20
                    heightCO=0
# modtowco.m:21
        typelist=' '
# modtowco.m:24
        list=' '
# modtowco.m:24
        command=0
# modtowco.m:25
    
    Z=[]
# modtowco.m:27
    
    Zoo=[]
# modtowco.m:28
    if logical_not(isempty(handle_listCO)):
        h_edit_elenumCO=handle_listCO(1)
# modtowco.m:30
        h_edit_deleleCO=handle_listCO(2)
# modtowco.m:31
        h_menu_typeCO=handle_listCO(3)
# modtowco.m:32
        h_menu_listCO=handle_listCO(4)
# modtowco.m:33
        h_edit_heightCO=handle_listCO(5)
# modtowco.m:34
    
    
    if isempty(floats):
        load('mdcodes')
    
    
    if command == 0:
        elenumCO=length(BCO) + 1
# modtowco.m:40
        deleleCO=0
# modtowco.m:41
        heightCO=0
# modtowco.m:42
        list=copy(floats)
# modtowco.m:43
        type_=1
# modtowco.m:44
        me,ne=size(list,nargout=2)
# modtowco.m:45
        for ii in arange(1,me).reshape(-1):
            typelist[arange((dot((ii - 1),17) + 1),(dot((ii - 1),17) + 17))]=concat([list(ii,arange(1,16)),'|'])
# modtowco.m:47
        typelist=typelist(arange(1,length(typelist) - 1))
# modtowco.m:49
        figure(2)
        clf
        set(gcf,'Units','Normalized','Position',concat([0.05,0.05,0.25,0.275]),'Name','Modify Clamp-On Devices','Color',concat([0.8,0.8,0.8]),'tag','modtowCO')
        telenum=uicontrol('Style','text','String','Element to Clamp-On','FontSize',fs,'Units','normalized','Position',concat([0.1,0.88,0.55,0.1]))
# modtowco.m:56
        h_edit_elenumCO=uicontrol('Style','edit','Callback','modtowCO(1)','String',num2str(elenumCO),'FontSize',fs,'Units','Normalized','Position',concat([0.7,0.88,0.2,0.1]))
# modtowco.m:60
        teleins=uicontrol('Style','text','String','Delete Clamp-On Element','FontSize',fs,'Units','normalized','Position',concat([0.1,0.76,0.55,0.1]))
# modtowco.m:65
        h_edit_deleleCO=uicontrol('Style','edit','Callback','modtowCO(2)','String',num2str(deleleCO),'FontSize',fs,'Units','Normalized','Position',concat([0.7,0.76,0.2,0.1]))
# modtowco.m:69
        h_menu_typeCO=uicontrol('Style','popupmenu','Callback','modtowCO(3)','FontSize',fs,'String',concat(['Floatation|Current Meter|Misc Instrument']),'Units','Normalized','Position',concat([0.1,0.64,0.8,0.1]))
# modtowco.m:74
        h_menu_listCO=uicontrol('Style','popupmenu','Callback','modtowCO(4)','String',typelist,'FontSize',fs,'Units','Normalized','Position',concat([0.1,0.52,0.8,0.1]))
# modtowco.m:79
        telehght=uicontrol('Style','text','String','Height Above Tow-Body [m]','FontSize',fs,'Units','normalized','Position',concat([0.1,0.4,0.55,0.1]))
# modtowco.m:84
        h_edit_heightCO=uicontrol('Style','edit','Callback','modtowCO(11)','String',num2str(heightCO),'FontSize',fs,'Units','Normalized','Position',concat([0.7,0.4,0.2,0.1]))
# modtowco.m:88
        h_push_file=uicontrol('Style','pushbutton','Callback','modtowCO(88)','String','Load Different Database','FontSize',fs,'Units','Normalized','Position',concat([0.25,0.27,0.5,0.1]))
# modtowco.m:93
        h_push_disp=uicontrol('Style','pushbutton','Callback','dismoor','String','Display Elements','FontSize',fs,'Units','Normalized','Position',concat([0.075,0.15,0.4,0.1]))
# modtowco.m:98
        h_push_update=uicontrol('Style','Pushbutton','String','Execute Update','FontSize',fs,'Units','normalized','Position',concat([0.525,0.15,0.4,0.1]),'Callback','modtowCO(5)')
# modtowco.m:103
        hmaincls=uicontrol('Style','Pushbutton','String','Close','FontSize',fs,'Units','normalized','Position',concat([0.3,0.02,0.4,0.1]),'Callback','modtowCO(6)')
# modtowco.m:108
        handle_listCO=concat([h_edit_elenumCO,h_edit_deleleCO,h_menu_typeCO,h_menu_listCO,h_edit_heightCO])
# modtowco.m:114
        set(gcf,'userdata',handle_listCO)
        insertCO=0
# modtowco.m:121
    else:
        if command == 88:
            ifile,ipath=uigetfile('*.mat','Load Database File MDCODES.MAT (cancel loads default)',nargout=2)
# modtowco.m:123
            if logical_and(ischar(ifile),ischar(ipath)):
                if logical_not(strcmp(ifile,'*.mat')):
                    load(concat([ipath,ifile]))
                else:
                    load('mdcodes')
            else:
                if ifile == logical_and(0,ipath) == 0:
                    load('mdcodes')
            clear('ifile','ipath')
            modtowCO(0)
        else:
            if command == 1:
                insertCO=str2num(get(h_edit_elenumCO,'String'))
# modtowco.m:136
            else:
                if command == 11:
                    heightCO=str2num(get(h_edit_heightCO,'String'))
# modtowco.m:138
                else:
                    if command == 2:
                        deleleCO=str2num(get(h_edit_deleleCO,'String'))
# modtowco.m:140
                        mb=length(BCO)
# modtowco.m:141
                        if deleleCO <= mb:
                            if deleleCO == 1:
                                if mb > 1:
                                    BCO=BCO(arange(2,mb))
# modtowco.m:145
                                    HCO=HCO(arange(),arange(2,mb))
# modtowco.m:146
                                    CdCO=CdCO(arange(2,mb))
# modtowco.m:147
                                    ZCO=ZCO(arange(2,mb))
# modtowco.m:148
                                    mooreleCO=mooreleCO(arange(2,mb),arange())
# modtowco.m:149
                                else:
                                    BCO=[]
# modtowco.m:151
                                    HCO=[]
# modtowco.m:151
                                    CdCO=[]
# modtowco.m:151
                                    ZCO=[]
# modtowco.m:151
                                    mooreleCO=[]
# modtowco.m:151
                            else:
                                if deleleCO == mb:
                                    BCO=BCO(arange(1,(mb - 1)))
# modtowco.m:154
                                    HCO=HCO(arange(),arange(1,(mb - 1)))
# modtowco.m:155
                                    CdCO=CdCO(arange(1,(mb - 1)))
# modtowco.m:156
                                    ZCO=ZCO(arange(1,(mb - 1)))
# modtowco.m:157
                                    mooreleCO=mooreleCO(arange(1,(mb - 1)),arange())
# modtowco.m:158
                                else:
                                    if deleleCO > logical_and(1,deleleCO) < mb:
                                        inew=concat([arange(1,deleleCO - 1),arange(deleleCO + 1,mb)])
# modtowco.m:160
                                        BCO=BCO(inew)
# modtowco.m:161
                                        HCO=HCO(arange(),inew)
# modtowco.m:162
                                        CdCO=CdCO(inew)
# modtowco.m:163
                                        ZCO=ZCO(inew)
# modtowco.m:164
                                        mooreleCO=mooreleCO(inew,arange())
# modtowco.m:165
                            Iojb=[]
# modtowco.m:167
                            Jobj=[]
# modtowco.m:167
                            Pobj=[]
# modtowco.m:167
                            mmCO=length(BCO)
# modtowco.m:168
                            mm=length(Bt)
# modtowco.m:169
                            for ico in arange(1,mmCO).reshape(-1):
                                for i in arange(1,mm - 1).reshape(-1):
                                    if ZCO(ico) > logical_and(sum(Ht(1,arange(1,i))),ZCO(ico)) <= sum(Ht(1,arange(1,(i + 1)))):
                                        Jobj[ico]=i + 1
# modtowco.m:173
                                        dz=ZCO(ico) - sum(Ht(1,arange(1,i)))
# modtowco.m:174
                                        Pobj[ico]=dz / Ht(1,i + 1)
# modtowco.m:175
                                        i=mm - 1
# modtowco.m:176
                            # re-set the next value to input.
                            elenumCO=length(BCO) + 1
# modtowco.m:181
                            if elenumCO <= 0:
                                elenumCO=1
# modtowco.m:182
                            deleleCO=0
# modtowco.m:183
                            set(h_edit_elenumCO,'String',num2str(elenumCO))
                            set(h_edit_deleleCO,'String',num2str(deleleCO))
                            dismoor
                        insertCO=0
# modtowco.m:188
                    else:
                        if command == 3:
                            clear('typelist')
                            type_=get(h_menu_typeCO,'Value')
# modtowco.m:191
                            if type_ == 1:
                                list=copy(floats)
# modtowco.m:193
                            else:
                                if type_ == 2:
                                    list=copy(cms)
# modtowco.m:195
                                else:
                                    if type_ == 3:
                                        list=copy(miscs)
# modtowco.m:197
                            me,ne=size(list,nargout=2)
# modtowco.m:199
                            for ii in arange(1,me).reshape(-1):
                                typelist[arange((dot((ii - 1),17) + 1),(dot((ii - 1),17) + 17))]=concat([list(ii,arange(1,16)),'|'])
# modtowco.m:201
                            typelist=typelist(arange(1,length(typelist) - 1))
# modtowco.m:203
                            set(h_menu_listCO,'Value',1)
                            set(h_menu_listCO,'String',typelist)
                        else:
                            if command == 4:
                                #ZCO=[];
                                val=get(h_menu_listCO,'Value')
# modtowco.m:208
                                elenumCO=str2num(get(h_edit_elenumCO,'String'))
# modtowco.m:210
                            else:
                                if command == 5:
                                    if heightCO == logical_and(0,elenumCO) > length(BCO):
                                        disp('You must set the height of the device (>0) above tow-body.')
                                        break
                                    # complete the operation
                                    if insertCO != logical_and(0,elenumCO) <= length(BCO):
                                        mb=length(BCO)
# modtowco.m:218
                                        bump=concat([arange(insertCO + 1,mb + 1)])
# modtowco.m:219
                                        mooreleCO[bump,arange()]=mooreleCO(arange(elenumCO,mb),arange())
# modtowco.m:220
                                        BCO[bump]=BCO(arange(elenumCO,mb))
# modtowco.m:221
                                        HCO[arange(),bump]=HCO(arange(),arange(elenumCO,mb))
# modtowco.m:222
                                        CdCO[bump]=CdCO(arange(elenumCO,mb))
# modtowco.m:223
                                        ZCO[bump]=ZCO(arange(elenumCO,mb))
# modtowco.m:224
                                    mooreleCO[elenumCO,arange()]=list(val,arange(format(1,1),format(1,2)))
# modtowco.m:226
                                    BCO[elenumCO]=str2num(list(val,arange(format(2,1),format(2,2))))
# modtowco.m:227
                                    HCO[1,elenumCO]=str2num(list(val,arange(format(3,1),format(3,2)))) / 100
# modtowco.m:228
                                    HCO[2,elenumCO]=str2num(list(val,arange(format(4,1),format(4,2)))) / 100
# modtowco.m:229
                                    HCO[3,elenumCO]=str2num(list(val,arange(format(5,1),format(5,2)))) / 100
# modtowco.m:230
                                    HCO[4,elenumCO]=0
# modtowco.m:231
                                    CdCO[elenumCO]=str2num(list(val,arange(format(6,1),format(6,2))))
# modtowco.m:232
                                    ZCO[elenumCO]=heightCO
# modtowco.m:233
                                    elenum0=copy(elenumCO)
# modtowco.m:234
                                    elenumCO=length(BCO) + 1
# modtowco.m:235
                                    set(h_edit_elenumCO,'String',num2str(elenumCO))
                                    insertCO=0
# modtowco.m:237
                                    elenumCO=length(BCO) + 1
# modtowco.m:237
                                    if HCO(1,elenum0) == 0:
                                        set(h_edit_deleleCO,'String',num2str(elenum0))
                                        modtowCO(2)
                                    mmCO=length(BCO)
# modtowco.m:242
                                    mm=length(Bt)
# modtowco.m:243
                                    for ico in arange(1,mmCO).reshape(-1):
                                        for i in arange(1,mm - 1).reshape(-1):
                                            if ZCO(ico) > logical_and(sum(Ht(1,arange(1,i))),ZCO(ico)) <= sum(Ht(1,arange(1,(i + 1)))):
                                                Jobj[ico]=i + 1
# modtowco.m:247
                                                dz=ZCO(ico) - sum(Ht(1,arange(1,i)))
# modtowco.m:248
                                                Pobj[ico]=dz / Ht(1,i + 1)
# modtowco.m:249
                                                i=mm - 1
# modtowco.m:250
                                    dismoor
                                else:
                                    if command == 6:
                                        close_(2)
                                        moordesign(3)
    
    # fini