# Generated with SMOP  0.41-beta
from libsmop import *
# addelement.m

    
@function
def addelement(command=None,*args,**kwargs):
    varargin = addelement.varargin
    nargin = addelement.nargin

    # Program to make a GUI for modifying a mooring element in the database
    
    global U,V,W,z,rho
    global H,B,Cd,ME,moorele
    global floats,wires,chains,acrels,cms,anchors,miscs,format
    global typelist,type_,list,addel,mat
    global h_menu_type,h_menu_list,h_menu_addel,h_menu_material
    global h_push_add,h_edit_elename,h_edit_elebuoy,h_edit_eledim,h_edit_elecd
    global fs
    
    if nargin < 1:
        command=0
# addelement.m:12
    
    if isempty(addel):
        addel=1
# addelement.m:13
    
    if command == 0:
        if isempty(floats):
            ifile,ipath=uigetfile('*.mat','Load MDCODES.MAT (cancel loads default)',nargout=2)
# addelement.m:16
            if logical_and(ischar(ifile),ischar(ipath)):
                if logical_not(strcmp(ifile,'*.mat')):
                    load(concat([ipath,ifile]))
                else:
                    load('mdcodes')
            else:
                if ifile == logical_and(0,ipath) == 0:
                    load('mdcodes')
            clear('ifile','ipath')
        list=copy(floats)
# addelement.m:28
        type_=1
# addelement.m:29
        typelist='*'
# addelement.m:30
        me,ne=size(list,nargout=2)
# addelement.m:31
        for ii in arange(1,me).reshape(-1):
            typelist[arange((dot((ii - 1),17) + 1),(dot((ii - 1),17) + 17))]=concat([list(ii,arange(1,16)),'|'])
# addelement.m:33
        typelist=typelist(arange(1,length(typelist) - 1))
# addelement.m:35
        figure(4)
        clf
        set(gcf,'Units','Normalized','Position',concat([0.05,0.02,0.35,0.4]),'Name','Add/Delete Elements','Color',concat([0.8,0.8,0.8]),'tag','modmoor')
        h_menu_type=uicontrol('Style','popupmenu','Callback','addelement(1)','FontSize',fs,'String',concat(['Floatation|Wire|Chain+Shackles|Current Meter|Acoustic Release|Anchor|Misc Instrument']),'Units','Normalized','Position',concat([0.1,0.875,0.8,0.1]))
# addelement.m:42
        h_menu_list=uicontrol('Style','popupmenu','Callback','addelement(2)','FontSize',fs,'String',typelist,'Units','Normalized','Position',concat([0.1,0.785,0.8,0.1]))
# addelement.m:47
        h_menu_addel=uicontrol('Style','popupmenu','Callback','addelement(2)','FontSize',fs,'String','Examine|Add Element|Delete Element|Modify Element','Units','Normalized','Position',concat([0.3,0.695,0.4,0.1]))
# addelement.m:52
        h_text_ele=uicontrol('Style','text','String','Element Name(16):','FontSize',fs,'Units','Normalized','Position',concat([0.05,0.6,0.3,0.08]))
# addelement.m:57
        h_edit_elename=uicontrol('Style','edit','String',' ','FontSize',fs,'Units','Normalized','Position',concat([0.45,0.6,0.5,0.08]))
# addelement.m:61
        h_text_elebuoy=uicontrol('Style','text','String','Buoyancy [kg]','FontSize',fs,'Units','Normalized','Position',concat([0.05,0.51,0.3,0.08]))
# addelement.m:65
        h_edit_elebuoy=uicontrol('Style','edit','String',' ','FontSize',fs,'Units','Normalized','Position',concat([0.45,0.51,0.5,0.08]))
# addelement.m:69
        h_text_eledim=uicontrol('Style','text','String','Dimensions [cm]','FontSize',fs,'Units','Normalized','Position',concat([0.05,0.42,0.3,0.08]))
# addelement.m:73
        h_edit_eledim=uicontrol('Style','edit','String',' ','FontSize',fs,'Units','Normalized','Position',concat([0.45,0.42,0.5,0.08]))
# addelement.m:77
        h_text_elecd=uicontrol('Style','text','String','Drag Coeff:','FontSize',fs,'Units','Normalized','Position',concat([0.05,0.33,0.3,0.08]))
# addelement.m:81
        h_edit_elecd=uicontrol('Style','edit','String',' ','FontSize',fs,'Units','Normalized','Position',concat([0.45,0.33,0.5,0.08]))
# addelement.m:85
        h_text_material=uicontrol('Style','text','String','Material','FontSize',fs,'Units','Normalized','Position',concat([0.05,0.22,0.3,0.08]))
# addelement.m:89
        h_menu_material=uicontrol('Style','popupmenu','Callback','addelement(3)','FontSize',fs,'String',concat(['Steel|Nylon|Dacron|Polypropylene|Polyethylene|Kevlar|Aluminum|Dyneema']),'Units','Normalized','Position',concat([0.45,0.22,0.4,0.08]))
# addelement.m:93
        h_push_help=uicontrol('Style','Pushbutton','String','Help','FontSize',fs,'Units','normalized','Position',concat([0.4,0.1,0.2,0.08]),'Callback','addelement(7)')
# addelement.m:98
        h_push_save=uicontrol('Style','Pushbutton','String','Save','FontSize',fs,'Units','normalized','Position',concat([0.75,0.1,0.2,0.08]),'Callback','addelement(6)')
# addelement.m:103
        hmaincls=uicontrol('Style','Pushbutton','String','Close','FontSize',fs,'Units','normalized','Position',concat([0.3,0.01,0.4,0.08]),'Callback','close')
# addelement.m:108
    
    if command == 2:
        addel=get(h_menu_addel,'Value')
# addelement.m:115
    
    if command == logical_or(1,command) == 2:
        if addel == 1:
            h_push_add=uicontrol('Style','Pushbutton','String','No Action','FontSize',fs,'Units','normalized','Position',concat([0.05,0.1,0.2,0.08]),'Callback','addelement(1)')
# addelement.m:119
        else:
            if addel == 2:
                h_push_add=uicontrol('Style','Pushbutton','String','Add','FontSize',fs,'Units','normalized','Position',concat([0.05,0.1,0.2,0.08]),'Callback','addelement(4)')
# addelement.m:125
            else:
                if addel == 3:
                    h_push_add=uicontrol('Style','Pushbutton','String','Delete','FontSize',fs,'Units','normalized','Position',concat([0.05,0.1,0.2,0.08]),'Callback','addelement(5)')
# addelement.m:131
                else:
                    if addel == 4:
                        h_push_add=uicontrol('Style','Pushbutton','String','Modify','FontSize',fs,'Units','normalized','Position',concat([0.05,0.1,0.2,0.08]),'Callback','addelement(8)')
# addelement.m:137
    
    if command == 1:
        clear('typelist')
        type_=get(h_menu_type,'Value')
# addelement.m:146
        if type_ == 1:
            list=copy(floats)
# addelement.m:148
        else:
            if type_ == 2:
                list=copy(wires)
# addelement.m:150
            else:
                if type_ == 3:
                    list=copy(chains)
# addelement.m:152
                else:
                    if type_ == 4:
                        list=copy(cms)
# addelement.m:154
                    else:
                        if type_ == 5:
                            list=copy(acrels)
# addelement.m:156
                        else:
                            if type_ == 6:
                                list=copy(anchors)
# addelement.m:158
                            else:
                                if type_ == 7:
                                    list=copy(miscs)
# addelement.m:160
        me,ne=size(list,nargout=2)
# addelement.m:162
        for ii in arange(1,me).reshape(-1):
            typelist[arange((dot((ii - 1),17) + 1),(dot((ii - 1),17) + 17))]=concat([list(ii,arange(1,16)),'|'])
# addelement.m:164
        typelist=typelist(arange(1,length(typelist) - 1))
# addelement.m:166
        set(h_menu_list,'Value',1)
        set(h_menu_list,'String',typelist)
    else:
        if command == 3:
            mat=get(h_menu_material,'Value')
# addelement.m:170
        else:
            if command == 4:
                if addel == 2:
                    name=get(h_edit_elename,'String')
# addelement.m:173
                    buoy=str2num(get(h_edit_elebuoy,'String'))
# addelement.m:174
                    dim=str2num(get(h_edit_eledim,'String'))
# addelement.m:175
                    cd=str2num(get(h_edit_elecd,'String'))
# addelement.m:176
                    mat=get(h_menu_material,'Value')
# addelement.m:177
                    if logical_and(logical_and(logical_not(strcmp(name,' ')),logical_not(isempty(buoy))),length(dim)) == logical_and(3,logical_not(isempty(cd))):
                        if logical_and(logical_and(logical_and(logical_and((buoy >= logical_and(- 9999.99,buoy) <= 9999.99),(dim(1) <= logical_and(9999,dim(1)) >= 0)),(dim(2) <= logical_and(1000,dim(2)) >= 0)),(dim(3) <= logical_and(1000,dim(3)) >= 0)),(cd >= logical_and(0,cd) <= 100)):
                            text='*                '
# addelement.m:184
                            #12345678901234567
                            lname=min(concat([length(name),16]))
# addelement.m:186
                            if length(name) > 16:
                                disp('Warning: Element Name has too many characters! Limited to 16.')
                            text[arange(1,lname)]=name(arange(1,lname))
# addelement.m:188
                            tbuoy='        '
# addelement.m:189
                            if abs(buoy) < 999:
                                buoy=num2str(buoy,'%8.3f')
# addelement.m:191
                            else:
                                buoy=num2str(buoy,'%8.2f')
# addelement.m:193
                            tbuoy[arange((9 - length(buoy)),8)]=buoy
# addelement.m:195
                            tdim='                  '
# addelement.m:196
                            if dim(1) < 1000:
                                dim1=num2str(dim(1),'%5.1f')
# addelement.m:198
                            else:
                                dim1=num2str(dim(1),'%5.0f')
# addelement.m:200
                            tdim[arange((7 - length(dim1)),6)]=dim1
# addelement.m:202
                            dim2=num2str(dim(2),'%5.1f')
# addelement.m:203
                            tdim[arange((13 - length(dim2)),12)]=dim2
# addelement.m:204
                            dim3=num2str(dim(3),'%5.1f')
# addelement.m:205
                            tdim[arange((19 - length(dim3)),18)]=dim3
# addelement.m:206
                            tcd='     '
# addelement.m:207
                            cd=num2str(cd,'%4.2f')
# addelement.m:208
                            tcd[arange((6 - length(cd)),5)]=cd
# addelement.m:209
                            tmat='  '
# addelement.m:210
                            mat=num2str(mat,'%1.0f')
# addelement.m:211
                            tmat[2]=mat
# addelement.m:212
                            newele=concat([text,tbuoy,tdim,tcd,tmat])
# addelement.m:213
                            type_=get(h_menu_type,'Value')
# addelement.m:214
                            already=0
# addelement.m:215
                            if type_ == 1:
                                m,n=size(floats,nargout=2)
# addelement.m:217
                                for ii in arange(1,m).reshape(-1):
                                    if sum(strcmp(text,floats(ii,arange(1,17)))) != 0:
                                        already=1
# addelement.m:220
                                if already == 0:
                                    floats[m + 1,arange()]=newele
# addelement.m:224
                                    floats
                                else:
                                    disp('That element name is in use already.')
                            else:
                                if type_ == 2:
                                    m,n=size(wires,nargout=2)
# addelement.m:230
                                    for ii in arange(1,m).reshape(-1):
                                        if sum(strcmp(text,wires(ii,arange(1,17)))) != 0:
                                            already=1
# addelement.m:233
                                    if already == 0:
                                        wires[m + 1,arange()]=newele
# addelement.m:237
                                        wires
                                    else:
                                        disp('That element name is in use already.')
                                else:
                                    if type_ == 3:
                                        m,n=size(chains,nargout=2)
# addelement.m:243
                                        for ii in arange(1,m).reshape(-1):
                                            if sum(strcmp(text,chains(ii,arange(1,17)))) != 0:
                                                already=1
# addelement.m:246
                                        if already == 0:
                                            chains[m + 1,arange()]=newele
# addelement.m:250
                                            chains
                                        else:
                                            disp('That element name is in use already.')
                                    else:
                                        if type_ == 4:
                                            m,n=size(cms,nargout=2)
# addelement.m:256
                                            for ii in arange(1,m).reshape(-1):
                                                if sum(strcmp(text,cms(ii,arange(1,17)))) != 0:
                                                    already=1
# addelement.m:259
                                            if already == 0:
                                                cms[m + 1,arange()]=newele
# addelement.m:263
                                                cms
                                            else:
                                                disp('That element name is in use already.')
                                        else:
                                            if type_ == 5:
                                                m,n=size(acrels,nargout=2)
# addelement.m:269
                                                for ii in arange(1,m).reshape(-1):
                                                    if sum(strcmp(text,acrels(ii,arange(1,17)))) != 0:
                                                        already=1
# addelement.m:272
                                                if already == 0:
                                                    acrels[m + 1,arange()]=newele
# addelement.m:276
                                                    acrels
                                                else:
                                                    disp('That element name is in use already.')
                                            else:
                                                if type_ == 6:
                                                    m,n=size(anchors,nargout=2)
# addelement.m:282
                                                    for ii in arange(1,m).reshape(-1):
                                                        if sum(strcmp(text,anchors(ii,arange(1,17)))) != 0:
                                                            already=1
# addelement.m:285
                                                    if already == 0:
                                                        anchors[m + 1,arange()]=newele
# addelement.m:289
                                                        anchors
                                                    else:
                                                        disp('That element name is in use already.')
                                                else:
                                                    if type_ == 7:
                                                        m,n=size(miscs,nargout=2)
# addelement.m:295
                                                        for ii in arange(1,m).reshape(-1):
                                                            if sum(strcmp(text,miscs(ii,arange(1,17)))) != 0:
                                                                already=1
# addelement.m:298
                                                        if already == 0:
                                                            newele
                                                            miscs[m + 1,arange()]=newele
# addelement.m:303
                                                            miscs
                                                        else:
                                                            disp('That element name is in use already.')
                            addelement(1)
                        else:
                            disp('Check format and range of allowable values (moordyn.txt)')
                            name
                            buoy
                            dim
                            cd
                    else:
                        disp('Didn't get all the necessary information/within bounds...')
                        name
                        buoy
                        dim
                        cd
                addel=1
# addelement.m:319
                set(h_menu_addel,'Value',1)
                h_push_add=uicontrol('Style','Pushbutton','String','No Action','FontSize',fs,'Units','normalized','Position',concat([0.05,0.1,0.2,0.08]),'Callback','addelement(1)')
# addelement.m:321
            else:
                if command == 5:
                    if addel == 3:
                        val=get(h_menu_list,'Value')
# addelement.m:328
                        type_=get(h_menu_type,'Value')
# addelement.m:329
                        if type_ == 1:
                            m,n=size(floats,nargout=2)
# addelement.m:331
                            if val == 1:
                                id=(arange(2,m))
# addelement.m:333
                            else:
                                if val > logical_and(1,val) < m:
                                    id=concat([(arange(1,val - 1)),(arange(val + 1,m))])
# addelement.m:335
                                else:
                                    if val == m:
                                        id=(arange(1,m - 1))
# addelement.m:337
                            disp(concat(['!! I am deleting: ',floats(val,arange())]))
                            floats=floats(id,arange())
# addelement.m:340
                        else:
                            if type_ == 2:
                                m,n=size(wires,nargout=2)
# addelement.m:342
                                if val == 1:
                                    id=(arange(2,m))
# addelement.m:344
                                else:
                                    if val > logical_and(1,val) < m:
                                        id=concat([(arange(1,val - 1)),(arange(val + 1,m))])
# addelement.m:346
                                    else:
                                        if val == m:
                                            id=(arange(1,m - 1))
# addelement.m:348
                                disp(concat(['!! I am deleting: ',wires(val,arange())]))
                                wires=wires(id,arange())
# addelement.m:351
                            else:
                                if type_ == 3:
                                    m,n=size(chains,nargout=2)
# addelement.m:353
                                    if val == 1:
                                        id=(arange(2,m))
# addelement.m:355
                                    else:
                                        if val > logical_and(1,val) < m:
                                            id=concat([(arange(1,val - 1)),(arange(val + 1,m))])
# addelement.m:357
                                        else:
                                            if val == m:
                                                id=(arange(1,m - 1))
# addelement.m:359
                                    disp(concat(['!! I am deleting: ',chains(val,arange())]))
                                    chains=chains(id,arange())
# addelement.m:362
                                else:
                                    if type_ == 4:
                                        m,n=size(cms,nargout=2)
# addelement.m:364
                                        if val == 1:
                                            id=(arange(2,m))
# addelement.m:366
                                        else:
                                            if val > logical_and(1,val) < m:
                                                id=concat([(arange(1,val - 1)),(arange(val + 1,m))])
# addelement.m:368
                                            else:
                                                if val == m:
                                                    id=(arange(1,m - 1))
# addelement.m:370
                                        disp(concat(['!! I am deleting: ',cms(val,arange())]))
                                        cms=cms(id,arange())
# addelement.m:373
                                    else:
                                        if type_ == 5:
                                            m,n=size(acrels,nargout=2)
# addelement.m:375
                                            if val == 1:
                                                id=(arange(2,m))
# addelement.m:377
                                            else:
                                                if val > logical_and(1,val) < m:
                                                    id=concat([(arange(1,val - 1)),(arange(val + 1,m))])
# addelement.m:379
                                                else:
                                                    if val == m:
                                                        id=(arange(1,m - 1))
# addelement.m:381
                                            disp(concat(['!! I am deleting: ',acrels(val,arange())]))
                                            acrels=acrels(id,arange())
# addelement.m:384
                                        else:
                                            if type_ == 6:
                                                m,n=size(anchors,nargout=2)
# addelement.m:386
                                                if val == 1:
                                                    id=(arange(2,m))
# addelement.m:388
                                                else:
                                                    if val > logical_and(1,val) < m:
                                                        id=concat([(arange(1,val - 1)),(arange(val + 1,m))])
# addelement.m:390
                                                    else:
                                                        if val == m:
                                                            id=(arange(1,m - 1))
# addelement.m:392
                                                disp(concat(['!! I am deleting: ',anchors(val,arange())]))
                                                anchors=anchors(id,arange())
# addelement.m:395
                                            else:
                                                if type_ == 7:
                                                    m,n=size(miscs,nargout=2)
# addelement.m:397
                                                    if val == 1:
                                                        id=(arange(2,m))
# addelement.m:399
                                                    else:
                                                        if val > logical_and(1,val) < m:
                                                            id=concat([(arange(1,val - 1)),(arange(val + 1,m))])
# addelement.m:401
                                                        else:
                                                            if val == m:
                                                                id=(arange(1,m - 1))
# addelement.m:403
                                                    disp(concat(['!! I am deleting: ',miscs(val,arange())]))
                                                    miscs=miscs(id,arange())
# addelement.m:406
                        disp('!! Don't SAVE unless you're sure of this deletion !!')
                        addelement(1)
                    addel=1
# addelement.m:411
                    set(h_menu_addel,'Value',1)
                    h_push_add=uicontrol('Style','Pushbutton','String','No Action','FontSize',fs,'Units','normalized','Position',concat([0.05,0.1,0.2,0.08]),'Callback','addelement(1)')
# addelement.m:413
                else:
                    if command == 6:
                        disp('Saving a new MDCODES.MAT File! Should go into mooring directory.')
                        ofile,opath=uiputfile('mdcodes.mat','Save A New MDCODES.MAT',nargout=2)
# addelement.m:420
                        if logical_not(isempty(ofile)):
                            save(concat([opath,ofile]),'acrels','cms','format','miscs','anchors','chains','floats','wires')
                        else:
                            disp('No Database file saved. Check file name.')
                        clear('ofile','opath')
                        addelement(1)
                    else:
                        if command == 7:
                            load('addelehelp')
                            h_help=msgbox(addhelp)
# addelement.m:430
                            set(h_help,'Units','Normalized','Position',concat([0.35,0.01,0.6,0.95]))
                            clear('addhelp')
                        else:
                            if command == 8:
                                if addel == 4:
                                    name=get(h_edit_elename,'String')
# addelement.m:435
                                    buoy=str2num(get(h_edit_elebuoy,'String'))
# addelement.m:436
                                    dim=str2num(get(h_edit_eledim,'String'))
# addelement.m:437
                                    cd=str2num(get(h_edit_elecd,'String'))
# addelement.m:438
                                    mat=get(h_menu_material,'Value')
# addelement.m:439
                                    if logical_and(logical_and(logical_not(strcmp(name,' ')),logical_not(isempty(buoy))),length(dim)) == logical_and(3,logical_not(isempty(cd))):
                                        if logical_and(logical_and(logical_and(logical_and((buoy > logical_and(- 10000,buoy) < 10000),(dim(1) <= logical_and(9999,dim(1)) >= 0)),(dim(2) <= logical_and(9999,dim(2)) >= 0)),(dim(3) <= logical_and(9999,dim(3)) >= 0)),(cd >= logical_and(0,cd) <= 10)):
                                            text='*                '
# addelement.m:446
                                            #12345678901234567
                                            text[arange(1,length(name))]=name
# addelement.m:448
                                            tbuoy='        '
# addelement.m:449
                                            if abs(buoy) < 999:
                                                buoy=num2str(buoy,'%8.3f')
# addelement.m:451
                                            else:
                                                buoy=num2str(buoy,'%8.2f')
# addelement.m:453
                                            tbuoy[arange((9 - length(buoy)),8)]=buoy
# addelement.m:455
                                            tdim='                  '
# addelement.m:456
                                            if dim(1) < 1000:
                                                dim1=num2str(dim(1),'%5.1f')
# addelement.m:458
                                            else:
                                                dim1=num2str(dim(1),'%5.0f')
# addelement.m:460
                                            tdim[arange((7 - length(dim1)),6)]=dim1
# addelement.m:462
                                            dim2=num2str(dim(2),'%5.1f')
# addelement.m:463
                                            tdim[arange((13 - length(dim2)),12)]=dim2
# addelement.m:464
                                            dim3=num2str(dim(3),'%5.1f')
# addelement.m:465
                                            tdim[arange((19 - length(dim3)),18)]=dim3
# addelement.m:466
                                            tcd='     '
# addelement.m:467
                                            cd=num2str(cd,'%4.2f')
# addelement.m:468
                                            tcd[arange((6 - length(cd)),5)]=cd
# addelement.m:469
                                            tmat='  '
# addelement.m:470
                                            mat=num2str(mat,'%1.0f')
# addelement.m:471
                                            tmat[2]=mat
# addelement.m:472
                                            newele=concat([text,tbuoy,tdim,tcd,tmat])
# addelement.m:473
                                            type_=get(h_menu_type,'Value')
# addelement.m:474
                                            already=0
# addelement.m:475
                                            if type_ == 1:
                                                m,n=size(floats,nargout=2)
# addelement.m:477
                                                for ii in arange(1,m).reshape(-1):
                                                    if sum(strcmp(text,floats(ii,arange(1,17)))) != 0:
                                                        already=1
# addelement.m:480
                                                        imod=copy(ii)
# addelement.m:481
                                                if already == 1:
                                                    disp('Modifying float element characteristics ! ')
                                                    floats[imod,arange()]=newele
# addelement.m:486
                                                    floats
                                            else:
                                                if type_ == 2:
                                                    m,n=size(wires,nargout=2)
# addelement.m:490
                                                    for ii in arange(1,m).reshape(-1):
                                                        if sum(strcmp(text,wires(ii,arange(1,17)))) != 0:
                                                            already=1
# addelement.m:493
                                                            imod=copy(ii)
# addelement.m:494
                                                    if already == 1:
                                                        disp('Modifying wire/rope element characteristics ! ')
                                                        wires[imod,arange()]=newele
# addelement.m:499
                                                        wires
                                                else:
                                                    if type_ == 3:
                                                        m,n=size(chains,nargout=2)
# addelement.m:503
                                                        for ii in arange(1,m).reshape(-1):
                                                            if sum(strcmp(text,chains(ii,arange(1,17)))) != 0:
                                                                already=1
# addelement.m:506
                                                                imod=copy(ii)
# addelement.m:507
                                                        if already == 1:
                                                            disp('Modifying chain/shackle element characteristics ! ')
                                                            chains[imod,arange()]=newele
# addelement.m:512
                                                            chains
                                                    else:
                                                        if type_ == 4:
                                                            m,n=size(cms,nargout=2)
# addelement.m:516
                                                            for ii in arange(1,m).reshape(-1):
                                                                if sum(strcmp(text,cms(ii,arange(1,17)))) != 0:
                                                                    already=1
# addelement.m:519
                                                                    imod=copy(ii)
# addelement.m:520
                                                            if already == 1:
                                                                disp('Modifying current meter element characteristics ! ')
                                                                cms[imod,arange()]=newele
# addelement.m:525
                                                                cms
                                                        else:
                                                            if type_ == 5:
                                                                m,n=size(acrels,nargout=2)
# addelement.m:529
                                                                for ii in arange(1,m).reshape(-1):
                                                                    if sum(strcmp(text,acrels(ii,arange(1,17)))) != 0:
                                                                        already=1
# addelement.m:532
                                                                        imod=copy(ii)
# addelement.m:533
                                                                if already == 1:
                                                                    disp('Modifying acoustic release element characteristics ! ')
                                                                    acrels[imod,arange()]=newele
# addelement.m:538
                                                                    acrels
                                                            else:
                                                                if type_ == 6:
                                                                    m,n=size(anchors,nargout=2)
# addelement.m:542
                                                                    for ii in arange(1,m).reshape(-1):
                                                                        if sum(strcmp(text,anchors(ii,arange(1,17)))) != 0:
                                                                            already=1
# addelement.m:545
                                                                            imod=copy(ii)
# addelement.m:546
                                                                    if already == 1:
                                                                        disp('Modifying anchor element characteristics ! ')
                                                                        anchors[imod,arange()]=newele
# addelement.m:551
                                                                        anchors
                                                                else:
                                                                    if type_ == 7:
                                                                        m,n=size(miscs,nargout=2)
# addelement.m:555
                                                                        for ii in arange(1,m).reshape(-1):
                                                                            if sum(strcmp(text,miscs(ii,arange(1,17)))) != 0:
                                                                                already=1
# addelement.m:558
                                                                                imod=copy(ii)
# addelement.m:559
                                                                        if already == 1:
                                                                            disp('Modifying miscellaneous element characteristics ! ')
                                                                            miscs[imod,arange()]=newele
# addelement.m:564
                                                                            miscs
                                            addelement(1)
                                        else:
                                            disp('Check format and range of allowable values.')
                                            name
                                            buoy
                                            dim
                                            cd
                                    else:
                                        disp('Didn't get all the necessary information...')
                                        name
                                        buoy
                                        dim
                                        cd
                                addel=1
# addelement.m:578
                                set(h_menu_addel,'Value',1)
                                h_push_add=uicontrol('Style','Pushbutton','String','No Action','FontSize',fs,'Units','normalized','Position',concat([0.05,0.1,0.2,0.08]),'Callback','addelement(1)')
# addelement.m:580
    
    if command == logical_or(1,command) == 2:
        val=get(h_menu_list,'Value')
# addelement.m:588
        ele=list(val,arange(format(1,1),format(1,2)))
# addelement.m:589
        buoy=list(val,arange(format(2,1),format(2,2)))
# addelement.m:590
        dim=list(val,arange(format(3,1),format(5,2)))
# addelement.m:591
        cd=list(val,arange(format(6,1),format(6,2)))
# addelement.m:592
        mat=str2num(list(val,arange(format(7,1),format(7,2))))
# addelement.m:593
        set(h_edit_elename,'String',ele)
        set(h_edit_elebuoy,'String',buoy)
        set(h_edit_eledim,'String',dim)
        set(h_edit_elecd,'String',cd)
        set(h_menu_material,'Value',mat)
    
    # fini