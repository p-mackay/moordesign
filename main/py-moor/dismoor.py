# Generated with SMOP  0.41-beta
from libsmop import *
# dismoor.m

    
@function
def dismoor(command=None,*args,**kwargs):
    varargin = dismoor.varargin
    nargin = dismoor.nargin

    # function to display the present mooring elements in the command window

    global moorele,H,B,ME,X,Y,Z,Ti,iobj,jobj,psi
    global HCO,BCO,CdCO,mooreleCO,ZCO,Iobj,Jobj,Pobj
    global Z0co,Zfco,Xfco,Yfco,psifco
    global Zoo
    global Ht,Bt,Cdt,MEt,moorelet,Usp,Vsp
    moorele=char(moorele)
# dismoor.m:10

    mooreleCO=char(mooreleCO)
# dismoor.m:11
    moorelet=char(moorelet)
# dismoor.m:12
    if nargin == 0:
        command=0
# dismoor.m:15

    line0='  0                                                                                                 '
# dismoor.m:17
    if logical_and(logical_not(isempty(H)),isempty(Ht)):
        mm,nm=size(moorele,nargout=2)
# dismoor.m:19
    else:
        moorele=copy(moorelet)
# dismoor.m:21
        H=copy(Ht)
# dismoor.m:22
        B=copy(Bt)
# dismoor.m:22
        ME=copy(MEt)
# dismoor.m:22
        mm,nm=size(moorelet,nargout=2)
# dismoor.m:23
        psisave=copy(psi)
# dismoor.m:24
        psi=pi - psi
# dismoor.m:24
        psi[1]=0
# dismoor.m:24

    io=0
# dismoor.m:27
    jo=0
# dismoor.m:28
    mz1,nz1=size(Z,nargout=2)
# dismoor.m:29
    mzo,nzo=size(Zoo,nargout=2)
# dismoor.m:30
    if mz1 == mzo:
        dZ=Zoo - Z
# dismoor.m:32
        dZco=Z0co - Zfco
# dismoor.m:33
    else:
        if mz1 == nzo:
            dZ=Zoo.T - Z
# dismoor.m:35
            dZco=Z0co.T - Zfco
# dismoor.m:36
    
    clear('line')
    if logical_and(logical_not(isempty(H)),isempty(Ht)):
        hdr1=' # Mooring Element   Length[m] Buoy[kg] Height[m]    dZ[m]   dX[m]   dY[m]   Tension[kg]   Angle[deg]'
# dismoor.m:40
        #     1234567891123456789212345678931234567894123456789512345678961234567897123456789812345678991234567890123
        if isempty(Z):
            hdr2='                                         (top)                               Top  Bottom   Top Bottom'
# dismoor.m:43
        else:
            hdr2='                                        (middle)                             Top  Bottom   Top Bottom'
# dismoor.m:45
    else:
        hdr1=' # Towed Element     Length[m] Buoy[kg]  Depth[m]    dZ[m]   dX[m]   dY[m]   Tension[kg]   Angle[deg]'
# dismoor.m:48
        #     1234567891123456789212345678931234567894123456789512345678961234567897123456789812345678991234567890123
        if isempty(Z):
            hdr2='                                        (bottom)                             Bottom  Top   Bottom Top'
# dismoor.m:51
        else:
            hdr2='                                        (middle)                             Bottom  Top   Bottom Top'
# dismoor.m:53
    
    # first display the In-Line mooring components, then do the Clamp-on, then tally up all components
    if command == 1:
        pf=figure(5)
# dismoor.m:59
        clf
        axis('off')
        fs=8
# dismoor.m:61
        set(pf,'PaperOrient','Portrait','PaperUnits','Normalized','PaperPosition',concat([0,0,1,1]),'Visible','on')
        dates=num2str(fix(clock),'%3.0f')
# dismoor.m:64
        dates[8]='/'
# dismoor.m:64
        dates[concat([14,17])]=':'
# dismoor.m:64
        tit=concat(['Mooring Design and Dynamics  ',dates])
# dismoor.m:65
        ht=title(tit)
# dismoor.m:66
        pos=get(ht,'Position')
# dismoor.m:67
        set(ht,'Position',concat([pos(1),dot(pos(2),1.02),pos(3)]),'Fontname','Courier New','FontSize',dot(fs,1.2))
        orient('tall')
        ypos=1 + 3 / 90
# dismoor.m:70
        h=text(- 0.1,ypos,'   In-Line')
# dismoor.m:71
        set(h,'Units','Normalized','Position',concat([- 0.075,ypos]),'Fontname','Courier New','FontSize',fs)
        ypos=1 + 2 / 90
# dismoor.m:73
        h=text(- 0.1,ypos,hdr1)
# dismoor.m:74
        set(h,'Units','Normalized','Position',concat([- 0.075,ypos]),'Fontname','Courier New','FontSize',fs)
        ypos=1 + 1 / 90
# dismoor.m:76
        h=text(- 0.1,ypos,hdr2)
# dismoor.m:77
        set(h,'Units','Normalized','Position',concat([- 0.075,ypos]),'Fontname','Courier New','FontSize',fs)
    else:
        disp(' ')
        disp('   In-Line')
        disp(hdr1)
        disp(hdr2)
        refresh
    
    
    ell=0
# dismoor.m:87
    jo=0
# dismoor.m:88
    io=0
# dismoor.m:88
    for el in arange(1,mm).reshape(-1):
        ell=ell + 1
# dismoor.m:90
        line=copy(line0)
# dismoor.m:91
        tmp=num2str(el)
# dismoor.m:92
        line[arange(4 - length(tmp),3)]=tmp
# dismoor.m:93
        line[arange(5,20)]=moorele(el,arange())
# dismoor.m:94
        tmp=num2str(H(1,el),'%8.2f')
# dismoor.m:95
        if logical_and(logical_not(isempty(Z)),H(4,el)) == 1:
            jo=jo + 1
# dismoor.m:97
            if (jo + 1) > length(jobj):
                tmp=num2str(dot(H(1,el),(1 + dot(2,(Ti(jobj(jo)) + Ti(jobj(jo) + 1))) / (dot(dot(pi,H(2,el) ** 2),ME(el))))),'%8.2f')
# dismoor.m:99
            else:
                tmp=num2str(dot(H(1,el),(1 + dot(2,(Ti(jobj(jo)) + Ti(jobj(jo + 1) + 1))) / (dot(dot(pi,H(2,el) ** 2),ME(el))))),'%8.2f')
# dismoor.m:101
        line[arange(31 - length(tmp),30)]=tmp
# dismoor.m:104
        tmp=num2str(B(el),'%8.2f')
# dismoor.m:105
        line[arange(40 - length(tmp),39)]=tmp
# dismoor.m:106
        if isempty(Z):
            hght=sum(H(1,arange(el,mm)))
# dismoor.m:108
            tmp=num2str(hght,'%8.2f')
# dismoor.m:109
            line[arange(50 - length(tmp),49)]=tmp
# dismoor.m:110
        else:
            if logical_and(logical_not(isempty(Z)),H(4,el)) != logical_and(1,el) != mm:
                io=io + 1
# dismoor.m:112
                tmp=num2str(Z(iobj(io)),'%8.2f')
# dismoor.m:113
                line[arange(50 - length(tmp),49)]=tmp
# dismoor.m:114
                tmp=num2str(dZ(iobj(io)),'%5.1f')
# dismoor.m:115
                line[arange(59 - length(tmp),58)]=tmp
# dismoor.m:116
                tmp=num2str(X(iobj(io)),'%5.1f')
# dismoor.m:117
                line[arange(67 - length(tmp),66)]=tmp
# dismoor.m:118
                tmp=num2str(Y(iobj(io)),'%5.1f')
# dismoor.m:119
                line[arange(75 - length(tmp),74)]=tmp
# dismoor.m:120
                tmp=num2str(Ti(iobj(io)) / 9.81,'%6.1f')
# dismoor.m:121
                line[arange(82 - length(tmp),81)]=tmp
# dismoor.m:122
                tmp=num2str(dot(psi(iobj(io)),180) / pi,'%4.1f')
# dismoor.m:123
                line[arange(95 - length(tmp),94)]=tmp
# dismoor.m:124
                tmp=num2str(Ti(iobj(io) + 1) / 9.81,'%6.1f')
# dismoor.m:125
                line[arange(89 - length(tmp),88)]=tmp
# dismoor.m:126
                tmp=num2str(dot(psi(iobj(io) + 1),180) / pi,'%4.1f')
# dismoor.m:127
                line[arange(101 - length(tmp),100)]=tmp
# dismoor.m:128
            else:
                if logical_and(logical_not(isempty(Z)),H(4,el)) == 1:
                    tmp=num2str(Ti(jobj(jo)) / 9.81,'%6.1f')
# dismoor.m:130
                    line[arange(82 - length(tmp),81)]=tmp
# dismoor.m:131
                    tmp=num2str(dot(psi(jobj(jo)),180) / pi,'%4.1f')
# dismoor.m:132
                    line[arange(95 - length(tmp),94)]=tmp
# dismoor.m:133
                    jo=jo + 1
# dismoor.m:134
                    tmp=num2str(Ti(jobj(jo) + 1) / 9.81,'%6.1f')
# dismoor.m:135
                    line[arange(89 - length(tmp),88)]=tmp
# dismoor.m:136
                    tmp=num2str(dot(psi(jobj(jo) + 1),180) / pi,'%4.1f')
# dismoor.m:137
                    line[arange(101 - length(tmp),100)]=tmp
# dismoor.m:138
        if logical_and(logical_not(isempty(Z)),el) == mm:
            io=io + 1
# dismoor.m:141
            tmp=num2str(Z(iobj(io)) / 2,'%8.2f')
# dismoor.m:142
            line[arange(50 - length(tmp),49)]=tmp
# dismoor.m:143
            tmp=num2str(dZ(iobj(io)),'%5.1f')
# dismoor.m:144
            line[arange(59 - length(tmp),58)]=tmp
# dismoor.m:145
            tmp=num2str(X(iobj(io)),'%5.1f')
# dismoor.m:146
            line[arange(67 - length(tmp),66)]=tmp
# dismoor.m:147
            tmp=num2str(Y(iobj(io)),'%5.1f')
# dismoor.m:148
            line[arange(75 - length(tmp),74)]=tmp
# dismoor.m:149
            tmp=num2str(Ti(end()) / 9.81,'%8.1f')
# dismoor.m:150
            line[arange(85 - length(tmp),84)]=tmp
# dismoor.m:151
            tmp=num2str(dot(psi(end()),180) / pi,'%4.1f')
# dismoor.m:152
            line[arange(95 - length(tmp),94)]=tmp
# dismoor.m:153
        if command == 1:
            figure(5)
            ypos=1 - ell / 90
# dismoor.m:157
            h=text(- 0.1,ypos,line)
# dismoor.m:158
            set(h,'Units','normalized','Position',concat([- 0.075,ypos]),'FontName','Courier New','FontSize',fs)
        else:
            disp(line)
        if command == logical_and(1,ell) == 80:
            ell=1
# dismoor.m:164
            figure(5)
            orient('tall')
            unis=get(gcf,'units')
# dismoor.m:167
            ppos=get(gcf,'paperposition')
# dismoor.m:168
            set(gcf,'units',get(gcf,'paperunits'))
            pos=get(gcf,'position')
# dismoor.m:170
            pos[arange(3,4)]=ppos(arange(3,4))
# dismoor.m:171
            set(gcf,'position',pos)
            set(gcf,'units',unis)
            print_ - f5 - v
            clf
            axis('off')
            orient('tall')
            ypos=1 + 3 / 90
# dismoor.m:177
            h=text(- 0.1,ypos,'   In-Line')
# dismoor.m:178
            set(h,'Units','Normalized','Position',concat([- 0.075,ypos]),'Fontname','Courier New','FontSize',fs)
            ypos=1 + 2 / 90
# dismoor.m:180
            h=text(- 0.1,ypos,hdr1)
# dismoor.m:181
            set(h,'Units','Normalized','Position',concat([- 0.075,ypos]),'Fontname','Courier New','FontSize',fs)
            ypos=1 + 1 / 90
# dismoor.m:183
            h=text(- 0.1,ypos,hdr2)
# dismoor.m:184
            set(h,'Units','Normalized','Position',concat([- 0.075,ypos]),'Fontname','Courier New','FontSize',fs)
    
    # now display any Clamp-On devices
    if logical_and(logical_not(isempty(H)),isempty(Ht)):
        hdr1=' #  Device Type    Attched to     m Up      Height[m]    dZ[m]   dX[m]   dY[m]   Angle[deg]'
# dismoor.m:191
        hdr2='                   Element #  This Element  (middle)'
# dismoor.m:193
    else:
        hdr1=' #  Device Type    Attched to     m Up      Depth [m]    dZ[m]   dX[m]   dY[m]   Angle[deg]'
# dismoor.m:195
        hdr2='                   Element #  This Element  (middle)'
# dismoor.m:197
    
    mm=0
# dismoor.m:200
    if logical_not(isempty(BCO)):
        mm=length(BCO)
# dismoor.m:201
    
    if mm > 0:
        ellz=ell + 2
# dismoor.m:203
        if command == 1:
            ypos=1 - ellz / 90
# dismoor.m:206
            h=text(- 0.1,ypos,'   Clamp-On Devices')
# dismoor.m:207
            set(h,'Units','Normalized','Position',concat([- 0.075,ypos]),'Fontname','Courier New','FontSize',fs)
            ellz=ellz + 1
# dismoor.m:209
            ypos=1 - ellz / 90
# dismoor.m:210
            h=text(- 0.1,ypos,hdr1)
# dismoor.m:211
            set(h,'Units','Normalized','Position',concat([- 0.075,ypos]),'Fontname','Courier New','FontSize',fs)
            ellz=ellz + 1
# dismoor.m:213
            ypos=1 - ellz / 90
# dismoor.m:214
            h=text(- 0.1,ypos,hdr2)
# dismoor.m:215
            set(h,'Units','Normalized','Position',concat([- 0.075,ypos]),'Fontname','Courier New','FontSize',fs)
        else:
            disp(' ')
            disp('   Clamp-On Devices')
            disp(hdr1)
            disp(hdr2)
            refresh
        ell=copy(ellz)
# dismoor.m:225
        for elco in arange(1,mm).reshape(-1):
            el=Jobj(elco)
# dismoor.m:227
            io=0
# dismoor.m:228
            jo=0
# dismoor.m:228
            for ellh in arange(1,el).reshape(-1):
                if H(4,ellh) != 1:
                    io=io + 1
# dismoor.m:230
                if H(4,ellh) == 1:
                    jo=jo + 1
# dismoor.m:231
            perc=Pobj(elco)
# dismoor.m:233
            ell=ell + 1
# dismoor.m:234
            line=copy(line0)
# dismoor.m:235
            tmp=num2str(elco)
# dismoor.m:236
            line[arange(4 - length(tmp),3)]=tmp
# dismoor.m:237
            line[arange(5,20)]=mooreleCO(elco,arange())
# dismoor.m:238
            line[arange(26 - length(num2str(Jobj(elco))),25)]=num2str(Jobj(elco))
# dismoor.m:239
            if logical_and(logical_not(isempty(Z)),H(4,el)) == 1:
                #      tmp=num2str(perc*H(1,el)*(1+2*(Ti(jobj(jo+1))+Ti(jobj(jo+2)+1))/(pi*H(2,el)^2*ME(el))),'#8.2f');
                tmp=num2str(dot(dot(perc,H(1,el)),(1 + dot(2,(Ti(jobj(jo)) + Ti(jobj(jo + 1) + 1))) / (dot(dot(pi,H(2,el) ** 2),ME(el))))),'%8.2f')
# dismoor.m:243
            else:
                tmp=num2str(dot(perc,H(1,el)),'%8.2f')
# dismoor.m:245
            line[arange(41 - length(tmp),40)]=tmp
# dismoor.m:247
            if isempty(Z):
                hght=ZCO(elco)
# dismoor.m:249
                tmp=num2str(hght,'%8.2f')
# dismoor.m:250
                line[arange(54 - length(tmp),53)]=tmp
# dismoor.m:251
            else:
                tmp=num2str(Zfco(elco),'%8.2f')
# dismoor.m:253
                line[arange(53 - length(tmp),52)]=tmp
# dismoor.m:254
                tmp=num2str(dZco(elco),'%6.2f')
# dismoor.m:255
                line[arange(63 - length(tmp),62)]=tmp
# dismoor.m:256
                tmp=num2str(Xfco(elco),'%5.1f')
# dismoor.m:257
                line[arange(71 - length(tmp),70)]=tmp
# dismoor.m:258
                tmp=num2str(Yfco(elco),'%5.1f')
# dismoor.m:259
                line[arange(79 - length(tmp),78)]=tmp
# dismoor.m:260
                tmp=num2str(dot(psifco(elco),180) / pi,'%4.1f')
# dismoor.m:261
                line[arange(89 - length(tmp),88)]=tmp
# dismoor.m:262
            if command == 1:
                figure(5)
                ypos=1 - ell / 90
# dismoor.m:266
                h=text(- 0.1,ypos,line)
# dismoor.m:267
                set(h,'Units','normalized','Position',concat([- 0.075,ypos]),'FontName','Courier New','FontSize',fs)
            else:
                disp(line)
            if command == logical_and(1,ell) == 80:
                ell=1
# dismoor.m:273
                figure(5)
                orient('tall')
                unis=get(gcf,'units')
# dismoor.m:276
                ppos=get(gcf,'paperposition')
# dismoor.m:277
                set(gcf,'units',get(gcf,'paperunits'))
                pos=get(gcf,'position')
# dismoor.m:279
                pos[arange(3,4)]=ppos(arange(3,4))
# dismoor.m:280
                set(gcf,'position',pos)
                set(gcf,'units',unis)
                print_ - f5 - v
                clf
                axis('off')
                orient('tall')
                ypos=1 + 3 / 90
# dismoor.m:286
                h=text(- 0.1,ypos,'   In-Line')
# dismoor.m:287
                set(h,'Units','Normalized','Position',concat([- 0.075,ypos]),'Fontname','Courier New','FontSize',fs)
                ypos=1 + 2 / 90
# dismoor.m:289
                h=text(- 0.1,ypos,hdr1)
# dismoor.m:290
                set(h,'Units','Normalized','Position',concat([- 0.075,ypos]),'Fontname','Courier New','FontSize',fs)
                ypos=1 + 1 / 90
# dismoor.m:292
                h=text(- 0.1,ypos,hdr2)
# dismoor.m:293
                set(h,'Units','Normalized','Position',concat([- 0.075,ypos]),'Fontname','Courier New','FontSize',fs)
    
    # now make a tally of all components
    mm,nm=size(moorele,nargout=2)
# dismoor.m:299
    
    moortally=zeros(mm,2)
# dismoor.m:300
    mt=0
# dismoor.m:301
    mtco=0
# dismoor.m:301
    if mm > 1:
        icnt=1
# dismoor.m:303
        moortally[icnt,arange(1,2)]=concat([1,1])
# dismoor.m:304
        for el in arange(2,mm).reshape(-1):
            ifound=0
# dismoor.m:306
            for j in arange(1,icnt).reshape(-1):
                if strcmp(moorele(moortally(j,1),arange()),moorele(el,arange())) == 1:
                    if H(4,el) != 1:
                        moortally[j,2]=moortally(j,2) + 1
# dismoor.m:310
                    else:
                        moortally[j,2]=moortally(j,2) + H(1,el)
# dismoor.m:312
                    ifound=1
# dismoor.m:314
            if ifound == 0:
                icnt=icnt + 1
# dismoor.m:318
                if H(4,el) != 1:
                    moortally[icnt,arange(1,2)]=concat([el,1])
# dismoor.m:320
                else:
                    moortally[icnt,arange(1,2)]=concat([el,H(1,el)])
# dismoor.m:322
        moortally=moortally(arange(1,icnt),arange())
# dismoor.m:326
        mmco=length(BCO)
# dismoor.m:328
        if mmco > 0:
            moortallyco=zeros(mmco,2)
# dismoor.m:330
            icnt=1
# dismoor.m:331
            moortallyco[icnt,arange(1,2)]=concat([1,1])
# dismoor.m:332
            if mmco > 1:
                for elco in arange(2,mmco).reshape(-1):
                    ifound=0
# dismoor.m:335
                    for j in arange(1,icnt).reshape(-1):
                        if strcmp(mooreleCO(moortallyco(j,1),arange()),mooreleCO(elco,arange())) == 1:
                            moortallyco[j,2]=moortallyco(j,2) + 1
# dismoor.m:338
                            ifound=1
# dismoor.m:339
                    if ifound == 0:
                        icnt=icnt + 1
# dismoor.m:343
                        moortallyco[icnt,arange(1,2)]=concat([elco,1])
# dismoor.m:344
            moortallyco=moortallyco(arange(1,icnt),arange())
# dismoor.m:348
            mtco,ntco=size(moortallyco,nargout=2)
# dismoor.m:349
        mt,nt=size(moortally,nargout=2)
# dismoor.m:351
        if mtco < 1:
            mtco=0
# dismoor.m:353
            hdr3=' Tally of all In-Line mooring/tow components by type.'
# dismoor.m:354
            hdr4=' #    Element Name        Total Number/Length'
# dismoor.m:355
        else:
            hdr3=' Tally of all In-Line mooring/tow components by type       and       Clamp-on Devices.'
# dismoor.m:358
            hdr4=' #    Element Name        Total Number/Length          #   Device Name       Total Number'
# dismoor.m:359
        if command == 1:
            ypos=(mt + 2) / 90 - 0.1
# dismoor.m:363
            h=text(- 0.1,ypos,hdr3)
# dismoor.m:364
            set(h,'Units','Normalized','Position',concat([- 0.075,ypos]),'Fontname','Courier New','FontSize',fs)
            ypos=(mt + 1) / 90 - 0.1
# dismoor.m:366
            h=text(- 0.1,ypos,hdr4)
# dismoor.m:367
            set(h,'Units','Normalized','Position',concat([- 0.075,ypos]),'Fontname','Courier New','FontSize',fs)
        else:
            disp(' ')
            disp(hdr3)
            disp(hdr4)
        ii=0
# dismoor.m:374
        for i in arange(1,mt).reshape(-1):
            ii=ii + 1
# dismoor.m:376
            line=copy(line0)
# dismoor.m:377
            line[1]=' '
# dismoor.m:378
            line[arange(4 - length(num2str(i)),3)]=num2str(i)
# dismoor.m:379
            line[arange(6,21)]=moorele(moortally(i,1),arange())
# dismoor.m:380
            line[arange(31 - length(num2str(moortally(i,2),6)),30)]=num2str(moortally(i,2),6)
# dismoor.m:381
            if ii <= mtco:
                line[arange(57 - length(num2str(ii)),56)]=num2str(ii)
# dismoor.m:383
                line[arange(60,75)]=mooreleCO(moortallyco(ii,1),arange())
# dismoor.m:384
                line[arange(87 - length(num2str(moortallyco(ii,2))),86)]=num2str(moortallyco(ii,2))
# dismoor.m:385
            if H(4,moortally(i,1)) == 1:
                line[32]='m'
# dismoor.m:387
            if command == 1:
                figure(5)
                ypos=(mt - i) / 90 - 0.1
# dismoor.m:390
                h=text(- 0.1,ypos,line)
# dismoor.m:391
                set(h,'Units','normalized','Position',concat([- 0.075,ypos]),'FontName','Courier New','FontSize',fs)
            else:
                disp(line)
        if mtco > mt:
            iii=copy(ii)
# dismoor.m:398
            for ii in arange(iii + 1,length(BCO)).reshape(-1):
                line=copy(line0)
# dismoor.m:400
                line[1]=' '
# dismoor.m:401
                line[arange(57 - length(num2str(ii)),56)]=num2str(ii)
# dismoor.m:402
                line[arange(60,75)]=mooreleCO(moortallyco(ii,1),arange())
# dismoor.m:403
                line[arange(87 - length(num2str(moortallyco(ii,2))),86)]=num2str(moortally(ii,2))
# dismoor.m:404
                if command == 1:
                    figure(5)
                    ypos=(mt - i) / 90 - 0.1
# dismoor.m:407
                    h=text(- 0.1,ypos,line)
# dismoor.m:408
                    set(h,'Units','normalized','Position',concat([- 0.075,ypos]),'FontName','Courier New','FontSize',fs)
                else:
                    disp(line)
    
    
    if command == 1:
        figure(5)
        orient('tall')
        unis=get(gcf,'units')
# dismoor.m:421
        ppos=get(gcf,'paperposition')
# dismoor.m:422
        set(gcf,'units',get(gcf,'paperunits'))
        pos=get(gcf,'position')
# dismoor.m:424
        pos[arange(3,4)]=ppos(arange(3,4))
# dismoor.m:425
        set(gcf,'position',pos)
        set(gcf,'units',unis)
        print_ - f5 - v
        close_(5)
    else:
        disp(' ')
    
    if logical_not(isempty(Ht)):
        moorele=[]
# dismoor.m:435
        H=[]
# dismoor.m:435
        B=[]
# dismoor.m:435
        ME=[]
# dismoor.m:435
        psi=copy(psisave)
# dismoor.m:435
    
    drawnow
    # fini
