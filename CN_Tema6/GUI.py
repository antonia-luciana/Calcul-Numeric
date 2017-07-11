from Tkinter import *
from tema import *

p = 9
nn = 6
n = 20

def afiseaza(p,n, label):
    rang, norma, nr_conditionare, As, n2,s = svd(p,n)

    text = "Rang: " + str(rang) + "\n"
    text += "Norma " + str(norma) + "\n"
    text += "Nr conditionare " + str(nr_conditionare) + "\n"
    #text += "As: " + str(As) + "\n"
    text += "s: " + str(s) + "\n"
    text += "Norma: " + str(n2) + "\n"

    label.config(text = text)

def afiseaza_prop_gen(n, label):
    M = A(n)
    g, v , k= metoda_puterii(M)
    eps = pow(10,-1)
    while g == None and eps < 1000:
        eps *= 10
        g, v, k = metoda_puterii(M, epsilon=eps)

    text = "Valoare proprie: " + str(g) + "\n"
    text += "Vector propriu: " + str(v) + "\n"
    text += "Iteratii: " + str(k) + "\n"

    label.config(text = text)


def afiseaza_prop_f( label):
    matrice = Matrice()
    matrice.read_file("m_rar_sim_2017.txt")
    if not isSimmetric(matrice):
        text = "NU este simetrica!"
    else:
        g, v = metoda_puterii(matrice)
        text = "Valaore proprie: " + str(g) + "\n"
        text += "Vector propriu: " + str(v) + "\n"

    label.config(text=text)


def gui(top):

    btn1 = Button(top, text="SVD Metoda 1", font="Georgia 10 italic bold",
                  command=lambda: afiseaza(p, nn, M1))
    btn1.pack()

    M1 = Label(top, text="", font="Georgia 12 bold", fg="indigo")
    M1.pack()

    btn2 = Button(top, text="Metoda puterii pt matrice generata", font="Georgia 10 italic bold",
                  command=lambda: afiseaza_prop_gen(n, M2))
    btn2.pack()

    M2 = Label(top, text="", font="Georgia 12 bold", fg="dark green")
    M2.pack()

    btn3 = Button(top, text="Metoda puterii pt fisier", font="Georgia 10 italic bold",
                  command=lambda: afiseaza_prop_f(A, M3))
    btn3.pack()
    M3 = Label(top, text="", font="Georgia 12 bold", fg="dark green")
    M3.pack()

    top.geometry("400x400")




top = Tk()

top.title("Tema 6")
gui(top)


top.mainloop()
