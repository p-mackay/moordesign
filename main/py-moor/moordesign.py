# Generated with SMOP  0.41-beta
from libsmop import *
# moordesign.m

    
@function
def moordesign(command=None,*args,**kwargs):
    varargin = moordesign.varargin
    nargin = moordesign.nargin

    # GUI Program to HELP design and evaluate an oceanographic mooring.
# Use: moordesign
    
    # This program will ASSIST in the design and evaluation of oceanographic moorings
# in order to determine 1) wire tensions and anchor requirements, and
# 2) the anticipated depth and horizontal excursions of mooring elements
# forced by currents U(z) [V(z) W(z)], where V and W are optional.
    
    # Time varying currents can be fed to moordyn.m (the engine) by user written MATLAB
# code in order to simulate and even make movies of element positions.
# A preliminary data base of mooring components has been included (c/o C.Darnall of APL UW).
# Advanced users can add and modify the text mooring database (mdcodes.mat), which
# includes the component names, their buoyancy/mass [in kg], their dimensions 
#  (Length/height, Cylinder Width, Sphere Diameter, all in [m]), and Drag
#   Coefficients (0.65-0.95 for spheres, 1.1-1.3 for cylinders).
# The mooring motion/dynamics engine solves the 3-D wire tension problem 
# from the top of the mooring to the bottom (anchor). 
# Simple current profiles can be entered manually, more detailed current 
# profiles should be saved in user mat files: U(z) z [V(z) W(z)].
# Menu lay-out may varying depending on screen resolution/monitor size.
# Additional program help and use is documented in moordyn.txt
    
    # No liability is assumed, and users of this code must take full responsability
# for actual mooring design and potential mooring damage and/or loss.
    
    # R.Dewey, U.of Victoria, 12/97
    
    # Please forward improvements/suggestions/bugs to rdewey@uvic.ca
# The latest version of Mooring Dynamics is available at: ftp://canuck.seos.uvic.ca/
# This code has been tested on Windows 95, NT (4.0), and HP-UNIX, but is not idiot proof.
    
    global U,V,W,z,rho,time,uw,vw
    global Xts,Yts,Zts,Tits,psits,iobjts,M,figs
    global H,B,Cd,ME,moorele
    global X,Y,Z,Ti,iobj,jobj,psi
    global Ht,Bt,Cdt,MEt,moorelet,Usp,Vsp,DD
    global fs
    
    if nargin == 0:
        H=[]
# moordesign.m:42
        B=[]
# moordesign.m:42
        Cd=[]
# moordesign.m:42
        ME=[]
# moordesign.m:42
        moorele=[]
# moordesign.m:42
        U=[]
# moordesign.m:43
        V=[]
# moordesign.m:43
        W=[]
# moordesign.m:43
        z=[]
# moordesign.m:43
        rho=[]
# moordesign.m:43
        time=[]
# moordesign.m:43
        uw=[]
# moordesign.m:43
        vw=[]
# moordesign.m:43
        M=[]
# moordesign.m:44
        Xts=[]
# moordesign.m:44
        Yts=[]
# moordesign.m:44
        Zts=[]
# moordesign.m:44
        Tits=[]
# moordesign.m:44
        psits=[]
# moordesign.m:44
        iobjts=[]
# moordesign.m:44
        figs=[]
# moordesign.m:44
        X=[]
# moordesign.m:45
        Y=[]
# moordesign.m:45
        Z=[]
# moordesign.m:45
        Zoo=[]
# moordesign.m:45
        Ti=[]
# moordesign.m:45
        psi=[]
# moordesign.m:45
        iobj=[]
# moordesign.m:45
        jobj=[]
# moordesign.m:45
        Ht=[]
# moordesign.m:46
        Bt=[]
# moordesign.m:46
        Cdt=[]
# moordesign.m:46
        MEt=[]
# moordesign.m:46
        moorelet=[]
# moordesign.m:46
        Usp=[]
# moordesign.m:46
        Vsp=[]
# moordesign.m:46
        DD=[]
# moordesign.m:46
        command=0
# moordesign.m:47
    
    if command == 2:
        H=[]
# moordesign.m:50
        B=[]
# moordesign.m:50
        Cd=[]
# moordesign.m:50
        ME=[]
# moordesign.m:50
        moorele=[]
# moordesign.m:50
        U=[]
# moordesign.m:51
        V=[]
# moordesign.m:51
        W=[]
# moordesign.m:51
        z=[]
# moordesign.m:51
        rho=[]
# moordesign.m:51
        time=[]
# moordesign.m:51
        uw=[]
# moordesign.m:51
        vw=[]
# moordesign.m:51
        M=[]
# moordesign.m:52
        Xts=[]
# moordesign.m:52
        Yts=[]
# moordesign.m:52
        Zts=[]
# moordesign.m:52
        Tits=[]
# moordesign.m:52
        psits=[]
# moordesign.m:52
        iobjts=[]
# moordesign.m:52
        figs=[]
# moordesign.m:52
        X=[]
# moordesign.m:53
        Y=[]
# moordesign.m:53
        Z=[]
# moordesign.m:53
        Zoo=[]
# moordesign.m:53
        Ti=[]
# moordesign.m:53
        psi=[]
# moordesign.m:53
        iobj=[]
# moordesign.m:53
        jobj=[]
# moordesign.m:53
        Ht=[]
# moordesign.m:54
        Bt=[]
# moordesign.m:54
        Cdt=[]
# moordesign.m:54
        MEt=[]
# moordesign.m:54
        moorelet=[]
# moordesign.m:54
        Usp=[]
# moordesign.m:54
        Vsp=[]
# moordesign.m:54
        DD=[]
# moordesign.m:54
    
    
    fs=10
# moordesign.m:57
    
    ss=get(0,'ScreenSize')
# moordesign.m:58
    if ss(3) < 1024:
        fs=10
# moordesign.m:59
    
    if ss(3) >= 1024:
        fs=11
# moordesign.m:60
    
    if ss(3) > 1200:
        fs=12
# moordesign.m:61
    
    
    if isempty(uw):
        uw=0
# moordesign.m:63
        vw=0
# moordesign.m:63
    
    
    figure(1)
    figname=get(1,'Name')
# moordesign.m:65
    if strcmp(figname,'Mooring Design & Dynamics') == 1:
        mmppathfile=which('mmposition.mat')
# moordesign.m:67
        mmp=get(1,'Position')
# moordesign.m:68
        save(mmppathfile,'mmp')
    
    
    mmppathfile=which('mmposition.mat')
# moordesign.m:72
    
    if length(mmppathfile) >= 14:
        blank=0
# moordesign.m:74
        for i in arange(1,length(mmppathfile)).reshape(-1):
            if strcmp(' ',mmppathfile(i)):
                blank=1
# moordesign.m:74
        if blank == 1:
            mmppathfile=concat([pwd,'\mmposition.mat'])
# moordesign.m:76
            mmp=concat([0.05,0.6,0.32,0.33])
# moordesign.m:77
        else:
            load(mmppathfile)
    else:
        mmp=concat([0.05,0.6,0.32,0.33])
# moordesign.m:82
    
    
    figure(1)
    clf
    set(gcf,'Units','Normalized','Position',mmp,'Name','Mooring Design & Dynamics','Color',concat([0.2,0.6,0.9]))
    hmain1=uicontrol('Style','Pushbutton','String','Design New Mooring','FontSize',fs,'Units','normalized','Position',concat([0.05,0.89,0.44,0.08]),'Callback','modmoor(-1)')
# moordesign.m:90
    hmain11=uicontrol('Style','Pushbutton','String','Design Towed Body','FontSize',fs,'Units','normalized','Position',concat([0.51,0.89,0.44,0.08]),'Callback','modtow(-1)')
# moordesign.m:95
    if logical_or((logical_and(logical_not(isempty(H)),logical_not(isempty(moorele)))),(logical_and(logical_not(isempty(Ht)),logical_not(isempty(moorelet))))):
        hmain2=uicontrol('Style','Pushbutton','String','Load Existing Mooring/Tow','FontSize',fs,'Units','normalized','Position',concat([0.05,0.79,0.44,0.08]),'Callback','moordesign(2)')
# moordesign.m:101
        hmain3=uicontrol('Style','Pushbutton','String','Save Mooring/Towed Body','FontSize',fs,'Units','normalized','Position',concat([0.51,0.79,0.44,0.08]),'Callback','savemd')
# moordesign.m:106
        if isempty(Ht):
            hmain4=uicontrol('Style','Pushbutton','String','Add/Modify In-Line Elements','FontSize',fs,'Units','normalized','Position',concat([0.05,0.68,0.44,0.08]),'Callback','modmoor(0)')
# moordesign.m:112
            hmain44=uicontrol('Style','Pushbutton','String','Add/Modify Clamp-On Devices','FontSize',fs,'Units','normalized','Position',concat([0.51,0.68,0.44,0.08]),'Callback','modmoorCO(0)')
# moordesign.m:117
        else:
            hmain4=uicontrol('Style','Pushbutton','String','Add/Modify Towed Body','FontSize',fs,'Units','normalized','Position',concat([0.05,0.68,0.44,0.08]),'Callback','modtow(0)')
# moordesign.m:123
            hmain44=uicontrol('Style','Pushbutton','String','Add/Modify Clamp-On Devices','FontSize',fs,'Units','normalized','Position',concat([0.51,0.68,0.44,0.08]),'Callback','modtowCO(0)')
# moordesign.m:128
    else:
        hmain2=uicontrol('Style','Pushbutton','String','Load Existing Mooring','FontSize',fs,'Units','normalized','Position',concat([0.05,0.79,0.44,0.08]),'Callback','moordesign(2)')
# moordesign.m:135
        hmain21=uicontrol('Style','Pushbutton','String','Load Existing Towed Body','FontSize',fs,'Units','normalized','Position',concat([0.51,0.79,0.44,0.08]),'Callback','moordesign(2)')
# moordesign.m:140
    
    if logical_and(logical_not(isempty(U)),logical_not(isempty(z))):
        hmain5=uicontrol('Style','Pushbutton','String','Set/Load Envir. Cond.','FontSize',fs,'Units','normalized','Position',concat([0.05,0.57,0.44,0.08]),'Callback','getvelocity')
# moordesign.m:147
        hmain6=uicontrol('Style','Pushbutton','String','Display Currents/Ship Speed','FontSize',fs,'Units','normalized','Position',concat([0.51,0.57,0.44,0.08]),'Callback','getvelocity(40)')
# moordesign.m:152
    else:
        hmain5=uicontrol('Style','Pushbutton','String','Set/Load Environmental Conditions','FontSize',fs,'Units','normalized','Position',concat([0.1,0.57,0.8,0.08]),'Callback','getvelocity')
# moordesign.m:158
    
    if logical_or((logical_and(logical_not(isempty(H)),logical_not(isempty(moorele)))),(logical_and(logical_not(isempty(Ht)),logical_not(isempty(moorelet))))):
        hmain7=uicontrol('Style','Pushbutton','String','Evaluate and Plot 3-D Mooring/Towed Body','FontSize',fs,'Units','normalized','Position',concat([0.05,0.43,0.9,0.12]),'Callback','mdplot','FontWeight','bold')
# moordesign.m:165
        if logical_not(isempty(Z)):
            hmain8=uicontrol('Style','Pushbutton','String','Display Positions & Tensions','FontSize',fs,'Units','normalized','Position',concat([0.025,0.32,0.475,0.08]),'Callback','dismoor(0)')
# moordesign.m:172
            hmain9=uicontrol('Style','Pushbutton','String','Print','FontSize',fs,'Units','normalized','Position',concat([0.5,0.32,0.1,0.08]),'Callback','dismoor(1)')
# moordesign.m:177
        else:
            hmain8=uicontrol('Style','Pushbutton','String','Display Mooring Elements','Units','normalized','FontSize',fs,'Position',concat([0.05,0.32,0.425,0.08]),'Callback','dismoor(0)')
# moordesign.m:183
            hmain9=uicontrol('Style','Pushbutton','String','Print','FontSize',fs,'Units','normalized','Position',concat([0.475,0.32,0.1,0.08]),'Callback','dismoor(1)')
# moordesign.m:188
        if isempty(Ht):
            hmain8p=uicontrol('Style','Pushbutton','String','Plot Mooring','FontSize',fs,'Units','normalized','Position',concat([0.625,0.32,0.225,0.08]),'Callback','plot_elements(0)')
# moordesign.m:195
            hmain9p=uicontrol('Style','Pushbutton','String','Print','FontSize',fs,'Units','normalized','Position',concat([0.85,0.32,0.1,0.08]),'Callback','plot_elements(1)')
# moordesign.m:200
        else:
            hmain8p=uicontrol('Style','Pushbutton','String','Enter Desired Depth [m]','FontSize',fs,'Units','normalized','Position',concat([0.625,0.32,0.325,0.08]),'Callback','getvelocity(47)')
# moordesign.m:206
    
    hmain10=uicontrol('Style','Pushbutton','String','Add/Examine Elements in Database','Units','normalized','FontSize',fs,'Position',concat([0.1,0.21,0.8,0.08]),'Callback','addelement')
# moordesign.m:213
    hmainclr=uicontrol('Style','Pushbutton','String','Clear All','FontSize',fs,'Units','normalized','Position',concat([0.1,0.01,0.2,0.08]),'Callback','moordesign(1)')
# moordesign.m:218
    hmain_whos=uicontrol('Style','Pushbutton','String','Whos','FontSize',fs,'Units','normalized','Position',concat([0.4,0.01,0.2,0.08]),'Callback','whos global')
# moordesign.m:223
    hmaincls=uicontrol('Style','Pushbutton','String','Close','FontSize',fs,'Units','normalized','Position',concat([0.7,0.01,0.2,0.08]),'Callback','close all')
# moordesign.m:228
    
    if command == 1:
        mmp=get(1,'Position')
# moordesign.m:235
        mmppathfile=which('mmposition.mat')
# moordesign.m:236
        save(mmppathfile,'mmp')
        clear('all')
        close_('all')
        command=1
# moordesign.m:240
        moordesign(0)
    else:
        if command == 2:
            loadmd
            moordesign(100)
    
    
    if command != 1:
        if logical_not(isempty(U)):
            mu,nu=size(U,nargout=2)
# moordesign.m:249
            mz,nz=size(z,nargout=2)
# moordesign.m:250
            if mz == logical_and(nu,nz) != mu:
                U=U.T
# moordesign.m:252
                V=V.T
# moordesign.m:252
                W=W.T
# moordesign.m:252
            mu,nu=size(U,nargout=2)
# moordesign.m:254
            if logical_not(isempty(time)):
                if length(time) == logical_and(nu,nu) > 1:
                    if logical_or(exist('M'),exist('Zts')):
                        if logical_and(isempty(M),isempty(Zts)):
                            hmain11=uicontrol('Style','Pushbutton','String','Make a Time Series','FontSize',fs,'Units','normalized','Position',concat([0.3,0.12,0.4,0.08]),'Callback','makemovie(0)')
# moordesign.m:259
                        else:
                            if logical_or(logical_not(isempty(M)),logical_not(isempty(Zts))):
                                hmain11=uicontrol('Style','Pushbutton','String','Make Movie','FontSize',fs,'Units','normalized','Position',concat([0.1,0.12,0.25,0.08]),'Callback','makemovie(0)')
# moordesign.m:265
                                hmain12=uicontrol('Style','Pushbutton','String','Save Movie','FontSize',fs,'Units','normalized','Position',concat([0.37,0.12,0.26,0.08]),'Callback','savemovie')
# moordesign.m:270
                                if logical_not(isempty(M)):
                                    hmain13=uicontrol('Style','Pushbutton','String','Show Movie','FontSize',fs,'Units','normalized','Position',concat([0.65,0.12,0.25,0.08]),'Callback','makemovie(2)')
# moordesign.m:276
        else:
            if logical_not(isempty(M)):
                hmain11=uicontrol('Style','Pushbutton','String','Load a Movie','FontSize',fs,'Units','normalized','Position',concat([0.1,0.12,0.35,0.08]),'Callback','moordesign(2)')
# moordesign.m:288
                hmain13=uicontrol('Style','Pushbutton','String','Show Movie','FontSize',fs,'Units','normalized','Position',concat([0.55,0.12,0.35,0.08]),'Callback','makemovie(2)')
# moordesign.m:293
            else:
                hmain11=uicontrol('Style','Pushbutton','String','Load a Movie','FontSize',fs,'Units','normalized','Position',concat([0.3,0.12,0.4,0.08]),'Callback','moordesign(2)')
# moordesign.m:299
    
    mmp=get(1,'Position')
# moordesign.m:307
    mmppathfile=which('mmposition.mat')
# moordesign.m:308
    
    save(mmppathfile,'mmp')
    
    # fini