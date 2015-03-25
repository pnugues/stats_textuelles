# stats_textuelles
Le site contient des petits programmes Python de statistiques textuelles appliquées à Flaubert

Pour reproduire les analyses de l'article, vous avez le corpus des quatre textes provenant de Wikisource et les trois programmes en Python :

1. Le programme `symboles.py` calcule les fréquences relatives d’un texte. Il s’utilise de la manière suivante :

    `python3 symboles.py -[normalise] fichier`

    où l’option facultative `normalise` transforme toutes les lettres en majuscules et `fichier` contient le texte à analyser.

    On extrait l’ensemble des caractères de *Salammbô* avec leurs fréquences par la commande suivante :
    
    `python3 symboles.py corpus/salammbo.txt`

2. Le programme `divergence.py` calcule la divergence entre deux œuvres :

    `python3 divergence.py fichier_p fichier_q`

    Par exemple :
    
    `python3 divergence.py corpus/coeursimple.txt corpus/salammbo.txt`

    *Nota bene* : Le programme de calcul de DKL(P||Q) est assez simple à écrire, si ce n’est que l’on doit traiter le problème pratique suivant : la divergence de Kullback et Leibler n’est pas définie lorsqu’un caractère a une fréquence nulle dans la distribution Q ; on a alors une division par zéro. Ce cas se présente concrètement dans notre corpus, avec, par exemple, le caractère ñ qui est absent aussi bien de *Salammbô* que du *Conte de deux cités*, mais qu’on trouve dans *Notre-Dame de Paris* dans la phrase :

    Señor caballero, para comprar un pedaso de pan !

    Pour le résoudre, nous avons fait l’approximation suivante : lors du calcul de DKL(P||Q), nous n’avons considéré que les caractères communs aux deux distributions P et Q ; pour ñ, ceci signifie que nous l’avons tout simplement ignoré. Si cette façon de faire n’est pas complètement satisfaisante d’un point de théorique, elle simplifie beaucoup les calculs. Une amélioration possible du programme serait d’estimer les probabilités des fréquences nulles par une technique de lissage, Laplace (1820) ou autre.
3. Le programme `mots.py` calcule les fréquences des mots, des bigrammes et l’information mutuelle. Il s’utilise de la manière suivante :
    
    `python3 mots.py fichier option`

    où `option` peut être soit `mots`, `bigrammes`, ou `im` suivi d’une valeur de seuil. Par exemple
    *  `python3 mots.py corpus/salammbo.txt mots`

      calcule les fréquences des mots dans *Salammbô*.
    * `python3 mots.py corpus/notredame.txt bigrammes`

      calcule les fréquences des bigrammes dans *Notre-Dame de Paris*.
    * `python3 mots.py corpus/notredame.txt im 25`

    	calcule l’information mutuelle des bigrammes dans *Notre-Dame de Paris* et affiche les valeurs les plus hautes. Le seuil de bigrammes est de 25.
