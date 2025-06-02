#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 28 13:35:28 2025

@author: DEMANGE Martin
"""

import numpy as np

# /////////////////////////////////////////////////////////////////////////////
# EXO2.1
# X is the name of the array
def norme(X) :
    somme = 0
    for i in X :
        somme += i**2
    return np.sqrt(somme)

# /////////////////////////////////////////////////////////////////////////////
# EXO2.2

# M is the matrix
# e is the precision ( 10e-6 for exemple )
def power_iterate(M, e) :
    # X0 will be init randomly, X is the vector in the matrix M ( a matrix is a
    # array of array ) and so X0 is a array of the same lenght of M
    
    # counter is used for knowing the number of iteration
    counter = 0 
    X0 = np.array(np.random.randint(1,10))
    for _ in range (len(M)-1) : 
        np.append(X0,np.random.randint(1,10))

    newX = X0
    
    while 1 :
        # dot allow the multiplication of array by array
        newX = np.dot(M, X0) / norme(np.dot(M, X0))
        ++counter
        if (newX - X0).all() <= e :
            break
        X0 = newX
    ###########################
    return newX, norme(np.dot(M,X0)), counter

C = np.array([[2,3],[1,0]])


print(power_iterate(C, 10e-6))