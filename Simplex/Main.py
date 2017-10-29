import numpy as np
from numpy.linalg import inv
from decimal import Decimal
import fractions
np.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})
from fractions import Fraction
'''
#Main Input data
#Starndard Form
## coeff of obj function
## e.g. Max Z = 3x+2y   -> CT = np.array([[3,2]])
'''
CT = np.array([[1,0,0]])
'''
## coeff of constraint
## e.g   3x + 5y <= 3    -> A = np.array([[3,5],
##             x <= 2                     [2,0]])
'''
A = np.array([
    [1,0,-1],
    [1,2,-4],
    [1,-2,3],
    [0,1,1],
])
'''
##coeff of RHS
## e.g   3x + 5y <= 3    -> b = np.array([[3],
##             x <= 2                     [2]])
'''
b = np.transpose(np.array([[0,0,0,1]]))
'''(<-'#" this (if needed))
##INDEV 
##(for the x + y = 1 case : x + y <= 1 still works)
##
##comment out if you need to overwrite of AI and C
##e.g. if you need  Max x + y = 1 ->  C = np.array([[1,1,1]])
##                      x + y = 1 -> AI = np.array([[1,1,0],
##                    2x + 3y <= 1                 [2,3,1]])
                                     
AI = np.array([
     [1,0,-1,1,0,0],
     [1,2,-4,0,1,0],
     [1,-2,3,0,0,1],
     [0,1,1,0,0,0],
])
C = np.array([[1,0,0,0,0,0]])

##and run with main(CT,A,b,True,customAI = AI, customC = C)
##'''

##helper search of entering variable
##returns index of X in 1st row of matrix
def enteringVar(list):
    ret = -1
    for i in range(len(list)-1):
        if(list[i] == min(list)):
            ret = i
    return ret

##helper search of leaving varialbe
##returns index of X in basicVar[]
def leavingVar(matrix,entering):
    ret = -1
    minratio = []
    for i in range(1,len(matrix)):
        if(matrix[i][entering] > 0):
            minratio.append(matrix[i][len(matrix[0])-1]/matrix[i][entering])
        else:
            minratio.append(9999999)
    for i in range(len(minratio)):
        if(minratio[i] == min(minratio)):
            ret = i
    return ret

'''
##Main function
##No big M yet
##Takes in: nparray C^T,A,b;
               bool   debug:(true -> print slack var);
            OPTIONAL : nparray customAI,customC;
'''
def simplexSolve(CT,A,b,debug,customAI = None,customC = None):
    ##If Wrong input:
    if(len(A[0]) != len(CT[0]) or len(A) != len(b)):
        print("Error. Dimension mismatches. Aborted")
        return
    ##If big M or dual Simplex is needed:
    if(min(b) < 0):
        print("Error. Big M / Dual Simplex method is needed. Aborted")
        return
    ##print objective
    standardForm = ("Maximize Z = ")
    for i in range(len(CT[0])):
        if(i != 0):
            standardForm += (" + " + str(CT[0][i]) + " " + "x" + str(i+1))
        else:
            standardForm += (str(CT[0][i]) + " "  + "x" + str(i + 1))
    standardForm += "\n"
    for i in range(len(A)):
        for j in range(len(A[i])):
            if (j != 0):
                standardForm += (" + " + str(A[i][j]) + " " + "x" + str(j+1))
            else:
                standardForm += (str(A[i][j]) + " " + "x" + str(j + 1))
        standardForm += (" <= " + str(b[i][0]) + "\n")
    print(standardForm)
    ##assemble constant matrix elements
    #AI
    AI = np.concatenate((A, np.identity(len(A))), axis=1)
    #C^T
    temp = []
    for i in range(len(A)):
        temp.append(0)
    C = np.concatenate((CT, [temp]), axis=1)
    ##check if custom input:
    if(np.all(customAI != None)):
        AI = customAI
    if(np.all(customC != None)):
        C = customC
    #row/col
    row = len(A)
    col = len(AI[0])
    #rowarr:how many rows in A?
    rowarr = []
    for i in range(0,row):
        rowarr.append(i)
    #colarr:how many columns in AI?
    colarr = []
    for i in range(col):
        colarr.append(i)
    #variable list for print
    varlist = "  Z  "
    for i in colarr:
        varlist += ("x" + str(i+1) +"  ")
    varlist += "RHS "
    ##BV/NBV
    basicVar = []
    nonbasicVar = []
    for i in range(len(AI[0])):
        if(i < len(A[0])):
            nonbasicVar.append(i)
        else:
            basicVar.append(i)
    ## Z col
    zcol = [[1]]
    for i in range(row):
        zcol.append([0])
    ##initialize constant value
    flag = False
    result = ""
    iteration = 0
    ##main iteration loop
    while (flag == False):
        ##assemble the new matrix
        # B
        B = np.array(AI[rowarr][:,basicVar])
        # C_B^T
        CBT = np.array([C[0][basicVar]])
        #B^-1
        print(B)
        Binv = inv(B)
        #y^T
        yT = CBT.dot(Binv)
        '''
        Matrix concatenate to tabuluer
        [ M1 M2 M3 ] = [M7]
        [ M4 M5 M6 ]   [M8]
        Matrix concatenate to tabuluer
        tabZ = [Zcol tab]
       '''
        M1 = yT.dot(A)-CT
        M2 = yT
        M3 = yT.dot(b)
        M4 = Binv.dot(A)
        M5 = Binv
        M6 = Binv.dot(b)
        M7 = np.concatenate((M1,M2,M3),axis = 1)
        M8 = np.concatenate((M4,M5,M6),axis = 1)
        tab = np.concatenate((M7,M8),axis= 0 )
        tabZ = np.concatenate((zcol,tab),axis = 1)
        ##print
        print("Iteration #:" + str(iteration) + ".")
        print(varlist)
        print(tabZ)
        print("Basic Var(index): " + str(basicVar))
        print("Nonbasic Var(index): " + str(nonbasicVar))
        ##if optimal ( > -1e-10 to aviod computing error on floats)
        if (min(tab[0]) >= 0 or min(tab[0]) > -1e-10):
            flag = True
            result = ( "------------------------------------------- \n" + "Optimal Solution Found \n" + "Z = " + str(Fraction(tab[0][len(tab[0])-1]).limit_denominator()) + "\n")
            length = len(A[0])
            if(debug == True):
                length = len(basicVar)+len(nonbasicVar)
            for i in range(length):
                if(i in nonbasicVar):
                    result += ("x"+str(i+1) +" = 0" + "\n")
                else:
                    index = -1
                    for j in range(1,len(tab)):
                        if(tab[j][i] < 1.0011 and tab[j][i] > 0.9989):
                            index = j
                    result += ("x" + str(i + 1) + " = " + str(Fraction(tab[index][len(tab[index])-1]).limit_denominator())+ "\n")
            break
        ##entering var
        entering = -1
        tempEnter = enteringVar(tab[0])
        if(tempEnter != -1):
            entering = tempEnter
        print("Entering var : x" + str(entering+1) + " coeff val: "+str(tab[0][entering]) + " .")
        ##leaving var
        leaving = -1
        templeaving = leavingVar(tab,entering)
        if(templeaving != -1):
            leaving = basicVar[templeaving]
            leavingindex = -1
            for i in range(len(basicVar)):
                if(leaving == basicVar[i]):
                    leavingindex = i
            print("Leaving var  : x" + str(leaving+1) + " coeff val: "+str(tab[leavingindex+1][entering]) + ".")
        else:
            print("Leaving var : Does not Exist")
        ##if unbounded
        if (leaving == -1):
            flag = True
            result = "-------------------------------------------\n Unbounded"
            break
        ##update basicVar, nonbasicVar
        basicVar.append(entering)
        basicVar.remove(leaving)
        basicVar.sort()
        nonbasicVar[nonbasicVar.index(entering)] = leaving
        ##one more iteration
        iteration += 1
        print("-------------------------------------------")
    ##print result
    print(result)

##runit
simplexSolve(CT,A,b,False, customAI = None , customC = None)