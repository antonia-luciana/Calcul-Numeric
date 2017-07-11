import numpy as np
import math
import copy
import numpy as np
#n = input("Introdu n: ")


def creaza_A(n):
    A = [n * [0] for i in range(n)]

    for i in range(n):
        A[i][i] = 1
    for i in range(n-1):
        A[i][i+1] = 2
    return (A)

def matrice_I(n, nr = 1):
    I = [n*[0] for i in range(n)]
    for i in range(n):
       I[i][i] = 1.0 * nr
    return I

def norma_infinit(A):
    n  = len(A)
    norme = []
    for i in range(n):
        norme.append(sum([abs(x) for x in A[i]]))
    return max(norme)

def transpusa(Matrice):
    return [list(i) for i in zip(*Matrice)]

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

def inmultire_matrici(A, B):
    Res = []
    n = len(A)
    for i in range(n):
        line = []
        for j in range(n):
            suma = 0
            for k in range(n):
                suma += A[i][k]*B[k][j]
            line.append(suma)
        Res.append(line)

    return Res

def norma(z):
    return math.sqrt(np.sum( np.power(z,2.0)))

def norma_F(A):
    suma = 0

    for i in range(len(A)):
        for j in range(len(A)):
            suma += pow(A[i][j],2)

    return math.sqrt(suma)

def diferenta_matrici(A,B):
    Res = []
    for i in range(len(A)):
        line = []
        for j in range(len(B)):
            line.append(A[i][j]-B[i][j])
        Res.append(line)
    return Res


def a_ori_A(A,a):
    R = copy.copy(A)
    for i in range(n):
        for j in range(n):
            R[i][j] = a*R[i][j]
    return R

def norma_1(A):
    norme = []
    for i in range(n):

        norme.append(sum([abs(x) for x in A[i]]))
    return max(norme)

def metoda_iterativa_1(A, epsilon = pow(10,-5)):
    n =len(A)
    norma1 = norma_infinit(transpusa(A))
    norma_inf = norma_infinit(A)
    A_T = transpusa(A)

    B = []
    for i in range(n):
        line = [-x for x in A[i]]
        B.append(line)

    numitor = float(norma1*norma_inf)
    V1 =  [[float(x)/numitor for x in A_T[i]] for i in range(len(A_T))]
    V0 = V1
    k=0
    kmax =10000
    n = len(A)

    if norma_infinit(transpusa(diferenta_matrici(inmultire_matrici(A, V0), matrice_I(n)))) <1.0:
        print "V0 a fost corect initializat!"
    else:
        print "V0 NU a fost corect initializat!", norma_infinit(transpusa(diferenta_matrici(inmultire_matrici(A, V0), matrice_I(n))))

    while(1):
        V0 = V1
        C = inmultire_matrici(B, V0)

        for i in range(n):
            C[i][i] = C[i][i] + 2.0

        V1 = inmultire_matrici(V0, C)
        delta = norma_infinit(diferenta_matrici(V1, V0))
        k += 1
        #print delta
        if delta < epsilon or k>= kmax or delta > pow(10,10):
            break

    if delta < epsilon:
        #print "delta iesire",delta, epsilon,(delta < epsilon), k>= kmax , delta > pow(10,10)
        return (V1, k)
    else:
        return "divergenta"

def metoda_iterativa_3(A, epsilon = pow(10,-5)):
    n =len(A)
    norma1 = norma_infinit(transpusa(A))
    norma_inf = norma_infinit(A)
    A_T = transpusa(A)

    B = []
    for i in range(n):
        line = [-x for x in A[i]]
        B.append(line)

    V1 =  [[float(x)/float(norma1*norma_inf) for x in A_T[i]] for i in range(len(A_T))]
    V0 = V1
    k=0
    kmax =10000
    n = len(A)

    AV0 = inmultire_matrici(A, V0)
    for i in range(len(AV0)):
        AV0[i][i] -= 1

    if norma_infinit(AV0) <1.0:
        print "V0 a fost corect initializat!"
    else:
        print "V0 NU a fost corect initializat!", norma_infinit(AV0)

    while(1):
        V0 = V1
        C = inmultire_matrici( V0, B)

        Cprim = copy.deepcopy(C)
        Csecund = copy.deepcopy(C)

        for i in range(n):
            Cprim[i][i] = Cprim[i][i] + 3.0

        Cprim_p = inmultire_matrici(Cprim, Cprim)

        for i in range(n):
            Csecund[i][i] = Csecund[i][i] + 1.0

        D = inmultire_matrici(Csecund, Cprim_p)

        for i in range(n):
            for j in range(n):
                D[i][j] /= 4.0
                if i==j :
                    D[i][j] += 1.0

        V1 = inmultire_matrici(D, V0)

        delta = norma_infinit(diferenta_matrici(V1, V0))
        k += 1

        if delta < epsilon or k>= kmax or delta > pow(10,10):
            break

    if delta < epsilon:
        #print "delta iesire",delta, epsilon,(delta < epsilon), k>= kmax , delta > pow(10,10)
        return (V1, k)
    else:
        return "divergenta"

def metoda_iterativa_2(A, epsilon = pow(10,-5)):
    n = len(A)

    norma1 = norma_infinit(transpusa(A))
    norma_inf = norma_infinit(A)

    A_T = transpusa(A)
    B = []
    for i in range(n):
        line = [-x for x in A[i]]
        B.append(line)

    numitor = float(norma1)*float(norma_inf)
    V1 =  [[float(x)/numitor for x in A_T[i]] for i in range(len(A_T))]
    V0 = V1

    k=0
    kmax =10000

    AV0 = diferenta_matrici(inmultire_matrici(A, A_T),  matrice_I(n))
    R = [[float(x)/numitor for x in AV0[i]] for i in range(len(A_T))]

    if norma_infinit(R) < 1.0:
        print "V0 a fost corect initializat!", norma_infinit(R)
    else:
        print "V0 NU a fost corect initializat!", norma_infinit(R)

    while(1):
        V0 = V1
        V1 = []

        C = inmultire_matrici(B, V0)
        Cprim = copy.deepcopy(C)
        for i in range(n):
            Cprim[i][i] += 3.0
        Cprim = inmultire_matrici(C,Cprim)
        for i in range(n):
            Cprim[i][i] += 3.0

        V1 = inmultire_matrici(V0, Cprim)

        delta = norma_infinit(diferenta_matrici(V1, V0))

        k += 1
        if delta < epsilon or k>= kmax or delta > pow(10,10):
            break

    if delta < epsilon:
        return V1,k
    else:
        return "divergenta",k

def metoda_4(A):
    n = len(A)
    res = [[0.0]*n for i in range(n)]

    for i in range(n):
        res[i][i] = 1.0
        for j in range(i+1,n):
            res[i][j] = pow(-2,(j-i))

    return res, 0
