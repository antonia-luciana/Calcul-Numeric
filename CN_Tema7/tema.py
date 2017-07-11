import math
import numpy as np
import random
import copy


def calcul_dif(xs, dif_div, pas, f):   #este corecta
    n = len(dif_div) - 1
    res = []
    for i in range(n):
        res.append( (dif_div[i+1] - dif_div[i])/ (xs[i+pas] - xs[i]) )

    return res


def aitken(xs, f):
    n = len(xs) - 1
    dif_div = []
    y = [f(xs[0])]

    for i in range(n):
        dif_div.append( (f(xs[i+1]) - f(xs[i]))/(xs[i+1]-xs[i]) )

    y.append(dif_div[0])
    pas = 2

    while pas <= n:
        dif_div = calcul_dif(xs, dif_div, pas, f)
        y.append(dif_div[0])
        pas += 1

    return y


def aprox_lagrange(xs, f, x):
    y = aitken(xs, f)
    n = len(xs) - 1

    res = y[0]
    prod = 1
    for i in range(1, n+1):
        prod *= (x - xs[i-1])
        res += y[i] * prod

    return res

def aprox_lagrange_lista(xs, f, lista):
    res = []
    for nr in lista:
        res.append(aprox_lagrange(xs, f, nr))

    return res

def fi(nr, x):
    if nr == 0:
        return 1
    if nr % 2 == 1:
        return math.sin(((nr+1)/2)*x)
    else:
        return math.cos((nr/2)*x)


def getX(lista, f):
    n = len(lista)
    m = n/2

    T = []
    for nr in lista:
        T.append([fi(i, nr) for i in range(n)])

    T = np.array(T)
    Y = np.array([f(lista[i]) for i in range(len(lista))])
    X = np.linalg.solve(T, Y)

    #print np.linalg.norm(np.subtract(np.dot(T, X), Y)) < pow(10, -1)

    return X

def aprox_trigo(X, xb):
    aprox = X[0] * fi(0, xb)
    for i in range(1, len(X)/2):
        aprox += X[i] * fi(i, xb) + X[i + 1] * fi(i + 1, xb)

    return aprox

def trigo_lista(lista, f, xbs):
    X = getX(lista, f)
    res = []
    for xb in xbs:
        res.append(aprox_trigo(X, xb))

    return res

def trigo(lista, f, x):
    X = getX(lista, f)
    return  aprox_trigo(X, x)


def puncte_pol(x0, xn, n):
    lista = list(set(sorted([random.randint(x0, xn) for i in range(n)])))
    while len(lista)<n:
        lista.append(random.randint(x0, xn))
        lista = list(set(lista))
    return lista


def puncte_trigo(x0, xn, n):
    lista = sorted([random.uniform(x0, xn) for i in range(n)])
    return lista

#print "2x+1", f(0), f(1), f(2)

#print puncte





#res = trigo(puncte, t2, [math.pi/7])

#print "Diferenta dintre rezultate : ", abs( res[0] - t2(math.pi/7) )
'''
f(lista[0])
'''