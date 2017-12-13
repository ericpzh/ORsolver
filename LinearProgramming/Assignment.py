import numpy as np
from copy import copy, deepcopy

##Main input
matrix = np.array([[37.7,32.9,33.8,37,35.4],
                   [43.4, 33.1, 42.2, 34.7, 41.8],
                   [33.3, 28.5, 38.9, 30.4, 33.6],
                   [29.2, 26.4, 29.6, 28.5, 31.1]])


##Helper function of making assignment
##Takes in: np array() matrix
##return:   tuple(np.array() assignment,assignmentls)
def Assign(matrix):
    assignment = deepcopy(matrix)
    assignmentls = []
    for i in range(len(assignment)):
        done = False
        for j in range(len(assignment)):
            if (list(assignment[j]).count(0) == 1):
                col = 0
                for x in range(len(assignment[0])):
                    if (assignment[j][x] == 0):
                        col = x
                assignmentls.append((j, col))
                for x in range(len(assignment)):
                    assignment[x][col] = -1
                for x in range(len(assignment[0])):
                    assignment[j][x] = -1
                done = True
                break
        if (not done):
            for j in range(len(assignment)):
                count = 0
                for k in range(len(assignment[0])):
                    if (assignment[j][k] == 0):
                        count += 1
                if (count > 0):
                    col = 0
                    for x in range(len(assignment[0])):
                        if (assignment[j][x] == 0):
                            col = x
                    assignmentls.append((j, col))
                    for x in range(len(assignment)):
                        assignment[x][col] = -1
                    for x in range(len(assignment[0])):
                        assignment[j][x] = -1
                    break
    for i in range(len(assignment[0])):
        done = False
        for j in range(len(assignment[0])):
            count = 0
            for k in range(len(assignment)):
                if (assignment[k][j] == 0):
                    count += 1
            if (count == 1):
                row = 0
                for x in range(len(assignment)):
                    if (assignment[x][j] == 0):
                        row = x
                assignmentls.append((row, j))
                for x in range(len(assignment)):
                    assignment[x][j] = -1
                for x in range(len(assignment[0])):
                    assignment[row][x] = -1
                done = True
                break
        if (not done):
            for j in range(len(assignment[0])):
                count = 0
                for k in range(len(assignment)):
                    if (assignment[k][j] == 0):
                        count += 1
                if (count > 0):
                    row = 0
                    for x in range(len(assignment)):
                        if (assignment[x][j] == 0):
                            row = x
                    assignmentls.append((row, j))
                    for x in range(len(assignment)):
                        assignment[x][j] = -1
                    for x in range(len(assignment[0])):
                        assignment[row][x] = -1
                    break
    return  (assignment,assignmentls)


##Hungarian Solve
##Takes in: np array() orimatrix, bool debug (print if true)
##return:   np.array() assignment
def HungarianSolve(orimatrix,debug):
    matrix = deepcopy(orimatrix)
    if(len(matrix) > len(matrix[0])):
        zero = []
        for i in range(len(matrix)):
            zero.append([0])
        for i in range(len(matrix - len(matrix[0]))):
            matrix = np.concatenate((matrix, zero), axis=1)
    elif(len(matrix) < len(matrix[0])):
        zero = [[]]
        for i in range(len(matrix[0])):
            zero[0].append(0)
        for i in range(len(matrix[0]) - len(matrix) ):
            matrix = np.concatenate((matrix, zero), axis=0)
    if(debug):
        print("After Balancing the Matrix :")
        print(matrix)

    matrix -= matrix.min(axis=0)
    for i in range(len(matrix)):
        mini = min(matrix[i])
        for j in range(len(matrix[i])):
            matrix[i][j] -= mini
    if (debug):
        print("After reducing attempt :")
        print(matrix)

    assignment = Assign(matrix)[0]
    assignmentls =  Assign(matrix)[1]
    count = 1
    while(len(assignmentls) < len(matrix)-1):
        count += 1
        matrixcopy = []
        for i in range(len(assignment)):
            matrixcopy.append([])
            for j in range(len(assignment[0])):
                if(assignment[i][j] == -1):
                    matrixcopy[i].append("-")
                else:
                    matrixcopy[i].append(str(assignment[i][j]))
        for i in range(len(matrixcopy)):
            if(matrixcopy[i][0] != "-"):
                matrixcopy[i].append("x")
            else:
                matrixcopy[i].append("o")
        matrixcopy.append([])
        for i in range(len(matrixcopy[0])-1):
            flag = False
            for j in range(len(matrix)):
                if(matrix[j][i] == 0 and matrixcopy[j][len(matrixcopy[0])-1] == "x"):
                    flag = True
            if(flag):
                matrixcopy[len(matrixcopy) - 1].append("x")
            else:
                matrixcopy[len(matrixcopy) - 1].append("o")
        for i in range(len(matrixcopy[0])-1):
            for j in range(len(matrixcopy)-1):
                if(matrixcopy[len(matrixcopy)-1][i] == "x" and (j,i) in assignmentls):
                    matrixcopy[j][len(matrixcopy[0])-1] = "x"
        if(debug):
            print("After marking all rows/cols :" + "(Line thru 'o' Col and 'x' Row covers all zeros)")
            for i in matrixcopy:
                print(i)
        theta = 9999999999
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(matrixcopy[i][len(matrix[0])] == "x" and matrixcopy[len(matrix)][j] == "o" and matrix[i][j] < theta):
                    theta = matrix[i][j]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(matrixcopy[i][len(matrix[0])] == "x" and matrixcopy[len(matrix)][j] == "o"):
                    matrix[i][j] -= theta
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(matrixcopy[i][len(matrix[0])] == "o" and matrixcopy[len(matrix)][j] == "x"):
                    matrix[i][j] += theta
        if (debug):
            print("After #" + str(count) + " attempt :")
            print(matrix)
            print("------------------------------------------- \n")
        assignment = Assign(matrix)[0]
        assignmentls = Assign(matrix)[1]
    for i in range(len(assignment)):
        for j in range(len(assignment[0])):
            if(assignment[i][j] != -1):
                assignmentls.append((i,j))
    printmatrix = []
    for i in range(len(orimatrix)):
        printmatrix.append([])
        for j in range(len(orimatrix[0])):
            if(i < len(orimatrix) and j < len(orimatrix[0]) and (i,j) in assignmentls):
                printmatrix[i].append("*")
            else:
                printmatrix[i].append(str(orimatrix[i][j]))
    if (debug):
        print("Original Matrix :" )
        print(orimatrix)
        print("Assigns: ")
        print(assignmentls)
        print("Result :")
        for i in printmatrix:
            print(i)
    return assignmentls

##run it
HungarianSolve(matrix,True)