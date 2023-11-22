# Définition de la fonction check_sign
def check_sign(nombre):
    """
    Cette fonction prend un nombre en paramètre
    et affiche 'positif' s'il est supérieur à 0, 'negatif' sinon.
    """
    # Vérification du signe du nombre
    if nombre > 0:
        print("Positif")
    elif nombre < 0:
        print("Negatif")
    else:
        print("Le nombre est nul")

# Appels de la fonction avec différents paramètres
check_sign(5)
check_sign(-3)
check_sign(0)