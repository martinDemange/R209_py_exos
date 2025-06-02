#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 22 11:00:22 2025

@author: d24012688
"""

import matplotlib.pyplot as plt
import numpy as np

#EXO2
# on a la fonction f(x) = x² avec x dans R

def f(x):
    return x*x

# il y a aussi sa derivé  

def f_derive(x):
    return 2*x

def val_absolue(val):
    if val >= 0 :
        return val
    else :
        return val * -1

# l'algo de gradien est def par une suite : Xk+1 = Xk - p*f_derive(Xk) pour tout k dans N
# Xo = 1
# p = 0.1
# on arrete l'algo quand ...
# on peu l'imite le nombre de boucle, mais il faut ajouter un message si le programme s'arrete a cause de ça


#                           brouillons 
#  assert( k < 100000), " nombre de tentative ( 100 000 ) depassé"

# while ( step < max_step) and (abs(f_derive(k)) >= 0):
#     result = k - p*f_derive(k)
#     k += 1
#     step += 1
# return result,step

x0 = 1
pas = 0.1
tol = 10**(-6)

def algo_gradien(f, f_derive,x,pas,tol):
    nmax = 1000
    n = 0
    list_iter = [x]
    while  (abs(f_derive(x)) >= tol) and n < nmax:
        xold = x
        x = xold - pas * f_derive(xold)
        list_iter.append(x)
        n += 1
        if (n==nmax) :
            print("nombre de tentative ( ",nmax," ) depassé ")
            return list_iter,n
        else :
            return list_iter,n

# calling section : 
liste_iter, n = algo_gradien(f, f_derive, x0, pas, tol)
print("le resultat est : ",algo_gradien(f,f_derive,x0,pas,tol))

x_trace = np.linspace(-1.5,1.5, 1000)
plt.figure(figsize=(8,8))
plt.plot(x_trace, f(x_trace))

liste_trace = np.array(liste_iter)
plt.plot(liste_trace, f(liste_trace),marker='*',color='red')
plt.rcParams['text.usetext'] = True
plt.title("Itere de l'algorithme de descente de gradient à pas constant"+r'$\rho =$' + str(pas))
plt.show

# EXO3