from sympy import *
import numpy as np
from numpy.linalg import inv
##Main input function
#$declear variables e.g. system of x1,x2
x1 , x2, t = symbols('x1 x2 t')

##e.g. y = -x1^2-2x2^2+2x2+2x1x2
f = -x1**2-2*x2**2+2*x2+2*x1*x2

##Accuracy level:
lvl = 0.1

##Current point in array form e.g. x1 = 0, x2 = 0
xcurr = [0,0]


##Multi-Dimensional Gradient Search
##Takes in Sympy Function f, float array: xcurr: current point, float lvl: accuracy level, bool debug (print if True)
##Return result
def gradientSearch(f,xcurr,lvl,debug):
    dx1 = diff(f,x1).evalf(subs = {x1 : xcurr[0], x2 : xcurr[1]})
    dx2 = diff(f,x2).evalf(subs = {x1 : xcurr[0], x2 : xcurr[1]})
    if (debug):
        print("df/dx1 :" + str(diff(f,x1)) + "  ||    df/dx2 :" + str(diff(f,x2)))
    count = 1
    while(dx1 > lvl or dx2 > lvl):
        xnew = [xcurr[0] + t*dx1,xcurr[1] + t*dx2]
        maxt = solve(f.subs([(x1,xnew[0]),(x2,xnew[1])]).diff(t),t)[0]
        xcurr = [xcurr[0] + maxt*diff(f,x1).evalf(subs = {x1 : xcurr[0], x2 : xcurr[1]}),xcurr[1] + maxt*diff(f,x2).evalf(subs = {x1 : xcurr[0], x2 : xcurr[1]})]
        if(debug):
            print("Iteratrion :" + str(count) + " xcurr :" + str(xcurr) + " x1' :" + str(round(dx1,6)) + " x2' : " + str(round(dx2,6)) + " t :" + str(round(maxt,6)))
        dx1 = diff(f, x1).evalf(subs={x1: xcurr[0], x2: xcurr[1]})
        dx2 = diff(f, x2).evalf(subs={x1: xcurr[0], x2: xcurr[1]})
        count += 1
    return xcurr

##Multi-Dimensional Gradient Search
##Takes in Sympy Function f, float array: xcurr: current point, float lvl: accuracy level, bool debug (print if True)
##Return result
def newton2D(f,xcurr,lvl,debug):
    count = 1
    x = [[xcurr[0]], [xcurr[1]]]
    if(debug):
        print("Gradient :" + str([[diff(f,x1,2),diff(diff(f,x1),x2)],[diff(diff(f,x2),x1),diff(f,x2,2)]]))
    while(True):
        gradient = ([[round(diff(f,x1,2).evalf(subs = {x1 : x[0][0], x2 : x[1][0]}),6),round(diff(diff(f,x1),x2).evalf(subs = {x1 : x[0][0], x2 : x[1][0]}),6)],[round(diff(diff(f,x2),x1).evalf(subs = {x1 : x[0][0], x2 : x[1][0]}),6),round(diff(f,x2,2).evalf(subs = {x1 : x[0][0], x2 : x[1][0]}),6)] ])
        dx = [[diff(f,x1).evalf(subs = {x1 : x[0][0], x2 : x[1][0]})], [diff(f,x2).evalf(subs = {x1 : x[0][0], x2 : x[1][0]})]]
        xnext = x - np.dot(inv(np.array(gradient)),dx)
        if(debug):
            xi = [[round(x[0][0],6)],[round(x[1][0],6)]]
            xn = [[round(xnext[0][0],6)],[round(xnext[1][0],6)]]
            xp = [[round(dx[0][0],6)],[round(dx[1][0],6)]]
            print("Iteration : " + str(count) + " xi :" + str(xi) + " Gradient : " + str(gradient) + " x' : " + str(xp) + " xi+1 :" + str(xn) + " |xi+1 - xi| = " + str(round(((xnext[0][0]-x[0][0])**2+(xnext[1][0]-xnext[1][0])**2)**0.5,6)))
        if((xnext[0][0]-x[0][0])**2+(xnext[1][0]-xnext[1][0])**2 < lvl**2):
            break
        x = xnext
        count += 1
    return [xnext[0][0],xnext[1][0]]

##Main method
##Takes in Sympy Function f, float array: xcurr: current point, float lvl: accuracy level, bool debug (print if true)
##         Optional str method: method of evaluation (nt -> newtons(default) / gs -> gradient)
##Return result
def NLsolve2D(f,lvl,debug,xcurr,method = None):
    if(method == 'gs'):
        return gradientSearch(f,xcurr,lvl,debug)
    else:
        return newton2D(f,xcurr,lvl,debug)

##runit
print((NLsolve2D(f,lvl,True,method = 'nt',xcurr = xcurr)))