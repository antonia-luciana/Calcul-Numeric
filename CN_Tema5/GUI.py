from Tkinter import *
from tema import *
from nm import *

n = 4
A = creaza_A(int(n))

Anm = creaza_Anm(3, 4)

def afiseaza(A, metoda, label):
    res, iteratii = metoda(A)
    n = len(A)
    text = ""
    if type(res) == type("ana"):
        text = res + "\n" + "Nr de iteratii: " + str(iteratii)
    else:
        if len(res) <= 5:
            for row in res:
                text += str(row) + "\n"
        text += str(norma_infinit(diferenta_matrici(inmultire_matrici(A, res), matrice_I(n))) < pow(10, -5))
        text += "\n" + "NR de iteratii: " + str(iteratii)

    label.config(text = text)


def gui(top):

    btn1 = Button(top, text="Metoda 1", font="Georgia 10 italic bold",
                  command=lambda: afiseaza(A, metoda_iterativa_1, M1))
    btn1.pack()

    M1 = Label(top, text="", font="Georgia 12 bold", fg="indigo")
    M1.pack()

    btn2 = Button(top, text="Metoda 2", font="Georgia 10 italic bold",
                  command=lambda: afiseaza(A, metoda_iterativa_2, M2))
    btn2.pack()

    M2 = Label(top, text="", font="Georgia 12 bold", fg="dark green")
    M2.pack()

    btn3 = Button(top, text="Metoda 3", font="Georgia 10 italic bold",
                  command=lambda: afiseaza(A, metoda_iterativa_3, M3))
    btn3.pack()

    M3 = Label(top, text="", font="Georgia 12 bold", fg="blue")
    M3.pack()

    btn4 = Button(top, text="Solutie D", font="Georgia 10 italic bold",
                  command=lambda: afiseaza(A, metoda_4, M4))
    btn4.pack()

    M4 = Label(top, text="", font="Georgia 12 bold", fg="red")
    M4.pack()

    btn5 = Button(top, text="Matrice nepatratica", font="Georgia 10 italic bold",
                  command=lambda: afiseaza(Anm, metoda_iterativa_nm, M5))
    btn5.pack()

    M5 = Label(top, text="", font="Georgia 12 bold", fg="orange")
    M5.pack()

    top.geometry("400x400")




top = Tk()

top.title("Tema 5")
gui(top)


top.mainloop()
