from Tkinter import *
from Tema3 import *

A = Matrice()
B = Matrice()
P = Matrice()
O = Matrice()
A.read_file("a.txt")
B.read_file("b.txt")
P.read_file("aplusb.txt")
O.read_file("aorib.txt")

def verfica_adunare(A1, B1, P, label, t):
    start = time.time()
    res = aduna(A1, B1)
    timp = time.time() - start

    label.config( text = str(res.val == P.val and res.col == P.col) )
    t.config(text="Timp de rulare: " + str(timp))

def verfica_inmultire(A1, B1, O, label, t):
    A1, B1 = pregatire(A1, B1)
    start = time.time()
    res = inmultire_matrici_2(A1, B1)
    timp = time.time() - start
    #A1, B1 = post_pregatire(A1,B1)
    label.config( text = str(res.val == O.val and res.col == O.col) )
    t.config(text= "Timp de rulare: " + str(timp))

x = range(1,len(A.d)+1)
x.reverse()

def verfica_inmultire_vector(M, x, label, b_time):
    start = time.time()
    res = inmultire_vector_x(M, x)
    timp = time.time() - start

    label.config(text=str(M.b == res))
    b_time.config(text="Timp de rulare: " + str(timp))


def gui(top):
    L1 = Label(top, text="Matricea A", font = "Georgia 12 bold")
    L1.pack()

    ad = Label(top, text= "d = " + str(A.d[:20]) + "..." , font = "Georgia 12 bold", fg="blue"  )
    ad.pack()

    aval = Label(top, text= "val = " + str(A.val[:20]) + "...", font="Georgia 12 bold", fg="green")
    aval.pack()

    acol = Label(top, text="val = " + str(A.col[:20]) + "...", font="Georgia 12 bold", fg="purple")
    acol.pack()

    btn1 = Button(top, text="Adunare Matrici", font="Georgia 10 italic bold",
                  command=lambda: verfica_adunare(A, B, P, add, add_time))
    btn1.pack()

    add = Label(top, text="", font="Georgia 12 bold", fg="red")
    add.pack()
    add_time = Label(top, text="", font="Georgia 12 bold", fg="black")
    add_time.pack()

    btn2 = Button(top, text="Inmultire Matrici", font="Georgia 10 italic bold",
                  command=lambda: verfica_inmultire(A, B, O, ori, ori_time))
    btn2.pack()

    ori = Label(top, text="", font="Georgia 12 bold", fg="red")
    ori.pack()
    ori_time = Label(top, text="", font="Georgia 12 bold", fg="black")
    ori_time.pack()

    btn2 = Button(top, text="Inmultire cu vector A", font="Georgia 10 italic bold",
                  command=lambda: verfica_inmultire_vector(A, x, b, b_time))
    btn2.pack()

    b = Label(top, text="", font="Georgia 12 bold", fg="red")
    b.pack()
    b_time = Label(top, text="", font="Georgia 12 bold", fg="black")
    b_time.pack()

    btn3 = Button(top, text="Inmultire cu vector B", font="Georgia 10 italic bold",
                  command=lambda: verfica_inmultire_vector(B, x, Bb, Bb_time))
    btn3.pack()

    Bb = Label(top, text="", font="Georgia 12 bold", fg="red")
    Bb.pack()
    Bb_time = Label(top, text="", font="Georgia 12 bold", fg="black")
    Bb_time.pack()







top = Tk()

gui(top)

top.mainloop()