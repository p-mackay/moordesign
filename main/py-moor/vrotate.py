# Generated with SMOP  0.41-beta
from libsmop import *
# vrotate.m

    
@function
def vrotate(u1=None,v1=None,theta=None,*args,**kwargs):
    varargin = vrotate.varargin
    nargin = vrotate.nargin

    #    Function to perform 2-D vector rotation
#    Usage: [u2 v2] = vrotate(u1,v1,theta)
#    Where: u1, v1 = input vector coordinates
#           theta = rotation angle in degrees (- is clockwise)
#    RKD 4/97
    if size(u1) != size(v1):
        disp(concat(['Vectors must be the same size.']))
        return u2,v2
    
    # Use complex notation
    z1=u1 + dot(sqrt(- 1),v1)
# vrotate.m:9
    
    z=multiply(z1,exp(dot(dot(sqrt(- 1),theta),pi) / 180))
# vrotate.m:11
    
    
    u2=real(z)
# vrotate.m:13
    
    v2=imag(z)
# vrotate.m:14
    # fini