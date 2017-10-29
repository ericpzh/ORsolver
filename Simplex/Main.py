import numpy as np
from numpy.linalg import inv
from decimal import Decimal
import fractions
np.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})
from fractions import Fraction
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

##Main function
##No big M yet
##Takes in: nparray C^T,A,b; bool debug:(true -> print slack var)
def main(CT,A,b,debug):
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
    #row/col
    row = len(A)
    col = len(AI[0])
    #rowarr:how many rows in A?
    rowarr = []
    for i in range(row):
        rowarr.append(i)
    basicVar = [3, 4]
    nonbasicVar = [0, 1, 2]
    ##initialize constant value
    flag = False
    result = ""
    iteration = 0
    ##main iteration loop
    while (flag == False):
        ##assemble the new matrix
        # B
        tempB = np.ix_(rowarr, basicVar)
        for i in rowarr:
            tempB[i].shape
        B = AI[tempB]
        # C_B^T
        tempC = np.ix_([0], basicVar)
        tempC[0].shape
        CBT = C[tempC]
        #y^T
        yT = CBT.dot(inv(B))
        #B^-1
        Binv = inv(B)
        '''
        Matrix concatenate to tabuluer
        [ M1 M2 M3 ] = [M7]
        [ M4 M5 M6 ]   [M8]
       '''
        M1 = yT.dot(A)-CT
        M2 = yT
        M3 = yT.dot(b)
        M4 = Binv.dot(A)
        M5 = Binv
        M6 = Binv.dot(b)
        M7 = np.concatenate((M1,M2,M3),axis=1)
        M8 = np.concatenate((M4,M5,M6),axis=1)
        tab = np.concatenate((M7,M8),axis= 0 )
        ##print
        print("Iteration #:" + str(iteration) + ".")
        print(tab)
        print("Basic Var(index): " + str(basicVar))
        print("Nonbasic Var(index): " + str(nonbasicVar))
        ##if optimal
        if (min(tab[0]) >= 0):
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
        print("Entering var : x" + str(entering+1) + " val: "+str(tab[0][entering]) + " .")
        ##leaving var
        leaving = -1
        templeaving = leavingVar(tab,entering)
        if(templeaving != -1):
            leaving = basicVar[templeaving]
            leavingindex = -1
            for i in range(len(basicVar)):
                if(leaving == basicVar[i]):
                    leavingindex = i
            print("Leaving var : x" + str(leaving+1) + " val : "+str(tab[leavingindex+1][entering]) + ".")
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

#Main data
ct = np.array([[3,1,5]])

a = np.array([
    [7,3,5],
    [3,4,6]
])

B = np.transpose(np.array([[25,20]]))

main(ct,a,B,True)