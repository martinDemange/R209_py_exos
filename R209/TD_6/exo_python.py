#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 22 14:14:33 2025

@author: DEMANGE Martin
"""

# EXO2

# X = [1,2,3]
# Li ou i est l'indice du tableau X
# x est le param en parentthese comme : Li (x)
# L1 (1) = 1        L2 (1) = 0      L3 (1) = 0
# L1 (2) = 0        L2 (2) = 1      L3 (2) = 0
# L1 (3) = 0        L2 (3) = 0      L3 (3) = 1

def Lagrange_Elementaire(X,i,x):
    result = 1
    for j in range(0,len(X)):
        if i==j:
            continue
        result *= (x-X[j]) / (X[i] - X[j])
    
    return result

# section d'affichage :
#print(Lagrange_Elementaire([1,2,3,4,5,6], 3, 4))

# ////////////////////////////////////////////////////////////////////////////

# Y liste des resultat, exemple dans exo 1 Y[1,4,9]

def Lagrange(X,Y,x) :
    result = 1
    for i in range(len(X)):
        result += Y[i] * Lagrange(X, i, x)    
    return result

print(Lagrange([1,2,3], [1,4,9], 2))