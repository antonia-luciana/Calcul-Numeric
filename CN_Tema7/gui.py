from Tkinter import *
import matplotlib.pyplot as plt
from tema import *


puncte_polinom = puncte_pol(1, 100, 50)
puncte_trigo_1 = puncte_trigo(0, (31 * math.pi)/16, 50)
puncte_trigo_2 = puncte_trigo(0, (31 * math.pi)/16, 50)
puncte_trigo_3 = puncte_trigo(0, (63 * math.pi)/32, 50)

def f(x):
    coef = [ 1, -12, 30, 12]
    res = 0
    for c in coef[:-1]:
        res += c * x
    res += coef[-1]
    return res

def horner( x):
    coef = [1, -12, 30, 12]   # coeficientii polinomului
    p = coef[0]
    for i in range(1, len(coef)):
        p = p * x + coef[i]
    return p

def t1(x):
    return math.sin(x) - math.cos(x)

def t2(x):
    return math.sin(2*x) + math.sin(x) - math.cos(3*x)

def t3(x):
    return pow(math.sin(x), 2) - pow(math.cos(x), 2)


def afiseaza( puncte, func, func_aprox, func_aprox_lista , label, punct_de_aprox, mod_grafic):
    epsilon = pow(10, -4)
    sol = func_aprox(puncte, func, punct_de_aprox)

    text = "Aproximare : " + str(sol)
    text += "\nDiferenta : " + str(abs(sol - func(punct_de_aprox)))

    label.config(text = text)
    grafic(puncte, func, func_aprox_lista, mod_grafic)

def grafic(puncte, func, func_aprox_lista, mod):
    plt.plot(puncte, [func(x) for x in puncte], 'g')
    plt.plot(puncte, func_aprox_lista(puncte, func, puncte), mod)

    plt.plot()
    plt.show()

def gui(top):

    btn1 = Button(top, text="Aproximare Lagrange", font="Georgia 10 italic bold",
                  command=lambda: afiseaza(puncte_polinom, horner ,aprox_lagrange, aprox_lagrange_lista, M1, 10, 'ro'))
    btn1.pack()

    M1 = Label(top, text="", font="Georgia 12 bold", fg="indigo")
    M1.pack()

    btn2 = Button(top, text="Aproximare Trigonometrica T1", font="Georgia 10 italic bold",
                  command=lambda: afiseaza(puncte_trigo_1, t1, trigo, trigo_lista, M2, math.pi/9, 'r--'))
    btn2.pack()

    M2 = Label(top, text="", font="Georgia 12 bold", fg="light blue")
    M2.pack()

    btn3 = Button(top, text="Aproximare Trigonometrica T2", font="Georgia 10 italic bold",
                  command=lambda: afiseaza(puncte_trigo_2, t2, trigo,trigo_lista, M3, math.pi/2, 'r--'))
    btn3.pack()

    M3 = Label(top, text="", font="Georgia 12 bold", fg="dark green")
    M3.pack()

    btn4 = Button(top, text="Aproximare Trigonometrica T2", font="Georgia 10 italic bold",
                  command=lambda: afiseaza(puncte_trigo_3, t3, trigo,trigo_lista, M4, math.pi/4, 'r--'))
    btn4.pack()

    M4 = Label(top, text="", font="Georgia 12 bold", fg="dark red")
    M4.pack()


    top.geometry("400x400")




top = Tk()

top.title("Tema 7")
gui(top)


top.mainloop()
