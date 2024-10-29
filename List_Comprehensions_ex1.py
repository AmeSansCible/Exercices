ratings =  [4.3, 3.1, 5, 1.1]

# Vérifie si chaque élément de la liste correspond à ma condition
recommended = [rating > 4 for rating in ratings]

print (recommended)


ratings =  [4.3, 3.1, 5, 1.1]

# Me donne tous les éléments de la liste qui correspondent à ma condition
recommended = [rating for rating in ratings if rating > 4]

print (recommended)
