# Generated with SMOP  0.41-beta
from libsmop import *
# r8_random.m

    
@function
def r8_random(s1=None,s2=None,s3=None,*args,**kwargs):
    varargin = r8_random.varargin
    nargin = r8_random.nargin

    #*****************************************************************************80
    
    ## R8_RANDOM returns a pseudorandom number between 0 and 1.
    
    #  Discussion:
    
    #    This function returns a pseudo-random number rectangularly distributed
#    between 0 and 1.   The cycle length is 6.95E+12.  (See page 123
#    of Applied Statistics (1984) volume 33), not as claimed in the
#    original article.
    
    #  Licensing:
    
    #    This code is distributed under the GNU LGPL license.
    
    #  Modified:
    
    #    08 July 2008
    
    #  Author:
    
    #    Original FORTRAN77 version by Brian Wichman, David Hill.
#    MATLAB version by John Burkardt.
    
    #  Reference:
    
    #    Brian Wichman, David Hill,
#    Algorithm AS 183: An Efficient and Portable Pseudo-Random
#    Number Generator,
#    Applied Statistics,
#    Volume 31, Number 2, 1982, pages 188-190.
    
    #  Parameters:
    
    #    Input, integer S1, S2, S3, three values used as the
#    seed for the sequence.  These values should be positive
#    integers between 1 and 30,000.
    
    #    Output, real R, the next value in the sequence.
    
    #    Output, integer S1, S2, S3, updated seed values.
    
    s1=mod(dot(171,s1),30269)
# r8_random.m:45
    s2=mod(dot(172,s2),30307)
# r8_random.m:46
    s3=mod(dot(170,s3),30323)
# r8_random.m:47
    r=mod(s1 / 30269.0 + s2 / 30307.0 + s3 / 30323.0,1.0)
# r8_random.m:49
    return r,s1,s2,s3
    return r,s1,s2,s3
    
if __name__ == '__main__':
    pass
    