import numpy as np
from math import exp
import random

def f(ordre_ville):
    # Matrice qui contient les "distances"
    matrice_deplacement = np.array([[0, 6, 6, 1, 4], [6, 0, 8, 3, 5], [6, 8, 0, 6, 4], [1, 3, 6, 0, 2], [4, 5, 4, 2, 0]])

    # On calcule la distance en fonction de l ordre des villes
    distance = 0
    for k in range(len(ordre_ville) - 1):
        distance = distance + matrice_deplacement[ordre_ville[k] - 1][ordre_ville[k+1] - 1]
    return distance

def realiser_permutation(X_non_permute):
    # Initialisation de Y (variable locale X_permute)
    X_permute = []
    for noeud in X_non_permute:
        X_permute.append(noeud)

    # Realisation de la permutation
    permutation1 = np.random.randint(1, 5)
    permutation2 = np.random.randint(1, 5)

    # On s'assure de ne pas prendre 2 fois la meme position
    while permutation2 == permutation1:
        permutation2 = np.random.randint(1, 5)
    tmp = X_permute[permutation1]
    X_permute[permutation1] = X_permute[permutation2]
    X_permute[permutation2] = tmp


    return X_permute


X=[1,2,3,4,5,1]
Xbest = X
Fxbest = f(Xbest)

Tinit = 30
T = Tinit    # Tinitiale
Tf = 0
N = 1 # 2 parmi 4 valeurs (nombres de permutations possibles)


while T > Tf:
    i = 0
    while i < N:
        Y = realiser_permutation(X)

        deltaF = f(Y) - f(X)
        if deltaF < 0:
            X = Y
            if f(X) < f(Xbest):
                Xbest = X
                Fxbest = f(Xbest)

        else:
            p = random.uniform(0, 1)
            if p < exp(-deltaF/T):
                X = Y
        i = i + 1
    T = T - 0.001

print(Xbest)
print(f(Xbest))



