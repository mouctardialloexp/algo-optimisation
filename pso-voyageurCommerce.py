import random as rand
import numpy as np
import math

def fonc(A):
    sommDist = 0
    for i in range(len(A) - 1):
        sommDist += distance[A[i]-1][A[i+1]-1]
    return sommDist

def isVitesse(vector):
    if type(vector[0]) == tuple:
        return True
    else:
        return False

def addVitesse(op1, op2):
    result = []
    if isVitesse(op1) and isVitesse(op2):
        for i in range(len(op1)):
            result.append(op1[i])
        for i in range(len(op2)):
            result.append(op2[i])
    elif isVitesse(op2):
        for i in op1:
            result.append(i)
        for i in range(len(op2)):
            temp = result[op2[i][0]-1]
            result[op2[i][0]-1] = result[op2[i][1]-1]
            result[op2[i][1]-1] = temp
    return result

def mulVitesse(k, vit):
    if k > 0 and k < 1:
        k = math.floor(k * len(vit))
        for i in range(k):
            vit.pop()
            if len(vit) == 0:
                break
        if len(vit) == 0:
            vit.append((1,1))
    else:
        if type(k) == int:
            for i in range (k - 1):
                vit = addVitesse(vit, vit)
        else:
            if k > 1:
                k = int(k)
                for i in range (k - 1):
                    vit = addVitesse(vit, vit)
            else:
                if k < 1:
                    k = -k
                    k = int(k)
                    for i in range (k - 1):
                        vit = addVitesse(vit, vit)
    
    return vit

def subVitesse(X1, X2):
    vitesse = []
    X1prime = []
    for val in X1:
        X1prime.append(val) 
    for i in range(len(X1)):
        if X1prime[i] != X2[i]:
            j = X2.index(X1prime[i])
            V = (i+1 , j+1)
            temp = X1prime[i]
            X1prime[i] = X1prime[j]
            X1prime[j] = temp
            vitesse.append(V)
    if len(vitesse) == 0:
        vitesse.append((1,1))
    return vitesse



distance = np.array([[0, 1, 1, 3, 4, 5, 6, 1, 7],
                    [1, 0, 5, 4, 3, 6, 1, 9, 2],
                    [2, 5, 0, 1, 6, 1, 9, 3, 7],
                    [3, 4, 1, 0, 5, 9, 7, 2, 1],
                    [4, 3, 6, 5, 0, 9, 1, 2, 1],
                    [5, 6, 1, 9, 9, 0, 2, 1, 7],
                    [6, 1, 9, 7, 1, 2, 0, 4, 5],
                    [1, 9, 3, 2, 2, 1, 4, 0, 7],
                    [7, 2, 7, 1, 1, 7, 5, 7, 0]])
ville = [2, 3, 4, 5, 6, 7, 8, 9]
depart = [1]
rand.shuffle(ville)
x1 = []
x1.append(depart[0]) 
for i in ville:
    x1.append(i)
x1.append(depart[0])
rand.shuffle(ville)
x2 = []
x2.append(depart[0]) 
for i in ville:
    x2.append(i)
x2.append(depart[0])
rand.shuffle(ville)
x3 = []
x3.append(depart[0]) 
for i in ville:
    x3.append(i)
x3.append(depart[0])
w=1
nbitermax=200
V1 = [(1, 1)]
V2= [(1, 1)]
V3 = [(1, 1)]
p1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
p2=[1, 2, 4, 3, 5, 6, 7, 8, 9, 1]
p3=[1, 5, 4, 3, 2, 6, 7, 8, 9, 1]
nbiter=1
#Vecteurs reoprésentant l'évolution des solutions des 3 particules
X1 = [] 
X2 = [] 
X3=[] # vecteur vide
pg0=[1, 2, 3, 4, 5, 6, 7, 8, 9, 1] # solution globale initiale
sortie = 0
epsilon = 10*[0]

while nbiter<nbitermax and sortie == 0 :
    b1=rand.random()
    b2=rand.random()
    pg=[]
    if fonc(x1)<fonc(x2) and fonc(x1)<fonc(x3):
        for i in x1:
            pg.append(i)
    elif fonc(x2)<fonc(x1) and fonc(x2)<fonc(x3):
        for i in x2:
            pg.append(i)
    else:
        for i in x3:
            pg.append(i)

    #Nouvelle vitesse de la particule 1
    V1 = addVitesse(mulVitesse(w, V1), mulVitesse(b1, subVitesse(p1, x1)))
    V1 = addVitesse(V1, mulVitesse(b2, subVitesse(pg, x1)))
    if fonc(x1)<fonc(addVitesse(x1, V1)):
       for i in range(len(x1)):
            p1[i] = x1[i]
    else:
       p1=addVitesse(x1, V1)

    diff = 10*[0]
    for i in range(len(pg0)):
        diff[i] == abs(pg0[i]-pg[i])
        epsilon[i] = 10^(-10)
    if diff == epsilon:
        sortie = 1
    for i in range(len(pg)):
        pg0[i] = pg[i]
    x1=addVitesse(x1, V1)

    #Nouvelle vitesse de la particule 2
    V2 = addVitesse(mulVitesse(w, V2), mulVitesse(b1, subVitesse(p2, x2)))
    V2 = addVitesse(V2, mulVitesse(b2, subVitesse(pg, x2)))
    if fonc(x2)<fonc(addVitesse(x2, V2)):
       for i in range(len(x2)):
            p2[i] = x2[i]
    else:
        p2=addVitesse(x2, V2)
    x2=addVitesse(x2, V2)

    #Nouvelle vitesse de la particule 3
    V3 = addVitesse(mulVitesse(w, V3), mulVitesse(b1, subVitesse(p3, x3)))
    V3 = addVitesse(V3, mulVitesse(b2, subVitesse(pg, x3)))
    if fonc(x3)<fonc(addVitesse(x3, V3)):
       for i in range(len(x1)):
            p3[i] = x3[i]
    else:
       p3=addVitesse(x3, V3)
    x3=addVitesse(x3, V3)

    nbiter=nbiter+1
    X1.append(x1)
    X2.append(x2)
    X3.append(x3)
    #B1=[B1 b1]
    #B2=[B2 b2]
    print(pg)
    print(fonc(pg))