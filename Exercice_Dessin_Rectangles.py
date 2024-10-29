import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as patches

# Création de la figure et de l'axe
fig, ax = plt.subplots()

# Dessiner un rectangle
rectangle = patches.Rectangle((0.1, 0.1), 0.5, 0.3, linewidth=1, edgecolor='r', facecolor='none')
ax.add_patch(rectangle)

# Ajouter du texte au rectangle
ax.text(0.3, 0.2, 'Rectangle', fontsize=12, ha='center')

# Définir les limites des axes
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Afficher la figure
plt.show()