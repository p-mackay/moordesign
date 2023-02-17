# Generated with SMOP  0.41-beta
from libsmop import *
# modmoor.m

    
@function
def modmoor(command=None,parameter=None,*args,**kwargs):
    varargin = modmoor.varargin
    nargin = modmoor.nargin

    # Program to make a GUI for modifying a mooring design
    
    global U,V,W,z,rho
    global H,B,Cd,ME,moorele
    global Ht,Bt,Cdt,MEt,moorelet
    global BCO,ZCO,Jobj,Pobj
    global floats,wires,chains,acrels,cms,anchors,miscs,format,typelist,type_,list
    global handle_list,wire_length,h_edit_wirel,insert,elenum,delele,val
    global Z,Zoo
    global fs
    if nargin == logical_or(0,command) <= 0:
        if command == - 1:
            H=[]
# modmoor.m:15
            B=[]
# modmoor.m:15
            Cd=[]
# modmoor.m:15
            ME=[]
# modmoor.m:15
            moorele=[]
# modmoor.m:15
            X=[]
# modmoor.m:15
            Y=[]
# modmoor.m:15
            Z=[]
# modmoor.m:15
            Zoo=[]
# modmoor.m:15
            Ht=[]
# modmoor.m:16
            Bt=[]
# modmoor.m:16
            Cdt=[]
# modmoor.m:16
            MEt=[]
# modmoor.m:16
            moorelet=[]
# modmoor.m:16
            moorele='1234567890123456'
# modmoor.m:17
            handle_list=[]
# modmoor.m:18
        else:
            if command == 0:
                if logical_not(isempty(B)):
                    elenum=length(B) + 1
# modmoor.m:21
                    delele=0
# modmoor.m:22
                    dismoor
        elenum=length(B) + 1
# modmoor.m:26
        typelist=' '
# modmoor.m:27
        list=' '
# modmoor.m:28
        command=0
# modmoor.m:29
    
    Z=[]
# modmoor.m:31
    
    Zoo=[]
# modmoor.m:32
    if logical_not(isempty(handle_list)):
        h_edit_elenum=handle_list(1)
# modmoor.m:34
        h_edit_delele=handle_list(2)
# modmoor.m:35
        h_menu_type=handle_list(3)
# modmoor.m:36
        h_menu_list=handle_list(4)
# modmoor.m:37
    
    
    if logical_or(isempty(typelist),strcmp(typelist,concat([' ']))):
        load('mdcodes')
    
    
    if command == 0:
        if isempty(elenum):
            elenum=length(B) + 1
# modmoor.m:44
            delele=0
# modmoor.m:45
        list=copy(floats)
# modmoor.m:47
        type_=1
# modmoor.m:48
        me,ne=size(list,nargout=2)
# modmoor.m:49
        for ii in arange(1,me).reshape(-1):
            typelist[arange((dot((ii - 1),17) + 1),(dot((ii - 1),17) + 17))]=concat([list(ii,arange(1,16)),'|'])
# modmoor.m:51
        typelist=typelist(arange(1,length(typelist) - 1))
# modmoor.m:53
        figure(2)
        clf
        set(gcf,'Units','Normalized','Position',concat([0.05,0.05,0.25,0.3]),'Name','Modify Mooring Design','Color',concat([0.8,0.8,0.8]),'tag','modmoor')
        telenum=uicontrol('Style','text','String','Element to Add/Insert','FontSize',fs,'Units','normalized','Position',concat([0.1,0.89,0.55,0.1]))
# modmoor.m:60
        h_edit_elenum=uicontrol('Style','edit','Callback','modmoor(1)','String',num2str(elenum),'FontSize',fs,'Units','Normalized','Position',concat([0.7,0.89,0.2,0.1]))
# modmoor.m:64
        teleins=uicontrol('Style','text','String','Delete Element','FontSize',fs,'Units','normalized','Position',concat([0.1,0.77,0.55,0.1]))
# modmoor.m:69
        h_edit_delele=uicontrol('Style','edit','Callback','modmoor(2)','String',num2str(delele),'FontSize',fs,'Units','Normalized','Position',concat([0.7,0.77,0.2,0.1]))
# modmoor.m:73
        h_push_file=uicontrol('Style','pushbutton','Callback','modmoor(88)','String','Load Different Database','FontSize',fs,'Units','Normalized','Position',concat([0.25,0.65,0.5,0.1]))
# modmoor.m:78
        h_menu_type=uicontrol('Style','popupmenu','Callback','modmoor(3)','FontSize',fs,'String',concat(['Floatation|Wire|Chain+Shackles|Current Meter|Acoustic Release|Anchor|Misc Instrument']),'Units','Normalized','Position',concat([0.1,0.5,0.8,0.12]))
# modmoor.m:83
        h_menu_list=uicontrol('Style','popupmenu','Callback','modmoor(4)','String',typelist,'FontSize',fs,'Units','Normalized','Position',concat([0.1,0.37,0.8,0.12]))
# modmoor.m:88
        h_push_update=uicontrol('Style','pushbutton','Callback','modmoor(44)','String','Execute Update','FontSize',fs,'Units','Normalized','Position',concat([0.3,0.275,0.4,0.1]))
# modmoor.m:93
        h_push_disp=uicontrol('Style','pushbutton','Callback','dismoor','String','Display Elements','FontSize',fs,'Units','Normalized','Position',concat([0.075,0.15,0.4,0.1]))
# modmoor.m:98
        h_push_change=uicontrol('Style','pushbutton','Callback','globalchange(0)','String','Global Replace','FontSize',fs,'Units','Normalized','Position',concat([0.525,0.15,0.4,0.1]))
# modmoor.m:103
        hmaincls=uicontrol('Style','Pushbutton','String','Close','FontSize',fs,'Units','normalized','Position',concat([0.3,0.02,0.4,0.1]),'Callback','modmoor(6)')
# modmoor.m:108
        handle_list=concat([h_edit_elenum,h_edit_delele,h_menu_type,h_menu_list])
# modmoor.m:114
        set(gcf,'userdata',handle_list)
        insert=0
# modmoor.m:120
    else:
        if command == 88:
            ifile,ipath=uigetfile('*.mat','Load Database file MDCODES.MAT (cancel loads default)',nargout=2)
# modmoor.m:122
            if logical_and(ischar(ifile),ischar(ipath)):
                if logical_not(strcmp(ifile,'*.mat')):
                    load(concat([ipath,ifile]))
                else:
                    load('mdcodes')
            else:
                if ifile == logical_and(0,ipath) == 0:
                    load('mdcodes')
            clear('ifile','ipath')
            modmoor(0)
        else:
            if command == 1:
                insert=str2num(get(h_edit_elenum,'String'))
# modmoor.m:135
                delele=0
# modmoor.m:136
            else:
                if command == 2:
                    delele=str2num(get(h_edit_delele,'String'))
# modmoor.m:138
                else:
                    if command == 3:
                        clear('typelist')
                        type_=get(h_menu_type,'Value')
# modmoor.m:141
                        if type_ == 1:
                            list=copy(floats)
# modmoor.m:143
                        else:
                            if type_ == 2:
                                list=copy(wires)
# modmoor.m:145
                            else:
                                if type_ == 3:
                                    list=copy(chains)
# modmoor.m:147
                                else:
                                    if type_ == 4:
                                        list=copy(cms)
# modmoor.m:149
                                    else:
                                        if type_ == 5:
                                            list=copy(acrels)
# modmoor.m:151
                                        else:
                                            if type_ == 6:
                                                list=copy(anchors)
# modmoor.m:153
                                            else:
                                                if type_ == 7:
                                                    list=copy(miscs)
# modmoor.m:155
                        me,ne=size(list,nargout=2)
# modmoor.m:157
                        for ii in arange(1,me).reshape(-1):
                            typelist[arange((dot((ii - 1),17) + 1),(dot((ii - 1),17) + 17))]=concat([list(ii,arange(1,16)),'|'])
# modmoor.m:159
                        typelist=typelist(arange(1,length(typelist) - 1))
# modmoor.m:161
                        set(h_menu_list,'Value',1)
                        set(h_menu_list,'String',typelist)
                    else:
                        if command == 4:
                            val=get(h_menu_list,'Value')
# modmoor.m:165
                            elenum=str2num(get(h_edit_elenum,'String'))
# modmoor.m:167
                            delele=0
# modmoor.m:168
                        else:
                            if command == 44:
                                if delele > 0:
                                    Z=[]
# modmoor.m:171
                                    disp('Hello!')
                                    mb=length(B)
# modmoor.m:173
                                    if delele <= mb:
                                        if delele == 1:
                                            if mb > 1:
                                                B=B(arange(2,mb))
# modmoor.m:177
                                                H=H(arange(),arange(2,mb))
# modmoor.m:178
                                                Cd=Cd(arange(2,mb))
# modmoor.m:179
                                                moorele=moorele(arange(2,mb),arange())
# modmoor.m:180
                                                ME=ME(arange(2,mb))
# modmoor.m:181
                                            else:
                                                B=[]
# modmoor.m:183
                                                H=[]
# modmoor.m:183
                                                Cd=[]
# modmoor.m:183
                                                moorele=[]
# modmoor.m:183
                                                ME=[]
# modmoor.m:184
                                        else:
                                            if delele == mb:
                                                B=B(arange(1,(mb - 1)))
# modmoor.m:187
                                                H=H(arange(),arange(1,(mb - 1)))
# modmoor.m:188
                                                Cd=Cd(arange(1,(mb - 1)))
# modmoor.m:189
                                                moorele=moorele(arange(1,(mb - 1)),arange())
# modmoor.m:190
                                                ME=ME(arange(1,(mb - 1)))
# modmoor.m:191
                                            else:
                                                if delele > logical_and(1,delele) < mb:
                                                    inew=concat([arange(1,delele - 1),arange(delele + 1,mb)])
# modmoor.m:193
                                                    B=B(inew)
# modmoor.m:194
                                                    H=H(arange(),inew)
# modmoor.m:195
                                                    Cd=Cd(inew)
# modmoor.m:196
                                                    moorele=moorele(inew,arange())
# modmoor.m:197
                                                    ME=ME(inew)
# modmoor.m:198
                                        # re-set the next value to input.
                                        elenum=length(B) + 1
# modmoor.m:201
                                        if elenum <= 0:
                                            elenum=1
# modmoor.m:202
                                        delele=0
# modmoor.m:203
                                        set(h_edit_elenum,'String',num2str(elenum))
                                        set(h_edit_delele,'String',num2str(delele))
                                    insert=0
# modmoor.m:207
                                else:
                                    if insert != logical_and(0,elenum) <= length(B):
                                        mb=length(B)
# modmoor.m:210
                                        bump=concat([arange(insert + 1,mb + 1)])
# modmoor.m:211
                                        moorele[bump,arange()]=moorele(arange(elenum,mb),arange())
# modmoor.m:212
                                        B[bump]=B(arange(elenum,mb))
# modmoor.m:213
                                        H[arange(),bump]=H(arange(),arange(elenum,mb))
# modmoor.m:214
                                        Cd[bump]=Cd(arange(elenum,mb))
# modmoor.m:215
                                        ME[bump]=ME(arange(elenum,mb))
# modmoor.m:216
                                    moorele[elenum,arange()]=list(val,arange(format(1,1),format(1,2)))
# modmoor.m:218
                                    B[elenum]=str2num(list(val,arange(format(2,1),format(2,2))))
# modmoor.m:219
                                    H[1,elenum]=str2num(list(val,arange(format(3,1),format(3,2)))) / 100
# modmoor.m:220
                                    H[2,elenum]=str2num(list(val,arange(format(4,1),format(4,2)))) / 100
# modmoor.m:221
                                    H[3,elenum]=str2num(list(val,arange(format(5,1),format(5,2)))) / 100
# modmoor.m:222
                                    H[4,elenum]=0
# modmoor.m:223
                                    ME[elenum]=inf
# modmoor.m:224
                                    if type_ == logical_or(2,type_) == 3:
                                        if H(1,elenum) == 1:
                                            getwirel
                                            waitfor(h_edit_wirel)
                                            H[1,elenum]=wire_length
# modmoor.m:228
                                            H[4,elenum]=1
# modmoor.m:229
                                            mat=str2num(list(val,arange(format(7,1),format(7,2))))
# modmoor.m:230
                                            if mat == 1:
                                                ME[elenum]=138000000000.0
# modmoor.m:232
                                            else:
                                                if mat == 2:
                                                    ME[elenum]=345000000.0
# modmoor.m:234
                                                else:
                                                    if mat == 3:
                                                        ME[elenum]=800000000.0
# modmoor.m:236
                                                    else:
                                                        if mat == 4:
                                                            ME[elenum]=345000000.0
# modmoor.m:238
                                                        else:
                                                            if mat == 5:
                                                                ME[elenum]=690000000.0
# modmoor.m:240
                                                            else:
                                                                if mat == 6:
                                                                    ME[elenum]=69000000000.0
# modmoor.m:242
                                                                else:
                                                                    if mat == 7:
                                                                        ME[elenum]=76000000000.0
# modmoor.m:244
                                                                    else:
                                                                        if mat == 8:
                                                                            ME[elenum]=100000000000.0
# modmoor.m:246
                                        else:
                                            H[4,elenum]=2
# modmoor.m:249
                                    Cd[elenum]=str2num(list(val,arange(format(6,1),format(6,2))))
# modmoor.m:252
                                    elenum0=copy(elenum)
# modmoor.m:253
                                    elenum=length(B) + 1
# modmoor.m:254
                                    set(h_edit_elenum,'String',num2str(elenum))
                                    insert=0
# modmoor.m:256
                                    if H(1,elenum0) == 0:
                                        set(h_edit_delele,'String',num2str(elenum0))
                                        modmoor(2)
                                    delele=0
# modmoor.m:261
                                dismoor
                            else:
                                if command == 6:
                                    # if this mooring has been modified, and there are clamp-on devices, 
# then we must re-determine their location
                                    mmCO=length(BCO)
# modmoor.m:267
                                    if mmCO > 0:
                                        mm=length(B)
# modmoor.m:269
                                        for ico in arange(1,mmCO).reshape(-1):
                                            for i in arange(1,mm - 1).reshape(-1):
                                                if ZCO(ico) < logical_and(sum(H(1,arange(i,mm))),ZCO(ico)) >= sum(H(1,arange((i + 1),mm))):
                                                    Jobj[ico]=i
# modmoor.m:273
                                                    dz=ZCO(ico) - sum(H(1,arange((i + 1),mm)))
# modmoor.m:274
                                                    Pobj[ico]=dz / H(1,i)
# modmoor.m:275
                                                    i=mm - 1
# modmoor.m:276
                                    close_(2)
                                    moordesign(3)
    
    # fini