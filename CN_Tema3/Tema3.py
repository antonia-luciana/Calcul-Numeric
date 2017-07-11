import re
import time

#Quicksort
def switch(x, p, u):
    aux = x[p]
    x[p] = x[u]
    x[u] = aux

def poz(x, y, p, u):
    #piv, aux, k
    aux = -1
    piv = x[p]
    while (p < u):
        if x[p] > x[u]:
            switch(x, p, u)
            switch(y, p, u)
        if (x[p] == piv):
            u -= 1
        else:
            p += 1

    k = p
    return k


def quick(x, y, p, u):
    if p < u:
        k = poz(x, y, p, u)
        quick(x , y , p, k-1)
        quick(x , y, k+1, u)

def preprocesare(col):
    anterior = 0
    res = []
    for i in range(1,len(col)):
        if col[i] <= 0.0:
            res.append(col[anterior+1:i])
            anterior = i
    return res

def get_val_col(a):
    line = 0.0
    column = 0.0
    val = [0.0]
    col = [-(line + 1)]

    nr = 0
    for i in range(len(a)):
        if (a[i][1] != a[i][2]):
            if (a[i][1] == line):
                if a[i][2] == column:
                    val[-1] += a[i][0]

                else:
                    val.append(a[i][0])
                    column = a[i][2]
                    col.append(column + 1)  # am incrementat coloana, oare e bine?
                    nr += 1

            else:
                for z in range(0, int(a[i][1] - line)):
                    # print "NR de 0-uri : " + str(a[i][1]-line) + " " + str(a[i][1]) + " " + str(line)
                    val.append(0.0)
                    col.append(-(line + 2 + z))

                val.append(a[i][0])
                line = a[i][1]
                column = a[i][2]
                col.append(column + 1)
                #if nr > 10:
                    #print "Prea multe valori: " + str(nr)
                nr = 1
        else:
            nr += 1

    val.append(0.0)
    col.append(-(line + 2))


    anterior = 0
    for i in range(1, len(col)):
        if col[i] < 0:
            quick(col, val, anterior, i - 1)
            anterior = i

    return val, col

def transpune(a):
    for i in a:
        i[1], i[2] = i[2], i[1]

    return a
def postprocesare_val(val):
    anterior = 0
    res = [0.0]
    for i in range(len(val)):
        res += val[i]
        res += [0.0]

    return res

def postprocesare_col(col):
    anterior = 0
    res = [-1.0]
    for i in range(len(col)):
        res += col[i]
        res += [-(i+2)]

    return res

class Matrice:
    def __init__(self):
        self.d = []
        self.val = []
        self.col = []

    def read_file(self, filename):
        with open(filename) as f:
            lines = f.readlines()

            self.n = int(lines[0])

            lines = [x[:-1] for x in lines[:] if x != '\n']

            self.b = [float(x) for x in lines[1:self.n + 1]]
            a = [[float(y) for y in re.split('[,| ]+', x)] for x in lines[self.n + 1:]]

            a = sorted(a, key=lambda x: x[1])

            self.d = [x[0] for x in a if x[1] == x[2]]

            self.val, self.col = get_val_col(a)

            self.a = a

    def values(self, d, val, col):
        self.d = d
        self.val = val
        self.col = col

    def transpusa(self):
        aT = transpune(self.a)
        aT = sorted(aT, key=lambda x: x[1])
        self.valT, self.colT = get_val_col(aT)
        self.a = []


def aduna(A, B):

    d_res = [ A.d[i] + B.d[i] for i in range(len(A.d))]

    val_res = []
    col_res = []
    i = 0; j = 0
    nr = 0

    while i<len(A.col) and j<len(B.col) :      #A[2] e col

        if A.col[i]<0 and A.col[i]==B.col[j]:
            val_res.append(0.0)
            nr += 1

            col_res.append(A.col[i])    #A[1] e val
            i += 1
            j += 1

        elif A.col[i]>0 and B.col[j]<0:  #!!!
            val_res.append(A.val[i])
            col_res.append(A.col[i])
            i += 1

        elif A.col[i]<0 and B.col[j]>0:
            val_res.append(B.val[j])
            col_res.append(B.col[j])
            j += 1

        elif A.col[i]>0 and A.col[i]==B.col[j]:
            val_res.append(A.val[i] + B.val[j])
            col_res.append(A.col[i])
            i += 1
            j += 1

        elif A.col[i]>0 and B.col[j]>0 and A.col[i] < B.col[j]:
            val_res.append(A.val[i])
            col_res.append(A.col[i])
            i +=1
            '''val_res.append(A[1][i])
            col_res.append(A[2][i])
            val_res.append(B[1][j])
            col_res.append(B[2][j])
            i += 1
            j += 1'''

        elif A.col[i] > 0 and B.col[j] > 0 and A.col[i] > B.col[j]:
            val_res.append(B.val[j])
            col_res.append(B.col[j])
            j += 1

    res = Matrice()
    res.values(d_res, val_res, col_res)

    return res



def elem_linii(lista):
    linii = []
    linia_anterioara = 0
    for i in range(len(lista)):
        if lista[i] == 0:
            linii += [lista[linia_anterioara: i]]
            linia_anterioara = i + 1
    linii += [lista[linia_anterioara:]]

    #print linii
    return linii

#valP = elem_linii(valP[0:])
#valr = elem_linii(valr[0:])

#valP = [sorted(x) for x in valP]
#valr = [sorted(x) for x in valr]


#print valP == valr
#print colP == colr
#print (dP,valP,colP) == aduna((dA,valA,colA),(dB,valB,colB))

def inmultire_vector(val,col,d,n):
    res = []
    anterior = 0
    for i in range(1,len(col)):
        if col[i] < 0.0:
            res.append(sum([ (n+1-col[i-j-1])*val[i-j-1] for j in range(len(col[anterior+1:i]))]) + d[int(-col[anterior])-1 ] * ((n+1+col[anterior])))

            anterior = i

    return res

#bbA = inmultire_vector(valA,colA,dA,len(bA))

#print "Inmultire cu vecor",bA == bbA


def inmultire_vector_x(A, x):
    res = []
    anterior = 0
    n = len(A.d)
    for i in range(1,len(A.col)):
        if A.col[i] < 0.0:
            #print i,x[i]
            res.append(sum([ x[int(A.col[i - j - 1])-1] * A.val[i - j - 1] for j in range(len(A.col[anterior + 1:i]))]) + A.d[int(-A.col[anterior]) - 1] * x[int(-A.col[anterior]) - 1])
            anterior = i

    return res



def inmultire_matrici(A, B):
    B.transpusa()
    res_val = []
    res_col = []
    i = 1
    j = 1
    line_res = 0
    column_res = 0
    anterior_i = 0
    anterior_j = 0

    for i in range(1, len(A.col)):
        if A.col[i] < 0.0:
            j = 1
            anterior_j = 0
            res_val.append(0.0)
            line_res += 1
            res_col.append(-(line_res))
            column_res = 0
            while j < len(B.col):
                    if B.colT[j] < 0.0:
                        column_res += 1
                        if line_res != column_res:
                            suma = 0.0
                            if column_res in A.col[ anterior_i + 1: i ]:
                                suma += B.d[column_res - 1] * A.val[ A.col[anterior_i + 1: i].index(column_res) + anterior_i + 1]


                            if anterior_j != j + 1:
                                k = anterior_i + 1
                                p = anterior_j + 1
                                elem_diag_A = False

                                while k < anterior_i + 1 + len(A.col[anterior_i + 1: i]) and p < anterior_j + 1 + len(B.colT[anterior_j + 1: j]):

                                    if line_res == B.colT[p] and elem_diag_A == False:
                                        suma += A.d[ line_res - 1] * B.valT[p]
                                        elem_diag_A = True


                                    if A.col[k] == B.colT[p]:

                                        suma += A.val[k] * B.valT[p]
                                        k += 1
                                        p += 1

                                    elif A.col[k] < B.colT[p]:
                                        k += 1
                                    else:
                                        p += 1

                                while p < anterior_j + 1 + len(B.colT[anterior_j + 1: j]):
                                    if line_res == B.colT[p] and elem_diag_A == False:
                                        suma += A.d[line_res - 1] * B.valT[p]
                                        elem_diag_A = True

                                    p += 1

                            if suma != 0:
                                res_val.append(suma)
                                res_col.append(column_res)

                            anterior_j = j
                            j += 1
                        else:
                            anterior_j = j
                            j += 1
                    else:
                        j += 1

            anterior_i = i

    res_val.append(0.0)
    res_col.append(-(line_res + 1))

    res = Matrice()
    res.values([], res_val, res_col)

    return res

def pregatire(A, B):
    B.transpusa()
    A.val = preprocesare(A.val)
    A.col = preprocesare(A.col)
    B.val = preprocesare(B.val)
    B.col = preprocesare(B.col)
    B.valT = preprocesare(B.valT)
    B.colT = preprocesare(B.colT)
    return A, B

def post_pregatire(A, B):
    B.transpusa()
    A.val = postprocesare_val(A.val)
    A.col = postprocesare_col(A.col)
    B.val = postprocesare_val(B.val)
    B.col = postprocesare_col(B.col)
    B.valT = postprocesare_val(B.valT)
    B.colT = postprocesare_col(B.colT)
    return A, B

def inmultire_matrici_2(A, B):
    res_val = []
    res_col = []
    i = 1
    j = 1
    line_res = 0
    column_res = 0

    for i in range(len(A.col)):
        res_val.append(0.0)
        line_res += 1
        res_col.append(-(line_res))
        if len(A.col[i])>0:
            for j in range(len(B.colT)):
                if i != j:
                    suma = 0.0
                    if (j+1) in A.col[i]:
                        suma += B.d[j] * A.val[i][A.col[i].index(j+1)]

                    if len(B.colT[j])>0:
                        inters = set(A.col[i]).intersection(set(B.colT[j]))
                        if len(inters) > 0:
                            for k in inters:
                                #print A.col[i]
                                #print B.colT[j]
                                suma += A.val[i][A.col[i].index(k)]  * B.valT[j][B.colT[j].index(k)]

                    if (i+1) in B.colT[j]:
                        suma += A.d[i] * B.valT[j][B.colT[j].index(i+1)]

                    if suma != 0:
                        res_val.append(suma)
                        res_col.append(j+1)

    res_val.append(0.0)
    res_col.append(-(A.n + 1))

    res = Matrice()
    res.values([], res_val, res_col)

    return res



def multiply(A, B):
    dC = []
    for i in range(len(A.d)):
        sum = 0.0
        for k in range(len(A.val[i])):
            p = 0
            while p < len(B.col[int(A.col[i][k]) - 1]) and B.col[int(A.col[i][k]) - 1][p] <= i + 1:
                if B.col[int(A.col[i][k]) - 1][p] == i + 1:
                    sum += A.val[i][k] * B.val[int(A.col[i][k]) - 1][p]
                p += 1

        sum += A.d[i] * B.d[i]
        dC.append(sum)

    return dC


#res = aduna(A, B)
'''
print O.val,"\n"
#print "adunare", res.val == P.val
start = time.time()
inm = inmultire_matrici(A, B)
print time.time() - start

#with open("out.txt","w")
'''



#x = range(1,len(A.b) + 1)
#x.reverse()
#print x

#bbA = inmultire_vector_x(A,x)

#print "Inmultire cu vector x",A.b == bbA


































