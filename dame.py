from tkinter import *

fen = Tk()

fen.geometry("550x600")
fen.resizable(width=0, height=0)

SIZE = 515

cnv = Canvas(fen, width=SIZE, height=SIZE, bg="ivory")
cnv.pack()


def carre(x, y, coul):  # Pour le damier
    cnv.create_rectangle(x, y, x + 50, y + 50, fill=coul)


def cercle(x, y, r, coul):  # Pour les pions
    cnv.create_oval(x - r, y - r, x + r, y + r, fill=coul)


def plateau():  # Fonction qui créer le plateau de jeux
    x, y = 10, 10

    for i in range(10):
        x = 10

        for j in range(10):

            if (i + j) % 2 == 0:
                carre(x, y, "ivory")

            else:
                carre(x, y, "brown")

            x += 50

        y += 50


def initPionsNoirs():  # Fonction qui place les pions du joueur noir.
    pad = 10
    pady = 50

    x, y = 55, 5

    for i in range(4):
        for j in range(5):
            cnv.create_oval(x + pad, y + pad, x + 50, y + 50, fill="black")
            x += 100

        y += pady
        if i%2 == 0:
            x -= 550
        else:
            x -= 450

def initPionsBlanc():  # Fonction qui place les pions du joueur blanc.
    pad = 10
    pady = 50

    x, y = 5, 455

    for i in range(4):
        for j in range(5):
            cnv.create_oval(x + pad, y + pad, x + 50, y + 50, fill="#E2BC74")
            x += 100

        y -= pady
        if i%2 == 0:
            x -= 450
        else:
            x -= 550

def clic(event): #coordonée du clic
    pad = 10
    x=event.x
    y=event.y
    cnv.create_oval(x + pad, y + pad, x + 50, y + 50, fill="black")
    print(x,y)
cnv.bind("<Button-1>",clic)



# Affichage :
plateau()
initPionsNoirs()
initPionsBlanc()

fen.mainloop()
