import math
import numpy as np
import copy
import scipy
import scipy.linalg as sc
import math

#determinantul unei matrici folosind minori
def det(A):
    if len(A)==2:
        return float(A[0][0])*float(A[1][1])-float(A[0][1])*float(A[1][0])
    else:
        D=0
    for i in range(0,len(A)):
        M= copy.copy(A)
        #M = A[:]
        if i%2==0:
            D=D+float(A[0][i])*det(minor(M,0,i))
        else:
            D=D-float(A[0][i])*det(minor(M,0,i))
    return D

def minor(Matrice,i,j):  #matrice in care s-a sters linia i si coloana j
    Minor=[]
    Minor[:i]=Matrice[:i]
    Minor[i:]=Matrice[i+1:]
    Minor2=[x[:] for x in Minor]
    for rand in Minor2:
        del rand[j]
    return Minor2

#functia care verifica impartirea
def impartire(a, b, e):
    if b > e:
        return float(a / b)
    else:
        print "NU se poate face impartire " + str(a) + " / " + str(b)
        raise ArithmeticError

def factorizare_Clolesky(A, epsilon = 10**(-5)):
    n = len(A)
    D=[0.0 * n for i in range(0,n)]
    try:
            for i in range(0,n):
                if i==0:
                    D[i]=A[i][i]
                    value=[impartire(x,D[i],epsilon) for x in A[:][i]]
                    for j in range(0,n):
                        A[j][i]=value[j]
                else:
                    lista = [D[x]*(A[i][x]**2) for x in range(0,i)]
                    D[i] = A[i][i] - sum(lista)
                    suma = sum([D[x]*A[p][x]*A[i][x] for x in range(0,i) for p in range(i+1,n)])
                    for p in range(i+1,n):
                        A[p][i] = impartire(A[i+1][i] - suma, D[i],epsilon)
    except ArithmeticError as e:
        return

    return (D)


#Ex2

def determinant_chol(D):  #determinant ce foloseste descompunerea Cholensky
    #D = (factorizare_Clolesky(A,(10**(-6))))[1]
    return reduce(lambda x,y: x*y, D)

A = [[1,-1,2],[-1,5,-4],[2,-4,6]]

#print factorizare_Clolesky(A,(10**(-5)))
#print determinant(A)
print A

#Ex 3

def rezolvare_inferior_adaptat(A, b): #se adapteaza contextului vizat: elementele lui L sub diagonala matricei A si rezolva Lz = b
    z = [0.0] * len(A)

    for i in range(len(A)):
        suma = sum([A[i][j]*z[j] for j in range(0,i)])
        z[i] = (b[i]-suma)

    return z

def transpusa(Matrice):
    return [list(i) for i in zip(*Matrice)]

def rezolvare_superior_adaptata(A,b): #
    n = len(A)
    x = [0.0] * n

    for i in reversed(range(0,n)):
        suma = 0.0
        for j in range(i+1,n):
            suma += A[j][i] * x[j]
        #print "suma pt i = " + str(i) + " este "+str(suma)
        x[i] = (b[i] - suma)

    return x


def rezolvare_sistem(A,D,b):
    #D = factorizare_Clolesky(A, (10 ** (-6)))[1]
    #print A
    z = rezolvare_inferior_adaptat(A,b)
    #print "z: " + str(z)
    y = [z[i]/D[i]  for i in range(len(A))]
    print "y: " + str(y)
    x = rezolvare_superior_adaptata(A, y)
    return x

#Ex5
def prod(M,v):   #produsul dintre o matrice si un vector
    res = []

    for i in range(len(M)):
        s = 0.0
        for j in range(0,len(M)):
            if i<=j:
                s += M[i][j] * v[j]
            else:
                s += M[j][i] * v[j]
        res.append(s)

    return res

def norma(z):
    return math.sqrt(np.sum( np.power(z,2.0)))


def dif(a,b):
    return [ a[i]- b[i] for i in range(len(a)) ]


'''
b = [2,5,6]

Ainit = copy.deepcopy(A)

x = sc.solve(A, b)

print "Rezolvare corecta" + str(x)
print "verificare: " + str(np.linalg.norm((np.dot(A,x)-b)) )

xi = rezolvare_sistem(A,b,b)
print "Rezolvarea mea:" + str(xi)

print "verificare: " + str(np.linalg.norm((np.dot(Ainit,xi)-b)) )

print "verificare: " + str(norma(dif(prod(Ainit,xi),b)) )
'''










