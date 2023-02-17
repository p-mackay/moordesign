# Generated with SMOP  0.41-beta
from libsmop import *
# towdyn.m

    
@function
def towdyn(U=None,z=None,Ht=None,Bt=None,Cdt=None,MEt=None,V=None,W=None,rho=None,Usp=None,Vsp=None,*args,**kwargs):
    varargin = towdyn.varargin
    nargin = towdyn.nargin

    # function [X,Y,Z,iobj]=towdyn(U,z,H,B,Cd,ME,V,W,rho,Usp,Vsp)
    
    # Calculate the towed body positions relative to surface, 
# X (+East), Y (+North) and Z (+Up) all in metres
#    given a velocity profile U(z) at depths z [m] (+up), with U(0)=0 
# For an oceanographic towed body from bottom to top
#    with N elemental components (including wire sections as elements),
#    dimensions Ht(L W D i,N) [m] of each different mooring component/element, 
#    mass/buoyancies Bt(N) [in kg, or kg/m for wire/chain] (+up),
#    Drag coefficients (Cdt(N)). MEt (modulus of elasticity indecies)
#    where 1=steel,2=Nylon,3=Dacron,4=Polyprop,5=Polyethy,6=Kevlar,7=Aluminum, 8=Dyneema
# Output iobj are the idecices of the mooring "elements" not
#    including wire or chain [Ht(4,:)=1] elements.
#    Note: U (and V, W, and rho if provided) must extend to bottom (z=0).
#          Usp and Vsp are the speed velocities in the east and north dir. respec.
# Optional inputs:
#    velocity components V(z) and W(z), rho(z)=density profile
    
    # Ht(1,:) = Length/height of object/element including strength member [m]
#          H(1,N) is the height of the anchor [m]
# Ht(2,:) = Width of cylinder (0=zero if sphere) [m]
# Ht(3,:) = Diameter of sphere (0=zero if cylinder or wire/chain) [m]
# Ht(4,:) = 1 for wire/chain, 2 for fastener, 0 otherwise. Divide wire/chain into 1 m lengths
    
    # May be passed with no arguments, assuming: global U z H B Cd V W rho
# RKD 03/00 03/01
    
    if nargin == 0:
        global U,V,W,z,rho,uw,vw,Usp,Vsp
        global Ht,Bt,Cdt,MEt
    
    global VWa,HWa,ba,ha,wpm
    global Hs,Bs,Cds,MEs,iss
    global moorelet,X,Y,Z,Ti,iobj,jobj,psi,theta
    global HCO,BCO,CdCO,ZCO,Iobj,Jobj,Pobj
    global Z0co,Zfco,Xfco,Yfco,psifco
    global nomovie
    global Zoo,DD,iss,ztmp,Utmp,Vtmp,Wtmp,rhotmp,im1
    # global Qx Qy Qz theta Hi Cdi Ui Vi Wi zi U V z psi phix phiy
    
    if isempty(DD):
        DD=0
# towdyn.m:43
    
    upfac=1.01
# towdyn.m:45
    dnfac=0.99
# towdyn.m:45
    bw=0
# towdyn.m:46
    icprt=1
# towdyn.m:46
    ist=[]
# towdyn.m:46
    im1=[]
# towdyn.m:46
    
    iprt=0
# towdyn.m:48
    
    
    ss=get(0,'ScreenSize')
# towdyn.m:50
    X=[]
# towdyn.m:51
    Y=[]
# towdyn.m:51
    Z=[]
# towdyn.m:51
    Ti=[]
# towdyn.m:51
    iobj=[]
# towdyn.m:51
    jobj=[]
# towdyn.m:51
    psi=[]
# towdyn.m:51
    theta=[]
# towdyn.m:51
    Zoo=[]
# towdyn.m:51
    
    Zi=[]
# towdyn.m:52
    Bi=[]
# towdyn.m:52
    Cdi=[]
# towdyn.m:52
    MEi=[]
# towdyn.m:52
    Hi=[]
# towdyn.m:52
    
    mu,nu=size(U,nargout=2)
# towdyn.m:54
    if z(1) > z(end()):
        z=z(arange(end(),1,- 1))
# towdyn.m:55
    
    # Note for a towed body problem, velocities are measured from surface z=0 down
    if isempty(U):
        U=concat([0,0,0]).T
# towdyn.m:58
        V=copy(U)
# towdyn.m:58
        W=copy(U)
# towdyn.m:58
        z=fix(dot(sum(Ht(1,arange())),concat([0,0.2,1.2]).T))
# towdyn.m:58
        rho=concat([1024,1025,1026]).T
# towdyn.m:58
    
    if isempty(iss):
        Hs=copy(Ht)
# towdyn.m:62
        Bs=copy(Bt)
# towdyn.m:62
        Cds=copy(Cdt)
# towdyn.m:62
        MEs=copy(MEt)
# towdyn.m:62
        ztmp=copy(z)
# towdyn.m:63
        Utmp=copy(U)
# towdyn.m:63
        Vtmp=copy(V)
# towdyn.m:63
        Wtmp=copy(W)
# towdyn.m:63
        rhotmp=copy(rho)
# towdyn.m:63
        iss=1
# towdyn.m:64
    
    # add ship speed to current profile, temp velocities subscript s
    Us=U - Usp
# towdyn.m:67
    
    Vs=V - Vsp
# towdyn.m:68
    Ws=copy(W)
# towdyn.m:69
    
    mu,nu=size(Us,nargout=2)
# towdyn.m:71
    if mu != logical_and(1,nu) != 1:
        if mu == length(z):
            Us=Us(arange(),1)
# towdyn.m:74
            Vs=Vs(arange(),1)
# towdyn.m:75
            Ws=Ws(arange(),1)
# towdyn.m:76
        else:
            Us=Us(1,arange()).T
# towdyn.m:78
            Vs=Vs(1,arange()).T
# towdyn.m:79
            Ws=Ws(1,arange()).T
# towdyn.m:80
    
    # Add 2# of wind speed to top current value(s)
    windepth=sqrt(uw ** 2 + vw ** 2) / 0.02
# towdyn.m:84
    
    if windepth > z(end()):
        windepth == dot(0.8,z(end()))
    
    if (uw ** 2 + vw ** 2) > 0:
        if (z(2) - z(1)) > windepth:
            mu=length(z)
# towdyn.m:88
            z[arange(3,mu + 1)]=z(arange(2,mu))
# towdyn.m:89
            z[2]=windepth
# towdyn.m:90
            Us[arange(3,mu + 1)]=Us(arange(2,mu))
# towdyn.m:91
            Us[2]=interp1(concat([z(1),z(3)]),concat([Us(1),Us(3)]),z(2),'linear')
# towdyn.m:92
            Us[1]=Us(1) + uw
# towdyn.m:93
            Vs[arange(3,mu + 1)]=Vs(arange(2,mu))
# towdyn.m:94
            Vs[2]=interp1(concat([z(1),z(3)]),concat([Vs(1),Vs(3)]),z(2),'linear')
# towdyn.m:95
            Vs[1]=Vs(1) + vw
# towdyn.m:96
            Ws[arange(3,mu + 1)]=Ws(arange(2,mu))
# towdyn.m:97
            Ws[2]=interp1(concat([z(1),z(3)]),concat([Ws(1),Ws(3)]),z(2),'linear')
# towdyn.m:98
            rho[arange(3,mu + 1)]=rho(arange(2,mu))
# towdyn.m:99
            rho[2]=rho(1)
# towdyn.m:100
        else:
            uwindx=find(z < windepth)
# towdyn.m:102
            uw1=interp1(concat([z(1),windepth]),concat([uw,0]),z(uwindx),'linear')
# towdyn.m:103
            vw1=interp1(concat([z(1),windepth]),concat([vw,0]),z(uwindx),'linear')
# towdyn.m:104
            Us[uwindx]=Us(uwindx) + uw1
# towdyn.m:105
            Vs[uwindx]=Vs(uwindx) + vw1
# towdyn.m:106
    
    # first change masses/buoyancies into forces (Newtons)
    Bw=dot(Bt,9.81)
# towdyn.m:110
    
    Bmax=Bw(1)
# towdyn.m:111
    
    BwCO=dot(BCO,9.81)
# towdyn.m:112
    Zw=max(z)
# towdyn.m:113
    
    S=sum(Ht(1,arange()))
# towdyn.m:114
    
    
    N=length(Bt)
# towdyn.m:116
    
    
    disp('Searching for a converged solution.')
    
    j=1
# towdyn.m:120
    
    Zi[1]=Ht(1,N)
# towdyn.m:121
    
    Hi[arange(),1]=Ht(arange(),N)
# towdyn.m:122
    
    Bi[arange(),1]=Bw(arange(),N)
# towdyn.m:123
    Cdi[1]=Cdt(N)
# towdyn.m:124
    MEi[1]=MEt(N)
# towdyn.m:125
    z0=Ht(1,N) / 2
# towdyn.m:126
    
    # Note all z's are now depths below surface
    for i in arange(N - 1,1,- 1).reshape(-1):
        j=j + 1
# towdyn.m:129
        if Ht(4,i) == 1:
            n=fix(Ht(1,i))
# towdyn.m:131
            if n < 5:
                n=5
# towdyn.m:133
            else:
                if n > 50:
                    n=50
# towdyn.m:135
            dz=Ht(1,i) / n
# towdyn.m:137
            Elindx[i,1]=j
# towdyn.m:138
            for jj in arange(j,j + n - 1).reshape(-1):
                Zi[jj]=z0 + dz / 2
# towdyn.m:140
                z0=z0 + dz
# towdyn.m:141
                Hi[arange(),jj]=concat([dz,Ht(2,i),Ht(3,i),Ht(4,i)]).T
# towdyn.m:142
                Bi[jj]=dot(Bw(i),dz)
# towdyn.m:143
                Cdi[jj]=Cdt(i)
# towdyn.m:144
                MEi[jj]=MEt(i)
# towdyn.m:145
            j=j + n - 1
# towdyn.m:147
            Elindx[i,2]=j
# towdyn.m:148
        else:
            Elindx[i,arange(1,2)]=concat([j,j])
# towdyn.m:150
            Zi[j]=z0 + Ht(1,i) / 2
# towdyn.m:151
            z0=z0 + Ht(1,i)
# towdyn.m:152
            Hi[arange(),j]=Ht(arange(),i)
# towdyn.m:153
            Bi[j]=Bw(i)
# towdyn.m:154
            Cdi[j]=Cdt(i)
# towdyn.m:155
            MEi[j]=MEt(i)
# towdyn.m:156
    
    Elindx=j + 1 - Elindx
# towdyn.m:159
    
    # find interpolated indecise for any clamp-on devices
    if logical_not(isempty(ZCO)):
        mmCO=length(BCO)
# towdyn.m:163
        mm=length(Bi)
# towdyn.m:164
        for ico in arange(1,mmCO).reshape(-1):
            for i in arange(mm - 1,2,- 1).reshape(-1):
                if ZCO(ico) > logical_and(sum(Hi(1,arange(mm,i,- 1))),ZCO(ico)) <= sum(Hi(1,arange(mm,(i - 1),- 1))):
                    Iobj[ico]=mm - (i - 1)
# towdyn.m:168
                    dz=ZCO(ico) - sum(Hi(1,arange(mm,i,- 1)))
# towdyn.m:169
                    Piobj[ico]=1 - dz / Hi(1,i - 1)
# towdyn.m:170
                    i=2
# towdyn.m:171
    
    # Sum up vertical depth for hanging tow
    m,N=size(Hi,nargout=2)
# towdyn.m:178
    Zoo[N]=0
# towdyn.m:179
    dz0=0
# towdyn.m:179
    for ii in arange(N - 1,1,- 1).reshape(-1):
        Zoo[ii]=Zoo(ii + 1) + Hi(1,ii) / 2 + dz0
# towdyn.m:181
        dz0=Hi(1,ii) / 2
# towdyn.m:182
    
    
    # now interpolate the velocity profile to 1 m estimates
    dz=1
# towdyn.m:186
    dz0=mean(abs(diff(z)))
# towdyn.m:187
    maxz=sum(Ht(1,arange()))
# towdyn.m:188
    if DD > logical_and(0,max(z)) < maxz:
        indxz=length(z)
# towdyn.m:190
        z[indxz + 1]=dot(1.2,maxz)
# towdyn.m:191
        Us[indxz + 1]=Us(indxz)
# towdyn.m:192
        Vs[indxz + 1]=Vs(indxz)
# towdyn.m:193
        Ws[indxz + 1]=Ws(indxz)
# towdyn.m:194
        rho[indxz + 1]=rho(indxz)
# towdyn.m:195
    
    if dz0 < 1:
        Ui=copy(Us)
# towdyn.m:198
        Vi=copy(Vs)
# towdyn.m:199
        Wi=copy(Ws)
# towdyn.m:200
        rhoi=copy(rho)
# towdyn.m:201
        zi=copy(z)
# towdyn.m:202
    else:
        if z(1) > z(2):
            dz=- 1
# towdyn.m:204
        if abs(z(end()) - z(1)) < 10:
            dz=dot(sign(dz),0.1)
# towdyn.m:205
        zi=concat([arange(z(1),z(end()),dz)])
# towdyn.m:206
        Ui=interp1(z,Us,zi,'linear')
# towdyn.m:207
        Vi=interp1(z,Vs,zi,'linear')
# towdyn.m:208
        Wi=interp1(z,Ws,zi,'linear')
# towdyn.m:209
        rhoi=interp1(z,rho,zi,'linear')
# towdyn.m:210
    
    
    N=length(Bi)
# towdyn.m:213
    
    # Now find the drag on each element assuming first a vertical tow line.
    Umag=sqrt(Ui ** 2 + Vi ** 2 + Wi ** 2)
# towdyn.m:216
    
    for j in arange(1,N).reshape(-1):
        ico=[]
# towdyn.m:218
        if logical_not(isempty(Iobj)):
            ico=find(Iobj == j)
# towdyn.m:218
        i=find(zi >= logical_and((Zi(j) - 0.5),zi) <= (Zi(j) + 0.5))
# towdyn.m:219
        i=i(1)
# towdyn.m:220
        if Hi(3,j) == 0:
            A=dot(Hi(1,j),Hi(2,j))
# towdyn.m:222
        else:
            A=dot(pi,(Hi(3,j) / 2) ** 2)
# towdyn.m:224
        Qx[j]=dot(dot(dot(dot(dot(0.5,rhoi(i)),Cdi(j)),A),Umag(i)),Ui(i))
# towdyn.m:226
        Qy[j]=dot(dot(dot(dot(dot(0.5,rhoi(i)),Cdi(j)),A),Umag(i)),Vi(i))
# towdyn.m:227
        # if there are clamp-o devices here
        Qxco=0
# towdyn.m:229
        Qyco=0
# towdyn.m:229
        if logical_not(isempty(ico)):
            for icoc in ico.reshape(-1):
                if HCO(3,icoc) == 0:
                    Axco=dot(HCO(1,icoc),HCO(2,icoc))
# towdyn.m:233
                    Ayco=dot(HCO(1,icoc),HCO(2,icoc))
# towdyn.m:234
                    Cdjxco=CdCO(icoc)
# towdyn.m:235
                    Cdjyco=CdCO(icoc)
# towdyn.m:236
                else:
                    Axco=dot(pi,(HCO(3,icoc) / 2) ** 2)
# towdyn.m:238
                    Ayco=copy(Axco)
# towdyn.m:239
                    Cdjxco=CdCO(icoc)
# towdyn.m:240
                    Cdjyco=copy(Cdjxco)
# towdyn.m:241
                Qxco=Qxco + dot(dot(dot(dot(dot(0.5,rhoi(i)),Cdjxco),Axco),Umag(i)),Ui(i))
# towdyn.m:243
                Qyco=Qyco + dot(dot(dot(dot(dot(0.5,rhoi(i)),Cdjyco),Ayco),Umag(i)),Vi(i))
# towdyn.m:244
        Qx[j]=Qx(j) + Qxco
# towdyn.m:247
        Qy[j]=Qy(j) + Qxco
# towdyn.m:248
        if Hi(3,j) == 0:
            A=dot(pi,(Hi(2,j) / 2) ** 2)
# towdyn.m:251
            if Hi(4,j) == 1:
                A=0
# towdyn.m:252
        Qz[j]=dot(dot(dot(dot(dot(0.5,rhoi(i)),Cdi(j)),A),Umag(i)),Wi(i))
# towdyn.m:254
        Qzco=0
# towdyn.m:256
        if logical_not(isempty(ico)):
            for icoc in ico.reshape(-1):
                if HCO(3,icoc) == 0:
                    Azco=dot(pi,(HCO(2,icoc) / 2) ** 2)
# towdyn.m:260
                    Cdjzco=CdCO(icoc)
# towdyn.m:261
                else:
                    Azco=dot(pi,(HCO(3,icoc) / 2) ** 2)
# towdyn.m:263
                    Cdjzco=CdCO(icoc)
# towdyn.m:264
                Qzco=Qzco + dot(dot(dot(dot(dot(0.5,rhoi(i)),Cdjzco),Azco),Umag(i)),Wi(i))
# towdyn.m:266
        Qz[j]=Qz(j) + Qzco
# towdyn.m:269
    
    # Flip tow cable right side up, indecies start at bottom.
    Qx=fliplr(Qx)
# towdyn.m:272
    Qy=fliplr(Qy)
# towdyn.m:272
    Qz=fliplr(Qz)
# towdyn.m:272
    Hi=fliplr(Hi)
# towdyn.m:273
    Bi=fliplr(Bi)
# towdyn.m:273
    Cdi=fliplr(Cdi)
# towdyn.m:273
    MEi=fliplr(MEi)
# towdyn.m:273
    HCO=fliplr(HCO)
# towdyn.m:274
    BwCO=fliplr(BwCO)
# towdyn.m:274
    CdCO=fliplr(CdCO)
# towdyn.m:274
    
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
    
    Ti[1]=0
# towdyn.m:292
    
    theta[1]=0
# towdyn.m:293
    psi[1]=0
# towdyn.m:294
    b=Bi(1) + Qz(1)
# towdyn.m:295
    
    theta[2]=atan2(Qy(1),Qx(1))
# towdyn.m:296
    Ti[2]=sqrt(Qx(1) ** 2 + Qy(1) ** 2 + b ** 2)
# towdyn.m:297
    
    psi[2]=atan2(sqrt(Qx(1) ** 2 + Qy(1) ** 2),b)
# towdyn.m:298
    # Now Solve from bottom to top.
    for i in arange(2,N - 1).reshape(-1):
        ico=[]
# towdyn.m:301
        if logical_not(isempty(Iobj)):
            ico=find(Iobj == i)
# towdyn.m:301
        ip1=i + 1
# towdyn.m:302
        xx=Qx(i) + dot(dot(Ti(i),cos(theta(i))),sin(psi(i)))
# towdyn.m:303
        yy=Qy(i) + dot(dot(Ti(i),sin(theta(i))),sin(psi(i)))
# towdyn.m:304
        zz=Bi(i) + Qz(i) + dot(Ti(i),cos(psi(i)))
# towdyn.m:305
        if logical_not(isempty(ico)):
            zz=zz + sum(BwCO(ico))
# towdyn.m:306
        theta[ip1]=atan2(yy,xx)
# towdyn.m:307
        Ti[ip1]=sqrt(xx ** 2 + yy ** 2 + zz ** 2)
# towdyn.m:308
        if Ti(ip1) != 0:
            psi[ip1]=atan2(sqrt(xx ** 2 + yy ** 2),zz)
# towdyn.m:310
        else:
            psi[ip1]=psi(i)
# towdyn.m:312
    
    
    # Now integrate from the top to bottom to get the first order [x,y,z] relative to top
# Allow wire/rope sections to stretch under tension
    
    X[N]=0
# towdyn.m:319
    Y[N]=0
# towdyn.m:319
    Z[N]=Hi(1,N)
# towdyn.m:319
    
    dx0=0
# towdyn.m:320
    dy0=0
# towdyn.m:320
    dz0=0
# towdyn.m:320
    for i in arange(N - 1,1,- 1).reshape(-1):
        if Hi(2,i) != 0:
            dL=1 + (dot(Ti(i),4) / (dot(dot(pi,Hi(2,i) ** 2),MEi(i))))
# towdyn.m:323
        else:
            dL=1
# towdyn.m:325
        LpdL=dot(Hi(1,i),dL)
# towdyn.m:327
        X[i]=X(i + 1) + dot(dot(LpdL,cos(theta(i))),sin(psi(i))) / 2 + dx0
# towdyn.m:328
        Y[i]=Y(i + 1) + dot(dot(LpdL,sin(theta(i))),sin(psi(i))) / 2 + dy0
# towdyn.m:329
        Z[i]=Z(i + 1) - dot(LpdL,cos(psi(i))) / 2 - dz0
# towdyn.m:330
        dx0=dot(dot(LpdL,cos(theta(i))),sin(psi(i))) / 2
# towdyn.m:331
        dy0=dot(dot(LpdL,sin(theta(i))),sin(psi(i))) / 2
# towdyn.m:332
        dz0=dot(LpdL,cos(psi(i))) / 2
# towdyn.m:333
    
    
    # Now with the first order positions, we must re-estimate the new
# drags at the new heights (Zi) and for cylinders tilted by psi in flow.
# If this is a surface float mooring, then increase the amount of the
# surface float that is submerged until the height to the bottom of the float is 
# within the range Zw > Zf > (Zw - H(1,1))
    
    rand('state',sum(dot(100,clock)))
    breaknow=0
# towdyn.m:343
    iconv=0
# towdyn.m:343
    icnt=0
# towdyn.m:344
    iavg=0
# towdyn.m:345
    isave=0
# towdyn.m:346
    dg=0.1
# towdyn.m:347
    gf=0.75
# towdyn.m:347
    dgc=0
# towdyn.m:348
    deltaz=0.01
# towdyn.m:349
    
    im1=[]
# towdyn.m:350
    bw=0
# towdyn.m:350
    Cdskin=0.01
# towdyn.m:351
    
    #                                    # 
		# Main iteration/convergence loop    #
		#                                    # 
		######################################
    dZsave[arange(1,2)]=1000
# towdyn.m:357
    zcor=0
# towdyn.m:358
    ico=0
# towdyn.m:359
    iavgc=2
# towdyn.m:360
    ias=20
# towdyn.m:360
    Umag=sqrt(Ui ** 2 + Vi ** 2 + Wi ** 2)
# towdyn.m:361
    
    while breaknow == 0:

        ist=[]
# towdyn.m:364
        isave=isave + 1
# towdyn.m:365
        Zf=Z(1) - Hi(1,1) / 2
# towdyn.m:366
        icnt=icnt + 1
# towdyn.m:367
        if iprt == 0:
            if mod(icnt,icprt) == 0:
                fprintf(1,'.')
            if icnt == dot(60,icprt):
                icnt=0
# towdyn.m:370
                icprt=icprt + 1
# towdyn.m:370
                fprintf(1,'%8i',isave)
                disp(' ')
        #
        phix=atan2((multiply(multiply(Ti,cos(theta)),sin(pi - psi))),(multiply(Ti,cos(pi - psi))))
# towdyn.m:373
        phiy=atan2((multiply(multiply(Ti,sin(theta)),sin(pi - psi))),(multiply(Ti,cos(pi - psi))))
# towdyn.m:374
        Qx=dot(ones(1,N),0.0)
# towdyn.m:375
        Qy=copy(Qx)
# towdyn.m:376
        Qz=copy(Qx)
# towdyn.m:376
        psi1=pi - psi
# towdyn.m:377
        for j in arange(1,N).reshape(-1):
            ico=[]
# towdyn.m:379
            if logical_not(isempty(Iobj)):
                ico=find(Iobj == j)
# towdyn.m:380
            if min(Z) < 0:
                indx=find(Z <= 0)
# towdyn.m:381
                Z[indx]=0.01
# towdyn.m:381
            i=find(zi > logical_and((Z(j) - 1.0),zi) < (Z(j) + 1.0))
# towdyn.m:382
            if isempty(i):
                disp(concat(['Check this configuration: ',num2str(concat([j,Z(1),Z(j)]))]))
                error(' Can't find the velocity at this element! Near line 352 of towdyn.m')
            i=i(1)
# towdyn.m:387
            theta2=atan2(Vi(i),Ui(i))
# towdyn.m:389
            UVLmag=dot(sqrt(Ui(i) ** 2 + Vi(i) ** 2),cos(theta(j) - theta2))
# towdyn.m:390
            UL=dot(UVLmag,cos(theta(j)))
# towdyn.m:391
            VL=dot(UVLmag,sin(theta(j)))
# towdyn.m:392
            Up=Ui(i) - UL
# towdyn.m:393
            Vp=Vi(i) - VL
# towdyn.m:394
            theta3=atan2(VL,UL)
# towdyn.m:395
            thetap=atan2(Vp,Up)
# towdyn.m:396
            psi2=psi1(j) - pi / 2
# towdyn.m:397
            # The exposed area must be a positive number, but the drag coefficient may
      #     have to change sign in order to get the proper lift characteristics.
      # We will now (April 2009) split the drag on tilted cylinders into two calculations:
      #    1) the portion due to flow in the theta (tilt) plane and 
      #    2) the flow perpendicular to the theta plane
      # For spheres, the drag is more classic rho/2*Cd*A*U^2
            if Hi(3,j) == 0:
                A=dot(Hi(1,j),Hi(2,j))
# towdyn.m:407
                # first estimate the horizontal drag vector from Up & Vp, then break into components
                Qh=dot(dot(dot(dot(0.5,rhoi(i)),Cdi(j)),A),(Up ** 2 + Vp ** 2))
# towdyn.m:409
                Qx[j]=dot(Qh,cos(thetap))
# towdyn.m:410
                Qy[j]=dot(Qh,sin(thetap))
# towdyn.m:411
            else:
                A=dot(pi,(Hi(3,j) / 2) ** 2)
# towdyn.m:413
                Qh=dot(dot(dot(dot(0.5,rhoi(i)),Cdi(j)),A),(Ui(i) ** 2 + Vi(i) ** 2))
# towdyn.m:414
                Qx[j]=dot(Qh,cos(theta2))
# towdyn.m:415
                Qy[j]=dot(Qh,sin(theta2))
# towdyn.m:416
                Qz[j]=dot(dot(dot(dot(dot(0.5,rhoi(i)),Cdi(j)),A),abs(Wi(i))),Wi(i))
# towdyn.m:417
            Qxco=0
# towdyn.m:419
            Qyco=0
# towdyn.m:419
            Qzco=0
# towdyn.m:419
            if logical_not(isempty(ico)):
                if HCO(3,ico) == 0:
                    A=dot(HCO(1,ico),HCO(2,ico))
# towdyn.m:422
                    Cdjco=CdCO(ico) + dot(dot(dot(HCO(2,ico),pi),0.01),(1 - ((pi / 2 - psi1(j)) / (pi / 2))))
# towdyn.m:423
                    Qhco=dot(dot(dot(dot(0.5,rhoi(i)),Cdjco),A),(Up ** 2 + Vp ** 2))
# towdyn.m:424
                    Qxco=dot(Qhco,cos(thetap))
# towdyn.m:425
                    Qyco=dot(Qhco,sin(thetap))
# towdyn.m:426
                else:
                    A=dot(pi,(HCO(3,ico) / 2) ** 2)
# towdyn.m:428
                    Qhco=dot(dot(dot(dot(0.5,rhoi(i)),CdCO(ico)),A),(Ui(i) ** 2 + Vi(i) ** 2))
# towdyn.m:429
                    Qxco=dot(Qhco,cos(theta2))
# towdyn.m:430
                    Qyco=dot(Qhco,sin(theta2))
# towdyn.m:431
                    Qzco=dot(dot(dot(dot(dot(0.5,rhoi(i)),CdCO(j)),A),abs(Wi(i))),Wi(i))
# towdyn.m:432
            Qx[j]=Qx(j) + Qxco
# towdyn.m:435
            Qy[j]=Qy(j) + Qyco
# towdyn.m:436
            Qz[j]=Qz(j) + Qzco
# towdyn.m:437
            # This next section then estimates the drag associated with a lift/normal force in the theta plane
       # From Hoerner(1965) pages 3-11.
       # Because we are up-side down with a towed body, we use psi1=pi-psi and psi2=psi1-pi/2 (normal)
            if Hi(3,j) == 0:
                A=dot(Hi(1,j),Hi(2,j))
# towdyn.m:444
                CdUV=dot(Cdi(j),cos(psi1(j)) ** 3) + dot(dot(dot(Hi(2,j),pi),0.01),(1 - ((pi / 2) - psi1(j)) / (pi / 2)))
# towdyn.m:445
                CdW=dot(Cdi(j),cos(psi2) ** 3) + dot(dot(dot(Hi(2,j),pi),0.01),(1 - ((pi / 2) - psi1(j)) / (pi / 2)))
# towdyn.m:446
                sl=dot(sign(sin(theta(j))),sign(sin(theta3)))
# towdyn.m:447
                if sl == 0:
                    sl=1
# towdyn.m:448
                CdLUV=dot(dot(- Cdi(j),cos(psi1(j)) ** 2),sin(psi1(j)))
# towdyn.m:449
                CdLW=dot(dot(Cdi(j),cos(psi2) ** 2),sin(psi2))
# towdyn.m:450
                QhUV=dot(dot(dot(dot(0.5,rhoi(i)),CdUV),A),UVLmag ** 2)
# towdyn.m:452
                Qx[j]=Qx(j) + dot(QhUV,cos(theta3))
# towdyn.m:453
                Qy[j]=Qy(j) + dot(QhUV,sin(theta3))
# towdyn.m:454
                QhLW=dot(dot(dot(dot(dot(0.5,rhoi(i)),CdLW),A),abs(Wi(i))),Wi(i))
# towdyn.m:456
                Qx[j]=Qx(j) + dot(QhLW,cos(theta(j)))
# towdyn.m:457
                Qy[j]=Qy(j) + dot(QhLW,sin(theta(j)))
# towdyn.m:458
                Qz[j]=Qz(j) + dot(dot(dot(dot(dot(0.5,rhoi(i)),CdLUV),A),UVLmag ** 2),sl)
# towdyn.m:460
                Qz[j]=Qz(j) + dot(dot(dot(dot(dot(0.5,rhoi(i)),CdW),A),abs(Wi(i))),Wi(i))
# towdyn.m:461
            Qxco=0
# towdyn.m:463
            Qyco=0
# towdyn.m:463
            Qzco=0
# towdyn.m:463
            if logical_not(isempty(ico)):
                if HCO(3,ico) == 0:
                    Aco=dot(HCO(1,ico),HCO(2,ico))
# towdyn.m:466
                    Aeco=dot(pi,(HCO(1,ico) / 2) ** 2)
# towdyn.m:467
                    CdUV=dot(CdCO(ico),cos(psi1(j)) ** 3) + dot(dot(dot(HCO(2,j),pi),0.01),(1 - ((pi / 2) - psi1(j)) / (pi / 2)))
# towdyn.m:468
                    CdW=dot(CdCO(ico),cos(psi2) ** 3) + dot(dot(dot(HCO(2,j),pi),0.01),(1 - ((pi / 2) - psi1(j)) / (pi / 2)))
# towdyn.m:469
                    sl=dot(sign(sin(theta(j))),sign(sin(theta3)))
# towdyn.m:470
                    if sl == 0:
                        sl=1
# towdyn.m:471
                    CdLUV=dot(dot(- CdCO(ico),cos(psi1(j)) ** 2),sin(psi1(j)))
# towdyn.m:472
                    CdLW=dot(dot(CdCO(ico),cos(psi2) ** 2),sin(psi2))
# towdyn.m:473
                    QhUV=dot(dot(dot(dot(0.5,rhoi(i)),CdUV),Aco),UVLmag ** 2)
# towdyn.m:475
                    Qxco=dot(QhUV,cos(theta3))
# towdyn.m:476
                    Qyco=dot(QhUV,sin(theta3))
# towdyn.m:477
                    Qzco=dot(dot(dot(dot(dot(0.5,rhoi(i)),CdLUV),Aco),UVLmag ** 2),sl)
# towdyn.m:478
                    QhLW=dot(dot(dot(dot(dot(0.5,rhoi(i)),CdLW),Aco),abs(Wi(i))),Wi(i))
# towdyn.m:480
                    Qxco=Qxco + dot(QhLW,cos(theta(j)))
# towdyn.m:481
                    Qyco=Qyco + dot(QhLW,sin(theta(j)))
# towdyn.m:482
                    Qzco=Qzco + dot(dot(dot(dot(dot(0.5,rhoi(i)),CdW),Aco),abs(Wi(i))),Wi(i))
# towdyn.m:483
                    Qhe=dot(dot(dot(dot(dot(0.5,rhoi(i)),0.65),abs(sin(psi1(j)))),Aeco),UVLmag ** 2)
# towdyn.m:485
                    Qxco=Qxco + dot(Qhe,cos(theta3))
# towdyn.m:486
                    Qyco=Qyco + dot(Qhw,sin(theta3))
# towdyn.m:487
                    Qzco=Qzco + dot(dot(dot(dot(dot(dot(0.5,rhoi(i)),0.65),abs(cos(psi1(j)))),Aeco),abs(Wi(i))),Wi(i))
# towdyn.m:488
            Qx[j]=Qx(j) + Qxco
# towdyn.m:491
            Qy[j]=Qy(j) + Qyco
# towdyn.m:492
            Qz[j]=Qz(j) + Qzco
# towdyn.m:493
        # Now re-solve for displacements with new tensions/drags.
        Ti[1]=0
# towdyn.m:496
        b=Bi(1) + Qz(1)
# towdyn.m:497
        theta[2]=atan2(Qy(1),Qx(1))
# towdyn.m:498
        theta[1]=theta(2)
# towdyn.m:499
        Ti[2]=sqrt(Qx(1) ** 2 + Qy(1) ** 2 + b ** 2)
# towdyn.m:500
        psi[1]=atan2(sqrt(Qx(1) ** 2 + Qy(1) ** 2),b)
# towdyn.m:502
        psi[2]=psi(1)
# towdyn.m:503
        # For sphere objects, this changes nothing, for cylinders it matters.
        # Now Solve from bottom to top
        for i in arange(2,N - 1).reshape(-1):
            ico=[]
# towdyn.m:508
            if logical_not(isempty(Iobj)):
                ico=find(Iobj == i)
# towdyn.m:508
            ip1=i + 1
# towdyn.m:509
            if (Z(i) + dot(Hi(1,i),cos(psi(i))) / 2) > logical_and(0,(Z(i) - dot(Hi(1,i),cos(psi(i))) / 2)) < logical_and(0,Bi(i)) > 0:
                perofB=abs((Z(i) + (dot(Hi(1,i),cos(psi(i))) / 2) / Hi(1,i)))
# towdyn.m:511
                perofB=min(concat([1,perofB]))
# towdyn.m:512
                perofB=max(concat([0.01,perofB]))
# towdyn.m:512
            else:
                perofB=1
# towdyn.m:514
            xx=dot(perofB,Qx(i)) + dot(dot(Ti(i),cos(theta(i))),sin(pi - psi(i)))
# towdyn.m:516
            yy=dot(perofB,Qy(i)) + dot(dot(Ti(i),sin(theta(i))),sin(pi - psi(i)))
# towdyn.m:517
            zz=dot(perofB,(Bi(i) + Qz(i))) + dot(Ti(i),cos(psi(i)))
# towdyn.m:518
            if logical_and(logical_not(isempty(im1)),logical_not(isempty(ist))):
                if im1 == i:
                    zz=zz + sum(Bi(arange(ist + 1,end() - 1))) / 2
# towdyn.m:520
            if logical_not(isempty(ico)):
                zz=zz + sum(BwCO(ico))
# towdyn.m:522
            theta[ip1]=atan2(yy,xx)
# towdyn.m:523
            Ti[ip1]=sqrt(xx ** 2 + yy ** 2 + zz ** 2)
# towdyn.m:524
            if Ti(ip1) != 0:
                psi[ip1]=atan2(sqrt(xx ** 2 + yy ** 2),zz)
# towdyn.m:526
            else:
                psi[ip1]=psi(i)
# towdyn.m:528
        #
        # Now integrate from the bottom to top to get the second order [x,y,z] relative to the bottom
	# Allow wire/rope to stretch under tension
        X[N]=0
# towdyn.m:536
        Y[N]=0
# towdyn.m:536
        Z[N]=0
# towdyn.m:536
        dx0=0
# towdyn.m:537
        dy0=0
# towdyn.m:537
        dz0=0
# towdyn.m:537
        for i in arange(N - 1,1,- 1).reshape(-1):
            if Hi(2,i) != 0:
                dL=1 + (dot(Ti(i),4) / (dot(dot(pi,Hi(2,i) ** 2),MEi(i))))
# towdyn.m:540
            else:
                dL=1
# towdyn.m:542
            LpdL=dot(Hi(1,i),dL)
# towdyn.m:544
            X[i]=X(i + 1) + dot(dot(LpdL,cos(theta(i))),sin(pi - psi(i))) / 2 + dx0
# towdyn.m:545
            Y[i]=Y(i + 1) + dot(dot(LpdL,sin(theta(i))),sin(pi - psi(i))) / 2 + dy0
# towdyn.m:546
            Z[i]=Z(i + 1) - dot(LpdL,cos(psi(i))) / 2 - dz0
# towdyn.m:547
            dx0=dot(dot(LpdL,cos(theta(i))),sin(psi(i))) / 2
# towdyn.m:548
            dy0=dot(dot(LpdL,sin(theta(i))),sin(psi(i))) / 2
# towdyn.m:549
            dz0=dot(LpdL,cos(psi(i))) / 2
# towdyn.m:550
        psi[N]=psi(N - 1)
# towdyn.m:552
        im1=[]
# towdyn.m:553
        iup=0
# towdyn.m:553
        indx0=find(Z == min(Z))
# towdyn.m:554
        Znew=0
# towdyn.m:555
        if min((Z(arange(1,end() - 1)) - Hi(1,arange(1,end() - 1)) / 2)) < logical_and(0,sum(find(Bi(find((Z(arange(1,end() - 1)) - Hi(1,arange(1,end() - 1)) / 2) < 0)) > 0))) > 0:
            indx=find((Z(arange(1,end() - 1)) - Hi(1,arange(1,end() - 1)) / 2) < 0)
# towdyn.m:558
            im1=find(Bi(indx) > 0)
# towdyn.m:559
            if logical_not(isempty(im1)):
                im1=indx(im1(1))
# towdyn.m:561
                ist=im1 + 1
# towdyn.m:562
                peroffiw=(abs(dot(Ti(im1 - 1),cos(psi(im1 - 1)))) + abs(sum(Bi(arange(im1 + 1,end()))) / 2)) / Bi(im1)
# towdyn.m:563
                peroffiw=max(concat([0,peroffiw]))
# towdyn.m:564
                peroffiw=min(concat([1,peroffiw]))
# towdyn.m:564
                Znew=dot(peroffiw,Hi(1,im1)) - Hi(1,im1) / 2
# towdyn.m:565
                Zist=Znew - Hi(1,im1) / 4
# towdyn.m:566
                X[im1]=0
# towdyn.m:567
                Y[im1]=0
# towdyn.m:567
                Z[im1]=Znew
# towdyn.m:567
                dx0=dot(dot((Hi(1,im1) / 2),cos(theta(i))),sin(psi(i))) / 2
# towdyn.m:568
                dy0=dot(dot((Hi(1,im1) / 2),sin(theta(i))),sin(psi(i))) / 2
# towdyn.m:569
                dz0=dot((Hi(1,im1) / 2),cos(psi(i))) / 2
# towdyn.m:570
                for i in arange(im1 - 1,1,- 1).reshape(-1):
                    if Hi(2,i) != 0:
                        dL=1 + (dot(Ti(i),4) / (dot(dot(pi,Hi(2,i) ** 2),MEi(i))))
# towdyn.m:573
                    else:
                        dL=1
# towdyn.m:575
                    LpdL=dot(Hi(1,i),dL)
# towdyn.m:577
                    X[i]=X(i + 1) + dot(dot(LpdL,cos(theta(i))),sin(psi(i))) / 2 + dx0
# towdyn.m:578
                    Y[i]=Y(i + 1) + dot(dot(LpdL,sin(theta(i))),sin(psi(i))) / 2 + dy0
# towdyn.m:579
                    Z[i]=Z(i + 1) - dot(LpdL,cos(psi(i))) / 2 - dz0
# towdyn.m:580
                    dx0=dot(dot(LpdL,cos(theta(i))),sin(psi(i))) / 2
# towdyn.m:581
                    dy0=dot(dot(LpdL,sin(theta(i))),sin(psi(i))) / 2
# towdyn.m:582
                    dz0=dot(LpdL,cos(psi(i))) / 2
# towdyn.m:583
                iup=1
# towdyn.m:585
        if isave >= 20:
            iavg=iavg + 1
# towdyn.m:591
            if iavg == 1:
                Tiavg=copy(Ti)
# towdyn.m:593
                psiavg=copy(psi)
# towdyn.m:594
                Zavg=copy(Z)
# towdyn.m:595
                Z1[1]=Z(1)
# towdyn.m:596
                Xavg=copy(X)
# towdyn.m:597
                Yavg=copy(Y)
# towdyn.m:598
            else:
                Tiavg=Tiavg + Ti
# towdyn.m:600
                psiavg=psiavg + psi
# towdyn.m:601
                Zavg=Zavg + Z
# towdyn.m:602
                Z1[isave]=Z(1)
# towdyn.m:603
                Xavg=Xavg + X
# towdyn.m:604
                Yavg=Yavg + Y
# towdyn.m:605
                Z1std=std(Z1)
# towdyn.m:606
        if isave == logical_and(1,iprt) == 1:
            hf9=figure(9)
# towdyn.m:610
            set(hf9,'Position',concat([ss(3) - 220,10,190,100]))
            clf
        if iprt == logical_and(1,isave) > 20:
            figure(9)
            hold('on')
            plot(isave,Z(1),'ob')
            drawnow
            disp(concat([iavg,Z(1),Zavg(1) / iavg,dZsave(isave - 1)]))
        if isave > 2:
            if abs(Zsave(isave - 1) - Z(1)) < logical_and(deltaz,abs(Zsave(isave - 2) - Zsave(isave - 1))) < deltaz:
                breaknow=1
# towdyn.m:618
            if iavg == 200:
                X=Xavg / iavg
# towdyn.m:621
                Y=Yavg / iavg
# towdyn.m:622
                Z=Zavg / iavg
# towdyn.m:623
                Ti=Tiavg / iavg
# towdyn.m:624
                psi=psiavg / iavg
# towdyn.m:625
                breaknow=1
# towdyn.m:626
                iconv=1
# towdyn.m:627
            dZsave[isave]=(Zsave(isave - 1) - Z(1))
# towdyn.m:629
        Zsave[isave]=Z(1)
# towdyn.m:631
        if iavg > ias:
            Z=Zavg / iavg
# towdyn.m:634
            psi=psiavg / iavg
# towdyn.m:635
            if iavg > dot(ias,iavgc):
                Tiavg=dot(ias,Tiavg) / iavg
# towdyn.m:637
                psiavg=dot(ias,psiavg) / iavg
# towdyn.m:638
                Zavg=dot(ias,Zavg) / iavg
# towdyn.m:639
                Yavg=dot(ias,Yavg) / iavg
# towdyn.m:640
                Xavg=dot(ias,Xavg) / iavg
# towdyn.m:641
                iavg=copy(ias)
# towdyn.m:642
                iavgc=iavgc + 1
# towdyn.m:643

    
    
    tenfac=1.0
# towdyn.m:650
    decr=0.99
# towdyn.m:651
    incr=1.005
# towdyn.m:651
    iincr=- 1
# towdyn.m:652
    
    # The next section is for a tow with float configuration only, with the float on/near the surface
#  This solution has been broken into two separate "solutions", matched at the float
    if iup == logical_and(1,logical_not(isempty(ist))):
        if ist < logical_or(N,(min((Z(arange(1,end() - 1)) - Hi(1,arange(1,end() - 1)) / 2)) < logical_and(0,sum(find(Bi(find((Z(arange(1,end() - 1)) - Hi(1,arange(1,end() - 1)) / 2) < 0)) > 0))) > 0)):
            indx=find((Z(arange(1,end() - 1)) - Hi(1,arange(1,end() - 1)) / 2) < 0)
# towdyn.m:658
            im1=find(Bi(indx) > 0)
# towdyn.m:659
            if logical_not(isempty(im1)):
                disp('Solving for upper "loop".')
                im1=indx(im1(1))
# towdyn.m:662
                ist=im1 + 1
# towdyn.m:663
                Thx=Qx(im1) + dot(dot(Ti(im1 - 1),cos(theta(im1))),sin(pi - psi(im1)))
# towdyn.m:664
                Thy=Qy(im1) + dot(dot(Ti(im1 - 1),sin(theta(im1))),sin(pi - psi(im1)))
# towdyn.m:665
                break2=1
# towdyn.m:666
                icl2=0
# towdyn.m:667
                while break2:

                    icl2=icl2 + 1
# towdyn.m:669
                    phix=atan2((multiply(multiply(Ti,cos(theta)),sin(pi - psi))),(multiply(Ti,cos(pi - psi))))
# towdyn.m:670
                    phiy=atan2((multiply(multiply(Ti,sin(theta)),sin(pi - psi))),(multiply(Ti,cos(pi - psi))))
# towdyn.m:671
                    for j in arange(ist,N).reshape(-1):
                        ico=[]
# towdyn.m:673
                        if logical_not(isempty(Iobj)):
                            ico=find(Iobj == j)
# towdyn.m:673
                        if Z(j) < 0:
                            Z[j]=0.01
# towdyn.m:674
                        i=find(zi > logical_and((Z(j) - 1.0),zi) < (Z(j) + 1.0))
# towdyn.m:675
                        i=i(1)
# towdyn.m:676
                        if Hi(3,j) == 0:
                            Ax=dot(dot(Hi(1,j),Hi(2,j)),abs(cos(phix(j))))
# towdyn.m:678
                            Ay=dot(dot(Hi(1,j),Hi(2,j)),abs(cos(phiy(j))))
# towdyn.m:679
                            Cdjx=dot(Cdi(j),cos(phix(j)) ** 2) + dot(dot(pi,0.01),abs(sin(phix(j))))
# towdyn.m:680
                            Cdjy=dot(Cdi(j),cos(phiy(j)) ** 2) + dot(dot(pi,0.01),abs(sin(phiy(j))))
# towdyn.m:681
                            if Cdi(j) == 0.0:
                                Cdjx=0
# towdyn.m:682
                                Cdjy=0
# towdyn.m:682
                        else:
                            Ax=dot(pi,(Hi(3,j) / 2) ** 2)
# towdyn.m:684
                            Ay=copy(Ax)
# towdyn.m:685
                            Cdjx=Cdi(j)
# towdyn.m:686
                            Cdjy=copy(Cdjx)
# towdyn.m:687
                        Qxco=0
# towdyn.m:689
                        Qyco=0
# towdyn.m:689
                        if logical_not(isempty(ico)):
                            if HCO(3,ico) == 0:
                                Axco=dot(dot(HCO(1,ico),HCO(2,ico)),abs(cos(phix(j))))
# towdyn.m:692
                                Ayco=dot(dot(HCO(1,ico),HCO(2,ico)),abs(cos(phiy(j))))
# towdyn.m:693
                                Cdjxco=dot(CdCO(ico),cos(phix(j)) ** 2) + dot(dot(pi,0.01),abs(sin(phix(j))))
# towdyn.m:694
                                Cdjyco=dot(CdCO(ico),cos(phiy(j)) ** 2) + dot(dot(pi,0.01),abs(sin(phiy(j))))
# towdyn.m:695
                                if CdCO(ico) == 0.0:
                                    Cdjxco=0
# towdyn.m:696
                                    Cdjyco=0
# towdyn.m:696
                            else:
                                Axco=dot(pi,(HCO(3,ico) / 2) ** 2)
# towdyn.m:698
                                Ayco=copy(Axco)
# towdyn.m:699
                                Cdjxco=CdCO(ico)
# towdyn.m:700
                                Cdjyco=copy(Cdjxco)
# towdyn.m:701
                            Qxco=dot(dot(dot(dot(dot(0.5,rhoi(i)),Cdjxco),Axco),Umag(i)),Ui(i))
# towdyn.m:703
                            Qyco=dot(dot(dot(dot(dot(0.5,rhoi(i)),Cdjyco),Ayco),Umag(i)),Vi(i))
# towdyn.m:704
                        Qx[j]=dot(dot(dot(dot(dot(0.5,rhoi(i)),Cdjx),Ax),Umag(i)),Ui(i)) + Qxco
# towdyn.m:706
                        Qy[j]=dot(dot(dot(dot(dot(0.5,rhoi(i)),Cdjy),Ay),Umag(i)),Vi(i)) + Qyco
# towdyn.m:707
                        if Hi(3,j) == 0:
                            Az=dot(dot(Hi(1,j),abs(sin(psi(j)))),Hi(2,j)) + dot(dot(abs(cos(psi(j))),pi),(Hi(2,j) / 2) ** 2)
# towdyn.m:709
                            Cdjz=Cdi(j) + dot(dot(pi,0.01),(1 - (psi(j) / (pi / 2))))
# towdyn.m:710
                            Cdjx=dot(sign(dot(sign(phix(j)),cos(phix(j)))),(dot(dot(Cdi(j),abs(cos(phix(j)))),sin(phix(j)) ** 2) + dot(dot(pi,0.01),abs(sin(phix(j))))))
# towdyn.m:711
                            Cdjy=dot(sign(dot(sign(phiy(j)),cos(phiy(j)))),(dot(dot(Cdi(j),abs(cos(phiy(j)))),sin(phiy(j)) ** 2) + dot(dot(pi,0.01),abs(sin(phiy(j))))))
# towdyn.m:712
                            if Cdi(j) == 0.0:
                                Cdjx=0
# towdyn.m:713
                                Cdjy=0
# towdyn.m:713
                        else:
                            Az=dot(pi,(Hi(3,j) / 2) ** 2)
# towdyn.m:715
                            Cdjz=Cdi(j)
# towdyn.m:716
                            Cdjx=0
# towdyn.m:717
                            Cdjy=0
# towdyn.m:717
                        Qzco=0
# towdyn.m:719
                        if logical_not(isempty(ico)):
                            if HCO(3,ico) == 0:
                                Azco=dot(dot(HCO(1,ico),abs(sin(psi(j)))),HCO(2,ico)) + dot(dot(abs(cos(psi(j))),pi),(HCO(2,ico) / 2) ** 2)
# towdyn.m:722
                                Cdjzco=CdCO(ico) + dot(dot(pi,0.01),(1 - (psi(j) / (pi / 2))))
# towdyn.m:723
                                Cdjxco=dot(sign(dot(sign(phix(j)),cos(phix(j)))),(dot(dot(CdCO(ico),abs(cos(phix(j)))),sin(phix(j)) ** 2) + dot(dot(pi,0.01),abs(sin(phix(j))))))
# towdyn.m:724
                                Cdjyco=dot(sign(dot(sign(phiy(j)),cos(phix(j)))),(dot(dot(CdCO(ico),abs(cos(phiy(j)))),sin(phiy(j)) ** 2) + dot(dot(pi,0.01),abs(sin(phiy(j))))))
# towdyn.m:725
                                if CdCO(ico) == 0.0:
                                    Cdjxco=0
# towdyn.m:726
                                    Cdjyco=0
# towdyn.m:726
                            else:
                                Azco=dot(pi,(HCO(3,ico) / 2) ** 2)
# towdyn.m:728
                                Cdjzco=CdCO(ico)
# towdyn.m:729
                                Cdjxco=0
# towdyn.m:730
                                Cdjyco=0
# towdyn.m:730
                            Qzco=dot(dot(dot(dot(0.5,rhoi(i)),Azco),Umag(i)),(dot(Cdjzco,Wi(i)) + dot(Cdjxco,Ui(i)) + dot(Cdjyco,Vi(i))))
# towdyn.m:732
                        Qz[j]=dot(dot(dot(dot(0.5,rhoi(i)),Az),Umag(i)),(dot(Cdjz,Wi(i)) + dot(Cdjx,Ui(i)) + dot(Cdjy,Vi(i)))) + Qzco
# towdyn.m:734
                    Qzz=Qz(arange(ist,N - 1))
# towdyn.m:737
                    Tv1=dot(tenfac,sum(Bi(arange(ist + 1,end() - 1)))) / 2 + dot(sum(Qzz(find(Qzz < 0))),0.9)
# towdyn.m:738
                    Ti[ist]=sqrt(Thx ** 2 + Thy ** 2 + Tv1 ** 2)
# towdyn.m:739
                    psi[ist]=atan2(sqrt(Thx ** 2 + Thy ** 2),Tv1)
# towdyn.m:740
                    theta[ist]=atan2(Thy,Thx)
# towdyn.m:741
                    for i in arange(ist,N - 1).reshape(-1):
                        ip1=i + 1
# towdyn.m:743
                        xx=Qx(i) + dot(dot(Ti(i),cos(theta(i))),sin(pi - psi(i)))
# towdyn.m:744
                        yy=Qy(i) + dot(dot(Ti(i),sin(theta(i))),sin(pi - psi(i)))
# towdyn.m:745
                        zz=dot(Ti(i),cos(psi(i))) - Bi(i) - Qz(i)
# towdyn.m:746
                        theta[ip1]=atan2(yy,xx)
# towdyn.m:747
                        Ti[ip1]=sqrt(xx ** 2 + yy ** 2 + zz ** 2)
# towdyn.m:748
                        if Ti(ip1) != 0:
                            psi[ip1]=atan2(sqrt(xx ** 2 + yy ** 2),zz)
# towdyn.m:750
                        else:
                            psi[ip1]=psi(i)
# towdyn.m:752
                    psi[arange(ist,N)]=pi - psi(arange(ist,N))
# towdyn.m:755
                    X[N]=0
# towdyn.m:756
                    Y[N]=0
# towdyn.m:756
                    Z[N]=0
# towdyn.m:756
                    dx0=0
# towdyn.m:756
                    dy0=0
# towdyn.m:756
                    dz0=0
# towdyn.m:756
                    for i in arange(N - 1,ist,- 1).reshape(-1):
                        if Hi(2,i) != 0:
                            dL=1 + (dot(Ti(i),4) / (dot(dot(pi,Hi(2,i) ** 2),MEi(i))))
# towdyn.m:759
                        else:
                            dL=1
# towdyn.m:761
                        LpdL=dot(Hi(1,i),dL)
# towdyn.m:763
                        X[i]=X(i + 1) + dot(dot(LpdL,cos(theta(i))),sin(psi(i))) / 2 + dx0
# towdyn.m:764
                        Y[i]=Y(i + 1) + dot(dot(LpdL,sin(theta(i))),sin(psi(i))) / 2 + dy0
# towdyn.m:765
                        Z[i]=Z(i + 1) - dot(LpdL,cos(psi(i))) / 2 - dz0
# towdyn.m:766
                        dx0=dot(dot(LpdL,cos(theta(i))),sin(psi(i))) / 2
# towdyn.m:767
                        dy0=dot(dot(LpdL,sin(theta(i))),sin(psi(i))) / 2
# towdyn.m:768
                        dz0=dot(LpdL,cos(psi(i))) / 2
# towdyn.m:769
                    if icl2 > 50:
                        disp(concat([Zist,Z(ist),Ti(ist),dot(psi(ist),180) / pi,tenfac]))
                    if abs(Z(ist) - Zist) < (dot(2,Hi(1,ist))):
                        break2=0
# towdyn.m:773
                    else:
                        if Z(ist) < Zist:
                            if iincr == 1:
                                decr=decr ** 0.5
# towdyn.m:776
                            tenfac=dot(tenfac,decr)
# towdyn.m:777
                            iincr=- 1
# towdyn.m:778
                        else:
                            if iincr == - 1:
                                incr=incr ** 0.5
# towdyn.m:780
                            tenfac=dot(tenfac,incr)
# towdyn.m:781
                            iincr=1
# towdyn.m:782

                X[N]=0
# towdyn.m:786
                Y[N]=0
# towdyn.m:786
                Z[N]=0
# towdyn.m:786
                dx0=0
# towdyn.m:786
                dy0=0
# towdyn.m:786
                dz0=0
# towdyn.m:786
                for i in arange(N - 1,1,- 1).reshape(-1):
                    if Hi(2,i) != 0:
                        dL=1 + (dot(Ti(i),4) / (dot(dot(pi,Hi(2,i) ** 2),MEi(i))))
# towdyn.m:789
                    else:
                        dL=1
# towdyn.m:791
                    LpdL=dot(Hi(1,i),dL)
# towdyn.m:793
                    X[i]=X(i + 1) + dot(dot(LpdL,cos(theta(i))),sin(psi(i))) / 2 + dx0
# towdyn.m:794
                    Y[i]=Y(i + 1) + dot(dot(LpdL,sin(theta(i))),sin(psi(i))) / 2 + dy0
# towdyn.m:795
                    Z[i]=Z(i + 1) - dot(LpdL,cos(psi(i))) / 2 - dz0
# towdyn.m:796
                    dx0=dot(dot(LpdL,cos(theta(i))),sin(psi(i))) / 2
# towdyn.m:797
                    dy0=dot(dot(LpdL,sin(theta(i))),sin(psi(i))) / 2
# towdyn.m:798
                    dz0=dot(LpdL,cos(psi(i))) / 2
# towdyn.m:799
    
    
    
    if logical_not(isempty(ZCO)):
        mmco=length(ZCO)
# towdyn.m:807
        for jco in arange(1,mmco).reshape(-1):
            el=Jobj(jco)
# towdyn.m:809
            Z0co[jco]=Z(Iobj(jco)) - dot(Piobj(jco),(Z(Iobj(jco) - 1) - Z(Iobj(jco))))
# towdyn.m:810
    
    # if there are clamp-on device, figure out there position.
    if logical_not(isempty(ZCO)):
        mmco=length(ZCO)
# towdyn.m:815
        for jco in arange(1,mmco).reshape(-1):
            el=Iobj(jco)
# towdyn.m:817
            Zfco[jco]=Z(el) - dot(Piobj(jco),(Z(el - 1) - Z(el)))
# towdyn.m:818
            Xfco[jco]=X(el) - dot(Piobj(jco),(X(el - 1) - X(el)))
# towdyn.m:819
            Yfco[jco]=Y(el) - dot(Piobj(jco),(Y(el - 1) - Y(el)))
# towdyn.m:820
            psifco[jco]=psi(el) - dot(Piobj(jco),(psi(el - 1) - psi(el)))
# towdyn.m:821
            disp(concat([Z(el),Zfco(jco),X(el),Xfco(jco)]))
    
    
    I=(arange(2,N - 1))
# towdyn.m:826
    iobj=find(Hi(4,arange()) != 1)
# towdyn.m:827
    
    jobj=1 + find(Hi(4,I) == logical_and(1,(Hi(4,I - 1) != logical_or(1,Hi(4,I + 1)) != 1)))
# towdyn.m:828
    
    ba=psi(N - 1)
# towdyn.m:829
    
    ha=theta(N - 1)
# towdyn.m:830
    wpm=(dot(1024,(dot(pi,(Hi(2,N - 1) / 2) ** 2)))) - (Bi(N - 1) / 9.81)
# towdyn.m:831
    
    Wa=Ti(N) / 9.81
# towdyn.m:832
    VWa=dot(Wa,cos(ba))
# towdyn.m:833
    HWa=dot(Wa,sin(ba))
# towdyn.m:834
    disp('  ')
    
    disp(concat([' Total Tension at Surface [kg] = ',num2str(Wa,'%8.1f')]))
    disp(concat([' Vertical load [kg] = ',num2str(VWa,'%8.1f'),'  Horizontal load [kg] = ',num2str(HWa,'%8.1f')]))
    disp(concat([' Depth of End Device [m] = ',num2str(Z(1),'%8.1f')]))
    # reset original current profile.
    z=copy(ztmp)
# towdyn.m:841
    U=copy(Utmp)
# towdyn.m:841
    V=copy(Vtmp)
# towdyn.m:841
    W=copy(Wtmp)
# towdyn.m:841
    rho=copy(rhotmp)
# towdyn.m:841
    if iprt == 1:
        close_(9)
    
    # fini