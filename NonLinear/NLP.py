import numpy as np
from scipy import *

##Main input function
##e.g. y = x^2+x^3
def F(x):
    return x**2+x**3
##Accuracy level:
lvl = 0.005

##1D Bisection Search
##Takes in float lvl: accuracy level, bool debug (print if true)
##Return float result (Max/Min)

def bisection(lvl,debug):
    return

##MultiDimensional Newton's Methods
##Takes in float lvl: accuracy level, bool debug (print if true)
##Return float result (Max/Min)
def newton(lvl,debug):
    return

##1Dimensional Golden Ratio Search
##Takes in float lvl: accuracy level, bool debug (print if true)
##Return float result (Max/Min)
def goldenRatio(lvl,debug):
    return

##Main method
##Takes in float lvl: accuracy level, bool debug (print if true)
##         Optional str method: method of evaluation (nt -> newtons(default) / bs -> bisection / gr -> golden ratio)
##Return result
def NLsolve(lvl,debug,method = None):
    if(method == 'gr'):
        return goldenRatio(lvl,debug)
    elif(method == 'bs'):
        return bisection(lvl,debug)
    else:
        return newton(lvl, debug)

##Runit
NLsolve(lvl,True)
