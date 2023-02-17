# Generated with SMOP  0.41-beta
from libsmop import *
# moordyn.m

    
@function
def moordyn(U=None,z=None,H=None,B=None,Cd=None,ME=None,V=None,W=None,rho=None,*args,**kwargs):
    varargin = moordyn.varargin
    nargin = moordyn.nargin

    # function [X,Y,Z,iobj]=moordyn(U,z,H,B,Cd,ME,V,W,rho)
    
    # Calculate the mooring element positions relative to anchor,
# X (+East), Y (+North) and Z (+Up) all in metres
#    given a velocity profile U(z) at depths z [m] (+up), with U(0)=0
# For an oceanographic mooring from top to bottom
#    with N elemental components (including wire sections as elements),
#    dimensions H(L W D i,N) [m] of each different mooring component/element,
#    mass/buoyancies B(N) [in kg, or kg/m for wire/chain] (+up),
#    Drag coefficients (Cd(N)). ME (modulus of elasticity indecies)
#    where 1=steel,2=Nylon,3=Dacron,4=Polyprop,5=Polyethy,6=Kevlar,7=Aluminum, 8=Dyneema
# Output iobj are the idecices of the mooring "elements" not
#    including wire or chain [H(4,:)=1] elements.
#    Note: U (and V, W, and rho if provided) must extend to bottom (z=0).
# Optional inputs:
#    velocity components V(z) and W(z), rho(z)=density profile
    
    # H(1,:) = Length/height of object/element including strength member [m]
#          H(1,N) is the height of the anchor [m]
# H(2,:) = Width of cylinder (0=zero if sphere) [m]
# H(3,:) = Diameter of sphere (0=zero if cylinder or wire/chain) [m]
# H(4,:) = 1 for wire/chain, 2 for fastener, 0 otherwise. Divide wire/chain into 1 m lengths
    
    # May be passed with no arguments, assuming: global U z H B Cd V W rho
# RKD 12/97
    
    if nargin == 0:
        global U,V,W,z,rho,uw,vw
        global H,B,Cd,ME
    
    global Hs,Bs,Cds,MEs,iss
    global moorele,X,Y,Z,Ti,iobj,jobj,psi,iEle,theta
    global HCO,BCO,CdCO,mooreleCO,ZCO,Jobj,Pobj,PIobj,IEle
    global Z0co,Zfco,Xfco,Yfco,psifco
    global Iobj
    global nomovie
    global Zoo
    global Zi
    iprt=100
# moordyn.m:41
    
    X=[]
# moordyn.m:43
    Y=[]
# moordyn.m:43
    Z=[]
# moordyn.m:43
    Ti=[]
# moordyn.m:43
    iobj=[]
# moordyn.m:43
    jobj=[]
# moordyn.m:43
    psi=[]
# moordyn.m:43
    if isempty(iss):
        Hs=copy(H)
# moordyn.m:44
        Bs=copy(B)
# moordyn.m:44
        Cds=copy(Cd)
# moordyn.m:44
        MEs=copy(ME)
# moordyn.m:44
    
    if logical_not(isempty(find(B == 0))):
        B[find(B == 0)]=- 0.0001
# moordyn.m:45
    
    mu,nu=size(U,nargout=2)
# moordyn.m:46
    if logical_or((mu == logical_and(0,nu) == 0),max(z)) == 0:
        U=concat([0.1,0.1,0])
# moordyn.m:48
        U=ravel(U)
# moordyn.m:48
        V=copy(U)
# moordyn.m:48
        W=copy(U)
# moordyn.m:48
        z=fix(dot(sum(H(1,arange())),concat([1.5,0.1,0]).T))
# moordyn.m:48
        z=ravel(z)
# moordyn.m:48
        rho=concat([1024,1025,1026]).T
# moordyn.m:48
        rho=ravel(rho)
# moordyn.m:48
    
    z[find(z(arange(1,end() - 1)) == 0)]=0.1
# moordyn.m:50
    
    Zoo=[]
# moordyn.m:51
    Z0co=[]
# moordyn.m:51
    Utmpo=copy(U)
# moordyn.m:52
    Vtmpo=copy(V)
# moordyn.m:52
    Wtmpo=copy(W)
# moordyn.m:52
    U=dot(ones(size(z)),0)
# moordyn.m:53
    V=copy(U)
# moordyn.m:54
    W=copy(U)
# moordyn.m:54
    
    for izloop in arange(1,2).reshape(-1):
        # the first loop to estimate the initial component heights with no currents
        if izloop == 2:
            U=copy(Utmpo)
# moordyn.m:59
            V=copy(Vtmpo)
# moordyn.m:60
            W=copy(Wtmpo)
# moordyn.m:61
        # Add 2# of wind speed to top current (10m) value
        ztmp=copy(z)
# moordyn.m:64
        Utmp=copy(U)
# moordyn.m:64
        Vtmp=copy(V)
# moordyn.m:64
        Wtmp=copy(W)
# moordyn.m:64
        rhotmp=copy(rho)
# moordyn.m:64
        if mu != logical_and(1,nu) != 1:
            if mu == length(z):
                U=U(arange(),1)
# moordyn.m:67
                V=V(arange(),1)
# moordyn.m:68
                W=W(arange(),1)
# moordyn.m:69
            else:
                U=U(1,arange()).T
# moordyn.m:71
                V=V(1,arange()).T
# moordyn.m:72
                W=W(1,arange()).T
# moordyn.m:73
        # Add 2# of wind speed to top current value(s)
        if uw != logical_or(0,vw) != 0:
            windepth=sqrt(uw ** 2 + vw ** 2) / 0.02
# moordyn.m:79
            if (uw ** 2 + vw ** 2) > 0:
                if windepth > z(1):
                    windepth == dot(0.8,z(1))
                if z(2) < (z(1) - windepth):
                    mu=length(z)
# moordyn.m:83
                    z[arange(3,mu + 1)]=z(arange(2,mu))
# moordyn.m:84
                    z[2]=z(1) - windepth
# moordyn.m:85
                    U[arange(3,mu + 1)]=U(arange(2,mu))
# moordyn.m:86
                    U[2]=interp1(concat([z(1),z(3)]),concat([U(1),U(3)]),z(2),'linear')
# moordyn.m:87
                    U[1]=U(1) + uw
# moordyn.m:88
                    V[arange(3,mu + 1)]=V(arange(2,mu))
# moordyn.m:89
                    V[2]=interp1(concat([z(1),z(3)]),concat([V(1),V(3)]),z(2),'linear')
# moordyn.m:90
                    V[1]=V(1) + vw
# moordyn.m:91
                    W[arange(3,mu + 1)]=W(arange(2,mu))
# moordyn.m:92
                    W[2]=interp1(concat([z(1),z(3)]),concat([W(1),W(3)]),z(2),'linear')
# moordyn.m:93
                    rho[arange(3,mu + 1)]=rho(arange(2,mu))
# moordyn.m:94
                    rho[2]=rho(1)
# moordyn.m:95
                else:
                    uwindx=find(z > (z(1) - windepth))
# moordyn.m:97
                    uw1=interp1(concat([z(1),z(1) - windepth]),concat([uw,0]),z(uwindx),'linear')
# moordyn.m:98
                    vw1=interp1(concat([z(1),z(1) - windepth]),concat([vw,0]),z(uwindx),'linear')
# moordyn.m:99
                    izero=find(abs(uw1) < 0.01)
# moordyn.m:100
                    uw1[izero]=0
# moordyn.m:100
                    izero=find(abs(uw1) < 0.01)
# moordyn.m:101
                    uw1[izero]=0
# moordyn.m:101
                    qq=0
# moordyn.m:102
                    for wi in uwindx.reshape(-1):
                        qq=qq + 1
# moordyn.m:104
                        U[wi]=U(wi) + uw1(qq)
# moordyn.m:105
                        V[wi]=V(wi) + vw1(qq)
# moordyn.m:106
        # first change masses/buoyancies into forces (Newtons)
        Bw=dot(B,9.81)
# moordyn.m:113
        BwCO=dot(BCO,9.81)
# moordyn.m:114
        Bmax=Bw(1)
# moordyn.m:115
        N=length(B)
# moordyn.m:117
        # First determine if this is a sub-surface or surface float mooring.
    # This is determined by the maximum height of the velocity profile as the water depth
        Zw=max(z)
# moordyn.m:121
        S=sum(H(1,arange()))
# moordyn.m:122
        if isempty(nomovie):
            disp('  ')
        gamma=1
# moordyn.m:124
        if Zw > S:
            ss=1
# moordyn.m:126
            if logical_and(isempty(nomovie),izloop) == 2:
                disp('This is (starting off as) a sub-surface mooring')
        else:
            ss=0
# moordyn.m:129
            if logical_and(isempty(nomovie),izloop) == 2:
                disp('This is (starting off as) a potential surface float mooring')
        if izloop == 1:
            disp('First, find neutral (no current) mooring component positions.')
        else:
            disp('Searching for a converged solution.')
        Zi=[]
# moordyn.m:138
        Hi=[]
# moordyn.m:138
        Bi=[]
# moordyn.m:138
        Cdi=[]
# moordyn.m:138
        MEi=[]
# moordyn.m:138
        iobj=[]
# moordyn.m:138
        j=1
# moordyn.m:139
        Zi[1]=H(1,N)
# moordyn.m:140
        Hi[arange(),1]=H(arange(),N)
# moordyn.m:141
        Bi[arange(),1]=Bw(arange(),N)
# moordyn.m:142
        Cdi[1]=Cd(N)
# moordyn.m:143
        MEi[1]=ME(N)
# moordyn.m:144
        z0=H(1,N)
# moordyn.m:145
        for i in arange(N - 1,1,- 1).reshape(-1):
            j=j + 1
# moordyn.m:147
            if H(4,i) == 1:
                Hw=fix(H(1,i))
# moordyn.m:149
                dz=0.2
# moordyn.m:150
                if Hw > logical_and(5,Hw) <= 50:
                    dz=0.5
# moordyn.m:152
                else:
                    if Hw > logical_and(50,Hw) <= 100:
                        dz=1
# moordyn.m:154
                    else:
                        if Hw > logical_and(100,Hw) <= 500:
                            dz=2
# moordyn.m:156
                        else:
                            if Hw > 500:
                                dz=5
# moordyn.m:158
                n=round(H(1,i) / dz)
# moordyn.m:160
                dz=H(1,i) / n
# moordyn.m:161
                Elindx[i,1]=j
# moordyn.m:162
                for jj in arange(j,j + n - 1).reshape(-1):
                    Zi[jj]=z0 + dz / 2
# moordyn.m:164
                    z0=z0 + dz
# moordyn.m:165
                    Hi[arange(),jj]=concat([dz,H(2,i),H(3,i),H(4,i)]).T
# moordyn.m:166
                    Bi[jj]=dot(Bw(i),dz)
# moordyn.m:167
                    Cdi[jj]=Cd(i)
# moordyn.m:168
                    MEi[jj]=ME(i)
# moordyn.m:169
                j=j + n - 1
# moordyn.m:171
                Elindx[i,2]=j
# moordyn.m:172
            else:
                Elindx[i,arange(1,2)]=concat([j,j])
# moordyn.m:174
                Zi[j]=z0 + H(1,i) / 2
# moordyn.m:175
                z0=z0 + H(1,i)
# moordyn.m:176
                Hi[arange(),j]=H(arange(),i)
# moordyn.m:177
                Bi[j]=Bw(i)
# moordyn.m:178
                Cdi[j]=Cd(i)
# moordyn.m:179
                MEi[j]=ME(i)
# moordyn.m:180
        J=copy(j)
# moordyn.m:183
        if logical_not(isempty(ZCO)):
            Iobj=[]
# moordyn.m:186
            PIobj=[]
# moordyn.m:186
            mmco=length(ZCO)
# moordyn.m:187
            ZiCO[arange(1,mmco)]=ZCO(arange(mmco,1,- 1))
# moordyn.m:188
            HiCO[arange(),arange(1,mmco)]=HCO(arange(),arange(mmco,1,- 1))
# moordyn.m:189
            CdiCO[arange(1,mmco)]=CdCO(arange(mmco,1,- 1))
# moordyn.m:190
            Piobj[arange(1,mmco)]=Pobj(arange(mmco,1,- 1))
# moordyn.m:191
            Jiobj[arange(1,mmco)]=Jobj(arange(mmco,1,- 1))
# moordyn.m:192
            for jco in arange(1,mmco).reshape(-1):
                Iobj[jco]=fix(dot((abs(Elindx(Jiobj(jco),2) - Elindx(Jiobj(jco),1)) + 1),Piobj(jco))) + Elindx(Jiobj(jco),1)
# moordyn.m:194
                PIobj[jco]=(ZiCO(jco) - Zi(Iobj(jco)) + Hi(1,Iobj(jco)) / 2) / Hi(1,Iobj(jco))
# moordyn.m:195
            # precently, Iobj and PIobj are indexed from bottom to top, flip later
        Elindx=J + 1 - Elindx
# moordyn.m:199
        # now interpolate the velocity profile to 1 m estimates
        dz=1
# moordyn.m:202
        dz0=mean(abs(diff(z)))
# moordyn.m:203
        maxz=sum(H(1,arange()))
# moordyn.m:204
        if dz0 < 1:
            Ui=copy(U)
# moordyn.m:206
            Vi=copy(V)
# moordyn.m:207
            Wi=copy(W)
# moordyn.m:208
            rhoi=copy(rho)
# moordyn.m:209
            zi=copy(z)
# moordyn.m:210
        else:
            if z(1) > z(2):
                dz=- 1
# moordyn.m:212
            if abs(z(end()) - z(1)) < 10:
                dz=dot(sign(dz),0.1)
# moordyn.m:213
            zi=concat([arange(z(1),z(end()),dz)])
# moordyn.m:214
            if logical_not(isempty(U)):
                Ui=interp1(z,U,zi)
# moordyn.m:216
            else:
                zi=concat([arange(maxz,0,- 1)])
# moordyn.m:218
                Ui=interp1(concat([maxz + 1,20,0]),concat([0,0,0]),zi,'linear')
# moordyn.m:219
            if logical_not(isempty(V)):
                Vi=interp1(z,V,zi,'linear')
# moordyn.m:222
            else:
                Vi=zeros(size(Ui))
# moordyn.m:224
            if logical_not(isempty(W)):
                Wi=interp1(z,W,zi,'linear')
# moordyn.m:227
            else:
                Wi=zeros(size(Ui))
# moordyn.m:229
            if logical_not(isempty(rho)):
                rhoi=interp1(z,rho,zi,'linear')
# moordyn.m:232
            else:
                rhoi=dot(ones(size(Ui)),1025)
# moordyn.m:234
        Umag=sqrt(Ui ** 2 + Vi ** 2 + Wi ** 2)
# moordyn.m:237
        N=length(Bi)
# moordyn.m:239
        # Now find the drag on each element assuming first a vertical mooring.
        if ss == 0:
            Bo=- sum(Bi(arange(2,N - 1))) + sum(BwCO)
# moordyn.m:243
            Zi=dot(Zi,Zw) / S
# moordyn.m:244
            Boo=copy(Bo)
# moordyn.m:245
            gamma=Bo / Bmax
# moordyn.m:246
            if gamma > 1:
                gamma=0.9
# moordyn.m:247
        for j in arange(1,N).reshape(-1):
            ico=[]
# moordyn.m:250
            if logical_not(isempty(Iobj)):
                ico=find(Iobj == j)
# moordyn.m:250
            i=find(zi >= logical_and((Zi(j) - 0.5),zi) <= (Zi(j) + 0.5))
# moordyn.m:251
            i=i(1)
# moordyn.m:252
            if Hi(3,j) == 0:
                A=dot(Hi(1,j),Hi(2,j))
# moordyn.m:254
            else:
                A=dot(pi,(Hi(3,j) / 2) ** 2)
# moordyn.m:256
            Qx[j]=dot(dot(dot(dot(dot(0.5,rhoi(i)),Cdi(j)),A),Umag(i)),Ui(i))
# moordyn.m:258
            Qy[j]=dot(dot(dot(dot(dot(0.5,rhoi(i)),Cdi(j)),A),Umag(i)),Vi(i))
# moordyn.m:259
            # if there are clamp-o devices here
            Qxco=0
# moordyn.m:261
            Qyco=0
# moordyn.m:261
            if logical_not(isempty(ico)):
                for icoc in ico.reshape(-1):
                    if HiCO(3,icoc) == 0:
                        Axco=dot(HiCO(1,icoc),HiCO(2,icoc))
# moordyn.m:265
                        Ayco=dot(HiCO(1,icoc),HiCO(2,icoc))
# moordyn.m:266
                        Cdjxco=CdiCO(icoc)
# moordyn.m:267
                        Cdjyco=CdiCO(icoc)
# moordyn.m:268
                    else:
                        Axco=dot(pi,(HiCO(3,icoc) / 2) ** 2)
# moordyn.m:270
                        Ayco=copy(Axco)
# moordyn.m:271
                        Cdjxco=CdiCO(icoc)
# moordyn.m:272
                        Cdjyco=copy(Cdjxco)
# moordyn.m:273
                    Qxco=Qxco + dot(dot(dot(dot(dot(0.5,rhoi(i)),Cdjxco),Axco),Umag(i)),Ui(i))
# moordyn.m:275
                    Qyco=Qyco + dot(dot(dot(dot(dot(0.5,rhoi(i)),Cdjyco),Ayco),Umag(i)),Vi(i))
# moordyn.m:276
            Qx[j]=Qx(j) + Qxco
# moordyn.m:280
            Qy[j]=Qy(j) + Qyco
# moordyn.m:281
            if Hi(3,j) == 0:
                A=dot(pi,(Hi(2,j) / 2) ** 2)
# moordyn.m:284
                if Hi(4,j) == 1:
                    A=0
# moordyn.m:285
            Qz[j]=dot(dot(dot(dot(dot(0.5,rhoi(i)),Cdi(j)),A),Umag(i)),Wi(i))
# moordyn.m:287
            Qzco=0
# moordyn.m:289
            if logical_not(isempty(ico)):
                for icoc in ico.reshape(-1):
                    if HiCO(3,icoc) == 0:
                        Azco=dot(pi,(HiCO(2,icoc) / 2) ** 2)
# moordyn.m:293
                        Cdjzco=CdiCO(icoc)
# moordyn.m:294
                    else:
                        Azco=dot(pi,(HiCO(3,icoc) / 2) ** 2)
# moordyn.m:296
                        Cdjzco=CdiCO(icoc)
# moordyn.m:297
                    Qzco=Qzco + dot(dot(dot(dot(dot(0.5,rhoi(i)),Cdjzco),Azco),Umag(i)),Wi(i))
# moordyn.m:299
            Qz[j]=Qz(j) + Qzco
# moordyn.m:302
        # Flip mooring right side up, indecies now start at top.
        Qx=fliplr(Qx)
# moordyn.m:305
        Qy=fliplr(Qy)
# moordyn.m:305
        Qz=fliplr(Qz)
# moordyn.m:305
        Hi=fliplr(Hi)
# moordyn.m:306
        Bi=fliplr(Bi)
# moordyn.m:306
        Cdi=fliplr(Cdi)
# moordyn.m:306
        MEi=fliplr(MEi)
# moordyn.m:306
        Iobj=J + 1 - Iobj(arange(end(),1,- 1))
# moordyn.m:307
        PIobj=1 - PIobj(arange(end(),1,- 1))
# moordyn.m:308
        # First Pass
    # Now we solve for first order wire angles, starting at the top of the mooring,
    #  where there is no tension from above, Ti=0.
    # Then there are three equations and three unknowns at each element.
    # 1) Qx(i) + T(i)*cos(theta(i))*sin(psi(i)) = T(i+1)*cos(theta(i+1))*sin(psi(i+1))
    # 2) Qy(i) + T(i)*sin(theta(i))*sin(psi(i)) = T(i+1)*sin(theta(i+1))*sin(psi(i+1))
    # 3) Wz(i) + Qz(i) + T(i)*cos(psi(i)) = T(i+1)*cos(psi(i+1))
    # where the Q's are the drags, Wz is the weight/buoyancy,
    #    T(i) is the tension from above, T(i+1) is the tension from below,
    #    psi(i) is the wire angle from z, theta(i) angle in x-y plane
    #    Calculate T(i+1), phi(i+1) and theta(i+1) at element i,
    #    working from the top T(1)=0, to the bottom.
    #  All cylinders have a tangential drag coefficient of 0.01
    #  Here it is assumed that the top of the mooring is a float, or
    #  at least has positive buoyancy and will "lift" the first few elements.
        clear('HiCo','ZiCO','CdiCO')
        Ti=[]
# moordyn.m:327
        theta=[]
# moordyn.m:327
        psi=[]
# moordyn.m:327
        Ti[1]=0
# moordyn.m:328
        theta[1]=0
# moordyn.m:329
        psi[1]=0
# moordyn.m:330
        b=dot(gamma,(Bi(1) + Qz(1)))
# moordyn.m:331
        theta[2]=atan2(Qy(1),Qx(1))
# moordyn.m:332
        Ti[2]=sqrt(Qx(1) ** 2 + Qy(1) ** 2 + b ** 2)
# moordyn.m:333
        psi[2]=real(acos(b / Ti(2)))
# moordyn.m:334
        for i in arange(2,N - 1).reshape(-1):
            ico=[]
# moordyn.m:337
            if logical_not(isempty(Iobj)):
                ico=find(Iobj == i)
# moordyn.m:337
            ip1=i + 1
# moordyn.m:338
            xx=Qx(i) + dot(dot(Ti(i),cos(theta(i))),sin(psi(i)))
# moordyn.m:339
            yy=Qy(i) + dot(dot(Ti(i),sin(theta(i))),sin(psi(i)))
# moordyn.m:340
            zz=Bi(i) + Qz(i) + dot(Ti(i),cos(psi(i)))
# moordyn.m:341
            if logical_not(isempty(ico)):
                zz=zz + sum(BwCO(ico))
# moordyn.m:342
            theta[ip1]=atan2(yy,xx)
# moordyn.m:343
            Ti[ip1]=sqrt(xx ** 2 + yy ** 2 + zz ** 2)
# moordyn.m:344
            if Ti(ip1) != 0:
                psi[ip1]=real(acos(zz / Ti(ip1)))
# moordyn.m:346
            else:
                psi[ip1]=psi(i)
# moordyn.m:348
        # Now integrate from the bottom to the top to get the first order [x,y,z]
    # Allow wire/rope sections to stretch under tension
        for ii in arange(1,2).reshape(-1):
            X[N]=0
# moordyn.m:356
            Y[N]=0
# moordyn.m:356
            Z[N]=Hi(1,N)
# moordyn.m:356
            dx0=0
# moordyn.m:357
            dy0=0
# moordyn.m:357
            dz0=0
# moordyn.m:357
            for i in arange(N - 1,1,- 1).reshape(-1):
                if Hi(2,i) != 0:
                    dL=1 + (dot(Ti(i),4) / (dot(dot(pi,Hi(2,i) ** 2),MEi(i))))
# moordyn.m:360
                else:
                    dL=1
# moordyn.m:362
                LpdL=dot(Hi(1,i),dL)
# moordyn.m:364
                X[i]=X(i + 1) + dot(dot(LpdL,cos(theta(i))),sin(psi(i))) / 2 + dx0
# moordyn.m:365
                Y[i]=Y(i + 1) + dot(dot(LpdL,sin(theta(i))),sin(psi(i))) / 2 + dy0
# moordyn.m:366
                Z[i]=Z(i + 1) + dot(LpdL,cos(psi(i))) / 2 + dz0
# moordyn.m:367
                dx0=dot(dot(LpdL,cos(theta(i))),sin(psi(i))) / 2
# moordyn.m:368
                dy0=dot(dot(LpdL,sin(theta(i))),sin(psi(i))) / 2
# moordyn.m:369
                dz0=dot(LpdL,cos(psi(i))) / 2
# moordyn.m:370
                if Z(i) > logical_and(Zw,Hi(4,i)) == logical_and(1,Bi(i)) > 0:
                    Z[i]=Zw
# moordyn.m:371
                    psi[i]=pi / 2
# moordyn.m:371
                if Z(i) <= Z(N):
                    Z[i]=Z(N)
# moordyn.m:372
                    psi[i]=pi / 2
# moordyn.m:372
        if max(Z) > logical_and(Zw,ss) == 1:
            ss=0
# moordyn.m:375
            gamma=sqrt(gamma)
# moordyn.m:375
        # Now with the first order positions, we must re-estimate the new
    # drags at the new heights (Zi) and for cylinders tilted by psi in flow.
    # If this is a surface float mooring, then increase the amount of the
    # surface float that is submerged until the height to the bottom of the float is
    # within the range Zw > Zf > (Zw - H(1,1))
        rand('state',sum(dot(100,clock)))
        breaknow=0
# moordyn.m:384
        iconv=0
# moordyn.m:384
        icnt=0
# moordyn.m:385
        iavg=0
# moordyn.m:386
        isave=0
# moordyn.m:387
        dg=0.1
# moordyn.m:388
        gf=2
# moordyn.m:388
        dgf=0
# moordyn.m:388
        dgc=0
# moordyn.m:389
        if izloop == 1:
            deltaz=0.1
# moordyn.m:391
        else:
            deltaz=0.01
# moordyn.m:393
        gamma0=dot(Ti(2),cos(psi(2))) / Bi(1)
# moordyn.m:395
        gammas=- 1
# moordyn.m:396
        if gamma < gamma0:
            gammas=1
# moordyn.m:397
        ######################################
    #                                    #
    # Main iteration/convergence loop    #
    #                                    #
    ######################################
        ilines=1
# moordyn.m:403
        ico=[]
# moordyn.m:403
        iiprt=0
# moordyn.m:403
        dgci=10
# moordyn.m:403
        while breaknow == 0:

            isave=isave + 1
# moordyn.m:406
            Zf=Z(1) - Hi(1,1) / 2
# moordyn.m:407
            if ss == 0:
                if isave > iprt:
                    if isave == (iprt + 1):
                        disp('  ')
                        disp(' Take a closer look at the convergence...')
                        disp('Depth       Top      Bottom      % of float used  delta-converge')
                        disp(num2str(concat([Zw(Zf + Hi(1,1)),Zf,dot(gamma,100),dot(gammas,dg)])))
                    iiprt=iiprt + 1
# moordyn.m:416
                    if mod(iiprt,10) == 0:
                        disp(num2str(concat([Zw(Zf + Hi(1,1)),Zf,dot(gamma,100),dot(gammas,dg)])))
                izm=find(Z < 0)
# moordyn.m:419
                Z[izm]=0
# moordyn.m:420
                gamma0=dot(Ti(2),cos(psi(2))) / Bi(1)
# moordyn.m:421
                if dot((1 + gf),dg) >= logical_and(gamma,gammas) == - 1:
                    dg=dg / 10
# moordyn.m:422
                if gamma + (dot(dot((1 + gf),gammas),dg)) >= logical_and(1,gammas) == - 1:
                    dg=dg / 10
# moordyn.m:423
                if (Zf + Hi(1,1)) <= Zw:
                    dgc=dgc + 1
# moordyn.m:425
                    dgf=0
# moordyn.m:426
                    if gammas == - 1:
                        gammas=1
# moordyn.m:428
                        dg=dg / 10
# moordyn.m:429
                        if dg < 1e-10:
                            dg=1e-05
# moordyn.m:430
                        dgc=0
# moordyn.m:431
                    gamma=gamma + dot(dot(gammas,dg),(dot(gf,rand)))
# moordyn.m:433
                    if dgc > dgci:
                        dg=dot(dg,10)
# moordyn.m:435
                        dgc=0
# moordyn.m:436
                    #if (gamma+dg>1, gamma=1; ss=1; end # this is now a subsurface mooring.
                else:
                    if Zw > logical_and(Zf,Zw) < (Zf + Hi(1,1)):
                        dgc=dgc + 1
# moordyn.m:440
                        dgf=0
# moordyn.m:441
                        if ((Zw - Zf) / Hi(1,1)) < gamma:
                            if gammas == 1:
                                gammas=- 1
# moordyn.m:444
                                dg=dg / 10
# moordyn.m:445
                                dgc=0
# moordyn.m:446
                            gamma=gamma + dot(dot(gammas,dg),(dot(gf,rand)))
# moordyn.m:448
                            if dgc > dgci:
                                dg=dot(dg,10)
# moordyn.m:450
                                dgc=0
# moordyn.m:451
                        else:
                            if gammas == - 1:
                                gammas=1
# moordyn.m:455
                                dg=dg / 10
# moordyn.m:456
                                dgc=0
# moordyn.m:457
                            gamma=gamma + dot(dot(gammas,dg),(dot(gf,rand)))
# moordyn.m:459
                            if dgc > dgci:
                                dg=dot(dg,10)
# moordyn.m:461
                                dgc=0
# moordyn.m:462
                        izz=find(Hi(4,arange()) == 0)
# moordyn.m:465
                        if gamma < logical_and(1e-10,dg) < logical_and(1e-09,max(Z(izz))) > logical_and((Zf + Hi(1,1)),iavg) > 200:
                            NN=length(B)
# moordyn.m:467
                            inext=find(B > 1)
# moordyn.m:468
                            if length(inext) > 1:
                                H=H(arange(),arange(inext(2),NN))
# moordyn.m:470
                                B=B(arange(),arange(inext(2),NN))
# moordyn.m:471
                                Cd=Cd(arange(inext(2),NN))
# moordyn.m:472
                                ME=ME(arange(inext(2),NN))
# moordyn.m:473
                                moorele=moorele(arange(inext(2),NN),arange())
# moordyn.m:474
                                U=copy(Utmp)
# moordyn.m:475
                                V=copy(Vtmp)
# moordyn.m:475
                                W=copy(Wtmp)
# moordyn.m:475
                                z=copy(ztmp)
# moordyn.m:475
                                rho=copy(rhotmp)
# moordyn.m:475
                                disp('!! Top link(s) in mooring removed !!')
                                Z=[]
# moordyn.m:477
                                iss=1
# moordyn.m:477
                                dismoor
                                moordyn
                                return X,Y,Z,iobj
                            else:
                                error("'This mooring's not working! Please examine. Strong currents or shears? Try reducing them.'")
                    else:
                        if Zf >= Zw:
                            dgc=dgc + 1
# moordyn.m:486
                            dgf=dgf + 1
# moordyn.m:487
                            if gammas == 1:
                                gammas=- 1
# moordyn.m:489
                                if dg < 1e-10:
                                    dg=1e-05
# moordyn.m:491
                                dgc=0
# moordyn.m:492
                            if dgf > 5:
                                dg=0.001
# moordyn.m:494
                                dgf=0
# moordyn.m:494
                            gamma=gamma + dot(dot(gammas,dg),(dot(gf,rand)))
# moordyn.m:495
                            if dgc > dgci:
                                dg=dot(dg,10)
# moordyn.m:497
                                dgc=0
# moordyn.m:498
                            if gamma >= 1:
                                gamma=1
# moordyn.m:500
                                ss=1
# moordyn.m:500
                            if abs(gamma) < 1e-06:
                                NN=length(B)
# moordyn.m:502
                                inext=find(B > 1)
# moordyn.m:503
                                if length(inext) > 1:
                                    H=H(arange(),arange(inext(2),NN))
# moordyn.m:505
                                    B=B(arange(inext(2),NN))
# moordyn.m:506
                                    Cd=Cd(arange(inext(2),NN))
# moordyn.m:507
                                    ME=ME(arange(inext(2),NN))
# moordyn.m:508
                                    moorele=moorele(arange(inext(2),NN),arange())
# moordyn.m:509
                                    U=copy(Utmp)
# moordyn.m:510
                                    V=copy(Vtmp)
# moordyn.m:510
                                    W=copy(Wtmp)
# moordyn.m:510
                                    z=copy(ztmp)
# moordyn.m:510
                                    rho=copy(rhotmp)
# moordyn.m:510
                                    disp('!! Top link(s) in mooring removed !!')
                                    Z=[]
# moordyn.m:512
                                    iss=1
# moordyn.m:512
                                    dismoor
                                    moordyn
                                    return X,Y,Z,iobj
                                else:
                                    error("'This mooring's not working! Solution isn't converging. Please reduce shear and max speeds.'")
            if gamma < 0:
                gamma=abs(gamma)
# moordyn.m:523
            if gamma >= 1:
                gamma=1
# moordyn.m:524
                ss=1
# moordyn.m:524
            if isave >= 20:
                iavg=iavg + 1
# moordyn.m:526
                if iavg == 1:
                    Tiavg=copy(Ti)
# moordyn.m:528
                    psiavg=copy(psi)
# moordyn.m:529
                    Zavg=copy(Z)
# moordyn.m:530
                    Z1[1]=Z(1)
# moordyn.m:531
                    Xavg=copy(X)
# moordyn.m:532
                    Yavg=copy(Y)
# moordyn.m:533
                    gammavg=copy(gamma)
# moordyn.m:534
                    Uio=copy(Ui)
# moordyn.m:535
                else:
                    Tiavg=Tiavg + Ti
# moordyn.m:537
                    psiavg=psiavg + psi
# moordyn.m:538
                    Zavg=Zavg + Z
# moordyn.m:539
                    Z1[isave]=Z(1)
# moordyn.m:540
                    Xavg=Xavg + X
# moordyn.m:541
                    Yavg=Yavg + Y
# moordyn.m:542
                    gammavg=gammavg + gamma
# moordyn.m:543
                    Z1std=std(Z1)
# moordyn.m:544
            #if iavg > 20 & ss==0 & Z1std > 1, gamma=1; ss=1; end # This is bouncing around, its probably a subsurface solution.
            if iavg > 20:
                X=Xavg / iavg
# moordyn.m:549
                Y=Yavg / iavg
# moordyn.m:550
                Z=Zavg / iavg
# moordyn.m:551
                Ti=Tiavg / iavg
# moordyn.m:552
                psi=psiavg / iavg
# moordyn.m:553
            Zf=Z(1) - Hi(1,1) / 2
# moordyn.m:556
            if ss == logical_and(0,(Zf + dot(gamma,Hi(1,1)))) > Zw:
                Z=dot(Z,(Zw / (Zf + dot(gamma,Hi(1,1)))))
# moordyn.m:557
            icnt=icnt + 1
# moordyn.m:558
            if iiprt == 0:
                if mod(icnt,ilines) == 0:
                    fprintf(1,'.')
                if icnt >= dot(60,ilines):
                    icnt=0
# moordyn.m:561
                    ilines=ilines + 1
# moordyn.m:561
                    fprintf(1,'%8i',isave)
                    disp(' ')
            if iavg > logical_and(iprt,ss) == 1:
                disp(concat([Z(1),(Z(1) - Z1(isave - 1))]))
            phix=atan2((multiply(cos(theta),sin(psi))),cos(psi))
# moordyn.m:565
            phiy=atan2((multiply(sin(theta),sin(psi))),cos(psi))
# moordyn.m:566
            Umag=sqrt(Ui ** 2 + Vi ** 2 + Wi ** 2)
# moordyn.m:567
            Qx=dot(ones(1,N),0.0)
# moordyn.m:569
            Qy=copy(Qx)
# moordyn.m:570
            Qz=copy(Qx)
# moordyn.m:570
            for j in arange(1,N).reshape(-1):
                ico=[]
# moordyn.m:572
                if logical_not(isempty(Iobj)):
                    ico=find(Iobj == j)
# moordyn.m:572
                i=find(zi >= logical_and((Z(j) - 1.0),zi) <= (Z(j) + 1.0))
# moordyn.m:573
                if j == 1:
                    i=find(zi >= logical_and((Z(j) - Hi(1,1)),zi) <= (Z(j) + Hi(1,1)))
# moordyn.m:575
                    if isempty(i):
                        i=1
# moordyn.m:576
                if isempty(i):
                    disp(concat([' Check this configuration: ',num2str(concat([j,Z(1),Z(j)]))]))
                    error("' Can't find the velocity at this element! Near line 572 of moordyn.m'")
                i=i(1)
# moordyn.m:582
                theta2=atan2(Vi(i),Ui(i))
# moordyn.m:584
                UVLmag=dot(sqrt(Ui(i) ** 2 + Vi(i) ** 2),cos(theta(j) - theta2))
# moordyn.m:585
                UL=dot(UVLmag,cos(theta(j)))
# moordyn.m:586
                VL=dot(UVLmag,sin(theta(j)))
# moordyn.m:587
                Up=Ui(i) - UL
# moordyn.m:588
                Vp=Vi(i) - VL
# moordyn.m:589
                theta3=atan2(VL,UL)
# moordyn.m:590
                thetap=atan2(Vp,Up)
# moordyn.m:591
                # First calculate the direct form drag in X Y and Z, plus some frictional surface drag normal to the tilt/theta
                if Hi(3,j) == 0:
                    #
                    A=dot(Hi(1,j),Hi(2,j))
# moordyn.m:597
                    Cdjxy=Cdi(j)
# moordyn.m:598
                    # These are the base form drag terms aligned perpendicular to the theta plan.
                    Qh=dot(dot(dot(dot(0.5,rhoi(i)),Cdjxy),A),(Up ** 2 + Vp ** 2))
# moordyn.m:600
                    Qx[j]=dot(Qh,cos(thetap))
# moordyn.m:601
                    Qy[j]=dot(Qh,sin(thetap))
# moordyn.m:602
                else:
                    A=dot(pi,(Hi(3,j) / 2) ** 2)
# moordyn.m:604
                    Cdj=Cdi(j)
# moordyn.m:605
                    Qh=dot(dot(dot(dot(0.5,rhoi(i)),Cdi(j)),A),(Ui(i) ** 2 + Vi(i) ** 2))
# moordyn.m:607
                    Qx[j]=dot(Qh,cos(theta2))
# moordyn.m:608
                    Qy[j]=dot(Qh,sin(theta2))
# moordyn.m:609
                    Qz[j]=dot(dot(dot(dot(dot(0.5,rhoi(i)),Cdj),A),abs(Wi(i))),Wi(i))
# moordyn.m:610
                Qxco=0
# moordyn.m:613
                Qyco=0
# moordyn.m:613
                Qzco=0
# moordyn.m:613
                if logical_not(isempty(ico)):
                    for icoc in ico.reshape(-1):
                        Up=Ui(i) - UL
# moordyn.m:616
                        Vp=Vi(i) - VL
# moordyn.m:617
                        if HCO(3,icoc) == 0:
                            # re-done 03/09
                            A=dot(HCO(1,icoc),HCO(2,icoc))
# moordyn.m:620
                            Cdjco=CdCO(icoc) + dot(dot(dot(HCO(2,icoc),pi),0.01),(1 - ((pi / 2) - psi(j)) / (pi / 2)))
# moordyn.m:621
                            Qhco=dot(dot(dot(dot(0.5,rhoi(i)),Cdjco),A),(Up ** 2 + Vp ** 2))
# moordyn.m:622
                            Qxco=Qxco + dot(Qhco,cos(thetap))
# moordyn.m:623
                            Qyco=Qyco + dot(Qhco,sin(thetap))
# moordyn.m:624
                        else:
                            A=dot(pi,(HCO(3,icoc) / 2) ** 2)
# moordyn.m:626
                            Cdjco=CdCO(icoc)
# moordyn.m:627
                            Qh=dot(dot(dot(dot(0.5,rhoi(i)),Cdjco),A),(Ui(i) ** 2 + Vi(i) ** 2))
# moordyn.m:628
                            Qxco=Qxco + dot(Qh,cos(theta2))
# moordyn.m:629
                            Qyco=Qyco + dot(Qh,sin(theta2))
# moordyn.m:630
                            Qzco=Qzco + dot(dot(dot(dot(dot(0.5,rhoi(i)),Cdjco),A),abs(Wi(i))),Wi(i))
# moordyn.m:631
                # These are the base form drag terms aligned with u, v and w.
                Qx[j]=Qx(j) + Qxco
# moordyn.m:636
                Qy[j]=Qy(j) + Qyco
# moordyn.m:637
                Qz[j]=Qz(j) + Qzco
# moordyn.m:638
                # The next section represents the lift/normal drag due to tilted
            # cylinder/wire segments, associate only with the flow in the theta plane
            # Hoerner (1965): drag coeficients are reduced by cos(psi)^3=sin(pi/2-psi)^3
            # Chapter III, equations (22) & (23)
            # There are two additional horizontal forces associated with the component of u & v along theta
            # and a lift component coming from w.
            # There are two additional vertical components associated with w along theta and
            # a lift component from u & v along theta.
            # see Dewey's mooreleang.m rountine to plot these components.
                psi2=psi(j) - pi / 2
# moordyn.m:650
                if Hi(3,j) == 0:
                    A=dot(Hi(1,j),Hi(2,j))
# moordyn.m:652
                    CdUV=dot(Cdi(j),cos(psi(j)) ** 3) + dot(dot(dot(Hi(2,j),pi),0.01),(1 - ((pi / 2) - psi(j)) / (pi / 2)))
# moordyn.m:653
                    CdW=dot(Cdi(j),cos(psi2) ** 3) + dot(dot(dot(Hi(2,j),pi),0.01),(1 - ((pi / 2) - psi2) / (pi / 2)))
# moordyn.m:654
                    sl=dot(sign(sin(theta(j))),sign(sin(theta3)))
# moordyn.m:655
                    if sl == 0:
                        sl=1
# moordyn.m:655
                    CdLUV=dot(dot(- Cdi(j),cos(psi(j)) ** 2),sin(psi(j)))
# moordyn.m:656
                    CdLW=dot(dot(Cdi(j),cos(psi2) ** 2),sin(psi2))
# moordyn.m:657
                    QhUV=dot(dot(dot(dot(0.5,rhoi(i)),A),CdUV),UVLmag ** 2)
# moordyn.m:659
                    Qx[j]=Qx(j) + dot(QhUV,cos(theta3))
# moordyn.m:660
                    Qy[j]=Qy(j) + dot(QhUV,sin(theta3))
# moordyn.m:661
                    QhLW=dot(dot(dot(dot(dot(0.5,rhoi(i)),A),CdLW),abs(Wi(i))),Wi(i))
# moordyn.m:663
                    Qx[j]=Qx(j) + dot(QhLW,cos(theta(j)))
# moordyn.m:664
                    Qy[j]=Qy(j) + dot(QhLW,sin(theta(j)))
# moordyn.m:665
                    Qz[j]=Qz(j) + dot(dot(dot(dot(dot(0.5,rhoi(i)),A),CdLUV),UVLmag ** 2),sl)
# moordyn.m:667
                    Qz[j]=Qz(j) + dot(dot(dot(dot(dot(0.5,rhoi(i)),A),CdW),abs(Wi(i))),Wi(i))
# moordyn.m:668
                # Now add any lift terms associated with tiltes clamp-on devices
                Qxco=0
# moordyn.m:671
                Qyco=0
# moordyn.m:671
                Qzco=0
# moordyn.m:671
                if logical_not(isempty(ico)):
                    for icoc in ico.reshape(-1):
                        if HCO(3,icoc) == 0:
                            Aco=dot(HCO(1,icoc),HCO(2,icoc))
# moordyn.m:675
                            Aeco=dot(pi,(HCO(1,icoc) / 2) ** 2)
# moordyn.m:676
                            CdUV=dot(CdCO(icoc),cos(psi(j)) ** 3) + dot(dot(dot(HCO(2,icoc),pi),0.01),(1 - ((pi / 2) - psi(j)) / (pi / 2)))
# moordyn.m:677
                            CdW=dot(CdCO(icoc),cos(psi2) ** 3) + dot(dot(dot(HCO(2,icoc),pi),0.01),(1 - ((pi / 2) - psi2) / (pi / 2)))
# moordyn.m:678
                            sl=dot(sign(sin(theta(j))),sign(sin(theta3)))
# moordyn.m:679
                            if sl == 0:
                                sl=1
# moordyn.m:679
                            CdLUV=dot(dot(- CdCO(icoc),cos(psi(j)) ** 2),sin(psi(j)))
# moordyn.m:680
                            CdLW=dot(dot(CdCO(icoc),cos(psi2) ** 2),sin(psi2))
# moordyn.m:681
                            QhUV=dot(dot(dot(dot(0.5,rhoi(i)),CdUV),Aco),UVLmag ** 2)
# moordyn.m:683
                            Qxco=Qxco + dot(QhUV,cos(theta3))
# moordyn.m:684
                            Qyco=Qyco + dot(QhUV,sin(theta3))
# moordyn.m:685
                            Qzco=Qzco + dot(dot(dot(dot(dot(0.5,rhoi(i)),CdLUV),Aco),UVLmag ** 2),sl)
# moordyn.m:686
                            QhLW=dot(dot(dot(dot(dot(0.5,rhoi(i)),CdLW),Aco),abs(Wi(i))),Wi(i))
# moordyn.m:688
                            Qxco=Qxco + dot(QhLW,cos(theta(j)))
# moordyn.m:689
                            Qyco=Qyco + dot(QhLW,sin(theta(j)))
# moordyn.m:690
                            Qzco=Qzco + dot(dot(dot(dot(dot(0.5,rhoi(i)),CdW),Aco),abs(Wi(i))),Wi(i))
# moordyn.m:691
                            Qhe=dot(dot(dot(dot(dot(0.5,rhoi(i)),0.65),abs(sin(psi(j)))),Aeco),UVLmag ** 2)
# moordyn.m:693
                            Qxco=Qxco + dot(Qhe,cos(theta3))
# moordyn.m:694
                            Qyco=Qyco + dot(Qhe,sin(theta3))
# moordyn.m:695
                            Qzco=Qzco + dot(dot(dot(dot(dot(dot(0.5,rhoi(i)),0.65),abs(cos(psi(j)))),Aeco),abs(Wi(i))),Wi(i))
# moordyn.m:696
                    Qx[j]=Qx(j) + Qxco
# moordyn.m:699
                    Qy[j]=Qy(j) + Qyco
# moordyn.m:700
                    Qz[j]=Qz(j) + Qzco
# moordyn.m:701
            # Now re-solve for displacements with new positions/drags.
            Ti=[]
# moordyn.m:707
            thetaNew=[]
# moordyn.m:707
            psiNew=[]
# moordyn.m:707
            Ti[1]=0
# moordyn.m:708
            # Top element (float) is kept in place by tension from below (only)
            b=Bi(1) + Qz(1)
# moordyn.m:712
            thetaNew[2]=atan2(Qy(1),Qx(1))
# moordyn.m:713
            Ti[2]=sqrt(Qx(1) ** 2 + Qy(1) ** 2 + b ** 2)
# moordyn.m:714
            if gamma < 1:
                Ti[2]=sqrt((dot(gamma,Qx(1))) ** 2 + (dot(gamma,Qy(1))) ** 2 + (dot(gamma,b)) ** 2)
# moordyn.m:716
            psiNew[2]=real(acos(b / Ti(2)))
# moordyn.m:719
            psiNew[1]=psiNew(2) / 2
# moordyn.m:720
            thetaNew[1]=thetaNew(2)
# moordyn.m:721
            # Now Solve from top (just under float) to bottom (top of anchor).
            for Zii0 in arange(1,1).reshape(-1):
                for i in arange(2,N - 1).reshape(-1):
                    ico=[]
# moordyn.m:725
                    if logical_not(isempty(Iobj)):
                        ico=find(Iobj == i)
# moordyn.m:725
                    ip1=i + 1
# moordyn.m:726
                    xx=Qx(i) + dot(dot(Ti(i),cos(thetaNew(i))),sin(psiNew(i)))
# moordyn.m:727
                    yy=Qy(i) + dot(dot(Ti(i),sin(thetaNew(i))),sin(psiNew(i)))
# moordyn.m:728
                    zz=Bi(i) + Qz(i) + dot(Ti(i),cos(psiNew(i)))
# moordyn.m:729
                    if logical_not(isempty(ico)):
                        zz=zz + sum(BwCO(ico))
# moordyn.m:730
                    thetaNew[ip1]=atan2(yy,xx)
# moordyn.m:731
                    Ti[ip1]=sqrt(xx ** 2 + yy ** 2 + zz ** 2)
# moordyn.m:732
                    if Ti(ip1) != 0:
                        psiNew[ip1]=real(acos(zz / Ti(ip1)))
# moordyn.m:734
                    else:
                        psiNew[ip1]=psiNew(i)
# moordyn.m:736
                thetaNew=real(thetaNew)
# moordyn.m:739
                psiNew=real(psiNew)
# moordyn.m:740
                # Now integrate/sum positions from the bottom to the top to get the second order [x,y,z]
            # Allow wire/rope to stretch under tension
                X=[]
# moordyn.m:745
                Y=[]
# moordyn.m:745
                Z=[]
# moordyn.m:745
                X[N]=0
# moordyn.m:746
                Y[N]=0
# moordyn.m:746
                Z[N]=Hi(1,N)
# moordyn.m:746
                Zii=1
# moordyn.m:747
                iint=0
# moordyn.m:747
                while Zii:

                    Zii=0
# moordyn.m:749
                    S=0
# moordyn.m:750
                    SS=0
# moordyn.m:750
                    dx0=0
# moordyn.m:751
                    dy0=0
# moordyn.m:751
                    dz0=0
# moordyn.m:751
                    iint=iint + 1
# moordyn.m:752
                    for i in arange(N - 1,1,- 1).reshape(-1):
                        if Hi(2,i) != logical_and(0,MEi(i)) < Inf:
                            dL=1 + (dot(Ti(i),4) / (dot(dot(pi,Hi(2,i) ** 2),MEi(i))))
# moordyn.m:755
                        else:
                            dL=1
# moordyn.m:757
                        LpdL=dot(Hi(1,i),dL)
# moordyn.m:759
                        S=S + LpdL
# moordyn.m:760
                        dX=dot(dot(LpdL,cos(thetaNew(i))),sin(psiNew(i)))
# moordyn.m:761
                        dY=dot(dot(LpdL,sin(thetaNew(i))),sin(psiNew(i)))
# moordyn.m:762
                        dZ=dot(LpdL,cos(psiNew(i)))
# moordyn.m:763
                        SS=SS + sqrt(dX ** 2 + dY ** 2 + dZ ** 2)
# moordyn.m:764
                        X[i]=X(i + 1) + dX / 2 + dx0 / 2
# moordyn.m:765
                        Y[i]=Y(i + 1) + dY / 2 + dy0 / 2
# moordyn.m:766
                        Z[i]=Z(i + 1) + dZ / 2 + dz0 / 2
# moordyn.m:767
                        if Z(i) > logical_and(Zw,Hi(4,i)) == logical_and(1,Bi(i)) >= 0:
                            Zii=1
# moordyn.m:769
                            Z[i]=Zw
# moordyn.m:769
                            psi[i]=pi / 2
# moordyn.m:770
                        if Z(i) < 0:
                            Zii=1
# moordyn.m:773
                            Z[i]=0
# moordyn.m:773
                            psi[i]=pi / 2
# moordyn.m:774
                        dx0=copy(dX)
# moordyn.m:776
                        dy0=copy(dY)
# moordyn.m:776
                        dz0=copy(dZ)
# moordyn.m:776
                    if iint > 4:
                        Zii=0
# moordyn.m:778
                    # The last position is to the center of the float (thus don't add dx0, dy0 and dz0)

                psi[N]=psi(N - 1)
# moordyn.m:781
            Z=real(Z)
# moordyn.m:783
            X=real(X)
# moordyn.m:783
            Y=real(Y)
# moordyn.m:783
            theta=real(theta)
# moordyn.m:784
            psi=real(psi)
# moordyn.m:785
            scale=0.5
# moordyn.m:788
            psi=psi + dot((psiNew - psi),scale)
# moordyn.m:789
            theta=theta + dot((thetaNew - theta),scale)
# moordyn.m:790
            # Recompute the positions
            S=0
# moordyn.m:794
            SS=0
# moordyn.m:794
            dx0=0
# moordyn.m:795
            dy0=0
# moordyn.m:795
            dz0=0
# moordyn.m:795
            for i in arange(N - 1,1,- 1).reshape(-1):
                if Hi(2,i) != logical_and(0,MEi(i)) < Inf:
                    dL=1 + (dot(Ti(i),4) / (dot(dot(pi,Hi(2,i) ** 2),MEi(i))))
# moordyn.m:798
                else:
                    dL=1
# moordyn.m:800
                LpdL=dot(Hi(1,i),dL)
# moordyn.m:802
                S=S + LpdL
# moordyn.m:803
                dX=dot(dot(LpdL,cos(theta(i))),sin(psi(i)))
# moordyn.m:804
                dY=dot(dot(LpdL,sin(theta(i))),sin(psi(i)))
# moordyn.m:805
                dZ=dot(LpdL,cos(psi(i)))
# moordyn.m:806
                SS=SS + sqrt(dX ** 2 + dY ** 2 + dZ ** 2)
# moordyn.m:807
                X[i]=X(i + 1) + dX / 2 + dx0 / 2
# moordyn.m:808
                Y[i]=Y(i + 1) + dY / 2 + dy0 / 2
# moordyn.m:809
                Z[i]=Z(i + 1) + dZ / 2 + dz0 / 2
# moordyn.m:810
                if Z(i) > logical_and(Zw,Hi(4,i)) == logical_and(1,Bi(i)) >= 0:
                    Z[i]=Zw
# moordyn.m:812
                    psi[i]=pi / 2
# moordyn.m:813
                if Z(i) < 0:
                    Z[i]=0
# moordyn.m:816
                    psi[i]=pi / 2
# moordyn.m:817
                dx0=copy(dX)
# moordyn.m:819
                dy0=copy(dY)
# moordyn.m:819
                dz0=copy(dZ)
# moordyn.m:819
            Z=real(Z)
# moordyn.m:821
            X=real(X)
# moordyn.m:821
            Y=real(Y)
# moordyn.m:821
            psi=real(psi)
# moordyn.m:822
            Zf=Z(1) - Hi(1,1) / 2
# moordyn.m:824
            if max(Z) > logical_and(Zw,ss) == 1:
                ss=0
# moordyn.m:825
                gamma=sqrt(gamma)
# moordyn.m:825
            if isave > 2:
                if abs(Zsave(isave - 1) - Z(1)) < logical_and(deltaz,abs(Zsave(isave - 2) - Zsave(isave - 1))) < deltaz:
                    if ss == logical_and(1,Zw) > logical_and((Zf + Hi(1,1)),gamma) == 1:
                        breaknow=1
# moordyn.m:831
                    else:
                        if ss == logical_and(0,Zw) > logical_and(Zf,Zw) < logical_and((Zf + Hi(1,1)),abs(((Zw - Zf) / Hi(1,1)) - gamma)) < 0.01:
                            breaknow=1
# moordyn.m:834
                if iavg == logical_or(120,(iavg > logical_and(100,dg) < 1e-10)):
                    X=Xavg / iavg
# moordyn.m:839
                    Y=Yavg / iavg
# moordyn.m:840
                    Z=Zavg / iavg
# moordyn.m:841
                    Ti=Tiavg / iavg
# moordyn.m:842
                    psi=psiavg / iavg
# moordyn.m:843
                    breaknow=1
# moordyn.m:844
                    iconv=1
# moordyn.m:845
            Zsave[isave]=Z(1)
# moordyn.m:848
            if logical_not(rem(isave,100)):
                deltaz=dot(2,deltaz)
# moordyn.m:850

        if izloop == 1:
            Zoo=copy(Z)
# moordyn.m:854
            if logical_not(isempty(ZCO)):
                mmco=length(ZCO)
# moordyn.m:856
                for jco in arange(1,mmco).reshape(-1):
                    Z0co[jco]=Z(Iobj(jco)) + (dot(dot(cos(psi(Iobj(jco))),(0.5 - PIobj(jco))),Hi(1,Iobj(jco))))
# moordyn.m:858
    
    # if there are clamp-on device, figure out there final position.
    if logical_not(isempty(ZCO)):
        for jco in arange(1,length(ZCO)).reshape(-1):
            Xfco[jco]=X(Iobj(jco)) + dot(dot(dot(cos(theta(Iobj(jco))),sin(psi(Iobj(jco)))),(0.5 - PIobj(jco))),Hi(1,Iobj(jco)))
# moordyn.m:866
            Yfco[jco]=Y(Iobj(jco)) + dot(dot(dot(sin(theta(Iobj(jco))),sin(psi(Iobj(jco)))),(0.5 - PIobj(jco))),Hi(1,Iobj(jco)))
# moordyn.m:867
            Zfco[jco]=Z(Iobj(jco)) + dot(dot(cos(psi(Iobj(jco))),(0.5 - PIobj(jco))),Hi(1,Iobj(jco)))
# moordyn.m:868
            psifco[jco]=psi(Iobj(jco))
# moordyn.m:869
    
    
    if logical_and(iconv,ss) == 0:
        zcorr=(Zw - dot(Hi(1,1),gamma) + (Hi(1,1) / 2)) - Z(1)
# moordyn.m:874
        if abs(zcorr) > 0.01:
            Z10=Z(1)
# moordyn.m:876
            for ico in arange(1,length(Z)).reshape(-1):
                Z[ico]=Z(ico) + dot(abs(Z(ico) / Z10),zcorr)
# moordyn.m:878
            for jco in arange(1,length(ZCO)).reshape(-1):
                Zfco[jco]=Zfco(jco) + dot(abs(Z(Iobj(jco)) / Z10),zcorr)
# moordyn.m:881
    
    I=(arange(2,N - 1))
# moordyn.m:885
    
    iobj0=find(H(4,arange()) != 1)
# moordyn.m:887
    
    nnum1=num2str(concat([arange(1,length(iobj0))]).T,'%4.0f')
# moordyn.m:888
    nnum1[arange(),end() + 1]=' '
# moordyn.m:889
    nnum2=num2str(iobj0.T,'%4.0f')
# moordyn.m:890
    nnum2[arange(),end() + 1]=' '
# moordyn.m:891
    iEle=concat([nnum1,nnum2,moorele(iobj0,arange())])
# moordyn.m:892
    if logical_not(isempty(ZCO)):
        Iobj0=find(HCO(4,arange()) != 1)
# moordyn.m:894
        nnum1=num2str(concat([arange(1,length(Iobj0))]).T,'%4.0f')
# moordyn.m:895
        nnum1[arange(),end() + 1]=' '
# moordyn.m:896
        nnum2=num2str(Iobj0.T,'%4.0f')
# moordyn.m:897
        nnum2[arange(),end() + 1]=' '
# moordyn.m:898
        IEle=concat([nnum1,nnum2,mooreleCO(Iobj0,arange())])
# moordyn.m:899
    
    
    iobj=find(Hi(4,arange()) != 1)
# moordyn.m:903
    
    jobj=1 + find(Hi(4,I) == logical_and(1,(Hi(4,I - 1) != logical_or(1,Hi(4,I + 1)) != 1)))
# moordyn.m:904
    
    ba=psi(N - 1)
# moordyn.m:905
    Wa=Ti(N) / 9.81
# moordyn.m:906
    VWa=dot(Wa,cos(ba))
# moordyn.m:907
    HWa=dot(Wa,sin(ba))
# moordyn.m:908
    WoB=(Bi(N) + Qz(N) + Ti(N)) / 9.81
# moordyn.m:909
    
    disp('  ')
    if gamma >= logical_or(0.99,ss) == 1:
        disp('This is a sub-surface solution.')
    else:
        disp(concat(['This is a surface solution, using ',num2str(dot(gamma,100),2),'% of the surface buoyancy.']))
    
    #           In otherwords, the # submerged = the percent buoyancy (not so for a shpere).
    
    disp(concat(['Total Tension on Anchor [kg] = ',num2str(Wa,'%8.1f')]))
    disp(concat(['Vertical load [kg] = ',num2str(VWa,'%8.1f'),'  Horizontal load [kg] = ',num2str(HWa,'%8.1f')]))
    # disp(['After applying a WHOI saftey factor:']);
    TWa=dot(1.5,(VWa + HWa / 0.6))
# moordyn.m:921
    disp(concat(['Safe wet anchor mass = ',num2str(TWa,'%8.1f'),' [kg] = ',num2str((dot(TWa,2.2)),'%8.1f'),' [lb]']))
    disp(concat(['Safe dry steel anchor mass = ',num2str((TWa / 0.87),'%8.1f'),' [kg] = ',num2str((dot(TWa,2.2) / 0.87),'%8.1f'),' [lb]']))
    disp(concat(['Safe dry concrete anchor mass = ',num2str((TWa / 0.65),'%8.1f'),' [kg] = ',num2str((dot(TWa,2.2) / 0.65),'%8.1f'),' [lb]']))
    disp(concat(['Weight under anchor = ',num2str(WoB,'%8.1f'),' [kg]  (negative is down)']))
    
    if abs(B(end())) < TWa:
        disp('*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*')
        disp('*!*!*!*  Warning. Anchor is likely TOO light!   *!*!*!*')
        disp('*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*!*')
    
    #disp([S SS]); # display the summed length of mooring as a check...
# reset original current profile.
    z=copy(ztmp)
# moordyn.m:934
    U=copy(Utmp)
# moordyn.m:934
    V=copy(Vtmp)
# moordyn.m:934
    W=copy(Wtmp)
# moordyn.m:934
    rho=copy(rhotmp)
# moordyn.m:934
    # fini
