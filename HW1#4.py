# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 22:38:17 2023
CMDA 3605 HW1 #4
@author: Yihan Liu
"""

def logisticModel(M, gen, x0):
    """
    This function create a model of logistic growth to predict 
    the population.

    Parameters
    ----------
    M : The max population
    gen : Number of generation
    x0 : Initial Condition

    Returns
    -------
    Population at the desired generation.

    """
    x = x0
    for i in range(gen):
        x = x + 0.5*x - (0.5*x**2)/M
        print(x)
    
    
logisticModel(100, 15, 10)
print()
logisticModel(200, 15, 10)
