import sympy as sym
from sympy import *
import math

##Main input function
##e.g. y = -4x^4-5x^2+3x
x = symbols('x')
f = -4*x**4-5*x**2+3*x

##Accuracy level:
lvl = 0.005

##Lower bound(bisection,golden ratio)/ Starting x(newton) (= None if don't have one)
xL = 0
#xL = None #Uncomment this if your don't have lower bound/ Starting x

##Upper bound (= None if don't have one)
xU = 1
#xU = None #Uncomment this if your don't have upper bound


##1D Bisection Search
##Takes in Sympy Function f, float lvl: accuracy level, bool debug (print if true)
##         float xL,xU for lower/upper bound
##Return float result (Max/Min)
def bisection(f,xL,xU,lvl,debug):
    def dF(x1):
        return sym.diff(f,x,1).evalf(subs = {x : x1})
    count = 1
    while(abs(xU-xL) > 2*lvl):
        xM = (xL+xU)/2
        dx = dF(xM)
        if(debug):
            print("Iteration :" + str(count) + " xL :" + str(round(xL,6)) + " xU :" + str(round(xU,6)) + " xM :" + str(round(xM,6)) + " dx: " + str(round(dx,6)) + " (xU-xL)/2 :" + str(round((xU-xL)/2,6)))
        if(abs((xU-xL)/2) < 2*lvl):
            return xM
        count += 1
        if(dx > 0):
            xL = xM
        elif(dx < 0):
            xU = xM
        else:
            return xM
    return (xL+xU)/2

##1Dimensional Newton's Methods
##Takes in Sympy Function f, float lvl: accuracy level, bool debug (print if true)
##         float xL: current x
##Return float result (Max/Min)
def newton1D(f,xL,lvl,debug):
    def dF(x1):
        return sym.diff(f,x,1).evalf(subs = {x : x1})
    def dF2(x1):
        return sym.diff(f,x,2).evalf(subs = {x : x1})
    currx = xL
    count = 1
    while(True):
        nextx = currx - dF(currx)/dF2(currx)
        if(debug):
            print("Iteration :" + str(count) + " xi :" + str(round(currx,6)) + " f'(x) :" + str(round(dF(currx),6)) + " f''(x) :" + str(round(dF2(currx),6)) + " xi+1 :" + str(round(nextx,6)) + " |xi+1 - xi| :" + str(round(abs(nextx - currx),6)))
        if(abs(nextx - currx) < lvl):
            return nextx
        currx = nextx
        count += 1
    return currx

##1Dimensional Golden Ratio Search
##Takes in Sympy Function f,float lvl: accuracy level, bool debug (print if true)
##         float xL,xU for lower/upper bound
##Return float result (Max/Min)
def goldenRatio(f,xL,xU,lvl,debug):
    gr = (math.sqrt(5) + 1) / 2
    a = xU - (xU - xL) / gr
    b = xL + (xU - xL) / gr
    count = 1
    while(abs(a-b) > lvl):
        if(debug):
            print("Iteration :" + str(count) + " xL :" + str(round(xL,6)) + " xU :" + str(round(xU,6)) + " x1 :" + str(round(a,6)) + " x2: " + str(round(b,6)) + " (xU-xL) :" + str(round((xU-xL),6)))
        if(f.evalf(subs = {x : a}) > f.evalf(subs = {x : b})):
            xU = b
        else:
            xL = a
        a = xU - (xU - xL) / gr
        b = xL + (xU - xL) / gr
        count += 1
    return (xU+xL)/2


##Main method
##Takes in Sympy Function f, float lvl: accuracy level, bool debug (print if true)
##         Optional str method: method of evaluation (nt -> newtons(default) / bs -> bisection / gr -> golden ratio)
##         Optional float xL(current x),xU for lower/upper bound
##Return result
def NLsolve1D(f,lvl,debug,method = None,xL = None,xU = None,):
    if(xL == None or xU == None):
        def dF(x1):
            return sym.diff(f,x,1).evalf(subs = {x : x1})
        alpha = 1
        if(dF(0) > 0):
            xL = 0
            xU = xL + alpha
            while(dF(xU) > 0):
                xU += alpha
        elif(dF(0) < 0):
            xU = 0
            xL = xU - alpha
            while(dF(xL) < 0):
                xL -= alpha
        else:
            return 0
    if(method == 'gr'):
        return goldenRatio(f,xL,xU,lvl,debug)
    elif(method == 'bs'):
        return bisection(f,xL,xU,lvl,debug)
    else:
        return newton1D(f,xL,lvl, debug)

##Runit
#print(round(NLsolve1D(f,lvl,True,method = 'bs',xL = xL, xU = xU),6))