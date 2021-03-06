

from timeit import default_timer
from tkinter import *
from tkinter import messagebox

import pygame



"""  
Utilisation : 

Il suffit de cliquer sur la case où se trouve le pion pour l'enlever de la case, 
pour le placer vous devez cliquer sur une case "Noire" vide.
Si vous souhaitez manger un pion adverse cliquez d'abord sur votre pion, ensuite, sur le pion a manger, 
et enfin sur la case ou derrière le pion mangé pour replacer le pion.


Tout a été fait en Tkinter, mais l'intégration de musique et de son on nécessité le module Pygame.

Pour installer le module pygame :
https://youtu.be/2IaxbUnoOzo
Vidéo de M. Pascal Ortiz.

"""

# Gestion de la musique et des sons :
"""
Music Credits : 

Titre:  Reset
Auteur: Jaunter
Source: https://jaunter.bandcamp.com
Licence: https://creativecommons.org/licenses/by/3.0/
Téléchargement (6MB): https://auboutdufil.com/?id=497
"""
pygame.mixer.init()
p = pygame.mixer.Sound('audio/pion.wav')
app = pygame.mixer.Sound('audio/applaud.wav')
pygame.mixer.music.load('audio/Jaunter-Reset.ogg')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

# Variables fixes :
SIZE= 700
pad = SIZE * 0.007
pady = SIZE * 0.1
ecart = SIZE * 0.1
x = SIZE * 0.02
y = SIZE * 0.02
n = 10

# Variables GLOBALE :
global alt
alt = 0

# Gestion de la fenêtre :
fen = Tk()
fen.title("Jeu de Dame")
fen.iconbitmap('images/dame.ico')
fen.geometry("890x850")
fen.resizable(False, False)
fen.configure(bg="#E9D7A6")

# Assigne les images a des variables :
pionNoir = PhotoImage(file = "images/pionNoir.png")
pionBlanc = PhotoImage(file = "images/pionBlanc.png")
caseB = PhotoImage(file = "images/caseB.png")
caseN = PhotoImage(file = "images/caseN.png")


global text_clock
text_clock = Label(fen, text="")

# LES FONCTIONS :

start = default_timer()

# Gestion de la matrice  :

def afficher(M):
    "Affiche une matrice en respectant les alignements par colonnes"
    w=[max([len(str(M[i][j])) for i in range(len(M))]) for j in range(len(M[0]))]
    for i in range(len(M)):
        for j in range(len(M[0])):
            print("%*s" %(w[j],str(M[i][j])), end= ' ')
        print()

def matriceNulle(n, p):
    "Constructeur de matrice de dimensions données"
    M=[]
    for i in range(n):
        L=[]
        for j in range(p):
            L.append(0)
        M.append(L)
    return M

# Gestion du jeux :

def tour():
    "Gère l'aternance des joueurs Blanc/Noir"
    global alt
    alt+=1

def siblanc(i,j):
    "Change la valeur de la case dans la matrice, refresh le damier."
    damier[i][j] =1
    for c in fen.winfo_children():
        c.destroy()
    affichage(damier)



def sinoir(i,j):
    "Change la valeur de la case dans la matrice, refresh le damier."
    damier[i][j] =1

    for c in fen.winfo_children():
        c.destroy()
    affichage(damier)



def sicaseN(i,j):
    "Change la valeur de la case dans la matrice, refresh le damier. Affiche le gagnant"
    global alt
    if alt%2==0:
        damier[i][j] =2

    else:
        damier[i][j] =3

    p.set_volume(1)
    p.play()
    affichage(damier)
    wb = win_game_blc(damier)
    wn = win_game_noir(damier)
    if wb == True:
        app.set_volume(0.6)
        app.play()
        messagebox.showinfo(title=None, message="Victoire des Blancs")

    else:
        pass

    if wn == True:
        app.set_volume(0.6)
        app.play()
        messagebox.showinfo(title=None, message="Victoire des Noirs")

    else:
        pass

def win_game_blc(damier):
    "test si les noirs on encore des pions"
    drapblanc = True
    for i in range(n):
        for j in range(n):
            if damier[i][j] == 3:
                drapblanc = False


    return drapblanc

def win_game_noir(damier):
    "test si les blancs on encore des pions"
    drapNoir = True
    for i in range(n):
        for j in range(n):
            if damier[i][j] == 2:
                drapNoir = False


    return drapNoir




# Fonction création des boutons :

def caseBlanche(i,j):
    button = Button(fen,image=caseB, width = 70,height =72)
    button.grid(column = j, row = i)

def caseNoire(i,j):
    button = Button(fen,image=caseN,command =lambda:[sicaseN(i,j)],width = 70,height = 72)
    button.grid(column = j, row = i)

def pionN(i,j):
    button = Button(fen, image=pionNoir,command = lambda:[sinoir(i,j)],width = 70,height = 72)
    button.grid(column = j, row = i)

def pionB(i,j):
    button = Button(fen, image=pionBlanc,command =lambda:[siblanc(i,j),],width = 70,height = 72)
    button.grid(column = j, row = i)



# Fonction création du plateau avec la matrice :
plateauv= matriceNulle(n,n)

def plateau(plateauv):

    for i in range(n):

        for j in range(n):

            if (i+j) %2 == 0:
                plateauv[i][j] = 0
            else:
                plateauv[i][j] = 1


    return plateauv

pl = plateau(plateauv)


def dami(pl):

    for i in range(4):

        for j in range(n):
            if pl[i][j] == 1:
                pl[i][j] = 3

    for o in range(6,n):

        for p in range(n):

            if pl[o][p] == 1:
                pl[o][p] = 2
    return pl

damier = dami(pl)

# Fonction pour recommencer une partie :
def recommencer():
    global text_clock, alt
    MsgBox = messagebox.askquestion(title=None, message="Voulez vous vraiment recommencer la partie ?")
    if MsgBox == 'yes':
        for c in fen.winfo_children():
            c.destroy()
        pl = plateau(plateauv)
        damier =dami(pl)
        alt = 0
        affichage(damier)
    else:
        pass

# Permet l'affichage du damier :

def affichage(damier):
    global text_clock
    for i in range(n):

        for j in range(n):

            if damier[i][j] == 0:
                caseBlanche(i, j)
            elif damier[i][j] ==1:
                caseNoire(i,j)
            elif damier[i][j] == 3:
                pionN(i,j)
            else:
                pionB(i,j)

    button = Button(fen, text="Fin de Tour", command=tour, fg ="ivory", bg="brown")
    button.grid(column = 11, row = 0)

    button_reset = Button(fen, text="Restart", command= recommencer, fg ="ivory", bg= "brown")
    button_reset.grid(column=11, row =1)

    text_clock = Label(fen, text="")
    text_clock.grid(column=11, row=5)



def updateTime():
    "Gestion du chrono. Cette fonction est en travaux et n'est pas au point."
    global text_clock
    now = default_timer() - start
    minutes, seconds = divmod(now, 60)
    hours, minutes = divmod(minutes, 60)
    str_time = "%d:%02d:%02d" % (hours, minutes, seconds)
    text_clock['text'] = str_time
    fen.after(1000, updateTime)


affichage(damier)

updateTime()
fen.mainloop()
