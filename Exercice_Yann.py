# Générer un tableau 4x8 avec des saisies utilisateur
tableau_4x8 = []

# Boucle pour générer chaque ligne
for i in range(4):
    ligne = []

    # Boucle pour générer chaque colonne
    for j in range(8):
        # L'utilisateur doit saisir la valeur de chaque cellule
        valeur = input(f"Saisissez la valeur pour la ligne {i+1}, colonne {j+1}: ")
        ligne.append(valeur)

    # Ajouter la ligne au tableau
    tableau_4x8.append(ligne)

# Afficher le tableau
for ligne in tableau_4x8:
    print(ligne)