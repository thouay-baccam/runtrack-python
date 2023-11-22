# Définition de la fonction check_language
def check_language(langage):
    """
    Cette fonction prend une chaîne de caractères 'langage' en paramètre
    et affiche un message en fonction de la valeur de 'langage'.
    """
    # Vérification de la valeur de 'langage' et affichage du message approprié
    if langage == "JavaScript":
        print("Tu es un développeur web")
    elif langage == "Python":
        print("Tu es un développeur IA")
    elif langage == "Java":
        print("Tu es un développeur logiciel")
    elif langage == "ReactJS":
        print("Tu es un développeur mobile")
    else:
        print("Un jour, je serai le meilleur développeur...")

# Appels de la fonction avec différents paramètres
check_language("JavaScript")
check_language("Python")
check_language("Java")
check_language("ReactJS")
check_language("C++")