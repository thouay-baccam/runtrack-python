produit = {
    'nom': 'produit 1',
    'prix': 2,
    'quantite': 35
}

print("Détails du produit :")
print("Nom:", produit['nom'], "\nPrix unitaire:", produit['prix'], "€", "\nQuantité en stock:", produit['quantite'])

quantite_achat = input("Quelle est la quantité que vous souhaitez acheter? ")
cout_total = 2 * int(quantite_achat)
print("Le coût total de l'achat s'élève à", cout_total, "€")
print("")

produit['quantite'] -= int(quantite_achat)
print("Suite à l'achat :",
    "\nNom du produit:", produit['nom'], "\nPrix unitaire:", produit['prix'], "€", "\nQuantité en stock:", produit['quantite'])
print("")

produit['prix'] *= 1.1
print("Suite à une hausse de prix de 10% :",
    "\nNom du produit:", produit['nom'], "\nPrix unitaire ajusté:", produit['prix'], "€", "\nQuantité en stock:", produit['quantite'])
