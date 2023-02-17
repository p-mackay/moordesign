# Generated with SMOP  0.41-beta
from libsmop import *
# modtow.m

    
@function
def modtow(command=None,parameter=None,*args,**kwargs):
    varargin = modtow.varargin
    nargin = modtow.nargin

    # Program to make a GUI for modifying a towed body design
# For a towed body, the Surface is the reference and
# the "mooring" solution is turned up-side-down by setting
# d=-z and B=-B.
# So a sinking body, is made buoyant, towed upside down, then flipped back.
# RKD 3/00
    
    global Ht,Bt,Cdt,MEt,moorelet,Usp,Vsp,afh
    global H,B,Cd,ME,moorele
    global floats,wires,chains,acrels,cms,anchors,miscs,format,typelist,type_,list
    global handle_list,wire_length,h_edit_wirel,insert,elenum,delele,val,chele
    global Z,Zoo
    global fs
    if nargin == logical_or(0,command) <= 0:
        if command == - 1:
            handle_list=[]
# modtow.m:18
            Ht=[]
# modtow.m:19
            Bt=[]
# modtow.m:19
            Cdt=[]
# modtow.m:19
            moorelet='1234567890123456'
# modtow.m:20
            Ht=[]
# modtow.m:21
            Bt=[]
# modtow.m:21
            Cdt=[]
# modtow.m:21
            MEt=[]
# modtow.m:21
            moorelet=[]
# modtow.m:21
            X=[]
# modtow.m:21
            Y=[]
# modtow.m:21
            Z=[]
# modtow.m:21
            Zoo=[]
# modtow.m:21
            H=[]
# modtow.m:22
            B=[]
# modtow.m:22
            Cd=[]
# modtow.m:22
            ME=[]
# modtow.m:22
            moorele=[]
# modtow.m:22
            Usp=0
# modtow.m:23
            Vsp=0
# modtow.m:23
            afh=0
# modtow.m:23
        else:
            if command == 0:
                if logical_not(isempty(Bt)):
                    elenum=length(Bt) + 1
# modtow.m:26
                    delele=0
# modtow.m:27
                    dismoor
        typelist=' '
# modtow.m:31
        list=' '
# modtow.m:32
        command=0
# modtow.m:33
    
    Z=[]
# modtow.m:35
    
    Zoo=[]
# modtow.m:36
    if logical_not(isempty(handle_list)):
        h_edit_elenum=handle_list(1)
# modtow.m:38
        h_edit_delele=handle_list(2)
# modtow.m:39
        h_menu_type=handle_list(3)
# modtow.m:40
        h_menu_list=handle_list(4)
# modtow.m:41
        h_edit_shsp=handle_list(5)
# modtow.m:42
        h_edit_afh=handle_list(6)
# modtow.m:43
        if length(handle_list) > 6:
            h_edit_chele=handle_list(7)
# modtow.m:44
    
    
    if logical_or(isempty(typelist),strcmp(typelist,' ')):
        load('mdcodes')
    
    
    if command == 0:
        if isempty(elenum):
            elenum=1
# modtow.m:51
            delele=0
# modtow.m:52
        list=copy(floats)
# modtow.m:54
        type_=1
# modtow.m:55
        me,ne=size(list,nargout=2)
# modtow.m:56
        for ii in arange(1,me).reshape(-1):
            typelist[arange((dot((ii - 1),17) + 1),(dot((ii - 1),17) + 17))]=concat([list(ii,arange(1,16)),'|'])
# modtow.m:58
        typelist=typelist(arange(1,length(typelist) - 1))
# modtow.m:60
        figure(2)
        clf
        set(gcf,'Units','Normalized','Position',concat([0.02,0.05,0.3,0.4]),'Name','Modify Towed Body Configureation','Color',concat([0.8,0.8,0.8]),'tag','modtow')
        telenum=uicontrol('Style','text','String','Element to Add/Insert: Bottom-to-Top','FontSize',fs,'Units','normalized','Position',concat([0.1,0.9,0.65,0.07]))
# modtow.m:67
        h_edit_elenum=uicontrol('Style','edit','Callback','modtow(1)','String',num2str(elenum),'FontSize',fs,'Units','Normalized','Position',concat([0.8,0.9,0.1,0.07]))
# modtow.m:71
        teleins=uicontrol('Style','text','String','Delete Element Number','FontSize',fs,'Units','normalized','Position',concat([0.1,0.8,0.65,0.07]))
# modtow.m:76
        h_edit_delele=uicontrol('Style','edit','Callback','modtow(2)','String',num2str(delele),'FontSize',fs,'Units','Normalized','Position',concat([0.8,0.8,0.1,0.07]))
# modtow.m:80
        h_push_file=uicontrol('Style','pushbutton','Callback','modtow(88)','String','Load Different Database','FontSize',fs,'Units','Normalized','Position',concat([0.25,0.7,0.5,0.07]))
# modtow.m:85
        h_menu_type=uicontrol('Style','popupmenu','Callback','modtow(3)','FontSize',fs,'String',concat(['Floatation|Wire|Chain+Shackles|Current Meter|Misc Instrument']),'Units','Normalized','Position',concat([0.1,0.575,0.8,0.1]))
# modtow.m:90
        h_menu_list=uicontrol('Style','popupmenu','Callback','modtow(4)','String',typelist,'FontSize',fs,'Units','Normalized','Position',concat([0.1,0.5,0.8,0.1]))
# modtow.m:95
        if logical_not(isempty(Ht)):
            if logical_not(isempty(find(Ht(4,arange()) == 1))):
                indxw=find(Ht(4,arange()) == 1)
# modtow.m:102
                if isempty(chele):
                    chele=indxw(1)
# modtow.m:103
                h_push_chlength=uicontrol('Style','pushbutton','Callback','modtow(9)','String','Change Length of Wire Element #','FontSize',fs,'Units','Normalized','Position',concat([0.05,0.435,0.7,0.07]))
# modtow.m:104
                h_edit_chele=uicontrol('Style','edit','Callback','modtow(8)','String',num2str(chele),'FontSize',fs,'Units','Normalized','Position',concat([0.8,0.435,0.1,0.07]))
# modtow.m:109
            else:
                h_edit_chele=99999
# modtow.m:115
        tshsp=uicontrol('Style','text','String','Enter Ship Velocity [U V] (m/s)','FontSize',fs,'Units','normalized','Position',concat([0.05,0.33,0.6,0.07]))
# modtow.m:118
        h_edit_shsp=uicontrol('Style','edit','Callback','modtow(5)','String',num2str(concat([Usp,Vsp])),'FontSize',fs,'Units','Normalized','Position',concat([0.7,0.33,0.2,0.07]))
# modtow.m:122
        tafh=uicontrol('Style','text','String','Height of A-Frame Block Above Water (m)','FontSize',fs,'Units','normalized','Position',concat([0.05,0.22,0.7,0.07]))
# modtow.m:127
        h_edit_afh=uicontrol('Style','edit','Callback','modtow(6)','String',num2str(afh),'FontSize',fs,'Units','Normalized','Position',concat([0.8,0.22,0.1,0.07]))
# modtow.m:131
        h_push_update=uicontrol('Style','pushbutton','Callback','modtow(7)','String','Execute Add-Insert-Delete Operation','FontSize',fs,'Units','Normalized','Position',concat([0.1,0.11,0.8,0.07]))
# modtow.m:136
        h_push_disp=uicontrol('Style','pushbutton','Callback','dismoor','String','Display Elements','FontSize',fs,'Units','Normalized','Position',concat([0.075,0.02,0.4,0.07]))
# modtow.m:141
        hmaincls=uicontrol('Style','Pushbutton','String','Close','FontSize',fs,'Units','normalized','Position',concat([0.525,0.02,0.4,0.07]),'Callback','modtow(90)')
# modtow.m:146
        insert=0
# modtow.m:151
    else:
        if command == 88:
            ifile,ipath=uigetfile('*.mat','Load Database file MDCODES.MAT (cancel loads default)',nargout=2)
# modtow.m:153
            if logical_and(ischar(ifile),ischar(ipath)):
                if logical_not(strcmp(ifile,'*.mat')):
                    load(concat([ipath,ifile]))
                else:
                    load('mdcodes')
            else:
                if ifile == logical_and(0,ipath) == 0:
                    load('mdcodes')
            clear('ifile','ipath')
            modtow(0)
        else:
            if command == 1:
                insert=str2num(get(h_edit_elenum,'String'))
# modtow.m:166
                elenum=str2num(get(h_edit_elenum,'String'))
# modtow.m:167
                delele=0
# modtow.m:168
            else:
                if command == 2:
                    delele=str2num(get(h_edit_delele,'String'))
# modtow.m:170
                    insert=0
# modtow.m:171
                else:
                    if command == 3:
                        clear('typelist')
                        type_=get(h_menu_type,'Value')
# modtow.m:174
                        if type_ == 1:
                            list=copy(floats)
# modtow.m:176
                        else:
                            if type_ == 2:
                                list=copy(wires)
# modtow.m:178
                            else:
                                if type_ == 3:
                                    list=copy(chains)
# modtow.m:180
                                else:
                                    if type_ == 4:
                                        list=copy(cms)
# modtow.m:182
                                    else:
                                        if type_ == 5:
                                            list=copy(miscs)
# modtow.m:184
                        me,ne=size(list,nargout=2)
# modtow.m:186
                        for ii in arange(1,me).reshape(-1):
                            typelist[arange((dot((ii - 1),17) + 1),(dot((ii - 1),17) + 17))]=concat([list(ii,arange(1,16)),'|'])
# modtow.m:188
                        typelist=typelist(arange(1,length(typelist) - 1))
# modtow.m:190
                        set(h_menu_list,'Value',1)
                        set(h_menu_list,'String',typelist)
                    else:
                        if command == 4:
                            val=get(h_menu_list,'Value')
# modtow.m:194
                            if type_ >= logical_and(2,type_) <= 3:
                                if str2num(list(val,arange(format(3,1),format(3,2)))) / 100 == 1:
                                    getwirel
                                    waitfor(h_edit_wirel)
                        else:
                            if command == 5:
                                UVsp=str2num(get(h_edit_shsp,'String'))
# modtow.m:202
                                Usp=UVsp(1)
# modtow.m:203
                                Vsp=UVsp(2)
# modtow.m:203
                            else:
                                if command == 6:
                                    afh=str2num(get(h_edit_afh,'String'))
# modtow.m:205
                                else:
                                    if command == 7:
                                        Z=[]
# modtow.m:207
                                        if delele != logical_and(0,insert) == 0:
                                            mb=length(Bt)
# modtow.m:209
                                            if delele <= mb:
                                                if delele == 1:
                                                    if mb > 1:
                                                        Bt=Bt(arange(2,mb))
# modtow.m:213
                                                        Ht=Ht(arange(),arange(2,mb))
# modtow.m:214
                                                        Cdt=Cdt(arange(2,mb))
# modtow.m:215
                                                        moorelet=moorelet(arange(2,mb),arange())
# modtow.m:216
                                                    else:
                                                        Bt=[]
# modtow.m:218
                                                        Ht=[]
# modtow.m:218
                                                        Cdt=[]
# modtow.m:218
                                                        moorelet=[]
# modtow.m:218
                                                else:
                                                    if delele == mb:
                                                        Bt=Bt(arange(1,(mb - 1)))
# modtow.m:221
                                                        Ht=Ht(arange(),arange(1,(mb - 1)))
# modtow.m:222
                                                        Cdt=Cdt(arange(1,(mb - 1)))
# modtow.m:223
                                                        moorelet=moorelet(arange(1,(mb - 1)),arange())
# modtow.m:224
                                                    else:
                                                        if delele > logical_and(1,delele) < mb:
                                                            inew=concat([arange(1,delele - 1),arange(delele + 1,mb)])
# modtow.m:226
                                                            Bt=Bt(inew)
# modtow.m:227
                                                            Ht=Ht(arange(),inew)
# modtow.m:228
                                                            Cdt=Cdt(inew)
# modtow.m:229
                                                            moorelet=moorelet(inew,arange())
# modtow.m:230
                                                # re-set the next value to input.
                                                elenum=length(Bt) + 1
# modtow.m:233
                                                if elenum <= 0:
                                                    elenum=1
# modtow.m:234
                                                delele=0
# modtow.m:235
                                                set(h_edit_elenum,'String',num2str(elenum))
                                                set(h_edit_delele,'String',num2str(delele))
                                                dismoor
                                        else:
                                            # add or insert an element
                                            if insert != logical_and(0,elenum) <= length(Bt):
                                                mb=length(Bt)
# modtow.m:243
                                                bump=concat([arange(insert + 1,mb + 1)])
# modtow.m:244
                                                moorelet[bump,arange()]=moorelet(arange(elenum,mb),arange())
# modtow.m:245
                                                Bt[bump]=Bt(arange(elenum,mb))
# modtow.m:246
                                                Ht[arange(),bump]=Ht(arange(),arange(elenum,mb))
# modtow.m:247
                                                Cdt[bump]=Cdt(arange(elenum,mb))
# modtow.m:248
                                                MEt[bump]=MEt(arange(elenum,mb))
# modtow.m:249
                                            moorelet[elenum,arange()]=list(val,arange(format(1,1),format(1,2)))
# modtow.m:251
                                            Bt[elenum]=str2num(list(val,arange(format(2,1),format(2,2))))
# modtow.m:252
                                            Ht[1,elenum]=str2num(list(val,arange(format(3,1),format(3,2)))) / 100
# modtow.m:253
                                            Ht[2,elenum]=str2num(list(val,arange(format(4,1),format(4,2)))) / 100
# modtow.m:254
                                            Ht[3,elenum]=str2num(list(val,arange(format(5,1),format(5,2)))) / 100
# modtow.m:255
                                            Ht[4,elenum]=0
# modtow.m:256
                                            MEt[elenum]=inf
# modtow.m:257
                                            if type_ == logical_or(2,type_) == 3:
                                                if Ht(1,elenum) == 1:
                                                    Ht[1,elenum]=wire_length
# modtow.m:260
                                                    Ht[4,elenum]=1
# modtow.m:261
                                                    mat=str2num(list(val,arange(format(7,1),format(7,2))))
# modtow.m:262
                                                    if mat == 1:
                                                        MEt[elenum]=138000000000.0
# modtow.m:264
                                                    else:
                                                        if mat == 2:
                                                            MEt[elenum]=345000000.0
# modtow.m:266
                                                        else:
                                                            if mat == 3:
                                                                MEt[elenum]=690000000.0
# modtow.m:268
                                                            else:
                                                                if mat == 4:
                                                                    MEt[elenum]=345000000.0
# modtow.m:270
                                                                else:
                                                                    if mat == 5:
                                                                        MEt[elenum]=690000000.0
# modtow.m:272
                                                                    else:
                                                                        if mat == 6:
                                                                            MEt[elenum]=69000000000.0
# modtow.m:274
                                                                        else:
                                                                            if mat == 7:
                                                                                MEt[elenum]=76000000000.0
# modtow.m:276
                                                                            else:
                                                                                if mat == 8:
                                                                                    MEt[elenum]=100000000000.0
# modtow.m:278
                                                else:
                                                    Ht[4,elenum]=2
# modtow.m:281
                                            Cdt[elenum]=str2num(list(val,arange(format(6,1),format(6,2))))
# modtow.m:284
                                            elenum=length(Bt) + 1
# modtow.m:285
                                            set(h_edit_elenum,'String',num2str(elenum))
                                        dismoor
                                        insert=0
# modtow.m:289
                                        delele=0
# modtow.m:290
                                    else:
                                        if command == 8:
                                            chele=str2num(get(h_edit_chele,'String'))
# modtow.m:292
                                        else:
                                            if command == 9:
                                                if logical_not(isempty(chele)):
                                                    if chele <= length(Ht(1,arange())):
                                                        wire_length=Ht(1,chele)
# modtow.m:296
                                                        getwirel
                                                        waitfor(h_edit_wirel)
                                                        Ht[1,chele]=wire_length
# modtow.m:299
                                            else:
                                                if command == 90:
                                                    close_(2)
                                                    if logical_not(isempty(Ht)):
                                                        dismoor
                                                    moordesign(3)
    
    if exist('h_edit_chele'):
        handle_list=concat([h_edit_elenum,h_edit_delele,h_menu_type,h_menu_list,h_edit_shsp,h_edit_afh,h_edit_chele])
# modtow.m:308
    else:
        handle_list=concat([h_edit_elenum,h_edit_delele,h_menu_type,h_menu_list,h_edit_shsp,h_edit_afh])
# modtow.m:310
    
    # fini