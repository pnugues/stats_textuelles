import sys
from math import log


def compte_lettres(texte):
    lettres = {}
    for c in texte:
        lettres[c] = lettres.get(c, 0) + 1
    return lettres


def frequences_relatives(lettres):
    frequences = {}
    nbr_car = 0
    for lettre in lettres:
        nbr_car += lettres[lettre]
    for lettre in lettres:
        frequences[lettre] = lettres[lettre] / nbr_car
    return frequences


def entropie(frequence_relative):
    entropie = 0.0
    for lettre in frequence_relative:
        entropie -= frequence_relative[lettre] * log(frequence_relative[lettre])
    entropie = entropie / log(2)
    return entropie


def entropie_croisee(frequence_p, frequence_q):
    entropie_croisee = 0
    for lettre in frequence_p:
        if frequence_q.get(lettre, 0) != 0:  # Ici, on ignore les symboles manquants. Un lissage serait préférable
            entropie_croisee -= frequence_p[lettre] * log(frequence_q[lettre])
    entropie_croisee = entropie_croisee / log(2)
    return entropie_croisee


fichier_p = sys.argv[1]
fichier_q = sys.argv[2]
texte_p = open(fichier_p).read()
texte_q = open(fichier_q).read()
lettres_p = compte_lettres(texte_p)
lettres_q = compte_lettres(texte_q)

frequence_rel_p = frequences_relatives(lettres_p)
frequence_rel_q = frequences_relatives(lettres_q)
entropie_p = entropie(frequence_rel_p)
entropie_q = entropie(frequence_rel_q)
print("Entropie du texte P: ", entropie_p)
print("Entropie du texte Q: ", entropie_q)
entropie_croisee_v = entropie_croisee(frequence_rel_p, frequence_rel_q)
print("Entropie croisée : ", entropie_croisee_v)
print("Divergence D(P||Q) : ", - entropie_p + entropie_croisee_v)
