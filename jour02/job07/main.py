# Chaîne de caractères initiale
chaine = "abcdefghijklmnopqrstuvwxyz"

# Afficher une suite pyramidale de caractères
n = 26  # Nombre de lignes de la pyramide
for i in range(1, n + 1):
    espace = " " * (n - i)  # Ajouter des espaces pour aligner à droite
    motif = chaine[:i]  # Sélectionner les caractères de la chaîne
    ligne = espace + motif + motif[-2::-1]  # Construire la ligne de la pyramide
    print(ligne)