# Generated with SMOP  0.41-beta
from libsmop import *
# moordynold.m

    
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
#    where 1=steel,2=Nylon,3=Dacron,4=Polyprop,5=Polyethy,6=Kevlar,7=Aluminum
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
    iprt=50
# moordynold.m:41
    
    X=[]
# moordynold.m:43
    Y=[]
# moordynold.m:43
    Z=[]
# moordynold.m:43
    Ti=[]
# moordynold.m:43
    iobj=[]
# moordynold.m:43
    jobj=[]
# moordynold.m:43
    psi=[]
# moordynold.m:43
    if isempty(iss):
        Hs=copy(H)
# moordynold.m:44
        Bs=copy(B)
# moordynold.m:44
        Cds=copy(Cd)
# moordynold.m:44
        MEs=copy(ME)
# moordynold.m:44
    
    if logical_not(isempty(find(B == 0))):
        B[find(B == 0)]=- 0.0001
# moordynold.m:45
    
    mu,nu=size(U,nargout=2)
# moordynold.m:46
    if logical_or((mu == logical_and(0,nu) == 0),max(z)) == 0:
        U=concat([0.1,0.1,0])
# moordynold.m:48
        U=ravel(U)
# moordynold.m:48
        V=copy(U)
# moordynold.m:48
        W=copy(U)
# moordynold.m:48
        z=fix(dot(sum(H(1,arange())),concat([1.5,0.1,0]).T))
# moordynold.m:48
        z=ravel(z)
# moordynold.m:48
        rho=concat([1024,1025,1026]).T
# moordynold.m:48
        rho=ravel(rho)
# moordynold.m:48
    
    z[find(z(arange(1,end() - 1)) == 0)]=0.1
# moordynold.m:50
    
    Zoo=[]
# moordynold.m:51
    Z0co=[]
# moordynold.m:51
    Utmpo=copy(U)
# moordynold.m:52
    Vtmpo=copy(V)
# moordynold.m:52
    Wtmpo=copy(W)
# moordynold.m:52
    U=dot(ones(size(z)),0)
# moordynold.m:53
    V=copy(U)
# moordynold.m:54
    W=copy(U)
# moordynold.m:54
    
    for izloop in arange(1,2).reshape(-1):
        # the first loop to estimate the initial component heights with no currents
        if izloop == 2:
            U=copy(Utmpo)
# moordynold.m:59
            V=copy(Vtmpo)
# moordynold.m:60
            W=copy(Wtmpo)
# moordynold.m:61
        # Add 2# of wind speed to top current (10m) value
        ztmp=copy(z)
# moordynold.m:64
        Utmp=copy(U)
# moordynold.m:64
        Vtmp=copy(V)
# moordynold.m:64
        Wtmp=copy(W)
# moordynold.m:64
        rhotmp=copy(rho)
# moordynold.m:64
        if mu != logical_and(1,nu) != 1:
            if mu == length(z):
                U=U(arange(),1)
# moordynold.m:67
                V=V(arange(),1)
# moordynold.m:68
                W=W(arange(),1)
# moordynold.m:69
            else:
                U=U(1,arange()).T
# moordynold.m:71
                V=V(1,arange()).T
# moordynold.m:72
                W=W(1,arange()).T
# moordynold.m:73
        # Add 2# of wind speed to top current value(s)
        if uw != logical_or(0,vw) != 0:
            windepth=sqrt(uw ** 2 + vw ** 2) / 0.02
# moordynold.m:79
            if (uw ** 2 + vw ** 2) > 0:
                if windepth > z(1):
                    windepth == dot(0.8,z(1))
                if z(2) < (z(1) - windepth):
                    mu=length(z)
# moordynold.m:83
                    z[arange(3,mu + 1)]=z(arange(2,mu))
# moordynold.m:84
                    z[2]=z(1) - windepth
# moordynold.m:85
                    U[arange(3,mu + 1)]=U(arange(2,mu))
# moordynold.m:86
                    U[2]=interp1(concat([z(1),z(3)]),concat([U(1),U(3)]),z(2),'linear')
# moordynold.m:87
                    U[1]=U(1) + uw
# moordynold.m:88
                    V[arange(3,mu + 1)]=V(arange(2,mu))
# moordynold.m:89
                    V[2]=interp1(concat([z(1),z(3)]),concat([V(1),V(3)]),z(2),'linear')
# moordynold.m:90
                    V[1]=V(1) + vw
# moordynold.m:91
                    W[arange(3,mu + 1)]=W(arange(2,mu))
# moordynold.m:92
                    W[2]=interp1(concat([z(1),z(3)]),concat([W(1),W(3)]),z(2),'linear')
# moordynold.m:93
                    rho[arange(3,mu + 1)]=rho(arange(2,mu))
# moordynold.m:94
                    rho[2]=rho(1)
# moordynold.m:95
                else:
                    uwindx=find(z > (z(1) - windepth))
# moordynold.m:97
                    uw1=interp1(concat([z(1),z(1) - windepth]),concat([uw,0]),z(uwindx),'linear')
# moordynold.m:98
                    vw1=interp1(concat([z(1),z(1) - windepth]),concat([vw,0]),z(uwindx),'linear')
# moordynold.m:99
                    izero=find(abs(uw1) < 0.01)
# moordynold.m:100
                    uw1[izero]=0
# moordynold.m:100
                    izero=find(abs(uw1) < 0.01)
# moordynold.m:101
                    uw1[izero]=0
# moordynold.m:101
                    qq=0
# moordynold.m:102
                    for wi in uwindx.reshape(-1):
                        qq=qq + 1
# moordynold.m:104
                        U[wi]=U(wi) + uw1(qq)
# moordynold.m:105
                        V[wi]=V(wi) + vw1(qq)
# moordynold.m:106
        # first change masses/buoyancies into forces (Newtons)
        Bw=dot(B,9.81)
# moordynold.m:113
        BwCO=dot(BCO,9.81)
# moordynold.m:114
        Bmax=Bw(1)
# moordynold.m:115
        N=length(B)
# moordynold.m:117
        # First determine if this is a sub-surface or surface float mooring.
# This is determined by the maximum height of the velocity profile as the water depth
        Zw=max(z)
# moordynold.m:121
        S=sum(H(1,arange()))
# moordynold.m:122
        if isempty(nomovie):
            disp('  ')
        gamma=1
# moordynold.m:124
        if Zw > S:
            ss=1
# moordynold.m:126
            if logical_and(isempty(nomovie),izloop) == 2:
                disp('This is (starting off as) a sub-surface mooring')
        else:
            ss=0
# moordynold.m:129
            if logical_and(isempty(nomovie),izloop) == 2:
                disp('This is (starting off as) a potential surface float mooring')
        if izloop == 1:
            disp('First, find neutral (no current) mooring component positions.')
        else:
            disp('Searching for a converged solution.')
        Zi=[]
# moordynold.m:138
        Hi=[]
# moordynold.m:138
        Bi=[]
# moordynold.m:138
        Cdi=[]
# moordynold.m:138
        MEi=[]
# moordynold.m:138
        iobj=[]
# moordynold.m:138
        j=1
# moordynold.m:139
        Zi[1]=H(1,N)
# moordynold.m:140
        Hi[arange(),1]=H(arange(),N)
# moordynold.m:141
        Bi[arange(),1]=Bw(arange(),N)
# moordynold.m:142
        Cdi[1]=Cd(N)
# moordynold.m:143
        MEi[1]=ME(N)
# moordynold.m:144
        z0=H(1,N)
# moordynold.m:145
        for i in arange(N - 1,1,- 1).reshape(-1):
            j=j + 1
# moordynold.m:147
            if H(4,i) == 1:
                Hw=fix(H(1,i))
# moordynold.m:149
                dz=0.2
# moordynold.m:150
                if Hw > logical_and(5,Hw) <= 50:
                    dz=1
# moordynold.m:152
                else:
                    if Hw > logical_and(50,Hw) <= 100:
                        dz=5
# moordynold.m:154
                    else:
                        if Hw > logical_and(100,Hw) <= 500:
                            dz=10
# moordynold.m:156
                        else:
                            if Hw > 500:
                                dz=50
# moordynold.m:158
                n=fix(H(1,i) / dz)
# moordynold.m:160
                Elindx[i,1]=j
# moordynold.m:161
                for jj in arange(j,j + n - 1).reshape(-1):
                    Zi[jj]=z0 + dz / 2
# moordynold.m:163
                    z0=z0 + dz
# moordynold.m:164
                    Hi[arange(),jj]=concat([dz,H(2,i),H(3,i),H(4,i)]).T
# moordynold.m:165
                    Bi[jj]=dot(Bw(i),dz)
# moordynold.m:166
                    Cdi[jj]=Cd(i)
# moordynold.m:167
                    MEi[jj]=ME(i)
# moordynold.m:168
                j=j + n - 1
# moordynold.m:170
                Elindx[i,2]=j
# moordynold.m:171
            else:
                Elindx[i,arange(1,2)]=concat([j,j])
# moordynold.m:173
                Zi[j]=z0 + H(1,i) / 2
# moordynold.m:174
                z0=z0 + H(1,i)
# moordynold.m:175
                Hi[arange(),j]=H(arange(),i)
# moordynold.m:176
                Bi[j]=Bw(i)
# moordynold.m:177
                Cdi[j]=Cd(i)
# moordynold.m:178
                MEi[j]=ME(i)
# moordynold.m:179
        J=copy(j)
# moordynold.m:182
        # find interpolated indecise for the clamp-on devices
        if logical_not(isempty(ZCO)):
            Iobj=[]
# moordynold.m:185
            PIobj=[]
# moordynold.m:185
            mmco=length(ZCO)
# moordynold.m:186
            ZiCO[arange(1,mmco)]=ZCO(arange(mmco,1,- 1))
# moordynold.m:187
            HiCO[arange(),arange(1,mmco)]=HCO(arange(),arange(mmco,1,- 1))
# moordynold.m:188
            CdiCO[arange(1,mmco)]=CdCO(arange(mmco,1,- 1))
# moordynold.m:189
            Piobj[arange(1,mmco)]=Pobj(arange(mmco,1,- 1))
# moordynold.m:190
            Jiobj[arange(1,mmco)]=Jobj(arange(mmco,1,- 1))
# moordynold.m:191
            for jco in arange(1,mmco).reshape(-1):
                Iobj[jco]=fix(dot((abs(Elindx(Jiobj(jco),2) - Elindx(Jiobj(jco),1)) + 1),Piobj(jco))) + Elindx(Jiobj(jco),1)
# moordynold.m:193
                PIobj[jco]=(ZiCO(jco) - Zi(Iobj(jco)) + Hi(1,Iobj(jco)) / 2) / Hi(1,Iobj(jco))
# moordynold.m:194
            # precently, Iobj and PIobj are indexed from bottom to top, flip later
        Elindx=J + 1 - Elindx
# moordynold.m:198
        # now interpolate the velocity profile to 1 m estimates
        dz=1
# moordynold.m:201
        dz0=mean(abs(diff(z)))
# moordynold.m:202
        maxz=sum(H(1,arange()))
# moordynold.m:203
        if dz0 < 1:
            Ui=copy(U)
# moordynold.m:205
            Vi=copy(V)
# moordynold.m:206
            Wi=copy(W)
# moordynold.m:207
            rhoi=copy(rho)
# moordynold.m:208
            zi=copy(z)
# moordynold.m:209
        else:
            if z(1) > z(2):
                dz=- 1
# moordynold.m:211
            if abs(z(end()) - z(1)) < 10:
                dz=dot(sign(dz),0.1)
# moordynold.m:212
            zi=concat([arange(z(1),z(end()),dz)])
# moordynold.m:213
            if logical_not(isempty(U)):
                Ui=interp1(z,U,zi)
# moordynold.m:215
            else:
                zi=concat([arange(maxz,0,- 1)])
# moordynold.m:217
                Ui=interp1(concat([maxz + 1,20,0]),concat([0,0,0]),zi,'linear')
# moordynold.m:218
            #figure(9);plot(Ui,zi);drawnow
            if logical_not(isempty(V)):
                Vi=interp1(z,V,zi,'linear')
# moordynold.m:222
            else:
                Vi=zeros(size(Ui))
# moordynold.m:224
            if logical_not(isempty(W)):
                Wi=interp1(z,W,zi,'linear')
# moordynold.m:227
            else:
                Wi=zeros(size(Ui))
# moordynold.m:229
            if logical_not(isempty(rho)):
                rhoi=interp1(z,rho,zi,'linear')
# moordynold.m:232
            else:
                rhoi=dot(ones(size(Ui)),1025)
# moordynold.m:234
        Umag=sqrt(Ui ** 2 + Vi ** 2 + Wi ** 2)
# moordynold.m:237
        N=length(Bi)
# moordynold.m:239
        # Now find the drag on each element assuming first a vertical mooring.
        if ss == 0:
            Bo=- sum(Bi(arange(2,N - 1))) + sum(BwCO) + sum(Cdi(arange(2,N - 1)))
# moordynold.m:243
            Zi=dot(Zi,Zw) / S
# moordynold.m:244
            Boo=copy(Bo)
# moordynold.m:245
            gamma=Bo / Bmax
# moordynold.m:246
            if gamma > 1:
                gamma=0.9
# moordynold.m:247
        for j in arange(1,N).reshape(-1):
            ico=[]
# moordynold.m:250
            if logical_not(isempty(Iobj)):
                ico=find(Iobj == j)
# moordynold.m:250
            i=find(zi >= logical_and((Zi(j) - 0.5),zi) <= (Zi(j) + 0.5))
# moordynold.m:251
            i=i(1)
# moordynold.m:252
            if Hi(3,j) == 0:
                A=dot(Hi(1,j),Hi(2,j))
# moordynold.m:254
            else:
                A=dot(pi,(Hi(3,j) / 2) ** 2)
# moordynold.m:256
            Qx[j]=dot(dot(dot(dot(dot(0.5,rhoi(i)),Cdi(j)),A),Umag(i)),Ui(i))
# moordynold.m:258
            Qy[j]=dot(dot(dot(dot(dot(0.5,rhoi(i)),Cdi(j)),A),Umag(i)),Vi(i))
# moordynold.m:259
            # if there are clamp-o devices here
            Qxco=0
# moordynold.m:261
            Qyco=0
# moordynold.m:261
            if logical_not(isempty(ico)):
                for icoc in ico.reshape(-1):
                    if HiCO(3,icoc) == 0:
                        Axco=dot(HiCO(1,icoc),HiCO(2,icoc))
# moordynold.m:265
                        Ayco=dot(HiCO(1,icoc),HiCO(2,icoc))
# moordynold.m:266
                        Cdjxco=CdiCO(icoc)
# moordynold.m:267
                        Cdjyco=CdiCO(icoc)
# moordynold.m:268
                    else:
                        Axco=dot(pi,(HiCO(3,icoc) / 2) ** 2)
# moordynold.m:270
                        Ayco=copy(Axco)
# moordynold.m:271
                        Cdjxco=CdiCO(icoc)
# moordynold.m:272
                        Cdjyco=copy(Cdjxco)
# moordynold.m:273
                    Qxco=Qxco + dot(dot(dot(dot(dot(0.5,rhoi(i)),Cdjxco),Axco),Umag(i)),Ui(i))
# moordynold.m:275
                    Qyco=Qyco + dot(dot(dot(dot(dot(0.5,rhoi(i)),Cdjyco),Ayco),Umag(i)),Vi(i))
# moordynold.m:276
            Qx[j]=Qx(j) + Qxco
# moordynold.m:279
            Qy[j]=Qy(j) + Qxco
# moordynold.m:280
            if Hi(3,j) == 0:
                A=dot(pi,(Hi(2,j) / 2) ** 2)
# moordynold.m:282
                if Hi(4,j) == 1:
                    A=0
# moordynold.m:283
            Qz[j]=dot(dot(dot(dot(dot(0.5,rhoi(i)),Cdi(j)),A),Umag(i)),Wi(i))
# moordynold.m:285
            Qzco=0
# moordynold.m:287
            if logical_not(isempty(ico)):
                for icoc in ico.reshape(-1):
                    if HiCO(3,icoc) == 0:
                        Azco=dot(pi,(HiCO(2,icoc) / 2) ** 2)
# moordynold.m:291
                        Cdjzco=CdiCO(icoc)
# moordynold.m:292
                    else:
                        Azco=dot(pi,(HiCO(3,icoc) / 2) ** 2)
# moordynold.m:294
                        Cdjzco=CdiCO(icoc)
# moordynold.m:295
                    Qzco=Qzco + dot(dot(dot(dot(dot(0.5,rhoi(i)),Azco),Umag(i)),Cdjzco),Wi(i))
# moordynold.m:297
            Qz[j]=Qz(j) + Qzco
# moordynold.m:300
        # Flip mooring right side up, indecies now start at top.
        Qx=fliplr(Qx)
# moordynold.m:303
        Qy=fliplr(Qy)
# moordynold.m:303
        Qz=fliplr(Qz)
# moordynold.m:303
        Hi=fliplr(Hi)
# moordynold.m:304
        Bi=fliplr(Bi)
# moordynold.m:304
        Cdi=fliplr(Cdi)
# moordynold.m:304
        MEi=fliplr(MEi)
# moordynold.m:304
        Iobj=J + 1 - Iobj(arange(end(),1,- 1))
# moordynold.m:305
        PIobj=1 - PIobj(arange(end(),1,- 1))
# moordynold.m:306
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
# moordynold.m:325
        theta=[]
# moordynold.m:325
        psi=[]
# moordynold.m:325
        Ti[1]=0
# moordynold.m:326
        theta[1]=0
# moordynold.m:327
        psi[1]=0
# moordynold.m:328
        b=dot(gamma,(Bi(1) + Qz(1)))
# moordynold.m:329
        theta[2]=atan2(Qy(1),Qx(1))
# moordynold.m:330
        Ti[2]=sqrt(Qx(1) ** 2 + Qy(1) ** 2 + b ** 2)
# moordynold.m:331
        psi[2]=acos(b / Ti(2))
# moordynold.m:332
        # Now Solve from top to bottom.
        for i in arange(2,N - 1).reshape(-1):
            ico=[]
# moordynold.m:335
            if logical_not(isempty(Iobj)):
                ico=find(Iobj == i)
# moordynold.m:335
            ip1=i + 1
# moordynold.m:336
            xx=Qx(i) + dot(dot(Ti(i),cos(theta(i))),sin(psi(i)))
# moordynold.m:337
            yy=Qy(i) + dot(dot(Ti(i),sin(theta(i))),sin(psi(i)))
# moordynold.m:338
            zz=Bi(i) + Qz(i) + dot(Ti(i),cos(psi(i)))
# moordynold.m:339
            if logical_not(isempty(ico)):
                zz=zz + sum(BwCO(ico))
# moordynold.m:340
            theta[ip1]=atan2(yy,xx)
# moordynold.m:341
            Ti[ip1]=sqrt(xx ** 2 + yy ** 2 + zz ** 2)
# moordynold.m:342
            if Ti(ip1) != 0:
                psi[ip1]=acos(zz / Ti(ip1))
# moordynold.m:344
            else:
                psi[ip1]=psi(i)
# moordynold.m:346
        # Now integrate from the bottom to the top to get the first order [x,y,z]
# Allow wire/rope sections to stretch under tension
        for ii in arange(1,2).reshape(-1):
            X[N]=0
# moordynold.m:354
            Y[N]=0
# moordynold.m:354
            Z[N]=Hi(1,N)
# moordynold.m:354
            dx0=0
# moordynold.m:355
            dy0=0
# moordynold.m:355
            dz0=0
# moordynold.m:355
            for i in arange(N - 1,1,- 1).reshape(-1):
                if Hi(2,i) != 0:
                    dL=1 + (dot(Ti(i),4) / (dot(dot(pi,Hi(2,i) ** 2),MEi(i))))
# moordynold.m:358
                else:
                    dL=1
# moordynold.m:360
                LpdL=dot(Hi(1,i),dL)
# moordynold.m:362
                X[i]=X(i + 1) + dot(dot(LpdL,cos(theta(i))),sin(psi(i))) / 2 + dx0
# moordynold.m:363
                Y[i]=Y(i + 1) + dot(dot(LpdL,sin(theta(i))),sin(psi(i))) / 2 + dy0
# moordynold.m:364
                Z[i]=Z(i + 1) + dot(LpdL,cos(psi(i))) / 2 + dz0
# moordynold.m:365
                dx0=dot(dot(LpdL,cos(theta(i))),sin(psi(i))) / 2
# moordynold.m:366
                dy0=dot(dot(LpdL,sin(theta(i))),sin(psi(i))) / 2
# moordynold.m:367
                dz0=dot(LpdL,cos(psi(i))) / 2
# moordynold.m:368
                if Z(i) > logical_and(Zw,Hi(4,i)) == logical_and(1,Bi(i)) > 0:
                    Z[i]=Zw
# moordynold.m:369
                    psi[i]=pi / 2
# moordynold.m:369
                if Z(i) <= Z(N):
                    Z[i]=Z(N)
# moordynold.m:370
                    psi[i]=pi / 2
# moordynold.m:370
        if max(Z) > logical_and(Zw,ss) == 1:
            ss=0
# moordynold.m:373
            gamma=sqrt(gamma)
# moordynold.m:373
        # Now with the first order positions, we must re-estimate the new
# drags at the new heights (Zi) and for cylinders tilted by psi in flow.
# If this is a surface float mooring, then increase the amount of the
# surface float that is submerged until the height to the bottom of the float is 
# within the range Zw > Zf > (Zw - H(1,1))
        rand('state',sum(dot(100,clock)))
        breaknow=0
# moordynold.m:382
        iconv=0
# moordynold.m:382
        icnt=0
# moordynold.m:383
        iavg=0
# moordynold.m:384
        isave=0
# moordynold.m:385
        dg=0.1
# moordynold.m:386
        gf=2
# moordynold.m:386
        dgf=0
# moordynold.m:386
        dgc=0
# moordynold.m:387
        if izloop == 1:
            deltaz=0.1
# moordynold.m:389
        else:
            deltaz=0.01
# moordynold.m:391
        gamma0=dot(Ti(2),cos(psi(2))) / Bi(1)
# moordynold.m:393
        gammas=- 1
# moordynold.m:394
        if gamma < gamma0:
            gammas=1
# moordynold.m:395
        ######################################
#                                    # 
# Main iteration/convergence loop    #
#                                    # 
######################################
        ilines=1
# moordynold.m:401
        ico=[]
# moordynold.m:401
        iiprt=0
# moordynold.m:401
        dgci=10
# moordynold.m:401
        while breaknow == 0:

            isave=isave + 1
# moordynold.m:404
            Zf=Z(1) - Hi(1,1) / 2
# moordynold.m:405
            if ss == 0:
                if isave > iprt:
                    if isave == (iprt + 1):
                        disp('  ')
                        disp(' Take a closer look at the convergence...')
                        disp('Depth       Top      Bottom      % of float used  delta-converge')
                        disp(num2str(concat([Zw(Zf + Hi(1,1)),Zf,dot(gamma,100),dot(gammas,dg)])))
                    iiprt=iiprt + 1
# moordynold.m:414
                    if mod(iiprt,100) == 0:
                        disp(num2str(concat([Zw(Zf + Hi(1,1)),Zf,dot(gamma,100),dot(gammas,dg)])))
                izm=find(Z < 0)
# moordynold.m:417
                Z[izm]=0
# moordynold.m:418
                gamma0=dot(Ti(2),cos(psi(2))) / Bi(1)
# moordynold.m:419
                if dot((1 + gf),dg) >= logical_and(gamma,gammas) == - 1:
                    dg=dg / 10
# moordynold.m:420
                if gamma + (dot(dot((1 + gf),gammas),dg)) >= logical_and(1,gammas) == - 1:
                    dg=dg / 10
# moordynold.m:421
                if (Zf + Hi(1,1)) <= Zw:
                    dgc=dgc + 1
# moordynold.m:423
                    dgf=0
# moordynold.m:424
                    if gammas == - 1:
                        gammas=1
# moordynold.m:426
                        dg=dg / 10
# moordynold.m:427
                        if dg < 1e-10:
                            dg=1e-05
# moordynold.m:428
                        dgc=0
# moordynold.m:429
                    gamma=gamma + dot(dot(gammas,dg),(dot(gf,rand)))
# moordynold.m:431
                    if dgc > dgci:
                        dg=dot(dg,10)
# moordynold.m:433
                        dgc=0
# moordynold.m:434
                    #if (gamma+dg>1, gamma=1; ss=1; end # this is now a subsurface mooring.
                else:
                    if Zw > logical_and(Zf,Zw) < (Zf + Hi(1,1)):
                        dgc=dgc + 1
# moordynold.m:438
                        dgf=0
# moordynold.m:439
                        if ((Zw - Zf) / Hi(1,1)) < gamma:
                            if gammas == 1:
                                gammas=- 1
# moordynold.m:442
                                dg=dg / 10
# moordynold.m:443
                                dgc=0
# moordynold.m:444
                            gamma=gamma + dot(dot(gammas,dg),(dot(gf,rand)))
# moordynold.m:446
                            if dgc > dgci:
                                dg=dot(dg,10)
# moordynold.m:448
                                dgc=0
# moordynold.m:449
                        else:
                            if gammas == - 1:
                                gammas=1
# moordynold.m:453
                                dg=dg / 10
# moordynold.m:454
                                dgc=0
# moordynold.m:455
                            gamma=gamma + dot(dot(gammas,dg),(dot(gf,rand)))
# moordynold.m:457
                            if dgc > dgci:
                                dg=dot(dg,10)
# moordynold.m:459
                                dgc=0
# moordynold.m:460
                        izz=find(Hi(4,arange()) == 0)
# moordynold.m:463
                        if gamma < logical_and(1e-10,dg) < logical_and(1e-09,max(Z(izz))) > logical_and((Zf + Hi(1,1)),iavg) > 200:
                            NN=length(B)
# moordynold.m:465
                            inext=find(B > 1)
# moordynold.m:466
                            if length(inext) > 1:
                                H=H(arange(),arange(inext(2),NN))
# moordynold.m:468
                                B=B(arange(),arange(inext(2),NN))
# moordynold.m:469
                                Cd=Cd(arange(inext(2),NN))
# moordynold.m:470
                                ME=ME(arange(inext(2),NN))
# moordynold.m:471
                                moorele=moorele(arange(inext(2),NN),arange())
# moordynold.m:472
                                U=copy(Utmp)
# moordynold.m:473
                                V=copy(Vtmp)
# moordynold.m:473
                                W=copy(Wtmp)
# moordynold.m:473
                                z=copy(ztmp)
# moordynold.m:473
                                rho=copy(rhotmp)
# moordynold.m:473
                                disp('!! Top link(s) in mooring removed !!')
                                Z=[]
# moordynold.m:475
                                iss=1
# moordynold.m:475
                                dismoor
                                moordyn
                                return X,Y,Z,iobj
                            else:
                                error('This mooring's not working! Please examine. Strong currents or shears? Try reducing them.')
                    else:
                        if Zf >= Zw:
                            dgc=dgc + 1
# moordynold.m:484
                            dgf=dgf + 1
# moordynold.m:485
                            if gammas == 1:
                                gammas=- 1
# moordynold.m:487
                                if dg < 1e-10:
                                    dg=1e-05
# moordynold.m:489
                                dgc=0
# moordynold.m:490
                            if dgf > 5:
                                dg=0.001
# moordynold.m:492
                                dgf=0
# moordynold.m:492
                            gamma=gamma + dot(dot(gammas,dg),(dot(gf,rand)))
# moordynold.m:493
                            if dgc > dgci:
                                dg=dot(dg,10)
# moordynold.m:495
                                dgc=0
# moordynold.m:496
                            if gamma >= 1:
                                gamma=1
# moordynold.m:498
                                ss=1
# moordynold.m:498
                            if gamma < 1e-05:
                                NN=length(B)
# moordynold.m:500
                                inext=find(B > 1)
# moordynold.m:501
                                if length(inext) > 1:
                                    H=H(arange(),arange(inext(2),NN))
# moordynold.m:503
                                    B=B(arange(inext(2),NN))
# moordynold.m:504
                                    Cd=Cd(arange(inext(2),NN))
# moordynold.m:505
                                    ME=ME(arange(inext(2),NN))
# moordynold.m:506
                                    moorele=moorele(arange(inext(2),NN),arange())
# moordynold.m:507
                                    U=copy(Utmp)
# moordynold.m:508
                                    V=copy(Vtmp)
# moordynold.m:508
                                    W=copy(Wtmp)
# moordynold.m:508
                                    z=copy(ztmp)
# moordynold.m:508
                                    rho=copy(rhotmp)
# moordynold.m:508
                                    disp('!! Top link(s) in mooring removed !!')
                                    Z=[]
# moordynold.m:510
                                    iss=1
# moordynold.m:510
                                    dismoor
                                    moordyn
                                    return X,Y,Z,iobj
                                else:
                                    error('This mooring's not working! Solution isn't converging. Please reduce shear and max speeds')
            if gamma < 0:
                gamma=abs(gamma)
# moordynold.m:521
            if gamma >= 1:
                gamma=1
# moordynold.m:522
                ss=1
# moordynold.m:522
            if isave >= logical_and(20,(abs(Zf - Zw) < 1)):
                iavg=iavg + 1
# moordynold.m:525
                if iavg == 1:
                    Tiavg=copy(Ti)
# moordynold.m:527
                    psiavg=copy(psi)
# moordynold.m:528
                    Zavg=copy(Z)
# moordynold.m:529
                    Z1[1]=Z(1)
# moordynold.m:530
                    Xavg=copy(X)
# moordynold.m:531
                    Yavg=copy(Y)
# moordynold.m:532
                    gammavg=copy(gamma)
# moordynold.m:533
                    Uio=copy(Ui)
# moordynold.m:534
                else:
                    Tiavg=Tiavg + Ti
# moordynold.m:536
                    psiavg=psiavg + psi
# moordynold.m:537
                    Zavg=Zavg + Z
# moordynold.m:538
                    Z1[isave]=Z(1)
# moordynold.m:539
                    Xavg=Xavg + X
# moordynold.m:540
                    Yavg=Yavg + Y
# moordynold.m:541
                    gammavg=gammavg + gamma
# moordynold.m:542
                    Z1std=std(Z1)
# moordynold.m:543
            #if iavg > 20 & ss==0 & Z1std > 1, gamma=1; ss=1; end # This is bouncing around, its probably a subsurface solution.
            if iavg > 20:
                Z=Zavg / iavg
# moordynold.m:548
                psi=psiavg / iavg
# moordynold.m:549
            Zf=Z(1) - Hi(1,1) / 2
# moordynold.m:553
            if ss == logical_and(0,(Zf + dot(gamma,Hi(1,1)))) > Zw:
                Z=dot(Z,(Zw / (Zf + dot(gamma,Hi(1,1)))))
# moordynold.m:554
            icnt=icnt + 1
# moordynold.m:555
            if iiprt == 0:
                if mod(icnt,ilines) == 0:
                    fprintf(1,'.')
                if icnt >= dot(60,ilines):
                    icnt=0
# moordynold.m:558
                    ilines=ilines + 1
# moordynold.m:558
                    fprintf(1,'%8i',isave)
                    disp(' ')
            if iavg > logical_and(iprt,ss) == 1:
                disp(concat([Z(1),(Z(1) - Z1(isave - 1))]))
            # Note drag on tilted cylinders/wire is Cd(psi)=Cd(0)*sin^3(phi),
            phix=atan2((multiply(multiply(Ti,cos(theta)),sin(psi))),(multiply(Ti,cos(psi))))
# moordynold.m:562
            phiy=atan2((multiply(multiply(Ti,sin(theta)),sin(psi))),(multiply(Ti,cos(psi))))
# moordynold.m:563
            Umag=sqrt(Ui ** 2 + Vi ** 2 + Wi ** 2)
# moordynold.m:564
            for j in arange(1,N).reshape(-1):
                ico=[]
# moordynold.m:566
                if logical_not(isempty(Iobj)):
                    ico=find(Iobj == j)
# moordynold.m:566
                i=find(zi > logical_and((Z(j) - 1.0),zi) < (Z(j) + 1.0))
# moordynold.m:567
                if j == 1:
                    i=find(zi > logical_and((Z(j) - Hi(1,1)),zi) < (Z(j) + Hi(1,1)))
# moordynold.m:569
                    if isempty(i):
                        i=1
# moordynold.m:570
                if isempty(i):
                    disp(concat([' Check this configuration: ',num2str(concat([j,Z(1),Z(j)]))]))
                    error(' Can't find the velocity at this element! Near line 572 of moordyn.m')
                i=i(1)
# moordynold.m:576
                if Hi(3,j) == 0:
                    Ax=dot(dot(Hi(1,j),Hi(2,j)),abs(cos(phix(j))))
# moordynold.m:578
                    Ay=dot(dot(Hi(1,j),Hi(2,j)),abs(cos(phiy(j))))
# moordynold.m:579
                    Cdjx=dot(Cdi(j),abs(sin(pi / 2 - phix(j)) ** 3)) + dot(dot(pi,0.01),(1 - ((pi / 2) - phix(j)) / (pi / 2)))
# moordynold.m:580
                    Cdjy=dot(Cdi(j),abs(sin(pi / 2 - phiy(j)) ** 3)) + dot(dot(pi,0.01),(1 - ((pi / 2) - phiy(j)) / (pi / 2)))
# moordynold.m:581
                else:
                    Ax=dot(pi,(Hi(3,j) / 2) ** 2)
# moordynold.m:583
                    Ay=copy(Ax)
# moordynold.m:584
                    Cdjx=Cdi(j)
# moordynold.m:585
                    Cdjy=copy(Cdjx)
# moordynold.m:586
                Qxco=0
# moordynold.m:588
                Qyco=0
# moordynold.m:588
                if logical_not(isempty(ico)):
                    for icoc in ico.reshape(-1):
                        if HCO(3,icoc) == 0:
                            Axco=dot(dot(HCO(1,icoc),HCO(2,icoc)),abs(cos(phix(j))))
# moordynold.m:592
                            Ayco=dot(dot(HCO(1,icoc),HCO(2,icoc)),abs(cos(phiy(j))))
# moordynold.m:593
                            Cdjxco=dot(CdCO(icoc),abs(sin(pi / 2 - phix(j)) ** 3)) + dot(dot(pi,0.01),(1 - ((pi / 2) - phix(j)) / (pi / 2)))
# moordynold.m:594
                            Cdjyco=dot(CdCO(icoc),abs(sin(pi / 2 - phiy(j)) ** 3)) + dot(dot(pi,0.01),(1 - ((pi / 2) - phiy(j)) / (pi / 2)))
# moordynold.m:595
                        else:
                            Axco=dot(pi,(HCO(3,icoc) / 2) ** 2)
# moordynold.m:597
                            Ayco=copy(Axco)
# moordynold.m:598
                            Cdjxco=CdCO(icoc)
# moordynold.m:599
                            Cdjyco=copy(Cdjxco)
# moordynold.m:600
                        Qxco=Qxco + dot(dot(dot(dot(dot(0.5,rhoi(i)),Cdjxco),Axco),Umag(i)),Ui(i))
# moordynold.m:602
                        Qyco=Qyco + dot(dot(dot(dot(dot(0.5,rhoi(i)),Cdjyco),Ayco),Umag(i)),Vi(i))
# moordynold.m:603
                Qx[j]=dot(dot(dot(dot(dot(0.5,rhoi(i)),Cdjx),Ax),Umag(i)),Ui(i)) + Qxco
# moordynold.m:606
                Qy[j]=dot(dot(dot(dot(dot(0.5,rhoi(i)),Cdjy),Ay),Umag(i)),Vi(i)) + Qyco
# moordynold.m:607
                if Hi(3,j) == 0:
                    Az=dot(dot(Hi(1,j),abs(sin(psi(j)))),Hi(2,j)) + dot(dot(abs(cos(psi(j))),pi),(Hi(2,j) / 2) ** 2)
# moordynold.m:609
                    Cdjz=Cdi(j) + dot(dot(pi,0.01),(1 - (psi(j) / (pi / 2))))
# moordynold.m:610
                    Cdjx=dot((- sign(phix(j))),(dot(dot(Cdi(j),sign(cos(phix(j)))),abs(sin(pi / 2 - phix(j)) ** 3)) + dot(dot(pi,0.01),(1 - phix(j) / (pi / 2)))))
# moordynold.m:611
                    Cdjy=dot((- sign(phiy(j))),(dot(dot(Cdi(j),sign(cos(phiy(j)))),abs(sin(pi / 2 - phiy(j)) ** 3)) + dot(dot(pi,0.01),(1 - phiy(j) / (pi / 2)))))
# moordynold.m:612
                else:
                    Az=dot(pi,(Hi(3,j) / 2) ** 2)
# moordynold.m:614
                    Cdjz=Cdi(j)
# moordynold.m:615
                    Cdjx=0
# moordynold.m:616
                    Cdjy=0
# moordynold.m:616
                Qzco=0
# moordynold.m:618
                if logical_not(isempty(ico)):
                    for icoc in ico.reshape(-1):
                        if HCO(3,icoc) == 0:
                            Azco=dot(dot(HCO(1,icoc),abs(sin(psi(j)))),HCO(2,icoc)) + dot(dot(abs(cos(psi(j))),pi),(HCO(2,icoc) / 2) ** 2)
# moordynold.m:622
                            Cdjzco=CdCO(icoc) + dot(dot(pi,0.01),(1 - (psi(j) / (pi / 2))))
# moordynold.m:623
                            Cdjxco=dot((- sign(phix(j))),(dot(dot(CdCO(icoc),sign(cos(phix(j)))),abs(sin(pi / 2 - phix(j)) ** 3)) + dot(dot(pi,0.01),(1 - phix(j) / (pi / 2)))))
# moordynold.m:624
                            Cdjyco=dot((- sign(phiy(j))),(dot(dot(CdCO(icoc),sign(cos(phiy(j)))),abs(sin(pi / 2 - phiy(j)) ** 3)) + dot(dot(pi,0.01),(1 - phiy(j) / (pi / 2)))))
# moordynold.m:625
                        else:
                            Azco=dot(pi,(HCO(3,icoc) / 2) ** 2)
# moordynold.m:627
                            Cdjzco=CdCO(icoc)
# moordynold.m:628
                            Cdjxco=0
# moordynold.m:629
                            Cdjyco=0
# moordynold.m:629
                        Qzco=Qzco + dot(dot(dot(dot(0.5,rhoi(i)),Azco),Umag(i)),(dot(Cdjzco,Wi(i)) + dot(dot(Cdjxco,sin(abs(dot(phix(j),2)))),Ui(i)) + dot(dot(Cdjyco,sin(abs(dot(phiy(j),2)))),Vi(i))))
# moordynold.m:631
                Qz[j]=dot(dot(dot(dot(0.5,rhoi(i)),Az),Umag(i)),(dot(Cdjz,Wi(i)) + dot(dot(Cdjx,sin(abs(dot(phix(j),2)))),Ui(i)) + dot(dot(Cdjy,sin(abs(dot(phiy(j),2)))),Vi(i)))) + Qzco
# moordynold.m:634
            # Now re-solve for displacements with new positions/drags.
            Ti=[]
# moordynold.m:637
            theta=[]
# moordynold.m:637
            psi=[]
# moordynold.m:637
            Ti[1]=0
# moordynold.m:638
            b=dot(gamma,(Bi(1) + Qz(1)))
# moordynold.m:639
            theta[2]=atan2(Qy(1),Qx(1))
# moordynold.m:640
            Ti[2]=sqrt(Qx(1) ** 2 + Qy(1) ** 2 + b ** 2)
# moordynold.m:641
            if gamma < 1:
                Ti[2]=sqrt((dot(gamma,Qx(1))) ** 2 + (dot(gamma,Qy(1))) ** 2 + b ** 2)
# moordynold.m:643
            psi[2]=acos(b / Ti(2))
# moordynold.m:646
            psi[1]=psi(2)
# moordynold.m:647
            theta[1]=theta(2)
# moordynold.m:648
            # Now Solve from top (just under float) to bottom (top of anchor).
            for Zii0 in arange(1,2).reshape(-1):
                for i in arange(2,N - 1).reshape(-1):
                    ico=[]
# moordynold.m:652
                    if logical_not(isempty(Iobj)):
                        ico=find(Iobj == i)
# moordynold.m:652
                    ip1=i + 1
# moordynold.m:653
                    xx=Qx(i) + dot(dot(Ti(i),cos(theta(i))),sin(psi(i)))
# moordynold.m:654
                    yy=Qy(i) + dot(dot(Ti(i),sin(theta(i))),sin(psi(i)))
# moordynold.m:655
                    zz=Bi(i) + Qz(i) + dot(Ti(i),cos(psi(i)))
# moordynold.m:656
                    if logical_not(isempty(ico)):
                        zz=zz + sum(BwCO(ico))
# moordynold.m:657
                    theta[ip1]=atan2(yy,xx)
# moordynold.m:658
                    Ti[ip1]=sqrt(xx ** 2 + yy ** 2 + zz ** 2)
# moordynold.m:659
                    if Ti(ip1) != 0:
                        psi[ip1]=acos(zz / Ti(ip1))
# moordynold.m:661
                    else:
                        psi[ip1]=psi(i)
# moordynold.m:663
                # Now integrate from the bottom to the top to get the second order [x,y,z]
	# Allow wire/rope to stretch under tension
                X=[]
# moordynold.m:670
                Y=[]
# moordynold.m:670
                Z=[]
# moordynold.m:670
                X[N]=0
# moordynold.m:671
                Y[N]=0
# moordynold.m:671
                Z[N]=Hi(1,N)
# moordynold.m:671
                Zii=1
# moordynold.m:672
                iint=0
# moordynold.m:672
                while Zii:

                    Zii=0
# moordynold.m:674
                    S=0
# moordynold.m:675
                    SS=0
# moordynold.m:675
                    dx0=0
# moordynold.m:676
                    dy0=0
# moordynold.m:676
                    dz0=0
# moordynold.m:676
                    iint=iint + 1
# moordynold.m:677
                    for i in arange(N - 1,1,- 1).reshape(-1):
                        if Hi(2,i) != logical_and(0,MEi(i)) < Inf:
                            dL=1 + (dot(Ti(i),4) / (dot(dot(pi,Hi(2,i) ** 2),MEi(i))))
# moordynold.m:680
                        else:
                            dL=1
# moordynold.m:682
                        LpdL=dot(Hi(1,i),dL)
# moordynold.m:684
                        S=S + LpdL
# moordynold.m:685
                        dX=dot(dot(LpdL,cos(theta(i))),sin(psi(i)))
# moordynold.m:686
                        dY=dot(dot(LpdL,sin(theta(i))),sin(psi(i)))
# moordynold.m:687
                        dZ=dot(LpdL,cos(psi(i)))
# moordynold.m:688
                        SS=SS + sqrt(dX ** 2 + dY ** 2 + dZ ** 2)
# moordynold.m:689
                        X[i]=X(i + 1) + dX / 2 + dx0 / 2
# moordynold.m:690
                        Y[i]=Y(i + 1) + dY / 2 + dy0 / 2
# moordynold.m:691
                        Z[i]=Z(i + 1) + dZ / 2 + dz0 / 2
# moordynold.m:692
                        if Z(i) > logical_and(Zw,Hi(4,i)) == logical_and(1,Bi(i)) >= 0:
                            Zii=1
# moordynold.m:694
                            Z[i]=Zw
# moordynold.m:694
                            psi[i]=pi / 2
# moordynold.m:695
                        if Z(i) <= 0:
                            Zii=1
# moordynold.m:698
                            psi[i]=pi / 2
# moordynold.m:699
                        dx0=copy(dX)
# moordynold.m:701
                        dy0=copy(dY)
# moordynold.m:701
                        dz0=copy(dZ)
# moordynold.m:701
                    if iint > 4:
                        Zii=0
# moordynold.m:703
                    # The last position is to the center of the float (thus don't add dx0, dy0 and dz0)

                psi[N]=psi(N - 1)
# moordynold.m:706
            Zf=Z(1) - Hi(1,1) / 2
# moordynold.m:708
            if max(Z) > logical_and(Zw,ss) == 1:
                ss=0
# moordynold.m:709
                gamma=sqrt(gamma)
# moordynold.m:709
            if isave > 2:
                if abs(Zsave(isave - 1) - Z(1)) < logical_and(deltaz,abs(Zsave(isave - 2) - Zsave(isave - 1))) < deltaz:
                    if ss == logical_and(1,Zw) > logical_and((Zf + Hi(1,1)),gamma) == 1:
                        breaknow=1
# moordynold.m:715
                    else:
                        if ss == logical_and(0,Zw) > logical_and(Zf,Zw) < logical_and((Zf + Hi(1,1)),abs(((Zw - Zf) / Hi(1,1)) - gamma)) < 0.01:
                            breaknow=1
# moordynold.m:718
                if iavg == logical_or(120,(iavg > logical_and(100,dg) < 1e-10)):
                    X=Xavg / iavg
# moordynold.m:723
                    Y=Yavg / iavg
# moordynold.m:724
                    Z=Zavg / iavg
# moordynold.m:725
                    Ti=Tiavg / iavg
# moordynold.m:726
                    psi=psiavg / iavg
# moordynold.m:727
                    breaknow=1
# moordynold.m:728
                    iconv=1
# moordynold.m:729
            Zsave[isave]=Z(1)
# moordynold.m:732
            if rem(isave,100):
                deltaz=dot(2,deltaz)
# moordynold.m:734

        if izloop == 1:
            Zoo=copy(Z)
# moordynold.m:738
            if logical_not(isempty(ZCO)):
                mmco=length(ZCO)
# moordynold.m:740
                for jco in arange(1,mmco).reshape(-1):
                    Z0co[jco]=Z(Iobj(jco)) + (dot(dot(cos(psi(Iobj(jco))),(0.5 - PIobj(jco))),Hi(1,Iobj(jco))))
# moordynold.m:742
    
    # if there are clamp-on device, figure out there position.
    if logical_not(isempty(ZCO)):
        for jco in arange(1,length(ZCO)).reshape(-1):
            Xfco[jco]=X(Iobj(jco)) + dot(dot(dot(cos(theta(Iobj(jco))),sin(psi(Iobj(jco)))),(0.5 - PIobj(jco))),Hi(1,Iobj(jco)))
# moordynold.m:750
            Yfco[jco]=Y(Iobj(jco)) + dot(dot(dot(sin(theta(Iobj(jco))),sin(psi(Iobj(jco)))),(0.5 - PIobj(jco))),Hi(1,Iobj(jco)))
# moordynold.m:751
            Zfco[jco]=Z(Iobj(jco)) + dot(dot(cos(psi(Iobj(jco))),(0.5 - PIobj(jco))),Hi(1,Iobj(jco)))
# moordynold.m:752
            psifco[jco]=psi(Iobj(jco))
# moordynold.m:753
    
    
    if logical_and(iconv,ss) == 0:
        zcorr=(Zw - dot(Hi(1,1),gamma) + (Hi(1,1) / 2)) - Z(1)
# moordynold.m:758
        if abs(zcorr) > 0.01:
            Z10=Z(1)
# moordynold.m:760
            for ico in arange(1,length(Z)).reshape(-1):
                Z[ico]=Z(ico) + dot(abs(Z(ico) / Z10),zcorr)
# moordynold.m:762
    
    I=(arange(2,N - 1))
# moordynold.m:766
    
    iobj0=find(H(4,arange()) != 1)
# moordynold.m:768
    
    nnum1=num2str(concat([arange(1,length(iobj0))]).T,'%4.0f')
# moordynold.m:769
    nnum1[arange(),end() + 1]=' '
# moordynold.m:770
    nnum2=num2str(iobj0.T,'%4.0f')
# moordynold.m:771
    nnum2[arange(),end() + 1]=' '
# moordynold.m:772
    iEle=concat([nnum1,nnum2,moorele(iobj0,arange())])
# moordynold.m:773
    if logical_not(isempty(ZCO)):
        Iobj0=find(HCO(4,arange()) != 1)
# moordynold.m:775
        nnum1=num2str(concat([arange(1,length(Iobj0))]).T,'%4.0f')
# moordynold.m:776
        nnum1[arange(),end() + 1]=' '
# moordynold.m:777
        nnum2=num2str(Iobj0.T,'%4.0f')
# moordynold.m:778
        nnum2[arange(),end() + 1]=' '
# moordynold.m:779
        IEle=concat([nnum1,nnum2,mooreleCO(Iobj0,arange())])
# moordynold.m:780
    
    
    iobj=find(Hi(4,arange()) != 1)
# moordynold.m:784
    
    jobj=1 + find(Hi(4,I) == logical_and(1,(Hi(4,I - 1) != logical_or(1,Hi(4,I + 1)) != 1)))
# moordynold.m:785
    
    ba=psi(N - 1)
# moordynold.m:786
    Wa=Ti(N) / 9.81
# moordynold.m:787
    VWa=dot(Wa,cos(ba))
# moordynold.m:788
    HWa=dot(Wa,sin(ba))
# moordynold.m:789
    WoB=(Bi(N) + Qz(N) + Ti(N)) / 9.81
# moordynold.m:790
    
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
# moordynold.m:802
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
# moordynold.m:815
    U=copy(Utmp)
# moordynold.m:815
    V=copy(Vtmp)
# moordynold.m:815
    W=copy(Wtmp)
# moordynold.m:815
    rho=copy(rhotmp)
# moordynold.m:815
    # fini