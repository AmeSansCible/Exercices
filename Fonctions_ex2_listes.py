#Fonction pour calculer la moyenne de mes 3 classes
def calcul_moyenne(classe):
    moyenne = sum(classe) / len(classe)
    return moyenne

#Notes des classes
list_nombres1 = [6, 5.5, 4, 3.5, 3, 5, 6]
list_nombres2 = [6, 3.5, 4, 3.5, 3, 3, 6]
list_nombres3 = [5, 5.5, 4.5, 3.5, 3, 6, 6]

#Utilisation du paramètre de la fonction avec les différentes listes
print(calcul_moyenne(list_nombres1))
print(calcul_moyenne(list_nombres2))
print(calcul_moyenne(list_nombres3))