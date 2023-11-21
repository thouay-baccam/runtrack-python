# Définition de la chaîne en multipliant "abcdefghijklmnopqrstuvwxyz" par 10
chaine = "abcdefghijklmnopqrstuvwxyz" * 10

# Définition de la variable n avec la valeur 40
n = 40

# Boucle for qui itère sur les valeurs de i de 1 à 39
for i in range(1, n):
    # Création d'un motif en extrayant les premiers 2*i - 2 caractères de la chaîne
    motif = chaine[:2*i - 2]

    # Affichage du motif actuel
    print(motif)
