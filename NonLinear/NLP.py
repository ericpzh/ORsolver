import numpy as np
import sympy as sym

##Main input function
##e.g. y = x^2+x^3
def F(x):
    return x**2+x**3
##Accuracy level:
lvl = 0.005

##1D Bisection Search
##Takes in float lvl: accuracy level, bool debug (print if true)
##         float xL,xU for lower/upper bound
##Return float result (Max/Min)
def bisection(xL,xU,lvl,debug):
    def dF(x1):
        return sym.diff(F(x),x,1).evalf(subs = {x : x1})
    count = 0
    while(xU-xL > 2*lvl):
        xM = (xL+xU)/2
        dx = df(xM)
        if(debug):
            print("Iteration :" + str(count) + " xL :" + str(xL) + " xU :" + str(xU) + " xM :" + str(xM) + " dx: " + str(dx))
        count += 1
        if(dx > 0):
            xL = xM
        elif(dx < 0):
            xU = xM
        else:
            return xM
    return (xL+xU)/2

##MultiDimensional Newton's Methods
##Takes in float lvl: accuracy level, bool debug (print if true)
##         float xL: current x
##Return float result (Max/Min)
def newton(xL,lvl,debug):
    def dF(x1):
        return sym.diff(F(x),x,1).evalf(subs = {x : x1})
    def dF2(x1):
        return sym.diff(F(x),x,2).evalf(subs = {x : x1})
    currx = xL
    count = 0
    while(True):
        nextx = currx - dF(currx)/dF2(currx)
        if(debug):
            print("Iteration :" + str(count) + " xi :" + str(currx) + " df :" + str(dF(currx)) + " df2 :" + str(dF2(currx)) + " xi+1 :" + str(nextx) + " |xi+1 - xi| :" + str(abs(nextx - currx)))
        if(abs(nextx - currx) < lvl):
            return nextx
        currx = nextx
        count += 1
    return

##1Dimensional Golden Ratio Search
##Takes in float lvl: accuracy level, bool debug (print if true)
##Return float result (Max/Min)
def goldenRatio(lvl,debug):
    return

##Main method
##Takes in float lvl: accuracy level, bool debug (print if true)
##         Optional str method: method of evaluation (nt -> newtons(default) / bs -> bisection / gr -> golden ratio)
##         Optional float xL(current x),xU for lower/upper bound
##Return result
def NLsolve(xL = None,xU = None,lvl,debug,method = None):
    if(xL == None or xU = None):
        def dF(x1):
            return sym.diff(F(x),x,1).evalf(subs = {x : x1})
        alpha = 1
        if(dF(0) > 0):
            xL = 0
            while(dF(xL + alpha) < 0):
                xU = xL + alpha
        elif(dF(0) < 0):
            xU = 0
            while(dF(xU - alpha) > 0):
                xL = xU - alpha
        else:
            return 0
    if(method == 'gr'):
        return goldenRatio(lvl,debug)
    elif(method == 'bs'):
        return bisection(xL,xU,lvl,debug)
    else:
        return newton(xL,lvl, debug)

##Runit
NLsolve(0,1,lvl,True)
