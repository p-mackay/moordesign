# Generated with SMOP  0.41-beta
from libsmop import *
# makemovie.m

    
@function
def makemovie(command=None,*args,**kwargs):
    varargin = makemovie.varargin
    nargin = makemovie.nargin

    # function to make a movie/time series of mooring component positions
    global U,V,W,z,rho,time,uw,vw
    global H,B,Cd,moorele,ME
    global Hs,Bs,Cds,mooreles,MEs
    global X,Y,Z,Ti,iobj,jobj,psi
    global ZCO,HCO,BCO,CdCO,mooreleCO,Iobj,Pobj,Jobj
    global ZCOs,HCOs,BCOs,CdCOs,mooreleCOs,Iobjs,Pobjs,Jobjs
    global Z0co,Zfco,Xfco,Yfco,psifco
    global Zcots,Xcots,Ycots,psicots,Iobjts,Jobjts,Pobjts
    global Xts,Yts,Zts,Tits,psits,iobjts,M,figs,ts
    global h_edit_times,h_edit_fps,h_edit_angle,h_edit_elevation,h_edit_plttitle,h_edit_time,h_edit_xmax,h_edit_figs
    global times,fps,az,el,tmin,tmax,xmax,nomovie,tit
    global its,tindx
    global fs
    fontsz=11
# makemovie.m:18
    if isempty('fs'):
        fs=12
# makemovie.m:19
    
    if nargin == 0:
        command=0
# makemovie.m:20
    
    if logical_and(isempty(tmin),logical_not(isempty(time))):
        tmin=min(time)
# makemovie.m:22
        tmax=max(time)
# makemovie.m:23
    
    if command == 5:
        az=340
# makemovie.m:26
        el=20
# makemovie.m:27
        xmax=100
# makemovie.m:28
        figs=1.0
# makemovie.m:29
        tit='Mooring Design and Dynamics'
# makemovie.m:30
    
    if command == 2:
        if isempty(times):
            times=1
# makemovie.m:33
        if isempty(fps):
            fps=8
# makemovie.m:34
    else:
        if command == logical_or(10,command) == 1:
            nomovie=1
# makemovie.m:36
            tminmax=str2num(get(h_edit_time,'String'))
# makemovie.m:37
            tmin=tminmax(1)
# makemovie.m:38
            tmax=tminmax(2)
# makemovie.m:38
            if command == 10:
                command=0
# makemovie.m:39
        else:
            if command == 101:
                nomovie=101
# makemovie.m:41
                tminmax=minmax(time)
# makemovie.m:42
                tmin=tminmax(1)
# makemovie.m:43
                tmax=tminmax(2)
# makemovie.m:43
                command=1
# makemovie.m:44
            else:
                if command == logical_or(20,command) == 9:
                    az=str2num(get(h_edit_angle,'String'))
# makemovie.m:46
                    el=str2num(get(h_edit_elevation,'String'))
# makemovie.m:47
                    xmax=str2num(get(h_edit_xmax,'String'))
# makemovie.m:48
                    figs=str2num(get(h_edit_figs,'String'))
# makemovie.m:49
                    if figs > 1.6:
                        figs=1.6
# makemovie.m:50
                    tit=get(h_edit_plttitle,'String')
# makemovie.m:51
                    tminmax=str2num(get(h_edit_time,'String'))
# makemovie.m:52
                    tmin=tminmax(1)
# makemovie.m:53
                    tmax=tminmax(2)
# makemovie.m:53
                    if command == 20:
                        command=5
# makemovie.m:54
    
    
    if command == 0:
        if logical_and(isempty(U),isempty(M)):
            msgbox('Re-load the time dependant velocity data.')
            return
        figure(3)
        close_(3)
        figure(4)
        close_(4)
        figure(4)
        clf
        set(gcf,'Units','Normalized','Position',concat([0.05,0.02,0.3,0.3]),'Name','Generate Time Series','Color',concat([0.8,0.8,0.8]),'tag','mdmodplt')
        tplot4=uicontrol('Style','text','String','Start:End Times','FontSize',fs,'Units','normalized','Position',concat([0.1,0.65,0.4,0.2]))
# makemovie.m:69
        h_edit_time=uicontrol('Style','edit','Callback','makemovie(10)','String',num2str(concat([tmin,tmax])),'FontSize',fs,'Units','Normalized','Position',concat([0.6,0.65,0.35,0.2]))
# makemovie.m:73
        if isempty(Xts):
            h_push_makeit=uicontrol('Style','Pushbutton','String','Generate Time Series','FontSize',fs,'Units','normalized','Position',concat([0.2,0.45,0.6,0.2]),'Callback','makemovie(1)')
# makemovie.m:79
        else:
            h_push_makeit=uicontrol('Style','Pushbutton','String','Generate New Time Series','FontSize',fs,'Units','normalized','Position',concat([0.2,0.45,0.6,0.15]),'Callback','makemovie(1)')
# makemovie.m:85
            h_push_makeit=uicontrol('Style','Pushbutton','String','Construct A Movie','FontSize',fs,'Units','normalized','Position',concat([0.3,0.25,0.4,0.15]),'Callback','makemovie(5)')
# makemovie.m:90
        h_push_cls=uicontrol('Style','Pushbutton','String','Close','FontSize',fs,'Units','normalized','Position',concat([0.3,0.01,0.4,0.1]),'Callback','makemovie(4)')
# makemovie.m:96
    else:
        if command == 1:
            figure(4)
            close_(4)
            if logical_and(logical_and(logical_not(isempty(H)),logical_not(isempty(B))),logical_not(isempty(Cd))):
                Us=copy(U)
# makemovie.m:105
                Vs=copy(V)
# makemovie.m:105
                Ws=copy(W)
# makemovie.m:105
                rhos=copy(rho)
# makemovie.m:105
                zs=copy(z)
# makemovie.m:105
                Hs=copy(H)
# makemovie.m:106
                Bs=copy(B)
# makemovie.m:106
                Cds=copy(Cd)
# makemovie.m:106
                MEs=copy(ME)
# makemovie.m:106
                mooreles=copy(moorele)
# makemovie.m:106
                Xts=[]
# makemovie.m:107
                Yts=[]
# makemovie.m:107
                Zts=[]
# makemovie.m:107
                iobjts=[]
# makemovie.m:107
                ts=[]
# makemovie.m:107
                Tits=[]
# makemovie.m:107
                psits=[]
# makemovie.m:107
                M=[]
# makemovie.m:107
                if logical_not(isempty(BCO)):
                    HCOs=copy(HCO)
# makemovie.m:109
                    BCOs=copy(BCO)
# makemovie.m:109
                    CdCOs=copy(CdCO)
# makemovie.m:109
                    mooreleCOs=copy(mooreleCO)
# makemovie.m:109
                    Iobjs=copy(Iobj)
# makemovie.m:109
                    Jobjs=copy(Jobj)
# makemovie.m:109
                    Pobjs=copy(Pobj)
# makemovie.m:109
                    Zcots=[]
# makemovie.m:110
                    Xcots=[]
# makemovie.m:110
                    Ycots=[]
# makemovie.m:110
                    Iobjts=[]
# makemovie.m:110
                    Jobjts=[]
# makemovie.m:110
                    Pobjts=[]
# makemovie.m:110
                mu,nu=size(U,nargout=2)
# makemovie.m:112
                mr,nr=size(rho,nargout=2)
# makemovie.m:113
                mz,nz=size(z,nargout=2)
# makemovie.m:114
                tindx=find(time >= logical_and(tmin,time) <= tmax)
# makemovie.m:115
                if length(tindx) == 0:
                    dt=time - tmin
# makemovie.m:117
                    dt=dt(find(dt > 0))
# makemovie.m:118
                    tindx=find(time == tmin + min(dt))
# makemovie.m:119
                iframe=0
# makemovie.m:122
                for it in tindx.reshape(-1):
                    iframe=iframe + 1
# makemovie.m:124
                    U=Us(arange(),it)
# makemovie.m:125
                    V=Vs(arange(),it)
# makemovie.m:126
                    W=Ws(arange(),it)
# makemovie.m:127
                    if mr == logical_and(mu,nr) == nu:
                        rho=rhos(arange(),it)
# makemovie.m:129
                    else:
                        rho=copy(rhos)
# makemovie.m:131
                    if mz == logical_and(mu,nz) == nu:
                        z=zs(arange(),it)
# makemovie.m:134
                    else:
                        z=copy(zs)
# makemovie.m:136
                    H=copy(Hs)
# makemovie.m:139
                    B=copy(Bs)
# makemovie.m:139
                    Cd=copy(Cds)
# makemovie.m:139
                    ME=copy(MEs)
# makemovie.m:139
                    moorele=copy(mooreles)
# makemovie.m:139
                    if logical_not(isempty(BCOs)):
                        HCO=copy(HCOs)
# makemovie.m:141
                        BCO=copy(BCOs)
# makemovie.m:141
                        CdCO=copy(CdCOs)
# makemovie.m:141
                        mooreleCO=copy(mooreleCOs)
# makemovie.m:141
                        Iobj=copy(Iobjs)
# makemovie.m:141
                        Jobj=copy(Jobjs)
# makemovie.m:141
                        Pobj=copy(Pobjs)
# makemovie.m:141
                    disp('  ')
                    if time(it) > 720000:
                        disp(concat(['Time: ',datestr(time(it),0),'   ',num2str(dot(100,(iframe / length(tindx))),'%5.1f'),'%']))
                    else:
                        disp(concat(['Time: ',num2str(time(it),'%6.2f'),'   ',num2str(dot(100,(iframe / length(tindx))),'%5.1f'),'%']))
                    X,Y,Z,iobj=moordyn
# makemovie.m:151
                    ts[iframe]=time(it)
# makemovie.m:153
                    Xts[arange(1,length(X)),iframe]=X.T
# makemovie.m:154
                    Yts[arange(1,length(Y)),iframe]=Y.T
# makemovie.m:155
                    Zts[arange(1,length(Z)),iframe]=Z.T
# makemovie.m:156
                    Tits[arange(1,length(Ti)),iframe]=Ti.T
# makemovie.m:157
                    psits[arange(1,length(psi)),iframe]=psi.T
# makemovie.m:158
                    iobjts[arange(1,length(iobj)),iframe]=iobj.T
# makemovie.m:159
                    if logical_not(isempty(BCO)):
                        Zcots[arange(1,length(Zfco)),iframe]=Zfco.T
# makemovie.m:161
                        Xcots[arange(1,length(Xfco)),iframe]=Xfco.T
# makemovie.m:162
                        Ycots[arange(1,length(Yfco)),iframe]=Yfco.T
# makemovie.m:163
                        psicots[arange(1,length(psifco)),iframe]=psifco.T
# makemovie.m:164
                        Iobjts[arange(1,length(Iobj)),iframe]=Iobj.T
# makemovie.m:165
                        Jobjts[arange(1,length(Jobj)),iframe]=Jobj.T
# makemovie.m:166
                        Pobjts[arange(1,length(Pobj)),iframe]=Pobj.T
# makemovie.m:167
                B=copy(Bs)
# makemovie.m:170
                H=copy(Hs)
# makemovie.m:170
                Cd=copy(Cds)
# makemovie.m:170
                ME=copy(MEs)
# makemovie.m:170
                moorele=copy(mooreles)
# makemovie.m:170
                if logical_not(isempty(BCOs)):
                    HCO=copy(HCOs)
# makemovie.m:172
                    BCO=copy(BCOs)
# makemovie.m:172
                    CdCO=copy(CdCOs)
# makemovie.m:172
                    mooreleCO=copy(mooreleCOs)
# makemovie.m:172
                    Iobj=copy(Iobjs)
# makemovie.m:172
                    Jobj=copy(Jobjs)
# makemovie.m:172
                    Pobj=copy(Pobjs)
# makemovie.m:172
                U=copy(Us)
# makemovie.m:174
                V=copy(Vs)
# makemovie.m:174
                W=copy(Ws)
# makemovie.m:174
                rho=copy(rhos)
# makemovie.m:174
                z=copy(zs)
# makemovie.m:174
                if nomovie != 101:
                    makemovie(5)
        else:
            if command == 5:
                figure(3)
                close_(3)
                figure(4)
                close_(4)
                figure(4)
                clf
                set(gcf,'Units','Normalized','Position',concat([0.05,0.02,0.3,0.3]),'Name','Construct a Movie','Color',concat([0.8,0.8,0.8]),'tag','mdmodplt')
                tplot1=uicontrol('Style','text','String','3D View Angle: AZ','FontSize',fs,'Units','normalized','Position',concat([0.1,0.875,0.55,0.12]))
# makemovie.m:186
                h_edit_angle=uicontrol('Style','edit','Callback','makemovie(20)','String',num2str(az),'FontSize',fs,'Units','Normalized','Position',concat([0.7,0.875,0.2,0.12]))
# makemovie.m:190
                tplot2=uicontrol('Style','text','String','3D View Elevation: EL','FontSize',fs,'Units','normalized','Position',concat([0.1,0.75,0.55,0.12]))
# makemovie.m:195
                h_edit_elevation=uicontrol('Style','edit','Callback','makemovie(20)','String',num2str(el),'FontSize',fs,'Units','Normalized','Position',concat([0.7,0.75,0.2,0.12]))
# makemovie.m:199
                tplot3=uicontrol('Style','text','String','Plot Title','FontSize',fs,'Units','normalized','Position',concat([0.1,0.625,0.2,0.12]))
# makemovie.m:204
                h_edit_plttitle=uicontrol('Style','edit','Callback','makemovie(20)','String',tit,'FontSize',fs,'Units','Normalized','Position',concat([0.35,0.625,0.6,0.12]))
# makemovie.m:208
                tplot4=uicontrol('Style','text','String','Start:End Times','FontSize',fs,'Units','normalized','Position',concat([0.1,0.5,0.4,0.12]))
# makemovie.m:213
                h_edit_time=uicontrol('Style','edit','Callback','makemovie(20)','String',num2str(concat([tmin,tmax])),'FontSize',fs,'Units','Normalized','Position',concat([0.6,0.5,0.35,0.12]))
# makemovie.m:217
                tplot5=uicontrol('Style','text','String','Set X-Axis Limit [m]','FontSize',fs,'Units','normalized','Position',concat([0.1,0.375,0.45,0.12]))
# makemovie.m:222
                h_edit_xmax=uicontrol('Style','edit','Callback','makemovie(20)','FontSize',fs,'String',num2str(xmax),'Units','Normalized','Position',concat([0.65,0.375,0.25,0.12]))
# makemovie.m:226
                tplot6=uicontrol('Style','text','String','Figure Scale Factor','FontSize',fs,'Units','normalized','Position',concat([0.1,0.25,0.5,0.12]))
# makemovie.m:231
                h_edit_figs=uicontrol('Style','edit','Callback','makemovie(20)','FontSize',fs,'String',num2str(figs),'Units','Normalized','Position',concat([0.7,0.25,0.2,0.12]))
# makemovie.m:235
                h_push_makeit=uicontrol('Style','Pushbutton','String','Make the Movie','FontSize',fs,'Units','normalized','Position',concat([0.3,0.125,0.4,0.12]),'Callback','makemovie(9)')
# makemovie.m:240
                h_push_cls=uicontrol('Style','Pushbutton','String','Close','FontSize',fs,'Units','normalized','Position',concat([0.3,0.01,0.4,0.1]),'Callback','makemovie(4)')
# makemovie.m:245
            else:
                if command == 9:
                    tindx=find(ts >= logical_and(tmin,ts) <= tmax)
# makemovie.m:253
                    iframe=0
# makemovie.m:254
                    for it in tindx.reshape(-1):
                        iframe=iframe + 1
# makemovie.m:256
                        figure(3)
                        clf
                        hold('on')
                        set(3,'Units','Normalized','Position',concat([0.3,0.1 / figs,dot(0.4,figs),dot(0.6,figs)]),'Name','The Mooring Movie','Color',concat([0.8,0.8,0.8]))
                        X=Xts(arange(),it)
# makemovie.m:263
                        Y=Yts(arange(),it)
# makemovie.m:264
                        Z=Zts(arange(),it)
# makemovie.m:265
                        iobj=iobjts(arange(),it)
# makemovie.m:266
                        if logical_not(isempty(BCO)):
                            Zfco=Zcots(arange(),it)
# makemovie.m:268
                            Xfco=Xcots(arange(),it)
# makemovie.m:269
                            Yfco=Ycots(arange(),it)
# makemovie.m:270
                            psifco=psicots(arange(),it)
# makemovie.m:271
                            Iobj=Iobjts(arange(),it)
# makemovie.m:272
                            Jobj=Jobjts(arange(),it)
# makemovie.m:273
                            Pobj=Pobjts(arange(),it)
# makemovie.m:274
                        if it == tindx(1):
                            zmax=dot(1.1,sum(H(1,arange())))
# makemovie.m:277
                            sw=0
# makemovie.m:278
                            dx=dot(floor(xmax / 40),10)
# makemovie.m:279
                            ymax=copy(xmax)
# makemovie.m:280
                            dy=copy(dx)
# makemovie.m:281
                            if zmax < 100:
                                zmax=100
# makemovie.m:283
                            else:
                                zmax=dot(ceil(zmax / 20),20)
# makemovie.m:285
                            if abs(max(Z) - max(z)) < 20:
                                zmax=max(z)
# makemovie.m:288
                                swx=concat([arange(- xmax,xmax,0.2)])
# makemovie.m:289
                                swzx=(zmax + 0.75) - sqrt(1 + sin(swx))
# makemovie.m:290
                                swy=concat([arange(- ymax,ymax,0.2)])
# makemovie.m:291
                                swzy=(zmax + 0.75) - sqrt(1 + sin(swy))
# makemovie.m:292
                                sw=1
# makemovie.m:293
                            xt=concat([arange(- xmax,0,dx),arange(dx,xmax,dx)])
# makemovie.m:295
                        # project onto sides
                        hxp=plot3(X,dot(ymax,ones(size(Y))),Z,'g')
# makemovie.m:298
                        plot3(X(iobj(1)),ymax,Z(iobj(1)),'or','Markersize',9,'MarkerFaceColor',concat([1,0.7,0.7]),'Clipping','off')
                        hyp=plot3(dot(ymax,ones(size(X))),Y,Z,'g')
# makemovie.m:301
                        plot3(xmax,Y(iobj(1)),Z(iobj(1)),'or','Markersize',9,'MarkerFaceColor',concat([1,0.7,0.7]),'Clipping','off')
                        hzp=plot3(X,Y,zeros(size(Z)),'g')
# makemovie.m:304
                        plot3(X(iobj(1)),Y(iobj(1)),0,'or','Markersize',9,'MarkerFaceColor',concat([1,0.7,0.7]),'Clipping','off')
                        plot3(X,Y,Z,'b')
                        li=length(iobj)
# makemovie.m:309
                        plot3(X(iobj(arange(2,li - 1))),Y(iobj(arange(2,li - 1))),Z(iobj(arange(2,li - 1))),'or','Markersize',8,'Clipping','off')
                        plot3(X(iobj(1)),Y(iobj(1)),Z(iobj(1)),'or','Markersize',10,'MarkerFaceColor',concat([0.9,0,0]),'Clipping','off')
                        plot3(X(iobj(li)),Y(iobj(li)),Z(iobj(li)),'^b','Markersize',8,'MarkerFaceColor','b','Clipping','off')
                        if logical_not(isempty(BCO)):
                            plot3(Xfco,Yfco,Zfco,'om','Markersize',6,'Clipping','off')
                        axis(concat([- xmax,xmax,- ymax,ymax,0,zmax]))
                        box('on')
                        if sw == 1:
                            box('off')
                            plot3(dot(xmax,ones(size(swy))),swy,swzy,'b','Clipping','off')
                            plot3(dot(- xmax,ones(size(swy))),swy,swzy,'b','Clipping','off')
                            plot3(swx,dot(ymax,ones(size(swx))),swzx,'b','Clipping','off')
                            plot3(swx,dot(- ymax,ones(size(swx))),swzx,'b','Clipping','off')
                        set(gca,'XTick',xt,'XTickLabel',xt,'Fontsize',dot(fontsz,figs))
                        set(gca,'YTick',xt,'YTickLabel',xt)
                        grid
                        view(az,el)
                        xlabel('X [m]','Fontsize',dot(fontsz,figs))
                        ylabel('Y [m]','Fontsize',dot(fontsz,figs))
                        zlabel('Z [m]','Fontsize',dot(fontsz,figs))
                        title(concat([tit,':  Time ',num2str(ts(it))]),'Fontsize',dot(fontsz,figs))
                        drawnow
                        if iframe == 1:
                            cfh=figure(3)
# makemovie.m:341
                            M=moviein(length(tindx),cfh)
# makemovie.m:342
                        M[arange(),iframe]=getframe(cfh)
# makemovie.m:344
                    if length(tindx) > 1:
                        figure(3)
                        clf
                        set(3,'Units','Normalized','Position',concat([0.3,0.1 / figs,dot(0.4,figs),dot(0.6,figs)]),'Name','The Mooring Movie')
                        movie(3,M,0)
                    figure(4)
                    close_(4)
                    figure(3)
                    close_(3)
                    moordesign(0)
                else:
                    if command == 2:
                        hf4=figure(4)
# makemovie.m:357
                        clf
                        set(gcf,'Units','Normalized','Position',concat([0.05,0.02,0.25,0.275]),'Name','Play Movie','Color',concat([0.8,0.8,0.8]))
                        tplot1=uicontrol('Style','text','String','Number of times:','FontSize',fs,'Units','normalized','Position',concat([0.1,0.8,0.55,0.125]))
# makemovie.m:362
                        h_edit_times=uicontrol('Style','edit','Callback','makemovie(11)','String',num2str(times),'FontSize',fs,'Units','Normalized','Position',concat([0.7,0.8,0.2,0.125]))
# makemovie.m:366
                        tplot2=uicontrol('Style','text','String','Speed (fps):','FontSize',fs,'Units','normalized','Position',concat([0.1,0.6,0.55,0.125]))
# makemovie.m:371
                        h_edit_fps=uicontrol('Style','edit','Callback','makemovie(11)','String',num2str(fps),'FontSize',fs,'Units','Normalized','Position',concat([0.7,0.6,0.2,0.125]))
# makemovie.m:375
                        tplot5=uicontrol('Style','text','String','Figure Scale Factor','FontSize',fs,'Units','normalized','Position',concat([0.1,0.4,0.5,0.125]))
# makemovie.m:380
                        h_edit_figs=uicontrol('Style','edit','Callback','makemovie(11)','String',num2str(figs),'FontSize',fs,'Units','Normalized','Position',concat([0.7,0.4,0.2,0.125]))
# makemovie.m:384
                        h_push_play=uicontrol('Style','Pushbutton','String','Play Movie','FontSize',fs,'Units','normalized','Position',concat([0.3,0.2,0.4,0.125]),'Callback','makemovie(3)')
# makemovie.m:389
                        h_push_cls=uicontrol('Style','Pushbutton','String','Close','FontSize',fs,'Units','normalized','Position',concat([0.35,0.01,0.3,0.125]),'Callback','makemovie(4)')
# makemovie.m:394
                    else:
                        if command == 11:
                            times=str2num(get(h_edit_times,'String'))
# makemovie.m:400
                            fps=str2num(get(h_edit_fps,'String'))
# makemovie.m:401
                            figs=str2num(get(h_edit_figs,'String'))
# makemovie.m:402
                            makemovie(2)
                        else:
                            if command == 3:
                                hf3=figure(3)
# makemovie.m:405
                                clf
                                axes('Visible','off')
                                set(hf3,'Units','Normalized','Position',concat([0.3,0.1 / figs,dot(0.4,figs),dot(0.6,figs)]),'Name','The Mooring Movie')
                                movie(hf3,M,times,fps)
                            else:
                                if command == 4:
                                    figure(3)
                                    close_(3)
                                    figure(4)
                                    close_(4)
                                    moordesign(0)
    
    # fini