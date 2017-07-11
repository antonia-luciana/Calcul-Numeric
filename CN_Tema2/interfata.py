from Tema2 import *
from Tkinter import *

global A
A = []

global D
D = []

global epsilon
epsilon = 10**(-5)

with open("input.txt","r") as f:
    m = f.read()
    rows = m.split("\n")

    A = [ filter(None,(rows[i].split(" "))) for i in range(len(rows))]
    A = [map(str,x) for x in A ]
    A = [map(float,x) for x in A]
    print A

def reconstructie():
    global A
    for i in range(0,len(A)):
        for j in range(i+1,len(A)):
            A[j][i] = A[i][j]

def factorizare(btn1,btn2,btn3,enuntChol,fact,enuntD,LD):
    global D, Ainit
    #Ainit = copy.deepcopy(A)


    D = factorizare_Clolesky(A)
    if D==None:
        fact.config(text="NU se poate face impartire la 0!!",fg="red")
    else:

        enuntChol.config(text = "Matricea A dupa factorizare: ")
        text = ""
        for row in A:
            text += str(row) + "\n"
        fact.config(text = text)
        enuntD.config(text = "Matricea D")
        text = "diag( " + str(D) + " )"
        LD.config(text = text)
        btn1.config(state= "disabled")
        btn2.config(state="active")
        btn3.config(state="active")


def afisare_determinant(label):

    label.config(text = determinant_chol(D))

def afisare_rezolvare_sistem(btn,label1,label2):

    with open("vector.txt", "r") as f:
        m = f.read()
        #m = m[:-1]
        global b
        b = m.split(" ")
        b = filter(None,b)
        b = map(str,b)
        b = map(float,b)
    if len(b)==len(A):
        global x,xb

        x = rezolvare_sistem(A, D, b)
        reconstructie()
        xb = sc.solve(A, b)
        label1.config( text =  str(xb) )
        label2.config(text = str(x))
        print A
    else:
        label1.config( text = "Vectorul b nu corespunde!" )

def afisare_LU( label):
    I,L,U = sc.lu(A)
    label.config( text = str(L) + "\n\n" + str(U))

def afisare_verificare(label):
    print prod(A,x)
    text = ""

    text =  str(np.linalg.norm(( np.dot(A,xb) -b)) ) + " \n"
    text += str(norma(dif(prod(A,xb),b))) + "\n"
    text += str(np.linalg.norm((np.dot(A, x) - b))) + " \n"
    text += str(norma(dif(prod(A, x), b))) + "\n"
    text += "Solutia calculata de numpy este mai mica decat 10^(-9): " + str(np.linalg.norm((np.dot(A, xb) - b)) < 10 ** (-9)) + "\n"
    text += "Solutia calculata de noi este mai mica decat 10^(-9): " + str(norma(dif(prod(A, x), b)) < 10 ** (-9)) +"\n"
    label.config(text=text)

def gui(top):
    L1 = Label(top, text="Matricea A", font = "Georgia 12 bold")
    L1.pack()
    LA = Label(top, text= m, font = "Georgia 12 bold", fg="red"  )
    LA.pack()

    btn1 = Button(top, text="Factorizarea Choleski", font="Georgia 10 italic bold",
                  command=lambda: factorizare(btn1,btn2,btn3,enuntChol,fact,enuntD,LD))
    btn1.pack()

    enuntChol = Label(top, text="", font="Georgia 12 bold")
    enuntChol.pack()

    fact = Label(top, text="", font="Georgia 12 bold", fg="dark blue")
    fact.pack()

    enuntD = Label(top, text="", font="Georgia 12 bold")
    enuntD.pack()

    LD = Label(top, text="", font="Georgia 12 bold", fg="dark green")
    LD.pack()

    btn2 = Button(top, text="Determinant Choleski", font="Georgia 10 italic bold", state = "disable",
                  command=lambda: afisare_determinant(Ldet))
    btn2.pack()

    Ldet = Label(top, text="", font="Georgia 12 bold", fg="dark green")
    Ldet.pack()

    btn3 = Button(top, text="Rezolva Sistem", font="Georgia 10 italic bold", state = "disable",
                  command=lambda: afisare_rezolvare_sistem(btn3,Lx,Lx_biblioteca))
    btn3.pack()

    Lx = Label(top, text="", font="Georgia 12 bold", fg="dark red")
    Lx.pack()

    Lx_biblioteca = Label(top, text="", font="Georgia 12 bold", fg="dark blue")
    Lx_biblioteca.pack()

    btn4 = Button(top, text="Descompunere LU", font="Georgia 10 italic bold",
                  command=lambda: afisare_LU( Llu))
    btn4.pack()

   # L = Label(top, text="L si U", font="Georgia 12 bold")
    #L.pack()

    Llu = Label(top, text="", font="Georgia 12 bold", fg="blue")
    Llu.pack()

    btn5 = Button(top, text="Verifica solutie", font="Georgia 10 italic bold",
                  command=lambda: afisare_verificare( Lverif))
    btn5.pack()

    Lverif = Label(top, text="", font="Georgia 12 bold", fg="dark red")
    Lverif.pack()

top = Tk()

if A == transpusa(A) and det(A) != 0:
    gui(top)
else:
    L1 = Label(top, text="Matricea nu corespunde cerintelor!")
    L1.pack()

top.mainloop()




