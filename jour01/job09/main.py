# Définition d'un dictionnaire représentant un produit avec son nom, son prix et sa quantité en stock.
produit = {
    'nom': 'produit 1',
    'prix': 2,
    'quantite': 35
}

# Affiche les détails du produit.
print("Détails du produit :")
print("Nom:", produit['nom'], "\nPrix unitaire:", produit['prix'], "€", "\nQuantité en stock:", produit['quantite'])

# Demande à l'utilisateur la quantité qu'il souhaite acheter.
quantite_achat = input("Quelle est la quantité que vous souhaitez acheter? ")

# Calcule le coût total de l'achat et l'affiche.
cout_total = produit['prix'] * int(quantite_achat)
print("Le coût total de l'achat s'élève à", cout_total, "€")
print("")

# Met à jour la quantité en stock du produit suite à l'achat.
produit['quantite'] -= int(quantite_achat)
print("Suite à l'achat :",
    "\nNom du produit:", produit['nom'], "\nPrix unitaire:", produit['prix'], "€", "\nQuantité en stock:", produit['quantite'])
print("")

# Augmente le prix unitaire du produit de 10% et affiche les informations mises à jour.
produit['prix'] *= 1.1
print("Suite à une hausse de prix de 10% :",
    "\nNom du produit:", produit['nom'], "\nPrix unitaire ajusté:", produit['prix'], "€", "\nQuantité en stock:", produit['quantite'])
