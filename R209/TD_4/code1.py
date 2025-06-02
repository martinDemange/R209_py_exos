#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  7 13:33:55 2025

@author: d24012688
"""
#exo1.1
def Dichotomie(f,a,b,e): 
    fa = f(a)
    fb = f(b)
    c = (a + b ) / 2
    fc = f(c)
    iter = 0        # a iterator for knowig the number of the 
    # contion de fin
    while fb - fa > e :
        # si fonc croissante
        if fa < 0 and fb > 0 :                     
            if fc > 0 + e: 
                n,iter = Dichotomie(f, a, c, e)
                return n,iter+1
            elif fc < 0 - e : 
                n,iter = Dichotomie(f, c, b, e)
                return n,iter+1
            else :
                return c, iter+1
            
         # si fonc decroissante   
        elif fa > 0 and fb < 0 :                    
            if fc > 0 - e: 
                n,iter = Dichotomie(f, c, b, e)
                return n,iter+1
            elif fc < 0 + e : 
                n,iter = Dichotomie(f, a, c, e)
                return n,iter+1
            else :
                return c,iter
        # en cas d'erreur
        else:
            print("error")
        
# exo1.2
def fonc1(x):
    return x

print(Dichotomie(fonc1, -5, 100, 0.001))


