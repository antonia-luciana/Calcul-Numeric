import Tkinter as tk
import random
import math
import random
import time

global valori
valori = []
global Pi
global y
y = 0.0

global c1
c1 = 1.0/ math.factorial(3)
global c2
c2 = 1.0 / math.factorial(5)
global c3
c3 = 1.0 / math.factorial(7)
global c4
c4 = 1.0 / math.factorial(9)
global c5
c5 = 1.0 / math.factorial(11)
global c6
c6 = 1.0 / math.factorial(13)


def P1(x):
    return x*(1 + y *(-c1 + c2 *y))
    #return (x - c1 * x**3 + c2 * x**5)

def P2(x):
    return x*(1 + y*( -c1 + y*(c2 - c3*y)))
    #return (x - c1 * x**3 + c2 * x**5 - c3 * x**7)

def P3(x):
    return x*( 1 + y* (-c1 + y * ( c2 + y * (-c3 + c4*y))))
    #return (x - c1 * x**3 + c2 * x**5 - c3 * x**7+ c4 * x**9)

def P4(x):
    return x * ( 1 + y* (-0.166 + y * (0.00833 + y * (-c3 + c4 * y))) )
    #return (x - 0.166 * x**3 + 0.00833 * x**5 - c3 * x**7+ c4 * x**9)

def P5(x):
    return x * (1 + y* (-c1 + y* (c2 + y * ((-c3 + y * (c4 - c5 * y))))))
    #return (x - c1 * x**3 + c2 * x**5 - c3 * x**7+ c4 * x**9-c5 * x**11)

def P6(x):
    return x* (1 + y *(-c1 + y* (c2 + y*( -c3 + y* (c4 + y* (-c5 + c6*y ))))))
    #return (x - c1 * x**3 + c2 * x**5 - c3 * x**7+ c4 * x**9-c5 * x**11 + c6* x**13)


def Po1(x):
    return (x - c1 * x**3 + c2 * x**5)

def Po2(x):
    return (x - c1 * x**3 + c2 * x**5 - c3 * x**7)

def Po3(x):
    return (x - c1 * x**3 + c2 * x**5 - c3 * x**7+ c4 * x**9)

def Po4(x):
    return (x - 0.166 * x**3 + 0.00833 * x**5 - c3 * x**7+ c4 * x**9)

def Po5(x):
    return (x - c1 * x**3 + c2 * x**5 - c3 * x**7+ c4 * x**9-c5 * x**11)

def Po6(x):
    return (x - c1 * x**3 + c2 * x**5 - c3 * x**7+ c4 * x**9-c5 * x**11 + c6* x**13)




polinoame = dict()
for i in range(1,7):
    polinoame[i] = 0

Pi = [P1,P2,P3,P4,P5,P6]
valori = []

erori = dict()
for i in range(1,7):
    erori[i]=0.0


index =0
while index <10000:
    x = random.uniform(-math.pi/2,math.pi/2)
    valori.append(x)
    y = x ** 2
    curent_errors = [(i, abs(Pi[i](x) - math.sin(x))) for i in range(0, 6)]
    for i in range(0,6):
        erori[i+1] += curent_errors[i][1]
    index +=1

rez = sorted(erori.items(),key = lambda x:x[1])
print rez

timpi = []
for i in range(0,6):
    start = time.time()
    for v in valori:
        Pi[i](v)
    stop = time.time()
    timpi.append(stop-start)

print timpi

Pio = [Po1,Po2,Po3,Po4,Po5,Po6]
timpi_o = []
for i in range(0,6):
    start = time.time()
    for v in valori:
        Pio[i](v)
    stop = time.time()
    timpi_o.append(stop-start)

print timpi_o

def btn_ex1(label):
    label.config(text = precizia_masina())

def btn_ex2(label):
    label.config(text = str(asociativitate_adunare()))

def btn_ex3(label):
    (x,y,z) = inmultire_neasociativa()
    label.config(text = "x= " + str(x) +"\ny= " + str(y)+ "\nz= " + str(z) )

def btn_ex4(label):
    text = ""
    for i in range(1,7):
        text += str(i)+". "
        text += " P" + str(rez[i-1][0]) + "\n"

    label.config(text = text)

def btn_ex5(label1,label2):
    text = ""
    for i in range(1,7):
        text += "P"+str(i)+": " + str(timpi[i-1]) + "\n"
    label1.config(text = text)
    text2 = ""
    for i in range(1, 7):
        text2 += "P" + str(i) + ": " + str(timpi_o[i - 1]) + "\n"
    label2.config(text=text2)

def precizia_masina():
    u = 1.0
    u = u/10
    while (1.0 + u != 1.0):
        u = u/10

    return u

def asociativitate_adunare():
    x = 1.0
    y = precizia_masina()
    z = precizia_masina()
    if (x + y) + z == x + (y+z):
        return True
    else:
        return False

def inmultire_neasociativa():
    x = random.uniform(10.0,1000.0)
    y = random.uniform(0, 0.001)
    z = random.uniform(0, 0.001)
    while (x * y) * z == x * (y * z):
        y = random.uniform(0, 0.001)
        z = random.uniform(0, 0.001)
    return (x,y,z)

root = tk.Tk()

root.geometry("550x700")
tk.Label(root, text = "Exercitiul 1",font = "Georgia 12 bold").grid()

btn1 = tk.Button(root, text = "Precizia masina", font = "Georgia 10 italic", command = lambda: btn_ex1(l1)).grid()

l1 = tk.Label(root, font="Georgia 12 bold", fg="red" , width=30)
l1.grid()

tk.Label(root, text = "Exercitiul 2",font = "Georgia 12 bold").grid()
tk.Label(root, text = "a. Pentru x=1.0, y=z=precizie masina, adunarea este asociativa?",font = "Georgia 12 bold").grid()

btn2 = tk.Button(root, text = "(x + y) + z == x + (y+z) ?", font = "Georgia 10 italic", command = lambda: btn_ex2(l2)).grid()

l2 = tk.Label(root, font="Georgia 12 bold",fg="red",width=30)
l2.grid()

tk.Label(root, text = "b. Gastiti trei numere pentru care inmutirea este neasociativa:",font = "Georgia 12 bold").grid()
btn3 = tk.Button(root, text = " x, y, z = ?", font = "Georgia 10 italic", command = lambda: btn_ex3(l3)).grid()

l3 = tk.Label(root, font="Georgia 12 bold",fg="red",width=30)
l3.grid()

tk.Label(root, text = "Exercitiul 3",font = "Georgia 12 bold").grid()
btn4 = tk.Button(root, text = "Clasament", font = "Georgia 10 italic", command = lambda: btn_ex4(l4)).grid()

l4 = tk.Label(root, font="Georgia 12 bold",fg="red",width=30)
l4.grid()

tk.Label(root, text = "Timpi de executie petru fiecare polinom",font = "Georgia 12 bold").grid()
btn5 = tk.Button(root, text = "Timpi", font = "Georgia 10 italic", command = lambda: btn_ex5(l5,l6)).grid()

l6 = tk.Label(root, font="Georgia 12 bold",fg="red",width=30)
l6.grid()

l5 = tk.Label(root, font="Georgia 12 bold",fg="red",width=30)
l5.grid()





root.mainloop()





