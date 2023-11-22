# Définition de la fonction 'food' avec deux paramètres: 'type' et 'saison'
def food(type, saison):
    # Vérifie si le type est "fruits" et la saison est "hiver"
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")
    
    # Vérifie si le type est "fruits" et la saison est "ete"
    if type == "fruits" and saison == "ete":
        print("poire, fraise, cassis")
    
    # Vérifie si le type est "legume" et la saison est "hiver"
    if type == "legume" and saison == "hiver":
        print("carotte, topinambour, endive")
    
    # Vérifie si le type est "legume" et la saison est "ete"
    if type == "legume" and saison == "ete":
        print("artichaut, aubergine, navet")

# Appels de la fonction 'food' avec différentes combinaisons de type et de saison
food("fruits", "hiver")
food("fruits", "ete")
food("legume", "hiver")
food("legume", "ete")
