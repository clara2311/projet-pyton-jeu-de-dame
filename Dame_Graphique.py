#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 10:44:01 2021

@author: valentinmerault
"""

from tkinter import *

# Fonction :
def carre(x, y, coul):
    "Permet de tracer des carre, utile au damier."
    cnv.create_rectangle(x, y, x + 50, y + 50, fill=coul)


def cercle(x, y, r, coul):
    "Permet de tracer les pions des joueurs"
    cnv.create_oval(x - r, y - r, x + r, y + r, fill=coul)


def plateau():
    "Permet de créer le plateau de jeux"
    x, y = 10, 10   # Coordonnée de base.

    for i in range(10):
        x = 10
        for j in range(10):

            if (i + j) % 2 == 0:
                carre(x, y, "ivory")
            else:
                carre(x, y, "brown")
            x += 50
        y += 50


def initPionsNoirs():
    "Permet de placer les pions du joueur noir"
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

def initPionsBlanc():
    "Permet de placer les pions du joueur blanc"
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

# Affichage :
fen = Tk()

fen.geometry("550x600")
fen.resizable(width=0, height=0) # Rend impossible le redimensionnement de la fenêtre.

SIZE = 515  # Longueur et Hauteur du canvas.

cnv = Canvas(fen, width=SIZE, height=SIZE, bg="ivory")
cnv.pack()

# On appel les fonctions :

# Interface Graphique :
plateau()
initPionsNoirs()
initPionsBlanc()

fen.mainloop()#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 10:44:01 2021

@author: valentinmerault
"""

from tkinter import *

# Fonction :
def carre(x, y, coul):
    "Permet de tracer des carre, utile au damier."
    cnv.create_rectangle(x, y, x + 50, y + 50, fill=coul)


def cercle(x, y, r, coul):
    "Permet de tracer les pions des joueurs"
    cnv.create_oval(x - r, y - r, x + r, y + r, fill=coul)


def plateau():
    "Permet de créer le plateau de jeux"
    x, y = 10, 10   # Coordonnée de base.

    for i in range(10):
        x = 10
        for j in range(10):

            if (i + j) % 2 == 0:
                carre(x, y, "ivory")
            else:
                carre(x, y, "brown")
            x += 50
        y += 50


def initPionsNoirs():
    "Permet de placer les pions du joueur noir"
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

def initPionsBlanc():
    "Permet de placer les pions du joueur blanc"
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

# Affichage :
fen = Tk()

fen.geometry("550x600")
fen.resizable(width=0, height=0) # Rend impossible le redimensionnement de la fenêtre.

SIZE = 515  # Longueur et Hauteur du canvas.

cnv = Canvas(fen, width=SIZE, height=SIZE, bg="ivory")
cnv.pack()

# On appel les fonctions :

# Interface Graphique :
plateau()
initPionsNoirs()
initPionsBlanc()

fen.mainloop()
