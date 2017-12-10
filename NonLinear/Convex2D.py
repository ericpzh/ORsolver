from sympy import *

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
    while(dx1 > lvl or dx2 > lvl):
        xnew = [xcurr[0] + t*dx1,xcurr[1] + t*dx2]
        maxt = solve(f.subs([(x1,xnew[0]),(x2,xnew[1])]).diff(t),t)[0]
        xcurr = [xcurr[0] + maxt*diff(f,x1).evalf(subs = {x1 : xcurr[0], x2 : xcurr[1]}),xcurr[1] + maxt*diff(f,x2).evalf(subs = {x1 : xcurr[0], x2 : xcurr[1]})]
        if(debug):
            print("xcurr :" + str(xcurr) + " x1' :" + str(round(dx1,6)) + " x2' : " + str(round(dx2,6)))
        dx1 = diff(f, x1).evalf(subs={x1: xcurr[0], x2: xcurr[1]})
        dx2 = diff(f, x2).evalf(subs={x1: xcurr[0], x2: xcurr[1]})

    return xcurr

##Multi-Dimensional Gradient Search
##Takes in Sympy Function f, float array: xcurr: current point, float lvl: accuracy level, bool debug (print if True)
##Return result
def newton2D(f,xcurr,lvl,debug):
    return xcurr

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
print((NLsolve2D(f,lvl,True,method = 'gs',xcurr = xcurr)))