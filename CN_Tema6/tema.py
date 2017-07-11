import random
import math
import time
import numpy as np

from Memorare_economica import *

def euclidian_norm(x):
    return math.sqrt(sum([pow(elem,2) for elem in x]))

def v0(n):
    x = random.sample(range(1000*n), n)
    norma2 = euclidian_norm(x)

    x = [float(elem)/norma2 for elem in x]

    return x

def A(n):
    diag = random.sample(set(range(-5*n,5*n)).difference(set([0])), n)
    val = [[] for i in range(n)]
    col = [[] for i in range(n)]
    #nr = int(n/200)
    nr = 2

    for i in range(n-1):
        while len(val[i]) <= random.randint(1,nr-1):
            coloana = random.randint(i,n-1)
            valoare = random.randint(1,10)

            if len(val[coloana]) <= nr:
                val[i] += [valoare]
                col[i].append(coloana)
                val[coloana].append(valoare)
                col[coloana] += [i]

    A = Matrice()
    val = postprocesare_val(val)
    col = postprocesare_col(col)
    A.values(diag,val,col)
    A.n = n
    return A

def produs_scalar(v, w):
    return sum([x*y for x in v for y in w])

def metoda_puterii(A, epsilon = pow(10,-4)):
    n = A.n
    v = v0(n)
    w = inmultire_vector_x(A, v)
    k = 0
    kmax = 1000
    gamma = produs_scalar(w, v)

    while(1):
        norma2 = euclidian_norm(w)
        v = [float(elem)/norma2 for elem in w]
        w = inmultire_vector_x(A, v)
        #print k," . ",gamma
        gamma = produs_scalar(w, v)
        k += 1
        if euclidian_norm([ x - (gamma*y) for x in w for y in v])<= (n*epsilon) or k > kmax:
            break

    if k > kmax:
        return None,"",k
    else:
        print "rez",epsilon, gamma, v, k
        return gamma, v, k

def inmultire_cu_vector(A, v):
    if len(A) is not len(v):
        raise Exception("Matricea si vectorul trebuie sa aiba aceeasi dimensiune!")
    Res = []
    for row in A:
        sum = 0
        for i in range(len(row)):
            sum += row[i]*v[i]
        Res.append(sum)
    return Res

def metoda_puterii_2(A, n, epsilon = pow(10,-4)):
    v = v0(n)
    w = inmultire_cu_vector(A, v)
    k = 0
    kmax = 1000

    gamma = produs_scalar(w, v)

    while(1):
        norma2 = euclidian_norm(w)
        v = [float(elem)/norma2 for elem in w]
        w = inmultire_cu_vector(A, v)

        gamma = produs_scalar(w, v)
        k += 1
        #if v == w:
         #   break
        if euclidian_norm([ x - (gamma*y) for x in w for y in v]) <= (n*epsilon) or k > kmax:
            break

    if k > kmax:
        return None,""
    else:
        print "rez",epsilon, gamma, v, k
        return gamma, v

#M = [[1,2,3],[4,5,6],[7,8,9]]


'''
n = 500

start = time.time()
print metoda_puterii(A(n))
print time.time() - start
'''

def citire():
    A = Matrice()
    A.read_file("m_rar_sim_2017.txt")
    return A

def isSimmetric(A):
    A.transpusa()
    return (A.val == A.valT and A.col == A.colT)

def norma_infinit(A):
    norme = []
    for i in range(len(A)):
        norme.append(sum([abs(x) for x in A[i]]))
    return max(norme)

def transpusa(Matrice):
    return [list(i) for i in zip(*Matrice)]

def diferenta_matrici(A,B, scadere=True):
    Res = []
    n = len(A)
    m = len(A[0])
    for i in range(n):
        line = []
        for j in range(m):
            if scadere:
                line.append(A[i][j] - B[i][j])
            else:
                line.append(A[i][j] + B[i][j])
        Res.append(line)

    return Res

def inmultire_matrici(A, B):
    n = len(A)
    m = len(A[0])
    p = len(B)
    q = len(B[0])

    Res = [[0]*q for i in range(n)]

    if m != p:
        raise Exception("Nu corespund")

    for i in range(n):
        for j in range(q):
            for k in range(p):
                #print  B[k][j], Res[i][j], i,k, len(A), len(A[i]),A[i][k]

                Res[i][j] += A[i][k]*B[k][j]

    return Res

def inmultire_vectori(v1,v2):
    return ([x*y for x in v1 for y in v2])

def inmultire_M_vector(M, v):
    res = []
    for i in range(len(M)):
        res.append(sum([x*y for x in M[i] for y in v]))
    return res

def transpune_vector(v):
    vT = []
    for elem in v:
        vT.append([elem])
    return vT

def svd(p, n):
    A = np.random.randn(p, n)

    (U,s,V) = np.linalg.svd(A, full_matrices=True)
    S = np.diag(s)
    rang2 = 3
    if p > n:
        for i in range(abs(n-p)):
            S = np.vstack([S, [0]*n])
            #S = np.insert(S, n + i, values=[0]*n, axis=1)

        s_poz = [x for x in s if x>0]
        rang = len(s_poz)
        nr_conditionare = max(s_poz)/min(s_poz)
        norma = norma_infinit(diferenta_matrici(A, inmultire_matrici(inmultire_matrici(U,S), transpusa(V))))

        #s_rand = random.randint(1, rang2)
        s_rand = random.randint(1, rang)
        print s_rand
        As = [[0]*n for i in range(p)]
        for i in range(s_rand):
            if i > 0:
                As = diferenta_matrici(As,inmultire_matrici([[s[i]*x] for x in U[i]], [V[i].tolist()]), scadere=False)
                #print As
            else:
                As = inmultire_matrici([[s[i]*x] for x in U[i]], [V[i].tolist()])
                #print As
        #print len(A), len(As), len(A[0]), len(As[0])

        for i in range(abs(n-p)):
            As = np.vstack([As, [0]*n])

        norma_2 = norma_infinit(diferenta_matrici(A, As, scadere=True))

        return rang, norma, nr_conditionare, As, norma_2,s_rand


#svd(9,6)


#M = citire()
'''
n = 500
M = A(n)
print "Am citit"
eps = pow(10,-1)
start = time.time()
gamma, v = metoda_puterii(M, eps)
print "intru in while"
while  gamma == None and eps < 1000:
    eps *= 10
    gamma, v = metoda_puterii(M, epsilon=eps)

print gamma, v, eps
print inmultire_cu_vector(M, v), v, [gamma * x for x in v]
print time.time() - start
'''