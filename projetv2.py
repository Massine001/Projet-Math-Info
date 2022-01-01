import numpy as np 
import matplotlib.pyplot as plt
from math import * 
import time 

n = int(input("Donner le nombre d'itr : "))
choix = int(input("La fonction de K(t,y(t)):\n 1/ t\n 2/ ln(t)\n 3/ 2*ln(t))/(t*(1+ln(t)*ln(t))\n 4/ y(t)*ln(y(t))/(y(t)−Tamb)\n 5/ K est constante\n Votre choix : "))
#t0 = int(input("Le temps t0 : "))
Tamb = int(input("La temperature de la piece : "))
y0 = int(input("La temperature initiale : "))
T = int(input("Le temps final T : "))



if choix == 1 :          # Condition init domaine de definition 
    t0 = 0
    lamda = y0 - Tamb
elif choix == 2 :                                               
    t0 = 1
    lamda = (y0 - Tamb)*exp(-1)
elif choix == 3 :                                   
    t0 = 1
    lamda = y0 - Tamb
elif choix == 4 :
    t0 = 0
    lamda = np.log(y0)       # avec y0 != 0
elif choix == 5 :
    k = int(input("Le K est une constante\n Donner une valeur de k : "))
    t0 = 0
    lamda = y0-Tamb

def f(t,y):                                   # La fonction F represente le T' selon le K(t,y(t))                              
    
    if choix == 1 :                           # T' = t*(Tamb-y(t))
        return t*(Tamb-y)         
    elif choix == 2 :                         # T' = ln(t)*(Tamb-y(t)) 
        return np.log(t)*(Tamb-y)       
    elif choix == 3 :                         # T' = (Tamb-y(t))* 2*ln(t)/((t*(1+ln(t)²)) 
        return (Tamb-y)*((2*np.log(t))/(t*(1+np.log(t)*np.log(t))))
    elif choix == 4 :                         # T' = -y(t)*ln(y(t))
        if y0 != 0 : 
            return y*np.log(y)*(-1)
        else :
            return 0;
    elif choix == 5 :
        return k*Tamb-k*y
    else :
        print("Entre 1 et 5 ")
        return 0


def Euler(y0, n, t0, T):                    # La fonction Euler explicite avec les parametres (y0,t0 conditions initiales) et T: temps final / n: nombre d'iteration
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


y,t = Euler(y0, n, t0, T)                    # L'appel de la fonction Euler            

def sol(t):                                  # La solution exacte selon le choix de K   
    g=np.zeros(n)
    if choix == 1 :                              
        for i in range(n):
            g[i] = lamda*exp(-(0.5*t[i]*t[i]))+Tamb
    elif choix == 2 :
        for i in range(n):
            g[i] = lamda*exp(t[i]*(1-np.log(t[i])))+Tamb
    elif choix == 3 :
        for i in range(n):
            g[i] = lamda / (1+(np.log(t[i])*np.log(t[i])))+Tamb
    elif choix == 4 :
        for i in range(n):
            g[i] = exp(lamda*exp(-t[i]))                    
    elif choix == 5 :
        for i in range(n):
            g[i] = lamda*exp(-k*t[i])+Tamb
    return g

sol_exa = sol(t)

def Runge_Kutta(y0, n, t0, T):
    print("Runge-Kutta")
    t = np.zeros(n)
    y = np.zeros(n)
    h = (T-t0)/n   
    t[0] = t0
    y[0] = y0
    for i in range(n-1):
        p1 = f(t[i],y[i])
        p2 = f(t[i]+(h/3),y[i]+p1*(h/3))
        p3 = f(t[i]+2*(h/3),y[i]-(p1/3)+p2)
        p4 = f(t[i]+h,y[i]+p1-p2+p3)

        y[i+1] = y[i]+(h/8)*(p1+3*p2+3*p3+p4)
        t[i+1] = t[i]+h
    print(y)
    return y,t 

y_r,t_r = Runge_Kutta(y0, n, t0, T)


def plot(t,y,s):                             # Pour afficher les deux graphes (soltion exacte avec la couleur bleu / solution approchée avec la couleur rouge)   
    axe1 = t                                 # L'axe des X 
    axe2 = y                                 # L'axe des Y 
    plt.figure()
    plt.title(" Figure -1- : Méthode d'Euler Explicite ")
    plt.plot(axe1,axe2,c="red",label="solution approchee")              # Euler 
    plt.plot(axe1,s,c="blue",label="solution exacte")
    plt.legend()
    plt.xlabel(' Temps ')
    plt.ylabel(' Temperature ')
    plt.show()




def plotR(t,y,s):                             # Pour afficher les deux graphes (soltion exacte avec la couleur bleu / solution approchée avec la couleur rouge)   
    axe1 = t                                 # L'axe des X 
    axe2 = y                                 # L'axe des Y 
    plt.figure()
    plt.title(" Figure -2- : Méthode de Runge  ")
    plt.plot(axe1,axe2,c="red",label="solution approchee")              # runge-kutta
    plt.plot(axe1,s,c="blue",label="solution exacte")
    plt.legend()
    plt.xlabel(' Temps ')
    plt.ylabel(' Temperature ')
    plt.show()

plot(t,y,sol_exa)
plotR(t,y,sol_exa)


