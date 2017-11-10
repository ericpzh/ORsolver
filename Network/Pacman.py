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