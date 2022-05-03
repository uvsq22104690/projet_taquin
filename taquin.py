# noms
# MITD04
# JOSEPH Kévin

# import des librairies
import tkinter as tk
import random as rd
import copy as cp

# variables

N = 4

taquin = []

grille = []

copie = []

listeint = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

solution = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

HAUTEUR = 400

LARGEUR = 400

i_vide, j_vide = 3, 3

resolvable = False

cpt = 0

coup_joue = []

# fonction + widgets


def initialisation():
    """ *Inititalise le taquin par une liste à deux dimensions et
        la remplit aléatoirement mais avec la case vide à la fin
        *Initialise la grille pour Tkinter par une liste à deux dimensions
        avec des id
        *Pour l'interface Tkinter, source:
        http://pascal.ortiz.free.fr/contents/tkinter/projets_tkinter/taquin/taquin.html
    """
    global N, taquin, grille, listeint
    for i in range(N):
        taquin.append([0]*N)
    grille = [0 for i in range(17)]
    for i in range(N):
        for j in range(N):
            n = rd.choice(listeint)
            taquin[i][j] = n
            listeint.remove(n)
            if len(listeint) < 1:
                listeint.append(16)
            x1 = 100 * j
            x2 = 100 * (j + 1)
            x3 = 100 * j + 50
            y1 = 100 * i
            y2 = 100 * (i + 1)
            y3 = 100 * i + 50
            carre = canvas.create_rectangle((x1, y1), (x2, y2), fill='brown')
            val = taquin[i][j]
            valeur = canvas.create_text((x3, y3), text=val,
                                        fill='light green', font=('Helvetica',
                                                                  25))
            grille[val] = carre, valeur
    canvas.delete(carre), canvas.delete(valeur)


def deplacement(event):
    """ A partir d'in clic gauche, déplace les nombres et les id
        dans le taquin et la grille
        source:
        http://pascal.ortiz.free.fr/contents/tkinter/projets_tkinter/taquin/taquin.html
    """
    global N, taquin, grille, i_vide, j_vide, coup_joue
    x = event.x
    y = event.y
    i = y // 100
    j = x // 100
    val = taquin[i][j]
    carre, valeur = grille[val]
    if i == i_vide and j+1 == j_vide:
        canvas.move(carre, 100, 0)
        canvas.move(valeur, 100, 0)
        taquin[i][j], taquin[i_vide][j_vide] = \
            (taquin[i_vide][j_vide], taquin[i][j])
        retour = i_vide, j_vide
        coup_joue.append(retour)
        retour = 0
        i_vide = i
        j_vide = j
    elif i == i_vide and j-1 == j_vide:
        canvas.move(carre, -100, 0)
        canvas.move(valeur, -100, 0)
        taquin[i][j], taquin[i_vide][j_vide] = \
            (taquin[i_vide][j_vide], taquin[i][j])
        retour = i_vide, j_vide
        coup_joue.append(retour)
        retour = 0
        i_vide = i
        j_vide = j
    elif i+1 == i_vide and j == j_vide:
        canvas.move(carre, 0, 100)
        canvas.move(valeur, 0, 100)
        taquin[i][j], taquin[i_vide][j_vide] = \
            (taquin[i_vide][j_vide], taquin[i][j])
        retour = i_vide, j_vide
        coup_joue.append(retour)
        retour = 0
        i_vide = i
        j_vide = j
    elif i-1 == i_vide and j == j_vide:
        canvas.move(carre, 0, -100)
        canvas.move(valeur, 0, -100)
        taquin[i][j], taquin[i_vide][j_vide] = \
            (taquin[i_vide][j_vide], taquin[i][j])
        retour = i_vide, j_vide
        coup_joue.append(retour)
        retour = 0
        i_vide = i
        j_vide = j
    else:
        pass
    succes()


def succes():
    """ Si le taquin est résolu, affiche victoire et
        rend le clic gauche inactif
    """
    global taquin, solution
    if taquin == solution:
        label_information.config("VICTOIRE!!")
        canvas.unbind("<Button-1>")


# def retour_arriere():
#    """ A partir d'une liste qui indique les coordonnées
#        et la valeur du dernieer coup joué,
#        fait un retour en arrière
#    """
#    global N, taquin, grille, coup_joue, i_vide, j_vide
#    i, j = coup_joue[-1]
#    val = taquin[i][j]
#    carre, valeur = grille[val]
#    if i == i_vide and j+1 == j_vide:
#        canvas.move(carre, 100, 0)
#        canvas.move(valeur, 100, 0)
#        taquin[i][j], taquin[i_vide][j_vide] = \
#            (taquin[i_vide][j_vide], taquin[i][j])
#        i_vide = i
#        j_vide = j
#    elif i == i_vide and j-1 == j_vide:
#        canvas.move(carre, -100, 0)
#        canvas.move(valeur, -100, 0)
#        taquin[i][j], taquin[i_vide][j_vide] = \
#            (taquin[i_vide][j_vide], taquin[i][j])
#        i_vide = i
#        j_vide = j
#    elif i+1 == i_vide and j == j_vide:
#        canvas.move(carre, 0, 100)
#        canvas.move(valeur, 0, 100)
#        taquin[i][j], taquin[i_vide][j_vide] = \
#            (taquin[i_vide][j_vide], taquin[i][j])
#        i_vide = i
#        j_vide = j
#    elif i-1 == i_vide and j == j_vide:
#        canvas.move(carre, 0, -100)
#        canvas.move(valeur, 0, -100)
#        taquin[i][j], taquin[i_vide][j_vide] = \
#            (taquin[i_vide][j_vide], taquin[i][j])
#        i_vide = i
#        j_vide = j
#    del coup_joue[-1]


def save():
    """ sauvegarde dans un fichier
    """
    global N, taquin, grille
    fic = open("sauvegarde.txt", "w")
    fic.write(str(N))
    fic.write("\n")
    for i in range(N):
        for j in range(N):
            fic.write(str(taquin[i][j]) + " ")
    fic.write("\n")
    for i in range(N):
        fic.write(str(grille[i]))
    label_information.configure(text="Partie sauvegardée")
    fic.close()


# def load():
#    """ Charge un fichier
#    """
#    global N, taquin, grille
#    fic = open("sauvegarde.txt", "r")
#    ligne_1 = fic.readline()
#    ligne_2 = fic.readline()
#    ligne_3 = fic.readline()
#   for ligne in ligne_2:
#        terrain[i][j] = int(ligne)
#        j += 1
#        if j == N:
#            j = 0
#            i += 1
#    for ligne in ligne_3:
#        grille[i] = int(ligne)
#        i += 1


def resolution():
    """ permet de savoir si un taquin est resolvable en
        substituant les cases d'une copie du taquin et
        et rend actif le clic gauche
    """
    global N, taquin, copie, cpt, solution
    copie = cp.deepcopy(taquin)
    if copie[0][0] != 1:
        for i in range(N):
            for j in range(N):
                if copie[i][j] == 1:
                    copie[i][j], copie[0][0] = copie[0][0], copie[i][j]
                    cpt += 1
    if copie[0][1] != 2:
        for i in range(N):
            for j in range(N):
                if copie[i][j] == 2:
                    copie[i][j], copie[0][1] = copie[0][1], copie[i][j]
                    cpt += 1
    if copie[0][2] != 3:
        for i in range(N):
            for j in range(N):
                if copie[i][j] == 3:
                    copie[i][j], copie[0][2] = copie[0][2], copie[i][j]
                    cpt += 1
    if copie[0][3] != 4:
        for i in range(N):
            for j in range(N):
                if copie[i][j] == 4:
                    copie[i][j], copie[0][3] = copie[0][3], copie[i][j]
                    cpt += 1
    if copie[1][0] != 5:
        for i in range(N):
            for j in range(N):
                if copie[i][j] == 5:
                    copie[i][j], copie[1][0] = copie[1][0], copie[i][j]
                    cpt += 1
    if copie[1][1] != 6:
        for i in range(N):
            for j in range(N):
                if copie[i][j] == 6:
                    copie[i][j], copie[1][1] = copie[1][1], copie[i][j]
                    cpt += 1
    if copie[1][2] != 7:
        for i in range(N):
            for j in range(N):
                if copie[i][j] == 7:
                    copie[i][j], copie[1][2] = copie[1][2], copie[i][j]
                    cpt += 1
    if copie[1][3] != 8:
        for i in range(N):
            for j in range(N):
                if copie[i][j] == 8:
                    copie[i][j], copie[1][3] = copie[1][3], copie[i][j]
                    cpt += 1
    if copie[2][0] != 9:
        for i in range(N):
            for j in range(N):
                if copie[i][j] == 9:
                    copie[i][j], copie[2][0] = copie[2][0], copie[i][j]
                    cpt += 1
    if copie[2][1] != 10:
        for i in range(N):
            for j in range(N):
                if copie[i][j] == 10:
                    copie[i][j], copie[2][1] = copie[2][1], copie[i][j]
                    cpt += 1
    if copie[2][2] != 11:
        for i in range(N):
            for j in range(N):
                if copie[i][j] == 11:
                    copie[i][j], copie[2][2] = copie[2][2], copie[i][j]
                    cpt += 1
    if copie[2][3] != 12:
        for i in range(N):
            for j in range(N):
                if copie[i][j] == 12:
                    copie[i][j], copie[2][3] = copie[2][3], copie[i][j]
                    cpt += 1
    if copie[3][0] != 13:
        for i in range(N):
            for j in range(N):
                if copie[i][j] == 13:
                    copie[i][j], copie[3][0] = copie[3][0], copie[i][j]
                    cpt += 1
    if copie[3][1] != 14:
        for i in range(N):
            for j in range(N):
                if copie[i][j] == 14:
                    copie[i][j], copie[3][1] = copie[3][1], copie[i][j]
                    cpt += 1
    if copie[3][2] != 15:
        for i in range(N):
            for j in range(N):
                if copie[i][j] == 15:
                    copie[i][j], copie[3][2] = copie[3][2], copie[i][j]
                    cpt += 1
    if copie == solution:
        if cpt % 2 == 1:
            resolvable = False
        elif cpt % 2 == 0:
            resolvable = True
    if resolvable:
        canvas.bind("<Button-1>", deplacement)
        label_information.configure(text="A vous de jouer")
    else:
        label_information.configure(text="Non resolvable. Recommencez")


racine = tk.Tk()
racine.title("Jeu du Taquin")
canvas = tk.Canvas(racine, height=HAUTEUR, width=LARGEUR)
bouton_commencer = tk.Button(racine, text="Démarrer", command=initialisation)
bouton_resolvable = tk.Button(racine, text="Résolution", command=resolution)
bouton_save = tk.Button(racine, text="Sauvegarder", command=save)
bouton_load = tk.Button(racine, text="Charger")
bouton_back = tk.Button(racine, text="Retour en arrière")
label_information = tk.Label(racine, text="                  ")

canvas.grid(row=0, column=1, rowspan=5)
bouton_commencer.grid(row=0, column=0)
bouton_resolvable.grid(row=1, column=0)
bouton_save.grid(row=3, column=0)
bouton_load.grid(row=4, column=0)
bouton_back.grid(row=2, column=0)
label_information.grid(row=0, column=2)

racine.mainloop()
