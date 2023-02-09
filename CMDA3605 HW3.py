# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 16:53:42 2023

@author: Yihan Liu
"""

import numpy as np
import math
from pylab import *
import scipy.linalg as sl
import matplotlib.pyplot as plt

"""
def problem_4(iteration, A, x0):
    x = A @ x0
    for i in range(iteration):
        x = A @ x
        print(x)

    
x0 = np.array([1, 0])
A = np.array([[math.sqrt(2)/2, -math.sqrt(2)/2],
              [math.sqrt(2)/2, math.sqrt(2)/2]])

problem_4(10000, A, x0)
"""


"""
#Problem 3
C = np.array([[0, 0, 0.45],
              [0.25, 0, 0],
              [0, 0.65, 0.95]])
eig_value, v = np.linalg.eig(C)
print("The eigenvalue is: ", eig_value)
"""


"""
#Problem 5
C = np.array([[1, 2, 1],
              [-2, 2, 1],
              [2, -2, 5]])
eig_value, v = np.linalg.eig(C)
print("The eigenvalue is: ", eig_value)
"""




A = np.array([[3, 1],
              [2, -4]])

pval = np.arange(0, 1.1, 0.1)
k = len(A)
i = 0
 
def scaled(A,p):
    A = (p*(ones((2,2)) -eye(2)) +eye(2))*A
    return A
 
def gerschgorin(B):
    B = scaledA - diag(scaledA)*eye(k)
    radvec = zeros(k)
    for i in range(k):
        radvec[i] = sum(abs(B[i,:]))
    return radvec
 
for p in pval:
    scaledA = scaled(A,p)
    radius = gerschgorin(scaledA)
    fig,ax = plt.subplots()
 
    for i in range(k):
        circle = plt.Circle((A[i,i],0), radius[i], fill=False)
        ax.add_artist(circle)
 
    z = sl.eig(scaledA)[0]
    
    plt.axis('equal')
    plt.xlim(-8, 8)
    plt.ylim(-8, 8)
    plt.title('Gershgorin disks for A')
    plt.xlabel('eigenvalue real part')
    plt.ylabel('eigenvalue imaginary part')
    plt.show()
    plt.close()
    i+=1






             