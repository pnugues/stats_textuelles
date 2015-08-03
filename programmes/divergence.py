import sys

from math import log


def compte_lettres(texte):
    lettres = {}
    for c in texte:
        lettres[c] = lettres.get(c, 0) + 1
    return lettres


def frequences_relatives(lettres):
    fréquences = {}
    nbr_car = 0
    for lettre in lettres:
        nbr_car += lettres[lettre]
    for lettre in lettres:
        fréquences[lettre] = lettres[lettre] / nbr_car
    return fréquences


def entropie(fréquence_relative):
    entropie = 0.0
    for lettre in fréquence_relative:
        entropie -= fréquence_relative[lettre] * log(fréquence_relative[lettre], 2.0)
    return entropie


def entropie_croisée(fréquence_p, fréquence_q):
    entropie_croisée = 0.0
    for lettre in fréquence_p:
        if fréquence_q.get(lettre, 0) != 0:  # Ici, on ignore les symboles manquants. Un lissage serait préférable
            entropie_croisée -= fréquence_p[lettre] * log(fréquence_q[lettre], 2.0)
    return entropie_croisée


fichier_p = sys.argv[1]
fichier_q = sys.argv[2]
texte_p = open(fichier_p).read()
texte_q = open(fichier_q).read()
lettres_p = compte_lettres(texte_p)
lettres_q = compte_lettres(texte_q)

fréquence_rel_p = frequences_relatives(lettres_p)
fréquence_rel_q = frequences_relatives(lettres_q)
entropie_p = entropie(fréquence_rel_p)
entropie_q = entropie(fréquence_rel_q)
print("Entropie du texte P: ", entropie_p)
print("Entropie du texte Q: ", entropie_q)
entropie_croisée_v = entropie_croisée(fréquence_rel_p, fréquence_rel_q)
print("Entropie croisée : ", entropie_croisée_v)
print("Divergence D(P||Q) : ", - entropie_p + entropie_croisée_v)
