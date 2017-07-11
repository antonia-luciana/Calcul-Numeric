from Memorare_economica import*
import numpy as np
import math


def get_matrice(filename):
    A=Matrice()
    A.read_file(filename)
    A.val=preprocesare(A.val)
    A.col=preprocesare(A.col)

    return A

def norma(z):
    return math.sqrt(np.sum( np.power(z, 2.0)))

def dif(a,b):
    return [ a[i]- b[i] for i in (range(len(a)))]


def metoda_iterativa(A, p):
    xc=range(1,A.n+1)
    xp=[]
    k=0
    kmax=10000
    dx=0
    eps = pow(10, (-p))
    while (1):
        xp = xc
        xc=[]
        for i in range(A.n):
            xc.append((A.b[i] - sum([ A.val[i][j] * xp[int(A.col[i][j])-1] for j in range(len(A.val[i]))]))/A.d[i])
        dx=norma([xc[i]-xp[i] for i in range(len(xc))])
        k+=1
        if not( dx >= eps and k <= kmax and dx<=pow(10,8)):
            break
    #print k
    if dx < eps:
        return (xc, k)
    else:
        return "Divergenta!!"

