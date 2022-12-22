#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 17:05:48 2022

@author: Mouctar
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import matplotlib as mpl
import math
import random

x1=np.random.random()
x2=np.random.random()
x3=np.random.random()
w=1
nbitermax=200
V1=0
V2=0
V3=0
p1=5
p2=10
p3=7
nbiter=1

pg=np.random.randint(4)

def fonc(x):
    return (x-1)**2*(x-8)**2
#Vecteurs reoprésentant l'évolution des solutions des 3 particules
X1=[]
X2=[] 
X3=[] #vecteur vide
pg0=4 #solution globale initiale
sortie = 0
epsilon = 10**(-10)
while nbiter<nbitermax and sortie == 0:
    b1=np.random.random()
    b2=np.random.random()
    if fonc(x1)<fonc(x2) and fonc(x1)<fonc(x3):
        pg=x1
    if fonc(x2)<fonc(x1) and fonc(x2)<fonc(x3):
        pg=x2
    if fonc(x3)<fonc(x1) and fonc(x3)<fonc(x2):
        pg=x3
    #Nouvelle vitesse de la particule 1
    V1=w*V1+b1*(p1-x1)+b2*(pg-x1)
    if fonc(x1)<fonc(x1+V1):
       p1=x1
    else:
       p1=(x1+V1)
    if abs(pg0-pg)<epsilon:
        sortie =1
    pg0=pg
    x1=x1+V1
    #Nouvelle vitesse de la particule 2
    V2=w*V2+b1*(p2-x2)+b2*(pg-x2)
    if fonc(x2)<fonc(x2+V2):
       p2=x2
    else:
       p2=(x2+V2)
    x2=x2+V2
    #Nouvelle vitesse de la particule 3
    V3=w*V3+b1*(p3-x3)+b2*(pg-x3)
    if fonc(x3)<fonc(x3+V3):
       p3=x3
    else:
       p3=(x3+V3)
    x3=x3+V3
    nbiter=nbiter+1
    X1=[X1, x1]
    X2=[X2, x2]
    X3=[X3, x3]
    #B1=[B1, b1]
    #B2=[B2, b2]
print(pg)