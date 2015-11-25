#-------------------------------------------------------------------------------
# Name:        GameMath
# Purpose:
#
# Author:      Reuben Unicruz
#
# Created:     09/12/2014
# Copyright:   (c) Reuben 2014
# Licence:     Creative Commons (CC-BY)
#-------------------------------------------------------------------------------
'''
Special thanks to:
    This website: http://freespace.virgin.net/hugo.elias/models/m_perlin.htm
'''

from math import pi, cos

def newLerp(a, b, x):
    return a*(1-x) + b*x

def newCosLerp(a, b, x, factor):
    ft = x * pi
    f = (1 - cos(ft)) * factor
    return (a*(1-f) + b*f)

def newCubLerp(v0, v1, v2, v3, x):
    P = (v3 - v2) - (v0 - v1)
    Q = (v0 - v1) - P
    R = v2 - v0
    S = v1

    return (P*pow(x, 3)) + (Q*pow(x, 2)) + (R*x) + S

def clamp(valueToClamp, minLimit, maxLimit):
    
    if (valueToClamp < maxLimit) and (valueToClamp > minLimit):
        return valueToClamp
    if (valueToClamp > maxLimit):
        return maxLimit
    if (valueToClamp < minLimit):
        return minLimit
    else:
        return valueToClamp

'''
def clamp(minLimit, maxLimit, value):
    return max(minLimit, min(value, maxLimit))
'''

def clamp2(valueToClamp, minLimit, maxLimit):
    return max(minLimit, min(valueToClamp, maxLimit))
    
