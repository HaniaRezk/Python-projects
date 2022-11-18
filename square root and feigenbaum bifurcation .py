import random
from math import *
import time
import numpy as np
import matplotlib.pyplot as plt
global y
y=0
def f(A,e): #square root function without using sqrt.
    x=random.random()
    x1=0.5*(x+A/x)
    global y
    while abs(x-x1)>e:
        x=x1
        x1=0.5*(x1+A/x)
        y=+1
    return x

def racine():
    global y
    for i in range (0,1000000):
        f(i,0.01)


def racine2():
    c=0
    for i in range (0,1000000):
        c=sqrt(i)

y1=time.time()
racine()
y2=time.time()
print("le temps d'execution de l'algo 1 est", y2-y1)
y3=time.time()
racine2()
y4=time.time()
print("le temps d'execution de l'algo 2 est", y4-y3)

def feigenbaum(n,u,x): #La bifurcation de Feigenbaum
    L=[x]
    for i in range(n+1):
        x=1-u*x**2
        L.append(x)
    return L


n=100
x=0.5
suite=feigenbaum(n,0.5,x)
plt.plot(range(len(suite)),suite, label="courbe 0.5", color="green")
plt.show()
