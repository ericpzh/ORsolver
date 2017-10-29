import numpy as np
from Main import simplexSolve

'''
- - - - - - - -
- - - - - - - -
- j k - m - - p
i - - l - n o -
- B - D - F - H
A - C - E - G -
- - - - - - - -
- - - - - - - -
'''
M = -10000 ##nope
F = 50 ##move forward
N = -100 ##nooo
E = 200 #free take
T = 100 #trade
payoffMatrix = np.array([
#i1  i2  i3  j1  j2  j3  k1  k2  k3  l1  l2  l3  m1  m2  m3  n1  n2  n3  o1  o2  o3  p1  p2  p3
[M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M], #A1
[F,  N,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F], #A2
[M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M], #A3
[E,  E,  E,  E,  E,  T,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E], #B1
[F,  F,  F,  F,  N,  F,  F,  F,  N,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F], #B2
[F,  F,  F,  N,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F], #B3
[M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M], #C1
[F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  N,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F], #C2
[M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M], #C3
[F,  F,  F,  N,  F,  F,  F,  N,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F], #D1
[E,  E,  E,  E,  E,  E,  T,  E,  E,  E,  E,  E,  E,  E,  T,  E,  E,  E,  E,  E,  E,  E,  E,  E], #D2
[F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  N,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F], #D3
[M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M], #E1
[F,  F,  F,  F,  F,  F,  F,  F,  F,  N,  F,  F,  F,  F,  F,  F,  F,  N,  F,  F,  F,  F,  F,  F], #E2
[M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M], #E3
[F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  N,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F], #F1
[E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  T,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E], #F2
[E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  T], #F3
[M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M], #G1
[F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  N,  F,  F,  F,  N,  F,  F,  F,  F], #G2
[M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M], #G3
[E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  E,  T], #H1
[F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  F,  N,  F], #H2
[M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M,  M] #H3
])
##build CT,A,b from payoff matrix
CTarr = [[]]
tempA = [[]]
tempb = [[]]
for i in range(len(payoffMatrix[0])):
    CTarr[0].append(0)
    tempA[0].append(1)
    tempb[0].append(0)
CTarr[0].insert(0,1)
CT = np.array(CTarr)
tempA = np.transpose(np.array(tempA))
A = np.transpose(payoffMatrix)*-1
A = np.concatenate((tempA,A),axis=1)
tempA = [[0]]
for i in range(len(payoffMatrix)):
    tempA[0].append(1)
A = np.concatenate((A,tempA),axis=0)
tempb[0].append(1)
b = np.transpose(np.array(tempb))
##solve

simplexSolve(CT,A,b,False)
print(A)
print(CT)
print(b)