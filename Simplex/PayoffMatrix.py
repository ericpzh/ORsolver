import numpy as np
from Simplex import simplexSolve
'''
Given a Payoff Matrix, solve it with Simplex method 
'''
Matrix = np.array([
    [2,3],
    [1,1]
])
##takes in a payoffMatrix and bool debug(print intermidates step if true)
def PayoffMatrixSolve(payoffMatrix,debug):
    if(debug == True):
        print("Payoff Matrix entered: ")
        print(payoffMatrix)
    ##build CT,A,b from payoff matrix
    CTarr = [[]]
    tempA = [[]]
    tempb = [[]]
    for i in range(len(payoffMatrix[0])):
        CTarr[0].append(0)
        tempA[0].append(1)
        tempb[0].append(0)
    CTarr[0].insert(0,1)
    CT = np.array(CTarr)
    tempA = np.transpose(np.array(tempA))
    A = np.transpose(payoffMatrix)*-1
    A = np.concatenate((tempA,A),axis=1)
    tempA = [[0]]
    for i in range(len(payoffMatrix)):
        tempA[0].append(1)
    A = np.concatenate((A,tempA),axis=0)
    tempb[0].append(1)
    b = np.transpose(np.array(tempb))
    ##solve
    ls = simplexSolve(CT,A,b,False)
    del ls[0]
    if(debug == True):
        print("Z = Expectation of the game \n" + "x1 = u \n" + "rest of Xs sum up to 1 = probabilities of certain strategies")
    return ls

##runit
PayoffMatrixSolve(Matrix,True)
