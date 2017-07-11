import random
import math
import copy

def semn(x):
    if x >= 0:
        return 1
    return -1

class P:
    def __init__(self, coef, z = []):
        self.coef = coef
        n = len(z)
        '''
        if n not in [0, 2]:
            raise Exception("Ai definit gresit nr complex!")
        if n == 2:
            self.c = z[0]
            self.d = z[1]
            self._complex = True
        else:
            self._complex = False
        '''

    def complex(self, z):
        c = z[0]
        d = z[1]

        if len(self.coef) == 1:
            return self.coef[0] * c, self.coef[0] * d

        p = -2*c
        q = pow(c, 2) + pow(d, 2)

        n = len(self.coef)-1
        b = copy.deepcopy(self.coef)
        #print "coef si b", self.coef, b

        b[1] = self.coef[1] - p * b[0]

        for i in range(2,n+1):
            b[i] = self.coef[i] - p * b[i-1] + q * b[i-2]

        C = c * b[n-1] + b[n] + p*b[n-1]
        D = d * b[n-1]
        return (C, D)

    def calculate(self, x):
        if type(x) == type((1,2)):
            return self.complex(x)
        return self.horner(x)

    def horner(self, x):
        p = self.coef[0]
        #print "p", p
        for i in range(1, len(self.coef)):
            p = p * x + self.coef[i]

        return p

def derivata(p):
    n = len(p.coef)
    res =  [p.coef[i] * (n-1-i) for i in range(n)]
    del res[-1]

    return P(res)

def inmultire_complex(z1, z2):
    #print "In functia de inmultire",z1, z2
    return (z1[0]*z2[0] - z1[1]*z2[1], z1[0]*z2[1] + z1[0]*z2[0])

def const_complex(c, z):
    return c*z[0], c*z[1]
def scadere_complex(z1,z2):
    return z1[0]-z2[0], z1[1] - z2[1]

def impartire(z1, z2):
    #print "impartire", z1[0], z2
    a = z1[0]
    b = z1[1]
    c = z2[0]
    d = z2[1]
    numitor = pow(c,2) + pow(d,2)
    return ((a*c + b*d)/numitor , (b*c - a*d)/numitor)

def modul(z):
    return math.sqrt(pow(z[0], 2) + pow(z[1], 2))

def sqrt_c(z):
    r = modul(z)
    numitor =  modul( (z[0],z[1] + r))
    return const_complex(r , (z[0]/numitor, z[1] + r / numitor) )

def Laguerre_Complex(P):
    epsilon = pow(10, -4)
    kmax = 10000

    n = len(P.coef)

    A = max([abs(P.coef[i]) for i in range(n)])
    #print "A", A
    R = (P.coef[0] - A) / (P.coef[0])

    x0 = random.uniform(-R, R)
    x1 = random.uniform(-R, R)

    x = (x0, x1)
    k = 0
    #print "x initial", x
    while (1):
        deriv = derivata(P)
        deriv_val = deriv.calculate(x)
        #print "deriv val",deriv_val, P.calculate(x)
        H = scadere_complex( pow(n - 1, 2) * inmultire_complex(deriv_val, deriv_val) ,
                              const_complex((pow(n, 2) - n) , inmultire_complex(P.calculate(x) , derivata(deriv).calculate(x))))

        #print "H", H, "deriv val", deriv_val
        numitor = inmultire_complex(deriv_val , sqrt_c(H))
        z = P.calculate(x)
        #print "numitor", numitor, n
        delta_x = impartire( (n * z[0], n * z[1]) , numitor)
        if H < 0:
            break
        if modul(numitor) < epsilon:
            break

        x = ( x[0]-delta_x[0],  x[1]-delta_x[1])

        k += 1

        if modul(delta_x) < epsilon or k > kmax or modul(delta_x) > pow(10, 8):
            print delta_x, modul(delta_x),  modul(delta_x) <= pow(10,-5)
            break

    if modul(delta_x) <= epsilon*10:
        return x
    else:
        return "divergenta"


def Laguerre(P):
    epsilon = pow(10, -5)
    kmax = 10000

    n = len(P.coef)
    A = max([abs(P.coef[i]) for i in range(n)])

    R = (P.coef[0] - A) / (P.coef[0])
    print "R", R
    x0 = random.uniform(-R, R)
    #x0 = random.uniform(-2, 2)
    x = x0
    k=0
    #print "R", R,"x0", x0
    while(1):
        deriv = derivata(P)
        deriv_val = deriv.calculate(x)
        H = (pow(n-1, 2) * pow(deriv_val, 2)) - ((pow(n, 2) - n)* P.calculate(x) * derivata(deriv).calculate(x))
        numitor = deriv_val * semn(deriv_val) * math.sqrt(H)
        delta_x = (n * P.calculate(x))/numitor
        if H < 0:
            break
        if abs(numitor) < epsilon:
            break

        x -= delta_x
        k += 1

        if abs(delta_x) < epsilon or k > kmax or abs(delta_x) > pow(10, 8):
            print abs(delta_x) < epsilon , k > kmax , abs(delta_x) > pow(10, 8)
            print delta_x
            break

    if abs(delta_x) < epsilon:
        return x
    else:
        return "divergenta"


def F(x):
    return pow(x, 2) + pow(math.e, x)


def g(F, x, h = pow(10, -5)):
    return (3*F(x) - 4*F(x-h) + F(x - 2*h))/2*h

def FII(F, x,  h = pow(10, -5)):
    return (-F(x + 2*h) + 16*F(x + h) - 30*F(x) + 16*F(x - h) - F(x - 2*h))/(12*pow(x, 2))

def secanta(F):
    epsilon = pow(10, -6)
    kmax = 10000

    x0 = random.uniform(-2, 2)
    x1 = random.uniform(-2, 2)
    print x0, x1

    x = x0
    delta_x = (x1-x0)
    k = 0
    while(1):
        gx = g(F, x1)
        gx0 = g(F, x0)
        numitor = (gx - gx0)
        if numitor == 0 or abs(numitor) <= epsilon:
            delta_x = epsilon
        else:
            delta_x = (x1 - x0)*gx/numitor
        x -= delta_x
        k += 1
        if abs(delta_x) <= epsilon or k > kmax or abs(delta_x) > pow(10, 8):
            #print abs(delta_x) < epsilon, k > kmax, abs(delta_x) > pow(10, 8)
            #print delta_x
            break

    if abs(delta_x) <= epsilon:
        return x
    else:
        return "divergenta"


#print secanta(F)

def fprim(x):
    return pow(x,2)-4*x +3

f = P([1, -4, 3])
#print f.calculate((3,4))
print "REZ", secanta(fprim)


