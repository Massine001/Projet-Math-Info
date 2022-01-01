import projetv2 as mp
import numpy as np 
import matplotlib.pyplot as plt
from time import time 

tmp = [0,0,0,0,0]
N = [5,30,40,50,100]
tmpsol = [0,0,0,0,0]
t = [0, 0.1, 0.2, 0.3, 0.4]

mp.choix = 1                                    # Juste pour la premier fonction K(t,y(t)) = t
y0 = 21                                                     # Conditions initials 
t0 = 0

for i in range(len(N)):

    start = time()
    y,t = mp.Euler(y0, N[i], t0, 1)                    # L'appel de la fonction Euler            
    print("temps d'execution pour n = ",N[i]," : ", time()-start)
    tmp[i] = time()-start

for j in range(len(N)):
    
    start = time()
    mp.sol(t)                                
    print("temps d'execution pour n = ",N[j]," : ", time()-start)
    tmpsol[j] = time()-start

def plot(t,ts,nbr):
    axe2 = t                                 # L'axe des X 
    axe1 = nbr                                 # L'axe des Y 
    axe3 = ts
    plt.figure()
    plt.title(" -- Profiling -- ")
    plt.plot(axe1,axe2,c="red",label="Profiling Euler")              # Avec Euler ou Runge-Kutta ça depend les parametres (l'appel de la fonction)
    plt.plot(axe1,axe3,c="blue",label="Profiling Solution") 
    plt.legend()
    plt.xlabel(' Nombre d\'iteration ')
    plt.ylabel(' Temps d\'exuion ')
    plt.show()

plot(tmp, tmpsol, N)
print(tmp)
print(tmpsol)
