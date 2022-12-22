#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 15:28:04 2022

@author: Mouctar
"""

import numpy as np
from random import *
from math import exp
# Choix de la solution initiale

x=np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 0])

T=20 # Temp´eture initiale
# Remplir la matrice d’adjacence (sommet-sommet) repr´esentant le graphe
M =[
   [0,3,2,3,4,4,6,1,7],
   [3,0,5,4,3,6,1,9,2],
   [2,5,8,1,6,1,9,3,7],
   [3,4,1,8,5,9,7,2,1],
   [4,3,6,5,0,9,1,2,1],
   [4,6,1,9,9,0,2,1,7],
   [6,1,9,7,1,2,0,4,5],
   [1,9,3,2,2,1,4,0,7],
   [7,2,7,1,1,7,5,7,0]
   ]
# La meilleure solution initialis´ee `a la solution initiale x
xbest=np.copy(x)
n=40 # nombre d’it´eration pour la m^eme temp´erature
while T>0.1:
    RepetitionTfixe=0
    while RepetitionTfixe<n:
        y=np.copy(x)
        distx=0
        for i in range(9):
            #print(i)
            distx=distx+M[x[i]][x[i+1]]
#choix al´eatoire des deux sommets `a permuter
        r1 = randint(1,8)
        r2 = randint(1,8)
        while r1==r2:
            r1 = randint(1,8)#r1 prend une valuer entre exclu 1 à 9
            r2 = randint(1,8)
        temp=y[r1]
        y[r1]=y[r2]
        y[r2]=temp
        disty=0
        for i in range(9):
            disty=disty+M[y[i]][y[i+1]]
        Delta = disty-distx
#si y est meilleure que x, copier y dans x
        if Delta<0:
            x=np.copy(y)
            distbest=0
            for i in range(9):
                distbest=distbest+M[xbest[i]][xbest[i+1]]
            alpha=distbest-disty;
            if alpha>0:
                xbest=np.copy(y)
                distbest=disty
        else:
            p=random(); # on tire al´eatoirement p entre 0
            if p < exp(-Delta/T): #crit`ere de metropolis
                x=np.copy(y)
        RepetitionTfixe=RepetitionTfixe+1
    T=T*0.99
    print('!!=======! Solution !========!!')
    print('xbest=',xbest)
    print('distbest=',distbest)
