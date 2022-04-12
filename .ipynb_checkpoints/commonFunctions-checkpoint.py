'''
commonFunctions.py
Module de fonctions communes entre les 2 notebooks
'''

def transform_year(intervalle):

''' 
Fonction transform_year
    Permet de définir une année au lieu d'un intervalle
Paramètres:
    Le dataframe contenant l'intervalle sous l'appellation "Année"
Retour:
    Le dataframe modifié
'''

    intervalle=intervalle.split("-") 
    intervalle=(int(intervalle[0])+int(intervalle[1]))/2
    return intervalle


def compare_content_dataframe(dataframe, list_to_compare):
'''
Fonction compare_content_dataframe 

Paramètres :
    - un dataframe, celui dans lequel se trouvent les données à comparer.
    - une liste qui contient les valeurs de l'autre fichier à comparer avec le dataframe.

Actions :
    On compare une liste à un dataframe contenant une colonne.
    - S'il y a correspondance, on stock "Oui" dans la liste.
    - Sinon, on stocke "Non"

    A la fin de la boucle, on a une liste de "oui" et/ou "non".
    On va la coller dans une nouvelle colonne dans le dataframe contenant la liste des pays.
    - Oui = on a trouvé une correspondane entre la liste et le dataframe. 
    - Non = l'inverse

Note : on stocke les oui et les non pour conserver la taille du fichier.

Retour:
    Le dataframe contenant 2 colonnes : le nom du pays, et son statut ("Oui"/"Non").
'''
    array = []
    new_df=dataframe.copy()
    for i in range  (0, len(dataframe)):
        for pays in dataframe.values[i]:
            if pays in list_to_compare:
                array.append("Oui")
            else:
                array.append("Non")  
    new_df["Present dans la liste"]=array
    return new_df


def search_for_potential_matching (missing_data_from_df1, missing_data_from_df2, list2, list1):
'''
Fonction search_for_potential_matching

Paramètres : 
    - Les 2 dataframes et les 2 listes de données uniques

Actions : 
    - Pour chaque entrée dans le premier dataframe, on regarde si on retrouve le nom dans la seconde liste.
        - Si on trouve une correspondance dans la liste, on stock le résultat de cette liste dans un tableau.
    - Pour chaque entrée dans le second dataframe, on regarde si on retrouve le nom dans la première liste.
        - Si on trouve une correspondance dans la liste, on stock le résultat du second dataframe dans un tableau.
Retour : 
     - Une liste de résultats contenant le nom des informations manquantes
'''
    potential_match=[]
    for missing_data in missing_data_from_df1:
        for element in list2:
            if missing_data.lower() in element.lower():
                print(f"Potential matching in second file for {element} :",element)
                potential_match.append(element)
    
    for missing_data2 in missing_data_from_df2:    
        for element2 in list1:
            if missing_data2.lower() in element2.lower():
                print(f"Potential matching in first file for {element2}:",missing_data2)
                potential_match.append(missing_data2)    
    return potential_match   