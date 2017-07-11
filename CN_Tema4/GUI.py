from Tkinter import *
from Tema import *

A = get_matrice("m_rar_2017_1.txt")
B = get_matrice("m_rar_2017_2.txt")
C = get_matrice("m_rar_2017_3.txt")
D = get_matrice("m_rar_2017_4.txt")

solutie_A = [float(i)/3.0 for i in range(1, A.n+1)]
solutie_B = [1.0/3.0] * B.n
solutie_C = [1.0] * C.n
solutie_D = [float(i) for i in range(1, D.n+1)]
#print solutie_A
def verificare_diagonala(A):
    ok=1
    for i in range (len(A.d)):
        if A.d[i] ==0 :
            return False
    return True

def verif(A):
    for i in range(A.n):
        if abs(A.d[i])<sum([abs(A.val[i][j]) for j in range(len(A.val[i]))]):
            return False
    return True


def afiseaza_solutie(A, solutie, label):
    if verificare_diagonala(A)==True and verif(A)==True:
        (sol,it) = metoda_iterativa(A, 5)
        text = str(sol[:5]) + "..."
        text +=  "\n" + str( norma(dif(solutie, sol)) < pow(10, -5))
        text += "\n" + str(norma(dif(inmultire_vector_x(A, A.b), sol)) < pow(10, -5))
        text += "\nNumar de iteratii: " + str(it)
    else:
        text = "Divergenta!!"

    label.config( text = text)


def gui(top):

    btn1 = Button(top, text="Solutie A", font="Georgia 10 italic bold",
                  command=lambda: afiseaza_solutie(A, solutie_A, M1))
    btn1.pack()

    M1 = Label(top, text="", font="Georgia 12 bold", fg="purple")
    M1.pack()

    btn2 = Button(top, text="Solutie B", font="Georgia 10 italic bold",
                  command=lambda: afiseaza_solutie(B, solutie_B, M2))
    btn2.pack()

    M2 = Label(top, text="", font="Georgia 12 bold", fg="green")
    M2.pack()

    btn3 = Button(top, text="Solutie C", font="Georgia 10 italic bold",
                  command=lambda: afiseaza_solutie(C, solutie_C, M3))
    btn3.pack()

    M3 = Label(top, text="", font="Georgia 12 bold", fg="blue")
    M3.pack()

    btn4 = Button(top, text="Solutie D", font="Georgia 10 italic bold",
                  command=lambda: afiseaza_solutie(D, solutie_D, M4))
    btn4.pack()

    M4 = Label(top, text="", font="Georgia 12 bold", fg="red")
    M4.pack()

    top.geometry("400x400")


top = Tk()

gui(top)

top.mainloop()
