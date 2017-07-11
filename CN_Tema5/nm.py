
def creaza_Anm(n, m):
    A = [m * [0] for i in range(n)]

    for i in range(min(n,m)):
        A[i][i] = 1
    for i in range(min(n-1,m-1)):
        A[i][i+1] = 2
    #print A
    return (A)

def norma_infinit(A):
    norme = []
    for i in range(len(A)):
        norme.append(sum([abs(x) for x in A[i]]))
    return max(norme)

def matrice_I(n):
    I = [n*[0] for i in range(n)]
    for i in range(n):
       I[i][i] = 1.0
    return I

def transpusa(Matrice):
    return [list(i) for i in zip(*Matrice)]

def diferenta_matrici(A, B, scadere=True):
    # "Scadere ", len(A), len(A[0]),  len(B), len(B[0])
    #print A, " \n", B
    Res = []
    n = len(A)
    m = len(A[0])
    for i in range(n):
        line = []
        for j in range(m):
            if scadere:
                #print i,j, A[i][j], B[i][j]
                line.append(A[i][j] - B[i][j])
            else:
                line.append(A[i][j] + B[i][j])
        Res.append(line)

    return Res

def inmultire_matrici(A, B):
    #print A,"\n", B
    n = len(A)
    m = len(A[0])
    p = len(B)
    q = len(B[0])

    #print n,m,p,q
    Res = [[0]*q for i in range(n)]

    if m != p:
        raise Exception("Nu corespund")

    for i in range(n):
        for j in range(q):
            for k in range(p):
                #print  k,j,B[k][j], Res[i][j], i,k, len(A), len(A[i]),A[i][k]
                Res[i][j] += A[i][k]*B[k][j]

    return Res


def metoda_iterativa_nm(A):
    n = len(A)
    m = len(A[0])

    norma1 = norma_infinit(transpusa(A))
    norma_inf = norma_infinit(A)
    A_T = transpusa(A)

    B = []
    for i in range(n):
        line = [-x for x in A[i]]
        B.append(line)
    #B = a_ori_A(A, -1.0)

    V1 =  [[float(x)/float(n*norma1*norma_inf) for x in A_T[i]] for i in range(len(A_T))]
    V0 = V1
    k=0
    kmax =10000
    n = len(A)
    epsilon = pow(10,-5)

    if norma_infinit(transpusa(diferenta_matrici(inmultire_matrici(A, V0), matrice_I(n)))) < 1.0:
        print "V0 a fost corect initializat!"
    else:
        print "V0 NU a fost corect initializat!", norma_infinit(transpusa(diferenta_matrici(inmultire_matrici(A, V0), matrice_I(n))))

    print inmultire_matrici(A, V1)


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



n = 3
m = 2
A = creaza_Anm(n,m)
#A = [[1,0],[0,5],[-1,1]]
(Raspuns, k) = metoda_iterativa_nm(A)
print A
print "Raspuns: ",  len(A), len(A[0]), len(Raspuns), len(Raspuns[0])

if type(Raspuns) == type("ana"):
    print Raspuns
else:
    print norma_infinit(transpusa(diferenta_matrici(inmultire_matrici(A, Raspuns),matrice_I(n))))<pow(10,-5)

