from random import *
# Choix de la solution initiale
def fn(a):
    return abs((a-2)*(a-4))
x=[0, 3, 6, 9, 12, 15] 
N=10 # Nombre d'itérations : Nombre de générations
i=0;
n=40 # nombre d'itération pour la même température
y=[] # vecteur vide
z=[] # vecteur vide qui contiendra à chaque itération i, la population i-1 et 
# les éléments résultats du croisement-mutation
z=z+x
print('x(',i,')=',x)
while i<N: 
  # Croisement
  if x[0]<x[1]:
    r1 = randint(x[0],x[1])
    r2 = randint(x[0],x[1])
  else: 
    r1 = randint(x[1],x[0])
    r2 = randint(x[1],x[0])
  y=y+[r1]
  y=y+[r2]
  if x[2]<x[3]:
    r3 = randint(x[2],x[3])
    r4 = randint(x[2],x[3])
  else:
    r3 = randint(x[3],x[2])
    r4 = randint(x[3],x[2])
  y=y+[r3]
  y=y+[r4]
  if x[4]<x[5]:
    r5 = randint(x[4],x[5])
    r6 = randint(x[4],x[5])
  else: 
    r5 = randint(x[5],x[4])
    r6 = randint(x[5],x[4])
  y=y+[r5]
  y=y+[r6]
  # Mutation 
  # Choisir aléatoirement deux éléments de y
  # Les modifier par deux valeurs aléatoires 
  # Contenues dans l'intervalle de recherche [0,15]
  t1=randint(0,5)
  t2=randint(0,5)
  while t1==t2:
    t1=randint(0,5)
    t2=randint(0,5)
  y[t1]=randint(0,15)
  y[t2]=randint(0,15)
  z=z+y
  # Selection pour composer la population suivante 
  # Les six individus ayant les plus petites valeurs
  # de la fonction fitness
  for k in range(12):
    l=k
    while l<12:
      if fn(z[k])>fn(z[l]):
        temp=z[k]
        z[k]=z[l]
        z[l]=temp
      l=l+1
  for m in range(6):
    x[m]=z[m]
  y=[]
  z=[] 
  z=z+x
  #print('z(',i,')=',z)
  i=i+1
  print('x(',i,')=',x)
  #print('r1=',r1)
  #print('r2=',r2)
  #print('r3=',r3)
  #print('r4=',r4)
  #print('r5=',r5)
  #print('r6=',r6)