# Définition de la fonction calcule
def calcule(num1, operator, num2):
    """
    Cette fonction prend trois paramètres : num1, operator, num2,
    et retourne le résultat de l'opération correspondante.
    """
    # Vérification du type d'opération et calcul du résultat
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        # Vérification pour éviter une division par zéro
        if num2 != 0:
            result = num1 / num2
        else:
            return "Erreur : Division par zéro"
    elif operator == '%':
        # Vérification pour éviter une opération de modulo par zéro
        if num2 != 0:
            result = num1 % num2
        else:
            return "Erreur : Modulo par zéro"
    else:
        return "Opérateur non reconnu"

    # Retour du résultat de l'opération
    return result

# Appel de la fonction avec différents paramètres
result1 = calcule(20, '+', 23)
result2 = calcule(13, '*', 9)
result3 = calcule(8, '/', 10)

# Affichage des résultats
print("Résultat 1:", result1)
print("Résultat 2:", result2)
print("Résultat 3:", result3)
