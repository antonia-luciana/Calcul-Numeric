from Tkinter import *
from Tema8 import *

p = 9
nn = 6
n = 20

pol = P([1,-4,3])

def afiseaza( pol, label):
    sol = Laguerre(pol)

    text = "Solutie : " + str(sol)
    text += "\nVerificare : " + str(pol.calculate(sol) < pow(10,-5))

    label.config(text = text)


def afiseaza_S( F, label):
    sol = secanta(F)

    text = "Solutie : " + str(sol)
    text += "\nVerificare : " + str(FII(F, sol) > 0)

    label.config(text = text)


def afiseaza_C( pol, label):
    sol = Laguerre_Complex(pol)

    text = "Solutie : " + str(sol)
    #text += "\nVerificare : " + str(pol.calculate(sol))

    label.config(text = text)




def gui(top):

    btn1 = Button(top, text="Laguerre", font="Georgia 10 italic bold",
                  command=lambda: afiseaza(pol, M1))
    btn1.pack()

    M1 = Label(top, text="", font="Georgia 12 bold", fg="indigo")
    M1.pack()

    btn2 = Button(top, text="Secanta", font="Georgia 10 italic bold",
                  command=lambda: afiseaza_S(F, M2))
    btn2.pack()

    M2 = Label(top, text="", font="Georgia 12 bold", fg="dark green")
    M2.pack()

    btn3 = Button(top, text="Laguerre Complex", font="Georgia 10 italic bold",
                  command=lambda: afiseaza_C(pol, M3))
    btn3.pack()

    M3 = Label(top, text="", font="Georgia 12 bold", fg="dark green")
    M3.pack()



    top.geometry("400x400")




top = Tk()

top.title("Tema 8")
gui(top)


top.mainloop()
