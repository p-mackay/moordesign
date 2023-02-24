# Generated with SMOP  0.41-beta
from libsmop import *

    
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
    
    X=[]
    Y=[]
    Z=[]
    Ti=[]
    iobj=[]
    jobj=[]
    psi=[]
    if isempty(iss):
        Hs=copy(H)
        Bs=copy(B)
        Cds=copy(Cd)
        MEs=copy(ME)
    
    if logical_not(isempty(find(B == 0))):
        B[find(B == 0)]=- 0.0001
    
    mu,nu=size(U,nargout=2)
    if logical_or((mu == logical_and(0,nu) == 0),max(z)) == 0:
        U=concat([0.1,0.1,0])
        U=ravel(U)
        V=copy(U)
        W=copy(U)
        z=fix(dot(sum(H(1,arange())),concat([1.5,0.1,0]).T))
        z=ravel(z)
        rho=concat([1024,1025,1026]).T
        rho=ravel(rho)
    
    z[find(z(arange(1,end() - 1)) == 0)]=0.1
    
    Zoo=[]
    Z0co=[]
    Utmpo=copy(U)
    Vtmpo=copy(V)
    Wtmpo=copy(W)
    U=dot(ones(size(z)),0)
    V=copy(U)
    W=copy(U)
    
    for izloop in arange(1,2).reshape(-1):
        # the first loop to estimate the initial component heights with no currents
        if izloop == 2:
            U=copy(Utmpo)
            V=copy(Vtmpo)
            W=copy(Wtmpo)
        # Add 2# of wind speed to top current (10m) value
        ztmp=copy(z)
        Utmp=copy(U)
        Vtmp=copy(V)
        Wtmp=copy(W)
        rhotmp=copy(rho)
        if mu != logical_and(1,nu) != 1:
            if mu == length(z):
                U=U(arange(),1)
                V=V(arange(),1)
                W=W(arange(),1)
            else:
                U=U(1,arange()).T
                V=V(1,arange()).T
                W=W(1,arange()).T
        # Add 2# of wind speed to top current value(s)
        if uw != logical_or(0,vw) != 0:
            windepth=sqrt(uw ** 2 + vw ** 2) / 0.02
            if (uw ** 2 + vw ** 2) > 0:
                if windepth > z(1):
                    windepth == dot(0.8,z(1))
                if z(2) < (z(1) - windepth):
                    mu=length(z)
                    z[arange(3,mu + 1)]=z(arange(2,mu))
                    z[2]=z(1) - windepth
                    U[arange(3,mu + 1)]=U(arange(2,mu))
                    U[2]=interp1(concat([z(1),z(3)]),concat([U(1),U(3)]),z(2),'linear')
                    U[1]=U(1) + uw
                    V[arange(3,mu + 1)]=V(arange(2,mu))
                    V[2]=interp1(concat([z(1),z(3)]),concat([V(1),V(3)]),z(2),'linear')
                    V[1]=V(1) + vw
                    W[arange(3,mu + 1)]=W(arange(2,mu))
                    W[2]=interp1(concat([z(1),z(3)]),concat([W(1),W(3)]),z(2),'linear')
                    rho[arange(3,mu + 1)]=rho(arange(2,mu))
                    rho[2]=rho(1)
                else:
                    uwindx=find(z > (z(1) - windepth))
                    uw1=interp1(concat([z(1),z(1) - windepth]),concat([uw,0]),z(uwindx),'linear')
                    vw1=interp1(concat([z(1),z(1) - windepth]),concat([vw,0]),z(uwindx),'linear')
                    izero=find(abs(uw1) < 0.01)
                    uw1[izero]=0
                    izero=find(abs(uw1) < 0.01)
                    uw1[izero]=0
                    qq=0
                    for wi in uwindx.reshape(-1):
                        qq=qq + 1
                        U[wi]=U(wi) + uw1(qq)
                        V[wi]=V(wi) + vw1(qq)
        # first change masses/buoyancies into forces (Newtons)
        Bw=dot(B,9.81)
        BwCO=dot(BCO,9.81)
        Bmax=Bw(1)
        N=length(B)
        # First determine if this is a sub-surface or surface float mooring.
    # This is determined by the maximum height of the velocity profile as the water depth
        Zw=max(z)
        S=sum(H(1,arange()))
        if isempty(nomovie):
            disp('  ')
        gamma=1
        if Zw > S:
            ss=1
            if logical_and(isempty(nomovie),izloop) == 2:
                disp('This is (starting off as) a sub-surface mooring')
        else:
            ss=0
            if logical_and(isempty(nomovie),izloop) == 2:
                disp('This is (starting off as) a potential surface float mooring')
        if izloop == 1:
            disp('First, find neutral (no current) mooring component positions.')
        else:
            disp('Searching for a converged solution.')
        Zi=[]
        Hi=[]
        Bi=[]
        Cdi=[]
        MEi=[]
        iobj=[]
        j=1
        Zi[1]=H(1,N)
        Hi[arange(),1]=H(arange(),N)
        Bi[arange(),1]=Bw(arange(),N)
        Cdi[1]=Cd(N)
        MEi[1]=ME(N)
        z0=H(1,N)
        for i in arange(N - 1,1,- 1).reshape(-1):
            j=j + 1
            if H(4,i) == 1:
                Hw=fix(H(1,i))
                dz=0.2
                if Hw > logical_and(5,Hw) <= 50:
                    dz=0.5
                else:
                    if Hw > logical_and(50,Hw) <= 100:
                        dz=1
                    else:
                        if Hw > logical_and(100,Hw) <= 500:
                            dz=2
                        else:
                            if Hw > 500:
                                dz=5
                n=round(H(1,i) / dz)
                dz=H(1,i) / n
                Elindx[i,1]=j
                for jj in arange(j,j + n - 1).reshape(-1):
                    Zi[jj]=z0 + dz / 2
                    z0=z0 + dz
                    Hi[arange(),jj]=concat([dz,H(2,i),H(3,i),H(4,i)]).T
                    Bi[jj]=dot(Bw(i),dz)
                    Cdi[jj]=Cd(i)
                    MEi[jj]=ME(i)
                j=j + n - 1
                Elindx[i,2]=j
            else:
                Elindx[i,arange(1,2)]=concat([j,j])
                Zi[j]=z0 + H(1,i) / 2
                z0=z0 + H(1,i)
                Hi[arange(),j]=H(arange(),i)
                Bi[j]=Bw(i)
                Cdi[j]=Cd(i)
                MEi[j]=ME(i)
        J=copy(j)
        if logical_not(isempty(ZCO)):
            Iobj=[]
            PIobj=[]
            mmco=length(ZCO)
            ZiCO[arange(1,mmco)]=ZCO(arange(mmco,1,- 1))
            HiCO[arange(),arange(1,mmco)]=HCO(arange(),arange(mmco,1,- 1))
            CdiCO[arange(1,mmco)]=CdCO(arange(mmco,1,- 1))
            Piobj[arange(1,mmco)]=Pobj(arange(mmco,1,- 1))
            Jiobj[arange(1,mmco)]=Jobj(arange(mmco,1,- 1))
            for jco in arange(1,mmco).reshape(-1):
                Iobj[jco]=fix(dot((abs(Elindx(Jiobj(jco),2) - Elindx(Jiobj(jco),1)) + 1),Piobj(jco))) + Elindx(Jiobj(jco),1)
                PIobj[jco]=(ZiCO(jco) - Zi(Iobj(jco)) + Hi(1,Iobj(jco)) / 2) / Hi(1,Iobj(jco))
            # precently, Iobj and PIobj are indexed from bottom to top, flip later
        Elindx=J + 1 - Elindx
        # now interpolate the velocity profile to 1 m estimates
        dz=1
        dz0=mean(abs(diff(z)))
        maxz=sum(H(1,arange()))
        if dz0 < 1:
            Ui=copy(U)
            Vi=copy(V)
            Wi=copy(W)
            rhoi=copy(rho)
            zi=copy(z)
        else:
            if z(1) > z(2):
                dz=- 1
            if abs(z(end()) - z(1)) < 10:
                dz=dot(sign(dz),0.1)
            zi=concat([arange(z(1),z(end()),dz)])
            if logical_not(isempty(U)):
                Ui=interp1(z,U,zi)
            else:
                zi=concat([arange(maxz,0,- 1)])
                Ui=interp1(concat([maxz + 1,20,0]),concat([0,0,0]),zi,'linear')
            if logical_not(isempty(V)):
                Vi=interp1(z,V,zi,'linear')
            else:
                Vi=zeros(size(Ui))
            if logical_not(isempty(W)):
                Wi=interp1(z,W,zi,'linear')
            else:
                Wi=zeros(size(Ui))
            if logical_not(isempty(rho)):
                rhoi=interp1(z,rho,zi,'linear')
            else:
                rhoi=dot(ones(size(Ui)),1025)
        Umag=sqrt(Ui ** 2 + Vi ** 2 + Wi ** 2)
        N=length(Bi)
        # Now find the drag on each element assuming first a vertical mooring.
        if ss == 0:
            Bo=- sum(Bi(arange(2,N - 1))) + sum(BwCO)
            Zi=dot(Zi,Zw) / S
            Boo=copy(Bo)
            gamma=Bo / Bmax
            if gamma > 1:
                gamma=0.9
        for j in arange(1,N).reshape(-1):
            ico=[]
            if logical_not(isempty(Iobj)):
                ico=find(Iobj == j)
            i=find(zi >= logical_and((Zi(j) - 0.5),zi) <= (Zi(j) + 0.5))
            i=i(1)
            if Hi(3,j) == 0:
                A=dot(Hi(1,j),Hi(2,j))
            else:
                A=dot(pi,(Hi(3,j) / 2) ** 2)
            Qx[j]=dot(dot(dot(dot(dot(0.5,rhoi(i)),Cdi(j)),A),Umag(i)),Ui(i))
            Qy[j]=dot(dot(dot(dot(dot(0.5,rhoi(i)),Cdi(j)),A),Umag(i)),Vi(i))
            # if there are clamp-o devices here
            Qxco=0
            Qyco=0
            if logical_not(isempty(ico)):
                for icoc in ico.reshape(-1):
                    if HiCO(3,icoc) == 0:
                        Axco=dot(HiCO(1,icoc),HiCO(2,icoc))
                        Ayco=dot(HiCO(1,icoc),HiCO(2,icoc))
                        Cdjxco=CdiCO(icoc)
                        Cdjyco=CdiCO(icoc)
                    else:
                        Axco=dot(pi,(HiCO(3,icoc) / 2) ** 2)
                        Ayco=copy(Axco)
                        Cdjxco=CdiCO(icoc)
                        Cdjyco=copy(Cdjxco)
                    Qxco=Qxco + dot(dot(dot(dot(dot(0.5,rhoi(i)),Cdjxco),Axco),Umag(i)),Ui(i))
                    Qyco=Qyco + dot(dot(dot(dot(dot(0.5,rhoi(i)),Cdjyco),Ayco),Umag(i)),Vi(i))
            Qx[j]=Qx(j) + Qxco
            Qy[j]=Qy(j) + Qyco
            if Hi(3,j) == 0:
                A=dot(pi,(Hi(2,j) / 2) ** 2)
                if Hi(4,j) == 1:
                    A=0
            Qz[j]=dot(dot(dot(dot(dot(0.5,rhoi(i)),Cdi(j)),A),Umag(i)),Wi(i))
            Qzco=0
            if logical_not(isempty(ico)):
                for icoc in ico.reshape(-1):
                    if HiCO(3,icoc) == 0:
                        Azco=dot(pi,(HiCO(2,icoc) / 2) ** 2)
                        Cdjzco=CdiCO(icoc)
                    else:
                        Azco=dot(pi,(HiCO(3,icoc) / 2) ** 2)
                        Cdjzco=CdiCO(icoc)
                    Qzco=Qzco + dot(dot(dot(dot(dot(0.5,rhoi(i)),Cdjzco),Azco),Umag(i)),Wi(i))
            Qz[j]=Qz(j) + Qzco
        # Flip mooring right side up, indecies now start at top.
        Qx=fliplr(Qx)
        Qy=fliplr(Qy)
        Qz=fliplr(Qz)
        Hi=fliplr(Hi)
        Bi=fliplr(Bi)
        Cdi=fliplr(Cdi)
        MEi=fliplr(MEi)
        Iobj=J + 1 - Iobj(arange(end(),1,- 1))
        PIobj=1 - PIobj(arange(end(),1,- 1))
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
        theta=[]
        psi=[]
        Ti[1]=0
        theta[1]=0
        psi[1]=0
        b=dot(gamma,(Bi(1) + Qz(1)))
        theta[2]=atan2(Qy(1),Qx(1))
        Ti[2]=sqrt(Qx(1) ** 2 + Qy(1) ** 2 + b ** 2)
        psi[2]=real(acos(b / Ti(2)))
        for i in arange(2,N - 1).reshape(-1):
            ico=[]
            if logical_not(isempty(Iobj)):
                ico=find(Iobj == i)
            ip1=i + 1
            xx=Qx(i) + dot(dot(Ti(i),cos(theta(i))),sin(psi(i)))
            yy=Qy(i) + dot(dot(Ti(i),sin(theta(i))),sin(psi(i)))
            zz=Bi(i) + Qz(i) + dot(Ti(i),cos(psi(i)))
            if logical_not(isempty(ico)):
                zz=zz + sum(BwCO(ico))
            theta[ip1]=atan2(yy,xx)
            Ti[ip1]=sqrt(xx ** 2 + yy ** 2 + zz ** 2)
            if Ti(ip1) != 0:
                psi[ip1]=real(acos(zz / Ti(ip1)))
            else:
                psi[ip1]=psi(i)
        # Now integrate from the bottom to the top to get the first order [x,y,z]
    # Allow wire/rope sections to stretch under tension
        for ii in arange(1,2).reshape(-1):
            X[N]=0
            Y[N]=0
            Z[N]=Hi(1,N)
            dx0=0
            dy0=0
            dz0=0
            for i in arange(N - 1,1,- 1).reshape(-1):
                if Hi(2,i) != 0:
                    dL=1 + (dot(Ti(i),4) / (dot(dot(pi,Hi(2,i) ** 2),MEi(i))))
                else:
                    dL=1
                LpdL=dot(Hi(1,i),dL)
                X[i]=X(i + 1) + dot(dot(LpdL,cos(theta(i))),sin(psi(i))) / 2 + dx0
                Y[i]=Y(i + 1) + dot(dot(LpdL,sin(theta(i))),sin(psi(i))) / 2 + dy0
                Z[i]=Z(i + 1) + dot(LpdL,cos(psi(i))) / 2 + dz0
                dx0=dot(dot(LpdL,cos(theta(i))),sin(psi(i))) / 2
                dy0=dot(dot(LpdL,sin(theta(i))),sin(psi(i))) / 2
                dz0=dot(LpdL,cos(psi(i))) / 2
                if Z(i) > logical_and(Zw,Hi(4,i)) == logical_and(1,Bi(i)) > 0:
                    Z[i]=Zw
                    psi[i]=pi / 2
                if Z(i) <= Z(N):
                    Z[i]=Z(N)
                    psi[i]=pi / 2
        if max(Z) > logical_and(Zw,ss) == 1:
            ss=0
            gamma=sqrt(gamma)
        # Now with the first order positions, we must re-estimate the new
    # drags at the new heights (Zi) and for cylinders tilted by psi in flow.
    # If this is a surface float mooring, then increase the amount of the
    # surface float that is submerged until the height to the bottom of the float is
    # within the range Zw > Zf > (Zw - H(1,1))
        rand('state',sum(dot(100,clock)))
        breaknow=0
        iconv=0
        icnt=0
        iavg=0
        isave=0
        dg=0.1
        gf=2
        dgf=0
        dgc=0
        if izloop == 1:
            deltaz=0.1
        else:
            deltaz=0.01
        gamma0=dot(Ti(2),cos(psi(2))) / Bi(1)
        gammas=- 1
        if gamma < gamma0:
            gammas=1
        ######################################
    #                                    #
    # Main iteration/convergence loop    #
    #                                    #
    ######################################
        ilines=1
        ico=[]
        iiprt=0
        dgci=10
        while breaknow == 0:

            isave=isave + 1
            Zf=Z(1) - Hi(1,1) / 2
            if ss == 0:
                if isave > iprt:
                    if isave == (iprt + 1):
                        disp('  ')
                        disp(' Take a closer look at the convergence...')
                        disp('Depth       Top      Bottom      % of float used  delta-converge')
                        disp(num2str(concat([Zw(Zf + Hi(1,1)),Zf,dot(gamma,100),dot(gammas,dg)])))
                    iiprt=iiprt + 1
                    if mod(iiprt,10) == 0:
                        disp(num2str(concat([Zw(Zf + Hi(1,1)),Zf,dot(gamma,100),dot(gammas,dg)])))
                izm=find(Z < 0)
                Z[izm]=0
                gamma0=dot(Ti(2),cos(psi(2))) / Bi(1)
                if dot((1 + gf),dg) >= logical_and(gamma,gammas) == - 1:
                    dg=dg / 10
                if gamma + (dot(dot((1 + gf),gammas),dg)) >= logical_and(1,gammas) == - 1:
                    dg=dg / 10
                if (Zf + Hi(1,1)) <= Zw:
                    dgc=dgc + 1
                    dgf=0
                    if gammas == - 1:
                        gammas=1
                        dg=dg / 10
                        if dg < 1e-10:
                            dg=1e-05
                        dgc=0
                    gamma=gamma + dot(dot(gammas,dg),(dot(gf,rand)))
                    if dgc > dgci:
                        dg=dot(dg,10)
                        dgc=0
                    #if (gamma+dg>1, gamma=1; ss=1; end # this is now a subsurface mooring.
                else:
                    if Zw > logical_and(Zf,Zw) < (Zf + Hi(1,1)):
                        dgc=dgc + 1
                        dgf=0
                        if ((Zw - Zf) / Hi(1,1)) < gamma:
                            if gammas == 1:
                                gammas=- 1
                                dg=dg / 10
                                dgc=0
                            gamma=gamma + dot(dot(gammas,dg),(dot(gf,rand)))
                            if dgc > dgci:
                                dg=dot(dg,10)
                                dgc=0
                        else:
                            if gammas == - 1:
                                gammas=1
                                dg=dg / 10
                                dgc=0
                            gamma=gamma + dot(dot(gammas,dg),(dot(gf,rand)))
                            if dgc > dgci:
                                dg=dot(dg,10)
                                dgc=0
                        izz=find(Hi(4,arange()) == 0)
                        if gamma < logical_and(1e-10,dg) < logical_and(1e-09,max(Z(izz))) > logical_and((Zf + Hi(1,1)),iavg) > 200:
                            NN=length(B)
                            inext=find(B > 1)
                            if length(inext) > 1:
                                H=H(arange(),arange(inext(2),NN))
                                B=B(arange(),arange(inext(2),NN))
                                Cd=Cd(arange(inext(2),NN))
                                ME=ME(arange(inext(2),NN))
                                moorele=moorele(arange(inext(2),NN),arange())
                                U=copy(Utmp)
                                V=copy(Vtmp)
                                W=copy(Wtmp)
                                z=copy(ztmp)
                                rho=copy(rhotmp)
                                disp('!! Top link(s) in mooring removed !!')
                                Z=[]
                                iss=1
                                dismoor
                                moordyn
                                return X,Y,Z,iobj
                            else:
                                error("'This mooring's not working! Please examine. Strong currents or shears? Try reducing them.'")
                    else:
                        if Zf >= Zw:
                            dgc=dgc + 1
                            dgf=dgf + 1
                            if gammas == 1:
                                gammas=- 1
                                if dg < 1e-10:
                                    dg=1e-05
                                dgc=0
                            if dgf > 5:
                                dg=0.001
                                dgf=0
                            gamma=gamma + dot(dot(gammas,dg),(dot(gf,rand)))
                            if dgc > dgci:
                                dg=dot(dg,10)
                                dgc=0
                            if gamma >= 1:
                                gamma=1
                                ss=1
                            if abs(gamma) < 1e-06:
                                NN=length(B)
                                inext=find(B > 1)
                                if length(inext) > 1:
                                    H=H(arange(),arange(inext(2),NN))
                                    B=B(arange(inext(2),NN))
                                    Cd=Cd(arange(inext(2),NN))
                                    ME=ME(arange(inext(2),NN))
                                    moorele=moorele(arange(inext(2),NN),arange())
                                    U=copy(Utmp)
                                    V=copy(Vtmp)
                                    W=copy(Wtmp)
                                    z=copy(ztmp)
                                    rho=copy(rhotmp)
                                    disp('!! Top link(s) in mooring removed !!')
                                    Z=[]
                                    iss=1
                                    dismoor
                                    moordyn
                                    return X,Y,Z,iobj
                                else:
                                    error("'This mooring's not working! Solution isn't converging. Please reduce shear and max speeds.'")
            if gamma < 0:
                gamma=abs(gamma)
            if gamma >= 1:
                gamma=1
                ss=1
            if isave >= 20:
                iavg=iavg + 1
                if iavg == 1:
                    Tiavg=copy(Ti)
                    psiavg=copy(psi)
                    Zavg=copy(Z)
                    Z1[1]=Z(1)
                    Xavg=copy(X)
                    Yavg=copy(Y)
                    gammavg=copy(gamma)
                    Uio=copy(Ui)
                else:
                    Tiavg=Tiavg + Ti
                    psiavg=psiavg + psi
                    Zavg=Zavg + Z
                    Z1[isave]=Z(1)
                    Xavg=Xavg + X
                    Yavg=Yavg + Y
                    gammavg=gammavg + gamma
                    Z1std=std(Z1)
            #if iavg > 20 & ss==0 & Z1std > 1, gamma=1; ss=1; end # This is bouncing around, its probably a subsurface solution.
            if iavg > 20:
                X=Xavg / iavg
                Y=Yavg / iavg
                Z=Zavg / iavg
                Ti=Tiavg / iavg
                psi=psiavg / iavg
            Zf=Z(1) - Hi(1,1) / 2
            if ss == logical_and(0,(Zf + dot(gamma,Hi(1,1)))) > Zw:
                Z=dot(Z,(Zw / (Zf + dot(gamma,Hi(1,1)))))
            icnt=icnt + 1
            if iiprt == 0:
                if mod(icnt,ilines) == 0:
                    fprintf(1,'.')
                if icnt >= dot(60,ilines):
                    icnt=0
                    ilines=ilines + 1
                    fprintf(1,'%8i',isave)
                    disp(' ')
            if iavg > logical_and(iprt,ss) == 1:
                disp(concat([Z(1),(Z(1) - Z1(isave - 1))]))
            phix=atan2((multiply(cos(theta),sin(psi))),cos(psi))
            phiy=atan2((multiply(sin(theta),sin(psi))),cos(psi))
            Umag=sqrt(Ui ** 2 + Vi ** 2 + Wi ** 2)
            Qx=dot(ones(1,N),0.0)
            Qy=copy(Qx)
            Qz=copy(Qx)
            for j in arange(1,N).reshape(-1):
                ico=[]
                if logical_not(isempty(Iobj)):
                    ico=find(Iobj == j)
                i=find(zi >= logical_and((Z(j) - 1.0),zi) <= (Z(j) + 1.0))
                if j == 1:
                    i=find(zi >= logical_and((Z(j) - Hi(1,1)),zi) <= (Z(j) + Hi(1,1)))
                    if isempty(i):
                        i=1
                if isempty(i):
                    disp(concat([' Check this configuration: ',num2str(concat([j,Z(1),Z(j)]))]))
                    error("' Can't find the velocity at this element! Near line 572 of moordyn.m'")
                i=i(1)
                theta2=atan2(Vi(i),Ui(i))
                UVLmag=dot(sqrt(Ui(i) ** 2 + Vi(i) ** 2),cos(theta(j) - theta2))
                UL=dot(UVLmag,cos(theta(j)))
                VL=dot(UVLmag,sin(theta(j)))
                Up=Ui(i) - UL
                Vp=Vi(i) - VL
                theta3=atan2(VL,UL)
                thetap=atan2(Vp,Up)
                # First calculate the direct form drag in X Y and Z, plus some frictional surface drag normal to the tilt/theta
                if Hi(3,j) == 0:
                    #
                    A=dot(Hi(1,j),Hi(2,j))
                    Cdjxy=Cdi(j)
                    # These are the base form drag terms aligned perpendicular to the theta plan.
                    Qh=dot(dot(dot(dot(0.5,rhoi(i)),Cdjxy),A),(Up ** 2 + Vp ** 2))
                    Qx[j]=dot(Qh,cos(thetap))
                    Qy[j]=dot(Qh,sin(thetap))
                else:
                    A=dot(pi,(Hi(3,j) / 2) ** 2)
                    Cdj=Cdi(j)
                    Qh=dot(dot(dot(dot(0.5,rhoi(i)),Cdi(j)),A),(Ui(i) ** 2 + Vi(i) ** 2))
                    Qx[j]=dot(Qh,cos(theta2))
                    Qy[j]=dot(Qh,sin(theta2))
                    Qz[j]=dot(dot(dot(dot(dot(0.5,rhoi(i)),Cdj),A),abs(Wi(i))),Wi(i))
                Qxco=0
                Qyco=0
                Qzco=0
                if logical_not(isempty(ico)):
                    for icoc in ico.reshape(-1):
                        Up=Ui(i) - UL
                        Vp=Vi(i) - VL
                        if HCO(3,icoc) == 0:
                            # re-done 03/09
                            A=dot(HCO(1,icoc),HCO(2,icoc))
                            Cdjco=CdCO(icoc) + dot(dot(dot(HCO(2,icoc),pi),0.01),(1 - ((pi / 2) - psi(j)) / (pi / 2)))
                            Qhco=dot(dot(dot(dot(0.5,rhoi(i)),Cdjco),A),(Up ** 2 + Vp ** 2))
                            Qxco=Qxco + dot(Qhco,cos(thetap))
                            Qyco=Qyco + dot(Qhco,sin(thetap))
                        else:
                            A=dot(pi,(HCO(3,icoc) / 2) ** 2)
                            Cdjco=CdCO(icoc)
                            Qh=dot(dot(dot(dot(0.5,rhoi(i)),Cdjco),A),(Ui(i) ** 2 + Vi(i) ** 2))
                            Qxco=Qxco + dot(Qh,cos(theta2))
                            Qyco=Qyco + dot(Qh,sin(theta2))
                            Qzco=Qzco + dot(dot(dot(dot(dot(0.5,rhoi(i)),Cdjco),A),abs(Wi(i))),Wi(i))
                # These are the base form drag terms aligned with u, v and w.
                Qx[j]=Qx(j) + Qxco
                Qy[j]=Qy(j) + Qyco
                Qz[j]=Qz(j) + Qzco
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
                if Hi(3,j) == 0:
                    A=dot(Hi(1,j),Hi(2,j))
                    CdUV=dot(Cdi(j),cos(psi(j)) ** 3) + dot(dot(dot(Hi(2,j),pi),0.01),(1 - ((pi / 2) - psi(j)) / (pi / 2)))
                    CdW=dot(Cdi(j),cos(psi2) ** 3) + dot(dot(dot(Hi(2,j),pi),0.01),(1 - ((pi / 2) - psi2) / (pi / 2)))
                    sl=dot(sign(sin(theta(j))),sign(sin(theta3)))
                    if sl == 0:
                        sl=1
                    CdLUV=dot(dot(- Cdi(j),cos(psi(j)) ** 2),sin(psi(j)))
                    CdLW=dot(dot(Cdi(j),cos(psi2) ** 2),sin(psi2))
                    QhUV=dot(dot(dot(dot(0.5,rhoi(i)),A),CdUV),UVLmag ** 2)
                    Qx[j]=Qx(j) + dot(QhUV,cos(theta3))
                    Qy[j]=Qy(j) + dot(QhUV,sin(theta3))
                    QhLW=dot(dot(dot(dot(dot(0.5,rhoi(i)),A),CdLW),abs(Wi(i))),Wi(i))
                    Qx[j]=Qx(j) + dot(QhLW,cos(theta(j)))
                    Qy[j]=Qy(j) + dot(QhLW,sin(theta(j)))
                    Qz[j]=Qz(j) + dot(dot(dot(dot(dot(0.5,rhoi(i)),A),CdLUV),UVLmag ** 2),sl)
                    Qz[j]=Qz(j) + dot(dot(dot(dot(dot(0.5,rhoi(i)),A),CdW),abs(Wi(i))),Wi(i))
                # Now add any lift terms associated with tiltes clamp-on devices
                Qxco=0
                Qyco=0
                Qzco=0
                if logical_not(isempty(ico)):
                    for icoc in ico.reshape(-1):
                        if HCO(3,icoc) == 0:
                            Aco=dot(HCO(1,icoc),HCO(2,icoc))
                            Aeco=dot(pi,(HCO(1,icoc) / 2) ** 2)
                            CdUV=dot(CdCO(icoc),cos(psi(j)) ** 3) + dot(dot(dot(HCO(2,icoc),pi),0.01),(1 - ((pi / 2) - psi(j)) / (pi / 2)))
                            CdW=dot(CdCO(icoc),cos(psi2) ** 3) + dot(dot(dot(HCO(2,icoc),pi),0.01),(1 - ((pi / 2) - psi2) / (pi / 2)))
                            sl=dot(sign(sin(theta(j))),sign(sin(theta3)))
                            if sl == 0:
                                sl=1
                            CdLUV=dot(dot(- CdCO(icoc),cos(psi(j)) ** 2),sin(psi(j)))
                            CdLW=dot(dot(CdCO(icoc),cos(psi2) ** 2),sin(psi2))
                            QhUV=dot(dot(dot(dot(0.5,rhoi(i)),CdUV),Aco),UVLmag ** 2)
                            Qxco=Qxco + dot(QhUV,cos(theta3))
                            Qyco=Qyco + dot(QhUV,sin(theta3))
                            Qzco=Qzco + dot(dot(dot(dot(dot(0.5,rhoi(i)),CdLUV),Aco),UVLmag ** 2),sl)
                            QhLW=dot(dot(dot(dot(dot(0.5,rhoi(i)),CdLW),Aco),abs(Wi(i))),Wi(i))
                            Qxco=Qxco + dot(QhLW,cos(theta(j)))
                            Qyco=Qyco + dot(QhLW,sin(theta(j)))
                            Qzco=Qzco + dot(dot(dot(dot(dot(0.5,rhoi(i)),CdW),Aco),abs(Wi(i))),Wi(i))
                            Qhe=dot(dot(dot(dot(dot(0.5,rhoi(i)),0.65),abs(sin(psi(j)))),Aeco),UVLmag ** 2)
                            Qxco=Qxco + dot(Qhe,cos(theta3))
                            Qyco=Qyco + dot(Qhe,sin(theta3))
                            Qzco=Qzco + dot(dot(dot(dot(dot(dot(0.5,rhoi(i)),0.65),abs(cos(psi(j)))),Aeco),abs(Wi(i))),Wi(i))
                    Qx[j]=Qx(j) + Qxco
                    Qy[j]=Qy(j) + Qyco
                    Qz[j]=Qz(j) + Qzco
            # Now re-solve for displacements with new positions/drags.
            Ti=[]
            thetaNew=[]
            psiNew=[]
            Ti[1]=0
            # Top element (float) is kept in place by tension from below (only)
            b=Bi(1) + Qz(1)
            thetaNew[2]=atan2(Qy(1),Qx(1))
            Ti[2]=sqrt(Qx(1) ** 2 + Qy(1) ** 2 + b ** 2)
            if gamma < 1:
                Ti[2]=sqrt((dot(gamma,Qx(1))) ** 2 + (dot(gamma,Qy(1))) ** 2 + (dot(gamma,b)) ** 2)
            psiNew[2]=real(acos(b / Ti(2)))
            psiNew[1]=psiNew(2) / 2
            thetaNew[1]=thetaNew(2)
            # Now Solve from top (just under float) to bottom (top of anchor).
            for Zii0 in arange(1,1).reshape(-1):
                for i in arange(2,N - 1).reshape(-1):
                    ico=[]
                    if logical_not(isempty(Iobj)):
                        ico=find(Iobj == i)
                    ip1=i + 1
                    xx=Qx(i) + dot(dot(Ti(i),cos(thetaNew(i))),sin(psiNew(i)))
                    yy=Qy(i) + dot(dot(Ti(i),sin(thetaNew(i))),sin(psiNew(i)))
                    zz=Bi(i) + Qz(i) + dot(Ti(i),cos(psiNew(i)))
                    if logical_not(isempty(ico)):
                        zz=zz + sum(BwCO(ico))
                    thetaNew[ip1]=atan2(yy,xx)
                    Ti[ip1]=sqrt(xx ** 2 + yy ** 2 + zz ** 2)
                    if Ti(ip1) != 0:
                        psiNew[ip1]=real(acos(zz / Ti(ip1)))
                    else:
                        psiNew[ip1]=psiNew(i)
                thetaNew=real(thetaNew)
                psiNew=real(psiNew)
                # Now integrate/sum positions from the bottom to the top to get the second order [x,y,z]
            # Allow wire/rope to stretch under tension
                X=[]
                Y=[]
                Z=[]
                X[N]=0
                Y[N]=0
                Z[N]=Hi(1,N)
                Zii=1
                iint=0
                while Zii:

                    Zii=0
                    S=0
                    SS=0
                    dx0=0
                    dy0=0
                    dz0=0
                    iint=iint + 1
                    for i in arange(N - 1,1,- 1).reshape(-1):
                        if Hi(2,i) != logical_and(0,MEi(i)) < Inf:
                            dL=1 + (dot(Ti(i),4) / (dot(dot(pi,Hi(2,i) ** 2),MEi(i))))
                        else:
                            dL=1
                        LpdL=dot(Hi(1,i),dL)
                        S=S + LpdL
                        dX=dot(dot(LpdL,cos(thetaNew(i))),sin(psiNew(i)))
                        dY=dot(dot(LpdL,sin(thetaNew(i))),sin(psiNew(i)))
                        dZ=dot(LpdL,cos(psiNew(i)))
                        SS=SS + sqrt(dX ** 2 + dY ** 2 + dZ ** 2)
                        X[i]=X(i + 1) + dX / 2 + dx0 / 2
                        Y[i]=Y(i + 1) + dY / 2 + dy0 / 2
                        Z[i]=Z(i + 1) + dZ / 2 + dz0 / 2
                        if Z(i) > logical_and(Zw,Hi(4,i)) == logical_and(1,Bi(i)) >= 0:
                            Zii=1
                            Z[i]=Zw
                            psi[i]=pi / 2
                        if Z(i) < 0:
                            Zii=1
                            Z[i]=0
                            psi[i]=pi / 2
                        dx0=copy(dX)
                        dy0=copy(dY)
                        dz0=copy(dZ)
                    if iint > 4:
                        Zii=0
                    # The last position is to the center of the float (thus don't add dx0, dy0 and dz0)

                psi[N]=psi(N - 1)
            Z=real(Z)
            X=real(X)
            Y=real(Y)
            theta=real(theta)
            psi=real(psi)
            scale=0.5
            psi=psi + dot((psiNew - psi),scale)
            theta=theta + dot((thetaNew - theta),scale)
            # Recompute the positions
            S=0
            SS=0
            dx0=0
            dy0=0
            dz0=0
            for i in arange(N - 1,1,- 1).reshape(-1):
                if Hi(2,i) != logical_and(0,MEi(i)) < Inf:
                    dL=1 + (dot(Ti(i),4) / (dot(dot(pi,Hi(2,i) ** 2),MEi(i))))
                else:
                    dL=1
                LpdL=dot(Hi(1,i),dL)
                S=S + LpdL
                dX=dot(dot(LpdL,cos(theta(i))),sin(psi(i)))
                dY=dot(dot(LpdL,sin(theta(i))),sin(psi(i)))
                dZ=dot(LpdL,cos(psi(i)))
                SS=SS + sqrt(dX ** 2 + dY ** 2 + dZ ** 2)
                X[i]=X(i + 1) + dX / 2 + dx0 / 2
                Y[i]=Y(i + 1) + dY / 2 + dy0 / 2
                Z[i]=Z(i + 1) + dZ / 2 + dz0 / 2
                if Z(i) > logical_and(Zw,Hi(4,i)) == logical_and(1,Bi(i)) >= 0:
                    Z[i]=Zw
                    psi[i]=pi / 2
                if Z(i) < 0:
                    Z[i]=0
                    psi[i]=pi / 2
                dx0=copy(dX)
                dy0=copy(dY)
                dz0=copy(dZ)
            Z=real(Z)
            X=real(X)
            Y=real(Y)
            psi=real(psi)
            Zf=Z(1) - Hi(1,1) / 2
            if max(Z) > logical_and(Zw,ss) == 1:
                ss=0
                gamma=sqrt(gamma)
            if isave > 2:
                if abs(Zsave(isave - 1) - Z(1)) < logical_and(deltaz,abs(Zsave(isave - 2) - Zsave(isave - 1))) < deltaz:
                    if ss == logical_and(1,Zw) > logical_and((Zf + Hi(1,1)),gamma) == 1:
                        breaknow=1
                    else:
                        if ss == logical_and(0,Zw) > logical_and(Zf,Zw) < logical_and((Zf + Hi(1,1)),abs(((Zw - Zf) / Hi(1,1)) - gamma)) < 0.01:
                            breaknow=1
                if iavg == logical_or(120,(iavg > logical_and(100,dg) < 1e-10)):
                    X=Xavg / iavg
                    Y=Yavg / iavg
                    Z=Zavg / iavg
                    Ti=Tiavg / iavg
                    psi=psiavg / iavg
                    breaknow=1
                    iconv=1
            Zsave[isave]=Z(1)
            if logical_not(rem(isave,100)):
                deltaz=dot(2,deltaz)

        if izloop == 1:
            Zoo=copy(Z)
            if logical_not(isempty(ZCO)):
                mmco=length(ZCO)
                for jco in arange(1,mmco).reshape(-1):
                    Z0co[jco]=Z(Iobj(jco)) + (dot(dot(cos(psi(Iobj(jco))),(0.5 - PIobj(jco))),Hi(1,Iobj(jco))))
    
    # if there are clamp-on device, figure out there final position.
    if logical_not(isempty(ZCO)):
        for jco in arange(1,length(ZCO)).reshape(-1):
            Xfco[jco]=X(Iobj(jco)) + dot(dot(dot(cos(theta(Iobj(jco))),sin(psi(Iobj(jco)))),(0.5 - PIobj(jco))),Hi(1,Iobj(jco)))
            Yfco[jco]=Y(Iobj(jco)) + dot(dot(dot(sin(theta(Iobj(jco))),sin(psi(Iobj(jco)))),(0.5 - PIobj(jco))),Hi(1,Iobj(jco)))
            Zfco[jco]=Z(Iobj(jco)) + dot(dot(cos(psi(Iobj(jco))),(0.5 - PIobj(jco))),Hi(1,Iobj(jco)))
            psifco[jco]=psi(Iobj(jco))
    
    
    if logical_and(iconv,ss) == 0:
        zcorr=(Zw - dot(Hi(1,1),gamma) + (Hi(1,1) / 2)) - Z(1)
        if abs(zcorr) > 0.01:
            Z10=Z(1)
            for ico in arange(1,length(Z)).reshape(-1):
                Z[ico]=Z(ico) + dot(abs(Z(ico) / Z10),zcorr)
            for jco in arange(1,length(ZCO)).reshape(-1):
                Zfco[jco]=Zfco(jco) + dot(abs(Z(Iobj(jco)) / Z10),zcorr)
    
    I=(arange(2,N - 1))
    
    iobj0=find(H(4,arange()) != 1)
    
    nnum1=num2str(concat([arange(1,length(iobj0))]).T,'%4.0f')
    nnum1[arange(),end() + 1]=' '
    nnum2=num2str(iobj0.T,'%4.0f')
    nnum2[arange(),end() + 1]=' '
    iEle=concat([nnum1,nnum2,moorele(iobj0,arange())])
    if logical_not(isempty(ZCO)):
        Iobj0=find(HCO(4,arange()) != 1)
        nnum1=num2str(concat([arange(1,length(Iobj0))]).T,'%4.0f')
        nnum1[arange(),end() + 1]=' '
        nnum2=num2str(Iobj0.T,'%4.0f')
        nnum2[arange(),end() + 1]=' '
        IEle=concat([nnum1,nnum2,mooreleCO(Iobj0,arange())])
    
    
    iobj=find(Hi(4,arange()) != 1)
    
    jobj=1 + find(Hi(4,I) == logical_and(1,(Hi(4,I - 1) != logical_or(1,Hi(4,I + 1)) != 1)))
    
    ba=psi(N - 1)
    Wa=Ti(N) / 9.81
    VWa=dot(Wa,cos(ba))
    HWa=dot(Wa,sin(ba))
    WoB=(Bi(N) + Qz(N) + Ti(N)) / 9.81
    
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
    U=copy(Utmp)
    V=copy(Vtmp)
    W=copy(Wtmp)
    rho=copy(rhotmp)
    # fini
