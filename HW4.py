# -*- coding: utf-8 -*-
import numpy as np
import math
"""
Created on Thu Feb 16 12:50:11 2023
CMDA 3605 HW4

@author: Yihan Liu
"""

#4
def power_method(A, v, epsilon, MAX_ITERS = 100):
    x = v/np.linalg.norm(v)
    theta_old = np.linalg.norm(A@x)
    for i in range(MAX_ITERS):
        x = A@x/np.linalg.norm(A@x)
        theta_new = np.linalg.norm(A@x)

        if np.abs(theta_new-theta_old) < epsilon:
            return x, (A@x)[0]/x[0], i #eigenvec, eigenval, iterations
        theta_old = theta_new
    return False

A = np.array([[-4,1,1],
              [2,-10,1],
              [3,-4,8]])

#print(power_method(A, np.array([1,1,1]), .01))
#print(np.linalg.eig(A))

def si_power_method(A, v, epsilon, mu = 0, MAX_ITERS = 100):
    B = np.linalg.inv(A-mu*np.identity(len(v)))
    x = v/np.linalg.norm(v)
    theta_old = x @ B @ x
    for i in range(MAX_ITERS):
        x = B@x/np.linalg.norm(B@x)
        theta_new = x @ B @ x  
        if np.abs(theta_new-theta_old) < epsilon:
            return x, 1/theta_new+mu , i #eigenvec, eigenval, iterations
        theta_old = theta_new
    return False

#print(si_power_method(A,np.ones(3),.01,10,1000))
#print(si_power_method(A,np.ones(3),.01,-4,1000))

def power_method_v3(A, v, epsilon, MAX_ITERS = 100):
    x = v/np.linalg.norm(v)
    theta_old = x @ A @ x
    for i in range(MAX_ITERS):
        x = A@x/np.linalg.norm(A@x)
        theta_new = x @ A @ x #change this
        if np.abs(theta_new-theta_old) < epsilon:
            return x, theta_new, i #eigenvec, eigenval, iterations
        theta_old = theta_new
    return False


A = np.array([[1,0,0],
              [0,-1,0],
              [0,0,.5]])

print(power_method_v3(A, np.array([1,1,0]), .001, 9000))
print(np.linalg.eig(A))









