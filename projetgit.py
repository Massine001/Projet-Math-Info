import numpy as np 
import matplotlib.pyplot as plt
from math import *

n = int(input("Donner le nombre d'itr : "))
choix = int(input("La fonction de K(t,y(t)):\n 1) t\n 2) ln(t)\n 3) 2*ln(t))/(t*(1+ln(t)*ln(t))\n 4) y(t)*ln(y(t))/(y(t)−Tamb)\n "))
T = int(input("Le temps final T : "))
#t0 = int(input("Le temps t0 : "))

if choix == 1 :          # Condition init 
    y0 = 21                                                     #Pour les exmples T = 2
    t0 = 0
if choix == 2 :                                                 #T = 3
    y0 = 20.3678794412
    t0 = 1
if choix == 3 :                                                 #T = 3
    y0 = 20.392348131
    t0 = 2
if choix == 4 :    
    y0 = 2.718281828459                                         #T = 1
    t0 = 0

def f(t,y):                                   # La fonction F represente le T' selon le K(t,y(t)) choisi avec Tamb =20                              
    
    if choix == 1 :                           # T' = t*(y(t)-Tamb) avec Tamb = 20
        return t*(y-20)         
    elif choix == 2 :                         # T' = ln(t)*(y(t)-Tamb) avec Tamb = 20
        return np.log(t)*(y-20)       
    elif choix == 3 :                         # T' = (y(t)-Tamb)* 2*ln(t)/((t*(1+ln(t)²)) 
        return (y-20)*((2*np.log(t))/(t*(1+np.log(t)*np.log(t))))
    elif choix == 4 :                         # T' = y(t)*ln(y(t)) 
        return y*np.log(y)
    else :
        print("Entre 1 et 4 ")
        return 0



def Euler(y0, n, t0, T ):                    # La fonction Euler explicite avec les parametres (y0,t0 conditions initiales) et T: temps final / n: nombre de points
    t = np.zeros(n)                          # Le vecteur de temps initialisé à 0
    Y = np.zeros(n)                          # Le vecteur des Y initialisé à 0
    h = (T-t0)/n                             # Le Pas h
    t[0] = t0
    Y[0] = y0
    for i in range(n-1):
        Y[i+1] = Y[i] + h*f(t[i],Y[i])       # Euler explicite    
        t[i+1] = t[i] + h                    # ti 
    print('*' *60)
    print(Y)
    return Y,t

#f(0,0)

y,t = Euler(y0, n, t0, T)                    # L'appel de la fonction Euler            

def sol(t):                                  # La solution exacte selon le choix de K   
    g = np.zeros(n)
    if choix == 1 :                              
        for i in range(n):
            g[i] = exp(0.5*t[i]*t[i])+20
    elif choix == 2 :
        for i in range(n):
            g[i] = exp(t[i]*(np.log(t[i])-1))+20
    elif choix == 3 :
        for i in range(n):
            g[i] = np.log(1+np.log(t[i])*np.log(t[i]))+20
    elif choix == 4 :
        for i in range(n):
            g[i] = exp(exp(t[i]))

    return g

s = sol(t)

############

def plot(t,y,s):                             # Pour afficher les deux graphes (soltion exacte avec la couleur bleu / solution approchée avec la couleur rouge)   
    axe1 = t                                 # L'axe des X 
    axe2 = y                                 # L'axe des Y 
    plt.figure()
    plt.title(" Fegure -1- ")
    plt.plot(axe1,axe2,c="red",label="solution approchee")
    plt.plot(axe1,s,c="blue",label="solution exacte")
    plt.legend()
    plt.xlabel(' Temps ')
    plt.ylabel(' Solution ')
    plt.show()


plot(t,y,s)

