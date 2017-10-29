import numpy as np
from Main import simplexSolve
from BreakThru import payoffMatrix
'''
Given a Payoff Matrix, solve it with Simplex method 
'''
def PayoffMatrixSolve(payoffMatrix):
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
    simplexSolve(CT,A,b,False)

##runit
PayoffMatrixSolve(payoffMatrix)