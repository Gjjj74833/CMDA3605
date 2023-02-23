import numpy as np
"""
Created on Wed Feb 22 18:20:31 2023

@author: Yihan Liu
"""

def power_method_markov(A, v, epsilon, MAX_ITERS = 100):
    x = v/np.linalg.norm(v, ord = 1)
    theta_old = (x @ A @ x) / (np.inner(x,x))
    for i in range(MAX_ITERS):
        x = A@x
        theta_new = (x @ A @ x) / (np.inner(x,x))
        if np.abs(theta_new-theta_old) < epsilon:
            return x, theta_new, i #eigenvec, eigenval, iterations
        theta_old = theta_new
    return False

M = np.array([[0,1/2,0,0,1/2,1/4],
              [1/3,0,0,1/2,1/2,1/4],
              [1/3,0,0,0,0,1/4],
              [1/3,0,1/2,0,0,1/4],
              [0,1/2,0,1/2,0,0],
              [0,0,1/2,0,0,0]])

B = 1/6*np.outer(np.ones(6),np.ones(6))

p = .9
A = p*M+(1-p)*B
#print(power_method_markov(A, np.ones(6), .00001))

A = np.array([[1,0,.5,0],
              [0,1,0,.5],
              [0,0,.5,0],
              [0,0,0,.5]
              ])
print(power_method_markov(A, np.ones(4), .0000000001))



