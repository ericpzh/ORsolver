import numpy as np
import heapq
from copy import copy, deepcopy

'''
In dev solver for transportation problem
You are able to call northwest(matrix)/vogel(matrix) to see initialization result
'''
##Main input
##Input costs,supply,demand of a transportation matrix
## [Cost] [Supply]
##[Demand]  [0]
##All cost item should be less than 999999999
cost = np.array([
    [16, 16, 13, 22, 17],
    [14, 14, 13, 19, 15],
    [19, 19, 20, 23, 99],
    [99, 0, 99, 0, 0]
])
supply = np.array([
    [50],
    [60],
    [50],
    [50]
])
demand = np.array([[30, 20, 70, 30, 60]])
##concatenate the matrix together
demand = np.concatenate((demand, [[0]]), axis=1)
matrix = np.concatenate((cost, supply), axis=1)
matrix = np.concatenate((matrix, demand), axis=0)


##Northwest corner rule of initialization
##Takes in combine cost matrix
##return a combine initialize matrix
def northwest(cost):
    matrix = np.array([[-1 for x in range(len(cost[0])-1)] for y in range(len(cost)-1)])
    supply = np.array([cost[:len(cost[0])-2,len(cost)]])
    supply = supply.transpose()
    demand = np.array([cost[len(cost)-1]])
    matrix = np.concatenate((matrix, supply), axis=1)
    matrix = np.concatenate((matrix, demand), axis=0)
    i,j = 0,0
    while i < len(matrix):
        while j < len(matrix[i]):
            if(matrix[i][len(matrix[i]) - 1] > 0 and matrix[len(matrix) - 1][j] > 0 ):
                minnumber = min(matrix[i][len(matrix[i]) - 1], matrix[len(matrix) - 1][j])
            else:
                minnumber = 0
            matrix[i][j] = minnumber
            matrix[i][len(matrix[i]) - 1] -= minnumber
            matrix[len(matrix) - 1][j] -= minnumber
            if(i == len(cost) - 2 and j == len(cost[0])- 2):
                i = len(matrix)
                break
            elif (matrix[i][len(matrix[i]) - 1] == 0):
                i += 1
            else:
                j += 1
    matrix = matrix[:len(matrix)-1,:len(matrix[0])-1]
    matrix = np.concatenate((matrix, supply), axis=1)
    matrix = np.concatenate((matrix, demand), axis=0)
    printmatrix = [[0 for x in range(len(cost[0])-1)] for y in range(len(cost)-1)]
    for i in range(len(matrix)-1):
        for j in range(len(matrix[i])-1):
            if(matrix[i][j] == -1):
                printmatrix[i][j] = '-'
                matrix[i][j] = 0
            else:
                printmatrix[i][j] = matrix[i][j]
    print("Northwest corner result ('-' as nonbasic var): ")
    for i in printmatrix:
        print(i)
    print("Initialize matrix : ")
    print(matrix)
    return matrix


##Vogel's approx of initialization
##Takes in combine cost matrix
##return a combine initialize matrix
def vogel(cost):
    costcopy = deepcopy(cost)
    costcopy = costcopy[:len(costcopy) - 1, :len(costcopy[0]) - 1]
    matrix = np.array([[-1 for x in range(len(cost[0])-1)] for y in range(len(cost)-1)])
    supply = np.array([cost[:len(cost[0])-2,len(cost)]])
    supply = supply.transpose()
    demand = np.array([cost[len(cost)-1]])
    matrix = np.concatenate((matrix, supply), axis=1)
    matrix = np.concatenate((matrix, demand), axis=0)
    i = 0
    print((len(cost)  + len(cost[0]) - 4 ))
    while (i < (len(cost)  + len(cost[0]) - 4 )):
        penaltycol, penaltyrow = [[]], [[]]
        for j in costcopy:
            penaltycol[0].append(heapq.nsmallest(2, j)[-1] - min(j))
        penaltycol = np.array(penaltycol)
        penaltycol = penaltycol.transpose()
        costcopy = costcopy.transpose()
        for j in costcopy:
            penaltyrow[0].append(heapq.nsmallest(2, j)[-1] - min(j))
        penaltyrow = np.array(penaltyrow)
        costcopy = costcopy.transpose()
        littlecost = deepcopy(costcopy)
        penaltyrow = np.concatenate((penaltyrow, [[0]]), axis=1)
        costcopy = np.concatenate((costcopy, penaltycol), axis=1)
        costcopy = np.concatenate((costcopy, penaltyrow), axis=0)
        if( i == (len(cost)  + len(cost[0]) - 5 )):
            firstcol,firstrow,secondcol,secondrow = 0,0,0,0
            flag = True
            for x in range(len(littlecost)):
                for y in range(len(littlecost[x])):
                    if(littlecost[x][y] != 999999999 and flag):
                        firstrow = x
                        firstcol = y
                        flag = False
                    elif(littlecost[x][y] != 999999999 and (flag == False)):
                        secondrow = x
                        secondcol = y
            if (matrix[firstrow][len(matrix[firstrow]) - 1] > 0 and matrix[len(matrix) - 1][firstcol] > 0):
                minnumber = min(matrix[firstrow][len(matrix[firstrow]) - 1], matrix[len(matrix) - 1][firstcol])
            else:
                minnumber = 0
            matrix[firstrow][firstcol] = minnumber
            matrix[firstrow][len(matrix[firstrow]) - 1] -= minnumber
            matrix[len(matrix) - 1][firstcol] -= minnumber
            if (matrix[secondrow][len(matrix[secondrow]) - 1] == 0 and matrix[len(matrix) - 1][secondcol] == 0):
                minnumber = 0
            else:
                minnumber = max(matrix[firstrow][len(matrix[firstrow]) - 1], matrix[len(matrix) - 1][firstcol])
            matrix[secondrow][secondcol] = minnumber
        else:
            if(max(penaltyrow[0]) > max(penaltycol[0])):
                col = max( (v, i) for i, v in enumerate(penaltyrow[0]) )[1]
                row = np.argmin(littlecost[:, col])
            else:
                row = max( (v, i) for i, v in enumerate(penaltycol[0]) )[1]
                col = np.argmin(littlecost[row, :])
            if (matrix[row][len(matrix[row]) - 1] > 0 and matrix[len(matrix) - 1][col] > 0):
                minnumber = min(matrix[row][len(matrix[row]) - 1], matrix[len(matrix) - 1][col])
            else:
                minnumber = 0
            if(matrix[row][len(matrix[row]) - 1] > matrix[len(matrix) - 1][col]): #elinmate the col
                for k in costcopy:
                    for h in range(len(k)):
                        if( h == col):
                            k[h] = 999999999
            else: #elinmate the row
                for k in range(len(costcopy[row])):
                    costcopy[row][k] = 999999999
            costcopy = costcopy[:len(costcopy) - 1, :len(costcopy[0]) - 1]
            matrix[row][col] = minnumber
            matrix[row][len(matrix[row]) - 1] -= minnumber
            matrix[len(matrix) - 1][col] -= minnumber
        i += 1
    matrix = matrix[:len(matrix) - 1, :len(matrix[0]) - 1]
    matrix = np.concatenate((matrix, supply), axis=1)
    matrix = np.concatenate((matrix, demand), axis=0)
    printmatrix = [[0 for x in range(len(cost[0]) - 1)] for y in range(len(cost) - 1)]
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i]) - 1):
            if (matrix[i][j] == -1):
                printmatrix[i][j] = '-'
                matrix[i][j] = 0
            else:
                printmatrix[i][j] = matrix[i][j]
    print("Vogel's approximation result ('-' as nonbasic var): ")
    for i in printmatrix:
        print(i)
    print("Initialize matrix : ")
    print(matrix)
    return matrix

##solver function
##Takes in cost matrix, bool debug(Print steps if True),
##         optional string method = method of initialization (default:"nw" | "nw" ->northwest corner "vog" ->Vogel's)
##         optional matrix = custom initialized matrix
##return matrix of optimal assignment
def transportationSolve(cost, debug ,method = None, matrix = None):
    if(matrix == None):
        if(method == "vog"):
            matrix = vogel(cost)
        else:
            matrix = northwest(cost)
    return

##runit
transportationSolve(matrix,True)