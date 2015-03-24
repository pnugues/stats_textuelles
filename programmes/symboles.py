import sys
import re
from math import log
import locale

def normalise_texte(texte):
    texte = texte.upper()
    texte = re.sub(" +", " ", texte)
    texte = re.sub("\n+", "\n", texte)
    return texte

def compte_nonlettres(lettres):
    nonlettres = 0
    for lettre in lettres:
        if not lettre.isalpha():
            nonlettres += lettres[lettre]
    return nonlettres

def compte_lettres(texte):
    lettres = {}
    for c in texte:
        lettres[c] = lettres.get(c, 0) + 1
    return lettres

def imprime_tableau(lettres):
    lettres_liste = list(lettres.items())
    lettres_liste.sort()
    print(lettres_liste)
    return

def frequences_relatives(lettres):
    frequences = {}
    nbr_car = 0
    for lettre in lettres:
        nbr_car += lettres[lettre]
    for lettre in lettres:
        frequences[lettre] = lettres[lettre]/nbr_car
    return frequences

def entropie(frequence_relative):
    entropie = 0.0
    for lettre in frequence_relative:
        entropie -= frequence_relative[lettre] * log(frequence_relative[lettre])
    entropie = entropie/log(2)
    return entropie

loc = locale.getlocale()
locale.setlocale(locale.LC_ALL, loc)
locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
fichier = sys.argv[1]
option = ""
if fichier[0] == "-":
    option = fichier[1:] # La seule option possible est normalise
    fichier = sys.argv[2]
texte = open(fichier).read()
print("Nombre de caractères : ", len(texte))
if option == "normalise":
    texte = normalise_texte(texte)
print("Nombre de caractères après normalisation : ", len(texte))
lettres = compte_lettres(texte)
print("Nombre de caractères différents : ", len(lettres))
liste_lettres = list(lettres.keys())
liste_lettres.sort(key=locale.strxfrm)
print("Liste des caractères : ", liste_lettres)
# Pour retrouver l'entropie de Nugues (2014), page 88, enlever ce commentaire et ne pas normaliser le texte
#del(lettres["\n"])
frequence_rel = frequences_relatives(lettres)
entropie = entropie(frequence_rel)
print("Fréquences absolues:")
imprime_tableau(lettres)
nbr_nonlettres = compte_nonlettres(lettres)
print("Nbr. de caractères qui ne sont pas des lettres : ", nbr_nonlettres)
print("Fréquences relatives:")
imprime_tableau(frequence_rel)
print("Entropie : ", entropie)
