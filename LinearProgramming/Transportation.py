import numpy as np
import heapq
from copy import copy, deepcopy
import networkx as nx
import matplotlib.pyplot as plt

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
##Takes in combine cost matrix, bool debug (print if true)
##return a tuple (combine initialize matrix, initialize string matrix)
def northwest(cost,debug):
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
    if(debug):
        print("Northwest corner result ('-' as nonbasic var): ")
        for i in printmatrix:
            print(i)
        print("Initialize matrix : ")
        print(matrix)
    return (matrix,printmatrix)


##Vogel's approx of initialization
##Takes in combine cost matrix, bool debug (print if true)
##return a tuple (combine initialize matrix, initialize string matrix)
def vogel(cost,debug):
    costcopy = deepcopy(cost)
    costcopy = costcopy[:len(costcopy) - 1, :len(costcopy[0]) - 1]
    matrix = np.array([[-1 for x in range(len(cost[0])-1)] for y in range(len(cost)-1)])
    supply = np.array([cost[:len(cost[0])-2,len(cost)]])
    supply = supply.transpose()
    demand = np.array([cost[len(cost)-1]])
    matrix = np.concatenate((matrix, supply), axis=1)
    matrix = np.concatenate((matrix, demand), axis=0)
    i = 0
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
    if(debug):
        print("Vogel's approximation result ('-' as nonbasic var): ")
        for i in printmatrix:
            print(i)
        print("Initialize matrix : ")
        print(matrix)
    return (matrix,printmatrix)

##solver function
##Takes in cost matrix, bool debug(Print steps if True),
##         optional string method = method of initialization (default:"nw" | "nw" ->northwest corner "vog" ->Vogel's)
##         optional matrix = custom initialized matrix/ printmatrix = custom initialized nested list with basicvar
##return matrix of optimal assignment
def transportationSolve(cost, debug ,method = None, matrix = None, printmatrix = None):
    if(matrix.any() == None or printmatrix == None):
        if(method == "nw"):
            a = northwest(cost,debug)
            matrix = a[0]
            printmatrix = a[1]
        else:
            a = vogel(cost,debug)
            matrix = a[0]
            printmatrix = a[1]
    count = 0
    while(True):
        count += 1
        ijmatrix = deepcopy(cost)
        subcost = cost[:len(cost)-1,:len(cost[0])-1]
        ##searching for Entering BV
        bvlist = []
        for i in printmatrix:
            bvlist.append(len(i) - i.count('-'))
        ijmatrix.fill(-1)
        interest = [(np.argmax(bvlist), 2)]
        ijmatrix[interest[0][0]][len(ijmatrix[0]) - 1] = 0
        while (len(interest) > 0):
            pt = interest[0][0]
            dir = interest[0][1]
            del interest[0]
            if (dir % 2 == 0):
                for j in range(len(ijmatrix[0]) - 1):
                    if (printmatrix[pt][j] != '-' and ijmatrix[len(ijmatrix) - 1][j] == -1):
                        ijmatrix[len(ijmatrix) - 1][j] = subcost[pt][j] - ijmatrix[pt][len(ijmatrix[0]) - 1]
                        interest.append((j, 1))
            else:
                for j in range(len(ijmatrix) - 1):
                    if (printmatrix[j][pt] != '-' and ijmatrix[j][len(ijmatrix[0]) - 1] == -1):
                        ijmatrix[j][len(ijmatrix[0]) - 1] = subcost[j][pt] - ijmatrix[len(ijmatrix) - 1][pt]
                        interest.append((j, 2))
        for i in range(len(ijmatrix) - 1):
            for j in range(len(ijmatrix[0]) - 1):
                if (printmatrix[i][j] == '-'):
                    ijmatrix[i][j] = subcost[i][j] - ijmatrix[i][len(ijmatrix[0]) - 1] - ijmatrix[len(ijmatrix) - 1][j]
                else:
                    ijmatrix[i][j] = 0
        subijmatrix = ijmatrix[:len(ijmatrix) - 1, :len(ijmatrix[0]) - 1]
        enterX = np.unravel_index(subijmatrix.argmin(), subijmatrix.shape)[0]
        enterY = np.unravel_index(subijmatrix.argmin(), subijmatrix.shape)[1]
        if(debug):
            print("Entering var is : x"+ str(enterX + 1) + "," + str(enterY + 1))
            print("Matrix for ui, vj is :")
            print(ijmatrix)
        if(subijmatrix[enterX][enterY] >= 0):
            break
        ##identifying loop
        matrix[np.unravel_index(subijmatrix.argmin(), subijmatrix.shape)[0]][np.unravel_index(subijmatrix.argmin(), subijmatrix.shape)[1]] = -1
        printmatrix[np.unravel_index(subijmatrix.argmin(), subijmatrix.shape)[0]][np.unravel_index(subijmatrix.argmin(), subijmatrix.shape)[1]] = '-1'
        if(debug):
            print("Matrix for iteration #" + str(count) + ", Entering Var is marked as '-1' :")
            for i in printmatrix:
                print(i)
        edgelist = []
        for i in range(len(printmatrix)):
            for j in range(len(printmatrix[0])):
                if(printmatrix[i][j] != '-'):
                    for col in range(len(printmatrix)):
                        if(printmatrix[col][j] != '-' and col != i and ((col,j),(i,j)) not in edgelist):
                            edgelist.append(((i,j),(col,j)))
                    for row in range(len(printmatrix[0])):
                        if(printmatrix[i][row] != '-' and row != j and ((i,row),(i,j)) not in edgelist):
                            edgelist.append(((i,j),(i,row)))
        G = nx.Graph(edgelist)
        cyclelist = (nx.cycle_basis(G, (enterX,enterY)))
        templist = []
        for i in cyclelist:
            if (len(i) % 2 == 0 and (enterX,enterY) in i):
                now = i.index((enterX, enterY))
                next = (now + 1) % len(i)
                dirlist = []
                while(i.index((enterX,enterY)) != next):
                    next = (now + 1) % len(i)
                    if(i[next][0] != i[now][0] and i[next][1] == i[now][1]):
                        dirlist.append(1)
                    elif(i[next][0] == i[now][0] and i[next][1] != i[now][1]):
                        dirlist.append(0)
                    else:
                        dirlist.append(-1)
                    now = next
                flag = True
                for j in range(len(dirlist)-1):
                    if(dirlist[j] == dirlist[j+1]):
                        flag = False
                if (-1 not in dirlist and flag):
                    templist.append(i)
        if(len(templist) == 0):
            break
        else:
            cycle = templist[0]
            if(debug):
                print("Cycle identified :")
                print(cycle)
            numberlist = [matrix[i[0]][i[1]] if matrix[i[0]][i[1]] != -1 else 0 for i in cycle]
            now = cycle.index((enterX, enterY))
            next = (now + 1) % len(cycle)
            flag = False
            minlist = []
            while (cycle.index((enterX, enterY)) != next):
                next = (now + 1) % len(cycle)
                if (flag):
                    minlist.append(numberlist[now])
                    flag = False
                else:
                    flag = True
                now = next
            now = cycle.index((enterX, enterY))
            next = (now + 1) % len(cycle)
            flag = False
            matrix[enterX][enterY] = 0
            while (cycle.index((enterX, enterY)) != next):
                next = (now + 1) % len(cycle)
                if (flag):
                    matrix[cycle[now][0]][cycle[now][1]] -= min(minlist)
                    flag = False
                else:
                    matrix[cycle[now][0]][cycle[now][1]] += min(minlist)
                    flag = True
                now = next
            exitX,exitY = 0,0
            for i in cycle:
                if(matrix[i[0]][i[1]] == 0):
                    exitX,exitY = i[0],i[1]
            if(debug):
                print("Leaving Var: x" + str(exitX+1) + "," +str(exitY + 1))
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if(i == exitX and j == exitY):
                        printmatrix[i][j] = '-'
                    elif(printmatrix[i][j] == '-'):
                        printmatrix[i][j] = '-'
                    else:
                        printmatrix[i][j] = str(matrix[i][j])
            if(debug):
                print("Matrix after iteration #" + str(count))
                for i in printmatrix:
                    print(i)
                print("------------------------------------------- \n")
        if(count > 4):
            break
    if(debug):
        print("Final Allocation :")
        print(matrix)
        sum = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                sum += matrix[i][j]*cost[i][j]
        print("Final Sum Z =:" + str(sum))
    return matrix

##runit
#example matrix,printmatrix input:
m = np.array([[0,0,40,0,10],[30,0,30,0,0],[0,20,0,30,0],[0,0,0,0,50]])
pm = [["-","-","40","-","10"],
      ["30","-","30","-","-"],
      ["0","20","-","30","-"],
      ["-","-","-","-","50"]]
transportationSolve(matrix,True,matrix = m,printmatrix=pm)
