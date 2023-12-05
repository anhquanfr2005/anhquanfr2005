import csv

def listeF(fichier : str) -> list[list[str]] :
    """Fonction qui lit le fichier en paramètre et le retourne sous forme de liste

    Args:
        fichier (str): chemin du fichier à parcourir

    Returns:
        list[list[str]]: liste contenant les listes de [ taille, timestamp ]
    """
    listeR : list[list[str]] = []
    
    with open(fichier, newline='') as csvfile:
        datareader = csv.reader(csvfile, delimiter= ',', quotechar='|')
        for ligne in datareader :
            print(ligne)# on passe en commentaire pour n'avoir que la liste que l'on souhaite
            listeR.append(ligne)
    
    return listeR

listeF("donnees.csv")

