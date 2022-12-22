#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 12:41:40 2022

@author: loumbi
"""

import numpy as np 
import matplotlib.pyplot as plt 
import random as rd

#Initialisation: les paramètre de l'algorithme du recuit simulé 

N=30
T0=15
T=T0
#Tmin=1e-2
Tmin=9
tau=1e2
beta=1e-1
k=0
t=0

# Calcul de la fonction cout
def fonction_cout():
    global chemin
    energie=0.0
    xy=np.column_stack((x[chemin],y[chemin]))
    energie=np.sum(np.sqrt(np.sum((xy-np.roll(xy,-1,axis=0))**2,axis=1)))
    return energie

# Fonction de déplacement dans le chemin
def Deplacement(ville1, ville2):
    global chemin
    Min=min(ville1, ville2)
    Max=max(ville1, ville2)
    chemin[Min:Max]=chemin[Min:Max].copy()[::-1]
    return

# Choix des coordonnées des points villes
x=np.random.uniform(0, 1, N)
y=np.random.uniform(0, 1, N)

# Choix du chemin initial
chemin=np.arange(N)
chemin1=chemin.copy()

# Calcul de la distance du chemin initiale
cout_courant=fonction_cout()

print('k= ', k, 'Chemin Hamiltonien: ' , chemin, 'Distance du chemin= ', cout_courant, 'Temperature',T)

#La boucle du processuce iteratif du recuit simulé

while T>Tmin:
    ville_voisine=rd.randint(0, N-1)
    ville_courante=rd.randint(0, N-1)
    if ville_voisine==ville_courante: continue

    #Deplacement
    Deplacement(ville_voisine, ville_courante)
    #calcul de la distance ou cout 
    cout_nouveau=fonction_cout()
    
    if cout_nouveau<=cout_courant:
        cout_courant=cout_nouveau
    else: #critère de metropolis
        dE=cout_nouveau-cout_courant
        #beta=rd.uniform(0, 1)
        if beta>np.exp(-dE/T):
            Deplacement(ville_voisine, ville_courante) #La nouvelle solution(chemin) est rejeté
        else:
            cout_courant=cout_nouveau #On accepte la nouvelle solution
        
        
        #Abaisser la température ======> Refroidissement 
        t+=1
        T=T0*np.exp(-t/tau)
        k+=1
print('k= ', k, 'Chemin Hamiltonien: ' , chemin, 'Distance du chemin= ', cout_courant, 'Temperature',T)
        
        #fin de hamilton 
        
print('          Résultat Final                                     ')
        #print('Chemin Hamiltonien Initial: ',chemin1, 'Distance du chemin initial = ', d1, 'Temperature Initiale ', T0)
print('Chemin Hamiltonien Optimal: ',chemin, 'Distance du chemin optimal = ', cout_courant, 'Temperature Finale ', T)
        
plt.plot(x[chemin1], y[chemin1], marker='o', color='g')
        
        
        


    