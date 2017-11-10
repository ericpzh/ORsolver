import numpy as np
import networkx as nx
import Network
'''
----------------------------------------
-oooooooooooooooooooooooooooooooooooooo-
-o----o----o----o-----o----o----o-----o-
-o----oooooo----o-----oooooo----o-----o-
-oooooo----o----ooooooo----o----ooooooo-
-o----o----oooooo-----o----oooooo-----o-
-o----oooooo----o-----oo>ooo----o-----o-
-o----o----o----o-----o----o----o-----o-
-oooooooooooooooooooooooooooooooooooooo-
----------------------------------------
'''
##Move function to calculate next move
##Takes in 2d-array:broad int:count number of remaining o
##return tuple (2d-array:broad , int:count number of remaining o)
def Move(borad,count):
    #search for '>'
    x,y,d = 0,0,1
    for i in range(len(borad)):
        for j in range(len(borad[i])):
            if(borad[i][j] == '>'):
                x,y,d = i,j,-1
                i,j = len(borad),len(borad[0])
            elif(borad[i][j] == '<'):
                x,y,d = i,j,1
                i, j = len(borad), len(borad[0])
    #next move
    borad[x][y] = ' '
    if(borad[x+1][y] == 'o'):
        borad[x + 1][y] = '<'
        count -= 1
    elif(borad[x-1][y] == 'o'):
        borad[x - 1][y] = '>'
        count -= 1
    elif(borad[x][y+1] == 'o'):
        borad[x][y + 1] = '>'
        count -= 1
    elif(borad[x][y-1] == 'o'):
        borad[x][y - 1] = '>'
        count -= 1
    else:
        count -= 0
    return (borad,count)

##Main function
##Take in string:path file location
##return nothing
def Pacman(path):
    #load text
    count = 0
    broad = [[]]
    with open(path) as f:
        content = list(f.read())
    j = 0
    for i in content:
        if(i == '\n'):
            broad.append([])
            j += 1
        else:
            broad[j].append(i)
            if(broad[j] == 'o'):
                count += 1
    # print
    for i in broad:
        print(*i)
    while(count > 0):
        (broad,count) = Move(broad,count)
        #print
        for i in broad:
            print(*i)

##runit
Pacman('broad.txt')