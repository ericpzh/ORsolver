import numpy as np
from copy import copy, deepcopy

##Main input
matrix = np.array([[37.7,32.9,33.8,37,35.4],
                   [43.4, 33.1, 42.2, 34.7, 41.8],
                   [33.3, 28.5, 38.9, 30.4, 33.6],
                   [29.2, 26.4, 29.6, 28.5, 31.1]])

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
        print("After First Attempt :")
        print(matrix)

    assignment = deepcopy(matrix)
    assignmentls = []
    for i in range(len(assignment)):
        done = False
        for j in range(len(assignment)):
            if(list(assignment[j]).count(0) == 1):
                col = 0
                for x in range(len(assignment[0])):
                    if(assignment[j][x] == 0):
                        col = x
                assignmentls.append((j,col))
                for x in range(len(assignment)):
                    assignment[x][col] = -1
                for x in range(len(assignment[0])):
                    assignment[j][x] = -1
                done = True
                break
        if(not done):
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
                if(assignment[k][j] == 0):
                    count += 1
            if(count == 1):
                row = 0
                for x in range(len(assignment)):
                    if(assignment[x][j] == 0):
                        row = x
                assignmentls.append((row,j))
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
    if(sum(list(x).count(-1) for x in assignment) == len(matrix)*len(matrix[0])):
        if(debug):
            print("Assigns: ")
            print(assignmentls)
        return assignmentls
    else:
        print("Not yet implenmented")
        return assignmentls

##run it
HungarianSolve(matrix,True)