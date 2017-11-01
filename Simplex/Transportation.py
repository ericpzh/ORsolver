import numpy as np
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
  cost = np.array([[]])
  for i in range(len(cost)):
    for j in range(len(cost[i])):
      
##Vogel's approx of initialization
##Takes in combine cost matrix
##return a combine initialize matrix
def vogel(cost):
  
##solver function
##Takes in cost matrix, initialize matrix, bool debug(Print steps if True)
##return matrix of optimal assignment
def transportationSolve(cost,matrix,debug):
  
##runit
transportationSolve(northwest(matrix))
