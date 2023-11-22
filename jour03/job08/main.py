# Définition de la fonction afficher_aliments
def afficher_aliments(type, saison):
    """
    Cette fonction prend deux paramètres : 'type' et 'saison',
    et affiche des aliments en fonction de ces valeurs.
    """
    # Vérification des valeurs de 'type' et 'saison' et affichage des aliments appropriés
    if type == "fruits" and saison == "hiver":
        print("Orange, mandarine et kiwi")
    elif type == "fruits" and saison == "ete":
        print("Poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
        print("Carotte, topinambour, endive")
    elif type == "legume" and saison == "ete":
        print("Artichaut, aubergine, navet")
    else:
        print("Aucune correspondance trouvée pour le type et la saison fournis.")

# Saisie utilisateur pour les paramètres
type_aliment = input("Entrez le type d'aliment (fruits ou legume) : ")
saison_aliment = input("Entrez la saison (hiver ou ete) : ")

# Appel de la fonction avec les saisies utilisateur comme paramètres
afficher_aliments(type_aliment, saison_aliment)