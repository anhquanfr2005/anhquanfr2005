# TD2, exercice 1, Groupe
# Morgan Pellé, Gwenn Travers
#23/11/2023

import csv

def lectureFichier(fichier : str) -> list[list[str]] :
    """Fonction qui lit le fichier en paramètre et le retourne sous forme de liste

    Args:
        fichier (str): chemin du fichier à parcourir

    Returns:
        list[list[str]]: liste contenant les listes de [ taille, timestamp ]
    """
    listeR : list[list[str]] = []
    
    with open(fichier, newline='') as csvfile :
        datareader = csv.reader(csvfile, delimiter= ',', quotechar='|')
        for ligne in datareader :
            # print(ligne) on passe en commentaire pour n'avoir que la liste que l'on souhaite
            listeR.append(ligne)
    
    return listeR



def transposer(listeParam : list[list[str]]) -> list[list[int]] :
    """Fonction qui retourne la transposée de la liste donnée en paramètre. La fonction caste 
    également les chaines de caractères en entier

    Args:
        listeParam (list[list[str]]): Liste de liste de chaines de caractères

    Returns:
        list[list[int]]: Liste de liste d'entier, premier élément -> taille du fichier, deuxième élément -> timestamp
    """
    listeR : list[list[int]] = [[], []]
    
    for elt in listeParam : #elt = élément
        # print(elt) #ou elt[0]
        listeR[0].append(int(elt[0])) # on rajoute liste[0] car c'est une liste de liste
        listeR[1].append(int(elt[1])) # on caste en entier
        
    
    return listeR



def calculValMini(listeParam : list[int]) -> int :
    mini : int = listeParam[0]
    
    #for i in range(1, len(listeParam)) :
    for elt in listeParam :
        if elt < mini :
            mini = elt
            
    
    return mini


def calculValMax(listeParam : list[int]) -> int :
    maxi : int = listeParam[0]
    
    for i in range(1, len(listeParam)) :
    # for elt in listeParam :
        if listeParam[i] > maxi :
            maxi = listeParam[i]
            
    
    return maxi


def calculValMoy(listeParam : list[int]) -> float :
    somme : int = 0
    for elt in listeParam :
        somme += elt
        
    return somme / len(listeParam)

def calculValMed(listeParam : list[int]) -> float :
    listeT : list[int] = sorted(listeParam) # sorted -> ordre croissant
    taille : int = len(listeT)
    milieu : int = taille // 2
    retour : int = 0
    
    print(listeT)
    print(milieu)
    if taille % 2 == 0 :
        retour = (listeT[milieu - 1] + listeT[milieu]) / 2
        
    else :
        retour = listeT[milieu]
    
    return retour
    
# ------------------- #
# Programme Principal #
# ------------------- #

# print("\nTest de la fonction lectureFichier() :")
# print(lectureFichier("resTailleDossier.csv"))

print("\nTest de la fonction transposer() :")
listeInit = lectureFichier("resTailleDossier.csv")
listeT = transposer(listeInit)
print(listeT)

print("Valeur minimal : ", calculValMini(listeT[0]))
print("Valeur maximal : ", calculValMax(listeT[0]))
print("Valeur moyenne : ", calculValMoy(listeT[0]))
print("Valeur médiane : ", calculValMed(listeT[0]))