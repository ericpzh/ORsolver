import numpy as np
import sympy as sym
from sympy import *
import math

##Main input function
##e.g. y = -x1^2-2x2^2+2x2+2x1xx2
def F(x1,x2):
    return -x1**2-2*x2**2+2*x2+2*x1*x2

##Accuracy level:
lvl = 0.1

##Current point in array form e.g. x1 = 0, x2 = 0
xcurr = [0,0]

#$declear variables e.g. system of x1,x2
x = symbols('x1','x2')


##Multi-Dimensional Gradient Search
##Takes in float array: xcurr: current point, float lvl: accuracy level, bool debug (print if True)
##Return result
def gradientSearch(xcurr,lvl,debug):
    return

##Main method
##Takes in float array: xcurr: current point, float lvl: accuracy level, bool debug (print if true)
##         Optional str method: method of evaluation (nt -> newtons(default) / bs -> bisection / gr -> golden ratio)
##Return result
def