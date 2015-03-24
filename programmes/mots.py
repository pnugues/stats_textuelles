import sys, re, operator
from math import log

def decoupe_mots(texte):
    mots = re.split('[\s\-,;:!?.’\'«»()–...&‘’“”*—]+', texte)
    mots.remove('')
    return mots

def compte_mots(mots):
    c_mots = {}
    for mot in mots:
        c_mots[mot] = c_mots.get(mot, 0) + 1
    return c_mots

def compte_bigrammes(mots):
    c_bigrammes = {}
    i = 0
    while i < (len(mots) - 1):
        bigramme = mots[i] + ' ' + mots[i + 1]
        c_bigrammes[bigramme] = c_bigrammes.get(bigramme, 0) + 1
        i = i + 1
    return c_bigrammes

def info_mutuelle(c_mots, c_bigrammes, taille):
    c_info_mutuelle = {}
    for bigramme in c_bigrammes.keys():
        mot = bigramme.split()
        c_info_mutuelle[bigramme] = log(taille * c_bigrammes[bigramme]/(c_mots[mot[0]] * c_mots[mot[1]]))/log(2)
    return c_info_mutuelle


if len(sys.argv) < 3:
    print("Usage: python3 mots.py fichier option")
    print("option: [mots|bigrammes|im [seuil]]")
    exit(1)
else:
    fichier = sys.argv[1]
    option = sys.argv[2]
    
texte = open(fichier).read()
texte = texte.lower()
mots = decoupe_mots(texte)
#print(mots)
c_mots = compte_mots(mots)
c_bigrammes = compte_bigrammes(mots)
c_bigrammes_ordonnés = sorted(c_bigrammes.items(), key=operator.itemgetter(1))

c_mots_ordonnés = sorted(c_mots.items(), key=operator.itemgetter(1))
if option == "mots":
    print("Fréq. mots: ", c_mots_ordonnés)
    print("Total :", len(mots), "mots et", len(c_mots), "mots différents")
elif option == "bigrammes":
    print(c_bigrammes_ordonnés)
    print("Total : ", len(c_bigrammes), "bigrammes différents")
elif option == "im":
    seuil = 25
    if sys.argv[3:]:
        seuil = int(sys.argv[3])
    c_info_mutuelle = info_mutuelle(c_mots, c_bigrammes, len(mots))
    c_info_mutuelle_ordonnée = sorted(c_info_mutuelle.items(), key=operator.itemgetter(1))
    for bigramme_im in c_info_mutuelle_ordonnée:
        if c_bigrammes[bigramme_im[0]] >= seuil:
            mots_du_bigramme = bigramme_im[0].split()
            print(c_info_mutuelle[bigramme_im[0]], "\t", bigramme_im[0], "\t", c_bigrammes[bigramme_im[0]], "\t", c_mots[mots_du_bigramme[0]], "\t", c_mots[mots_du_bigramme[1]])
else:
    print("Usage: python3 mots.py fichier option")
    print("option: [mots|bigrammes|im [seuil]]")
