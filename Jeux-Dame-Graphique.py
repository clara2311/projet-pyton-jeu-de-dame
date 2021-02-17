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
    ecart = 50
    cnv.create_rectangle(x, y, x + ecart, y + ecart, fill=coul)


def cercle(x, y, r, coul):
    "Permet de tracer les pions des joueurs"
    cnv.create_oval(x - r, y - r, x + r, y + r, fill=coul)


def plateau(x,y):
    "Permet de créer le plateau de jeux"

    for i in range(10):
        x = 10
        for j in range(10):

            if (i + j) % 2 == 0:
                carre(x, y, "ivory")
            else:
                carre(x, y, "brown")
            x += 50
        y += 50


def initPionsNoirs(pad,pady,x,y,ecart):
    "Permet de placer les pions du joueur noir"

    for i in range(4):

        for j in range(5):
            cnv.create_oval(x + pad, y + pad, x + ecart, y + ecart, fill="black")
            x += pady*2

        y += pady
        if i%2 == 0:
            x -= 550
        else:
            x -= 450

def initPionsBlanc(pad,pady,x,y,ecart):
    "Permet de placer les pions du joueur blanc"

    for i in range(4):

        for j in range(5):
            cnv.create_oval(x + pad, y + pad, x + ecart, y + ecart, fill="#E2BC74")
            x += pady*2

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

# On crée les variables utiles aux différents fonctions.
pad = 10
pady = 50
ecart = 50
x = 10
y = 10
# Interface Graphique :
# On appel les fonctions :
plateau(x,y)
initPionsNoirs(pad,pady,SIZE -460,SIZE - 510, ecart )
initPionsBlanc(pad,pady,SIZE - 510,SIZE - 60, ecart)

fen.mainloop()