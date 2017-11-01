import numpy as np
from copy import copy, deepcopy
'''
In progress solver for transportation problem
'''
##Main input
##input costs,supply,demand of a transportation matrix
## [Cost] [Supply]
##[Demand]
cost = np.array([
  [16,16,13,22,17],
  [14,14,13,19,15],
  [19,19,20,23,99],
  [99,0,99,0,0]
])
supply = np.array([
  [50],
  [60],
  [50],
  [50]
])
demand = np.array([[30,20,70,30,60]])
##concatenate the matrix together
demand = np.concatenate((demand,[0]),axis=1)
matrix = np.concatenate((cost,supply),axis=1)
matrix = np.concatenate((matrix,demand),axis=0)
##Northwest corner rule of initialization
##Takes in combine cost matrix
##return a combine initialize matrix
def northwest(cost):
  matrix = deepcopy(cost)
  for i in range(len(cost)):
    for j in range(len(cost[i])):
      minnumber = min(cost[i][len(cost[i])-1],cost[len(cost)-1][j])
      matrix[i][j] = minnumber
      if(cost[i][len(cost[i])-1] <= cost[len(cost)-1][j]):
        for k in range(j,len(cost[i])):
          matrix[i][k] = "--"
        i += 1
      else:
        for k in range(i,len(cost):
          matrix[k][j] = "|"
        j += 1
      matrix[i][len(cost[i])-1] -= minnumber
      matrix[len(cost)-1][j] -= minnumber               
  return matrix
      
##Vogel's approx of initialization
##Takes in combine cost matrix
##return a combine initialize matrix
def vogel(cost):
  matrix = deepcopy(cost)
  penaltycol, penaltyrow = [],[]
  int i = 0
  while(i < (len(cost)-1+len(cost[0])-1-1)):
    for i in range(len(cost)):
      penaltycol.append(np.amin(cost[cost != np.amin(cost[i]) and cost != cost[i][len(cost)-1]])
    for j in range(len(cost[0])):
      penaltyrow.append()
                       
  
##solver function
##Takes in cost matrix, initialize matrix, bool debug(Print steps if True)
##return matrix of optimal assignment
def transportationSolve(cost,matrix,debug):
  
##runit
transportationSolve(northwest(matrix))
