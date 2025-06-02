#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  2 13:33:40 2025

@author: d24012688
"""
import matplotlib.pyplot as plt
import numpy as np

a = 2
b = 10

def puissance(x,n) :
    if n==1 :
        return x
        #print(x)
    else  :
        return x*puissance(x,n-1)
        #print(x*puissance(x, n-1))

#print (puissance(a,b))
#puissance(x, n)



def puissance_dichotonomie(x,n) :
    if n==1 :
        return x,0
    elif n%2==0 :
        z, m = puissance_dichotonomie(x, n/2)
        return z*z, m+1
    else :
        z, m = puissance_dichotonomie(x, (n-1)/2)
        return x*z*z, m+2

#print(puissance_dichotonomie(a, b))

listMult   = [0]
list02     = [0] # x -> log2(x)
list03     = [0] # x -> 2(log2(x))
#dans cette liste x=2
for i in range(1,2099) :
    listMult.append( puissance_dichotonomie(2, i)[1] )
    
    list02.append( np.floor(np.log2(i)) )
    list03.append( 2*np.floor(np.log2(i)) )
    
    #list02.append( np.log2(i) )
    #list03.append( 2*(np.log2(i)) )
    

#print(listMult)

plt.plot( listMult )

#plt.plot( np.floor(list02) )
#plt.plot( np.floor(list03) )

plt.plot( list02 )
plt.plot( list03 )
plt.show()