import csv

def csvToDict(f : str) -> dict[str,list[list[int]]]:
    """ Fonction chargeant les données stockées dans un fichier csv avec un séparateur
    `,` et retournant un dictionnaire où les clés sont les différents noms de fichiers
    décrits et les valeurs [taille en ko, timestamp] sont stockées dans une liste de
    listes
    @param fichier (str): Le nom du fichier à charger
    @return dict[str,list]: les clés sont les noms des fichiers observés et les
    valeurs une liste de dimension 2 [[taille,timestamp]]
    """
    """
    liste : list = [[ ??? , ??? ]] # on crée une liste à deux dimensions
dictionnaire[cle] = liste
#Attention à bien stocker des valeurs numériques dans votre liste

    dictionnaire[cle].append [???, ???] # on crée une liste simple
    """
    dictR : dict[str,list[list[int]]] = {}
    
    with open(f, newline='') as csvfile :
        datareader = csv.reader(csvfile, delimiter= ',', quotechar='|')
        for ligne in datareader :
            print(ligne[0])
            # on teste si la clé est deja présente ou pas
            if ligne[0] not in dictR.keys() : #clé non présente
                dictR[ligne[0]] = []
            
            dictR[ligne[0]].append([int(ligne[1]), int(ligne[2])])
            
            # clé deja présente
        
        
        return dictR
    

def augmentationMoyenne(valeurs : list[int]) -> float :
    return 0


print(csvToDict("resTaillesFichiers.csv"))
print("Augmentation moyenne : ", augmentationMoyenne(4))