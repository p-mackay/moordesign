# Generated with SMOP  0.41-beta
from libsmop import *
# mdplot.m

    
@function
def mdplot(command=None,*args,**kwargs):
    varargin = mdplot.varargin
    nargin = mdplot.nargin

    # function to (update) the mooring plot
    global H,B,Cd,moorele
    global Ht,Bt,Cdt,MEt,moorelet,Usp,Vsp,DD
    global U,V,W,z,rho,uw,vw,time
    global X,Y,Z,iobj,figs
    global psi,theta,im1
    global ZCO,BCO,HCO,Jobj,Pobj,Z0co,Zfco,Xfco,Yfco,psifco
    global h_edit_angle,h_edit_elevation,h_edit_plttitle,h_edit_timemd
    global its,itplt,Us,Vs,Ws,rhos,iss
    global Iobj
    global fs
    global HWa,ba,ha,wpm,xair,yair,lgth
    im1=[]
# mdplot.m:15
    iss=[]
# mdplot.m:15
    if isempty(U):
        U=concat([0,0,0]).T
# mdplot.m:17
        V=copy(U)
# mdplot.m:17
        W=copy(U)
# mdplot.m:17
        if isempty(Ht):
            z=fix(dot(sum(H(1,arange())),concat([1.2,0.2,0]).T))
# mdplot.m:19
        else:
            z=fix(dot(sum(Ht(1,arange())),concat([0,0.2,1.2]).T))
# mdplot.m:21
        if isempty(rho):
            rho=concat([1024,1025,1026]).T
# mdplot.m:23
    else:
        mu,nu=size(U,nargout=2)
# mdplot.m:25
        if mu == logical_and(1,nu) > 1:
            U=U.T
# mdplot.m:27
            V=V.T
# mdplot.m:27
            W=W.T
# mdplot.m:27
            z=z.T
# mdplot.m:27
            rho=rho.T
# mdplot.m:27
    
    if logical_not(isempty(Ht)):
        if max(z) <= sum(Ht(1,arange())):
            z[end()]=dot(sum(Ht(1,arange())),1.2)
# mdplot.m:32
    
    if isempty(its):
        its=1
# mdplot.m:35
    
    if nargin == 0:
        command=0
# mdplot.m:36
    
    if command == 0:
        load('splash.mat')
        sound(wavedata / 8000,samplingrate,16)
        clear('wavedata','samplingrate')
    
    if logical_or((logical_and(logical_and(logical_not(isempty(H)),logical_not(isempty(B))),logical_not(isempty(Cd)))),(logical_and(logical_and(logical_not(isempty(Ht)),logical_not(isempty(Bt))),logical_not(isempty(Cdt))))):
        if command == logical_or(0,command) >= 20:
            if command == 0:
                clear('X','Y','Z','iobj')
            mu,nu=size(U,nargout=2)
# mdplot.m:45
            if nu > 1:
                if its == logical_and(1,command) != 21:
                    if isempty(h_edit_timemd):
                        tmin=min(time)
# mdplot.m:49
                        tmax=max(time)
# mdplot.m:49
                        figure(4)
                        close_(4)
                        figure(4)
                        clf
                        set(gcf,'Units','Normalized','Position',concat([0.05,0.2,0.3,0.15]),'Name','Select Time','Color',concat([0.8,0.8,0.8]),'tag','mdtplt')
                        tplot1=uicontrol('Style','text','String','Start:End Times','FontSize',fs,'Units','normalized','Position',concat([0.1,0.7,0.4,0.25]))
# mdplot.m:56
                        h_str_time=uicontrol('Style','text','String',num2str(concat([tmin,tmax])),'FontSize',fs,'Units','Normalized','Position',concat([0.6,0.7,0.35,0.25]))
# mdplot.m:60
                        tplot2=uicontrol('Style','text','String','Edit Time:','FontSize',fs,'Units','normalized','Position',concat([0.1,0.35,0.4,0.25]))
# mdplot.m:64
                        h_edit_timemd=uicontrol('Style','edit','Callback','mdplot(20)','FontSize',fs,'String',num2str(tmin),'Units','Normalized','Position',concat([0.6,0.35,0.35,0.25]))
# mdplot.m:68
                        h_push_ok=uicontrol('Style','Pushbutton','String','OK','FontSize',fs,'Units','normalized','Position',concat([0.35,0.02,0.3,0.2]),'Callback','mdplot(20)')
# mdplot.m:73
                        return
                    else:
                        timemd=str2num(get(h_edit_timemd,'String'))
# mdplot.m:80
                        dt=time - timemd
# mdplot.m:81
                        its=find(min(abs(dt)) == abs(dt))
# mdplot.m:82
                        figure(4)
                        close_(4)
                        h_edit_timemd=[]
# mdplot.m:84
                        mdplot(21)
                else:
                    if isempty(Ht):
                        Us=copy(U)
# mdplot.m:89
                        Vs=copy(V)
# mdplot.m:89
                        Ws=copy(W)
# mdplot.m:89
                        if its > logical_or(nu,its) < 1:
                            its=1
# mdplot.m:90
                        U=Us(arange(),its)
# mdplot.m:91
                        V=Vs(arange(),its)
# mdplot.m:91
                        W=Ws(arange(),its)
# mdplot.m:91
                        itplt=copy(its)
# mdplot.m:92
                        X,Y,Z,iobj=moordyn
# mdplot.m:93
                        U=copy(Us)
# mdplot.m:94
                        V=copy(Vs)
# mdplot.m:94
                        W=copy(Ws)
# mdplot.m:94
                        clear('Us','Vs','Ws')
                        its=1
# mdplot.m:96
                    else:
                        Us=copy(U)
# mdplot.m:98
                        Vs=copy(V)
# mdplot.m:98
                        Ws=copy(W)
# mdplot.m:98
                        if its > logical_or(nu,its) < 1:
                            its=1
# mdplot.m:99
                        U=Us(arange(),its)
# mdplot.m:100
                        V=Vs(arange(),its)
# mdplot.m:100
                        W=Ws(arange(),its)
# mdplot.m:100
                        itplt=copy(its)
# mdplot.m:101
                        X,Y,Z,iobj=towdyn
# mdplot.m:102
                        U=copy(Us)
# mdplot.m:103
                        V=copy(Vs)
# mdplot.m:103
                        W=copy(Ws)
# mdplot.m:103
                        clear('Us','Vs','Ws')
                        its=1
# mdplot.m:105
            else:
                if isempty(Ht):
                    X,Y,Z,iobj=moordyn
# mdplot.m:111
                else:
                    if DD > 0:
                        ish=0
# mdplot.m:115
                        idp=0
# mdplot.m:115
                        Htavg=0
# mdplot.m:115
                        iwl=find(Ht(4,arange()) == 1)
# mdplot.m:116
                        iwl=iwl(end())
# mdplot.m:117
                        X,Y,Z,iobj=towdyn
# mdplot.m:118
                        ibreakDD=1
# mdplot.m:119
                        icnt=0
# mdplot.m:119
                        while ibreakDD:

                            if logical_not(isempty(im1)):
                                iend=im1 - 1
# mdplot.m:122
                            else:
                                iend=length(Z)
# mdplot.m:124
                            icnt=icnt + 1
# mdplot.m:127
                            if abs(Z(1) - DD) > Ht(1,1) / 2:
                                if Z(1) < DD:
                                    Ht[1,iwl]=Ht(1,iwl) + abs(abs(Z(1) - DD) / cos(psi(iend)))
# mdplot.m:130
                                    if icnt > 2:
                                        ish=ish + 1
# mdplot.m:132
                                        Htavg=Htavg + Ht(1,iwl)
# mdplot.m:133
                                        if ish > logical_and(2,idp) > 2:
                                            Ht[1,iwl]=Htavg / (ish + idp)
# mdplot.m:134
                                else:
                                    Ht[1,iwl]=Ht(1,iwl) - abs(abs(Z(1) - DD) / cos(psi(iend)))
# mdplot.m:137
                                    if icnt > 2:
                                        idp=idp + 1
# mdplot.m:139
                                        Htavg=Htavg + Ht(1,iwl)
# mdplot.m:140
                                        if ish > logical_and(2,idp) > 2:
                                            Ht[1,iwl]=Htavg / (ish + idp)
# mdplot.m:141
                                X,Y,Z,iobj=towdyn
# mdplot.m:145
                            else:
                                ibreakDD=0
# mdplot.m:148

                    else:
                        X,Y,Z,iobj=towdyn
# mdplot.m:152
            figure(3)
            clf
            hold('on')
            if isempty(Ht):
                set(gcf,'Units','Normalized','Position',concat([0.4,0.3,0.5,0.6]),'Name','The Mooring','tag','mdplot')
                plot3(X,Y,Z,'b')
                hold('on')
                li=length(iobj)
# mdplot.m:164
                plot3(X(iobj(arange(2,li - 1))),Y(iobj(arange(2,li - 1))),Z(iobj(arange(2,li - 1))),'or','Markersize',5,'Clipping','off')
                plot3(X(iobj(1)),Y(iobj(1)),Z(iobj(1)),'or','Markersize',10,'MarkerFaceColor','r','Clipping','off')
                plot3(X(iobj(li)),Y(iobj(li)),Z(iobj(li)),'^b','Markersize',8,'MarkerFaceColor','b','Clipping','off')
                if logical_not(isempty(BCO)):
                    plot3(Xfco,Yfco,Zfco,'om','Markersize',5,'Clipping','off')
                grid
                box('on')
                axis('equal')
                xlabel('X [m]')
                ylabel('Y [m]')
                zlabel('Z [m]')
                if logical_or(isempty(time),isempty(itplt)):
                    title('Mooring Design and Dynamics')
                else:
                    title(concat(['Mooring Forced by Currents at ',num2str(time(itplt))]))
                zm=get(gca,'ZLim')
# mdplot.m:184
                xm=dot(get(gca,'XLim'),1.2)
# mdplot.m:185
                set(gca,'XLim',xm)
                ym=dot(get(gca,'YLim'),1.2)
# mdplot.m:187
                set(gca,'YLim',ym)
                if min(xm) > - 10:
                    xm[1]=- 10
# mdplot.m:189
                if max(xm) < 10:
                    xm[2]=10
# mdplot.m:190
                set(gca,'XLim',xm)
                if min(ym) > - 10:
                    ym[1]=- 10
# mdplot.m:192
                if max(ym) < 10:
                    ym[2]=10
# mdplot.m:193
                set(gca,'YLim',ym)
                if abs(max(Z) - max(z)) < 50:
                    zm=max(z)
# mdplot.m:196
                    xm=get(gca,'XLim')
# mdplot.m:197
                    ym=get(gca,'YLim')
# mdplot.m:197
                    swx=concat([arange(min(xm),max(xm),0.2)])
# mdplot.m:198
                    swzx=(zm + 0.75) - sqrt(1 + sin(swx))
# mdplot.m:199
                    swy=concat([arange(min(ym),max(ym),0.2)])
# mdplot.m:200
                    swzy=(zm + 0.75) - sqrt(1 + sin(swy))
# mdplot.m:201
                    box('off')
                    plot3(dot(max(xm),ones(size(swy))),swy,swzy,'b','Clipping','off')
                    plot3(dot(min(xm),ones(size(swy))),swy,swzy,'b','Clipping','off')
                    plot3(swx,dot(max(ym),ones(size(swx))),swzx,'b','Clipping','off')
                    plot3(swx,dot(min(ym),ones(size(swx))),swzx,'b','Clipping','off')
                    axis(concat([xm(1),xm(2),ym(1),ym(2),0,zm]))
                ha=copy(pi)
# mdplot.m:209
            else:
                set(gcf,'Units','Normalized','Position',concat([0.4,0.3,0.5,0.6]),'Name','The Towed Body','tag','mdplot')
                boat
                tlgth=lgth + sum(Ht(1,arange(2,end())))
# mdplot.m:216
                disp(concat([' Length of wire from Water surface to A-frame: ',num2str(lgth,'%7.2f'),'[m]']))
                disp(concat([' Total length of wire from A-frame to towed body: ',num2str(tlgth,'%7.2f'),'[m]']))
                X=X + xair
# mdplot.m:219
                Y=Y + yair
# mdplot.m:219
                Xfco=Xfco + xair
# mdplot.m:219
                Yfco=Yfco + yair
# mdplot.m:219
                plot3(X,Y,- Z,'b')
                hold('on')
                li=length(iobj)
# mdplot.m:221
                plot3(X(iobj(arange(2,li - 1))),Y(iobj(arange(2,li - 1))),- Z(iobj(arange(2,li - 1))),'or','Markersize',5,'Clipping','off')
                plot3(X(iobj(1)),Y(iobj(1)),- Z(iobj(1)),'or','Markersize',10,'MarkerFaceColor','r','Clipping','off')
                if logical_not(isempty(BCO)):
                    plot3(Xfco,Yfco,- Zfco,'om','Markersize',5,'Clipping','off')
                grid('on')
                axis('equal')
                xlabel('X [m]')
                ylabel('Y [m]')
                zlabel('Z [m]')
                if logical_and(isempty(time),isempty(itplt)):
                    title('Mooring Design and Dynamics Towed Body')
                else:
                    title(concat(['Towed Body at ',num2str(time(itplt))]))
                xm=dot(get(gca,'XLim'),1.2)
# mdplot.m:240
                set(gca,'XLim',xm)
                ym=dot(get(gca,'YLim'),1.2)
# mdplot.m:242
                set(gca,'YLim',ym)
                if min(xm) > - 10:
                    xm[1]=- 10
# mdplot.m:244
                if max(xm) < 10:
                    xm[2]=10
# mdplot.m:245
                set(gca,'XLim',xm)
                if min(ym) > - 10:
                    ym[1]=- 10
# mdplot.m:247
                if max(ym) < 10:
                    ym[2]=10
# mdplot.m:248
                set(gca,'YLim',ym)
                zm=0
# mdplot.m:251
                xm=get(gca,'XLim')
# mdplot.m:252
                ym=get(gca,'YLim')
# mdplot.m:252
                swx=concat([arange(min(xm),max(xm),0.2)])
# mdplot.m:253
                swzx=(zm + 0.75) - sqrt(1 + sin(swx))
# mdplot.m:254
                swy=concat([arange(min(ym),max(ym),0.2)])
# mdplot.m:255
                swzy=(zm + 0.75) - sqrt(1 + sin(swy))
# mdplot.m:256
                box('off')
                plot3(dot(max(xm),ones(size(swy))),swy,swzy,'b','Clipping','off')
                plot3(dot(min(xm),ones(size(swy))),swy,swzy,'b','Clipping','off')
                plot3(swx,dot(max(ym),ones(size(swx))),swzx,'b','Clipping','off')
                plot3(swx,dot(min(ym),ones(size(swx))),swzx,'b','Clipping','off')
            view(fix(dot((ha - pi),180) / pi + 20),10)
            drawnow
            az,el=view
# mdplot.m:266
            figure(4)
            clf
            set(gcf,'Units','Normalized','Position',concat([0.05,0.02,0.325,0.275]),'Name','Modify Plot','Color',concat([0.8,0.8,0.8]),'tag','mdmodplt')
            tplot1=uicontrol('Style','text','String','3D View Angle: AZ','FontSize',fs,'Units','normalized','Position',concat([0.1,0.8,0.55,0.125]))
# mdplot.m:274
            h_edit_angle=uicontrol('Style','edit','Callback','mdplot(1)','String',num2str(az),'FontSize',fs,'Units','Normalized','Position',concat([0.7,0.8,0.2,0.125]))
# mdplot.m:278
            tplot2=uicontrol('Style','text','String','3D View Elevation: EL','FontSize',fs,'Units','normalized','Position',concat([0.1,0.6,0.55,0.125]))
# mdplot.m:283
            h_edit_elevation=uicontrol('Style','edit','Callback','mdplot(2)','String',num2str(el),'FontSize',fs,'Units','Normalized','Position',concat([0.7,0.6,0.2,0.125]))
# mdplot.m:287
            tplot3=uicontrol('Style','text','String','Plot Title','FontSize',fs,'Units','normalized','Position',concat([0.1,0.4,0.2,0.125]))
# mdplot.m:292
            h_edit_plttitle=uicontrol('Style','edit','Callback','mdplot(3)','String','Mooring Design and Dynamics','FontSize',fs,'Units','Normalized','Position',concat([0.35,0.4,0.6,0.125]))
# mdplot.m:296
            if isempty(Ht):
                h_push_pltuvw=uicontrol('Style','Pushbutton','String','Plot Velocity Profiles','FontSize',fs,'Units','normalized','Position',concat([0.05,0.2,0.4,0.125]),'Callback','mdplot(4)')
# mdplot.m:302
            h_push_rotate=uicontrol('Style','Pushbutton','String','Rotate3D','FontSize',fs,'Units','normalized','Position',concat([0.6,0.2,0.3,0.125]),'Callback','mdplot(6)')
# mdplot.m:308
            h_push_print=uicontrol('Style','Pushbutton','String','Print','FontSize',fs,'Units','normalized','Position',concat([0.1,0.02,0.3,0.125]),'Callback','mdplot(5)')
# mdplot.m:313
            h_push_cls=uicontrol('Style','Pushbutton','String','Close','FontSize',fs,'Units','normalized','Position',concat([0.6,0.02,0.3,0.125]),'Callback','mdplot(7)')
# mdplot.m:318
        else:
            if command == logical_or(1,command) == 2:
                figure(3)
                axis('normal')
                az=str2num(get(h_edit_angle,'String'))
# mdplot.m:326
                el=str2num(get(h_edit_elevation,'String'))
# mdplot.m:327
                view(az,el)
                axis('equal')
            else:
                if command == 3:
                    figure(3)
                    axis('normal')
                    title(get(h_edit_plttitle,'String'))
                    axis('equal')
                else:
                    if command == 4:
                        if isempty(itplt):
                            itplt=1
# mdplot.m:335
                        ztmp=copy(z)
# mdplot.m:337
                        Utmp=copy(U)
# mdplot.m:337
                        Vtmp=copy(V)
# mdplot.m:337
                        if (z(1) - z(2)) > logical_and(10.01,(uw ** 2 + vw ** 2)) > 0:
                            mu=length(z)
# mdplot.m:339
                            z[arange(3,mu + 1)]=z(arange(2,mu))
# mdplot.m:340
                            z[2]=z(1) - 10
# mdplot.m:341
                            U[arange(3,mu + 1),itplt]=U(arange(2,mu),itplt)
# mdplot.m:342
                            U[2,its]=U(1,its)
# mdplot.m:343
                            V[arange(3,mu + 1),itplt]=V(arange(2,mu),itplt)
# mdplot.m:344
                            V[2,itplt]=V(1,itplt)
# mdplot.m:345
                        U[1,itplt]=U(1,itplt) + uw
# mdplot.m:347
                        V[1,itplt]=V(1,itplt) + vw
# mdplot.m:348
                        figure(3)
                        clf
                        axis('normal')
                        plot3(X,Y,Z,'b')
                        hold('on')
                        li=length(iobj)
# mdplot.m:352
                        plot3(X(iobj(arange(2,li - 1))),Y(iobj(arange(2,li - 1))),Z(iobj(arange(2,li - 1))),'or','Markersize',5,'Clipping','off')
                        plot3(X(iobj(1)),Y(iobj(1)),Z(iobj(1)),'or','Markersize',10,'MarkerFaceColor','r','Clipping','off')
                        plot3(X(iobj(li)),Y(iobj(li)),Z(iobj(li)),'^b','Markersize',8,'MarkerFaceColor','b','Clipping','off')
                        if logical_not(isempty(BCO)):
                            plot3(Xfco,Yfco,Zfco,'om','Markersize',5,'Clipping','off')
                        grid
                        box('on')
                        axis('equal')
                        xlabel('X [m]')
                        ylabel('Y [m]')
                        zlabel('Z [m]')
                        if isempty(time):
                            title('Mooring Forced by Currents')
                        else:
                            title(concat(['Mooring Forced by Currents at ',num2str(time(itplt))]))
                        xlim=dot(get(gca,'XLim'),1.2)
# mdplot.m:372
                        ylim=dot(get(gca,'YLim'),1.2)
# mdplot.m:373
                        if min(xlim) > - 10:
                            xlim[1]=- 10
# mdplot.m:374
                        if max(xlim) < 10:
                            xlim[2]=10
# mdplot.m:375
                        set(gca,'XLim',xlim)
                        if min(ylim) > - 10:
                            ylim[1]=- 10
# mdplot.m:377
                        if max(ylim) < 10:
                            ylim[2]=10
# mdplot.m:378
                        set(gca,'YLim',ylim)
                        zlim=get(gca,'ZLim')
# mdplot.m:380
                        xmax1=max(xlim)
# mdplot.m:381
                        ymax1=max(ylim)
# mdplot.m:382
                        zmax1=max(abs(zlim))
# mdplot.m:383
                        if max(abs(U(arange(),itplt))) != 0:
                            up=dot(xmax1,U(arange(),itplt)) / (max(abs(U(arange(),itplt))))
# mdplot.m:385
                        else:
                            up=zeros(size(z))
# mdplot.m:387
                        up=ravel(up)
# mdplot.m:389
                        if max(abs(V(arange(),itplt))) != 0:
                            vp=dot(ymax1,V(arange(),itplt)) / (max(abs(V(arange(),itplt))))
# mdplot.m:391
                        else:
                            vp=zeros(size(z))
# mdplot.m:393
                        vp=ravel(vp)
# mdplot.m:395
                        if logical_not(isempty(up)):
                            hup=plot3(up,dot(ymax1,ones(size(up))),z,'g')
# mdplot.m:397
                            set(hup,'Color',concat([0,0.5,0]))
                        if logical_not(isempty(vp)):
                            hvp=plot3(dot(xmax1,ones(size(vp))),vp,z,'m')
# mdplot.m:401
                        axis('equal')
                        zlim=get(gca,'ZLim')
# mdplot.m:404
                        zmax1=max(abs(zlim))
# mdplot.m:405
                        if logical_not(isempty(up)):
                            umax=max(abs(U(arange(),itplt)))
# mdplot.m:407
                            hut=text(dot(xmax1,1.1),ymax1,zmax1,concat(['|Umax|=',num2str(umax),' m/s']))
# mdplot.m:408
                            set(hut,'Color',concat([0,0.5,0]),'FontSize',8)
                        if logical_not(isempty(vp)):
                            vmax=max(abs(V(arange(),itplt)))
# mdplot.m:412
                            hvt=text(dot(xmax1,1.1),0,zmax1 - dot(zmax1,0.05),concat(['|Vmax|=',num2str(vmax),' m/s']))
# mdplot.m:413
                            set(hvt,'Color','m','FontSize',8)
                        if abs(max(Z) - max(z)) < 50:
                            zm=max(z)
# mdplot.m:417
                            swx=concat([arange(min(xlim),max(xlim),0.2)])
# mdplot.m:418
                            swzx=(zm + 0.75) - sqrt(1 + sin(swx))
# mdplot.m:419
                            swy=concat([arange(min(ylim),max(ylim),0.2)])
# mdplot.m:420
                            swzy=(zm + 0.75) - sqrt(1 + sin(swy))
# mdplot.m:421
                            box('off')
                            plot3(dot(max(xlim),ones(size(swy))),swy,swzy,'b','Clipping','off')
                            plot3(dot(min(xlim),ones(size(swy))),swy,swzy,'b','Clipping','off')
                            plot3(swx,dot(max(ylim),ones(size(swx))),swzx,'b','Clipping','off')
                            plot3(swx,dot(min(ylim),ones(size(swx))),swzx,'b','Clipping','off')
                            axis(concat([xlim(1),xlim(2),ylim(1),ylim(2),0,zm]))
                        drawnow
                        z=copy(ztmp)
# mdplot.m:431
                        U=copy(Utmp)
# mdplot.m:431
                        V=copy(Vtmp)
# mdplot.m:431
                    else:
                        if command == 5:
                            figure(3)
                            print_ - f3 - v
                        else:
                            if command == 6:
                                figure(3)
                                rotate3d
                                help('rotate3d')
                            else:
                                if command == 7:
                                    close_(3)
                                    close_(4)
    else:
        disp(' Must load or enter a mooring before evaluation/plotting. ')
    
    moordesign(0)
    # fini