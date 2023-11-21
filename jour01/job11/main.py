# On commence par demander à l'utilisateur de fournir une chaîne de caractères.
string_input = input("Veuillez fournir une chaîne de caractères : ")

# Vérifions si la lettre 'e' est présente dans la chaîne.
if "e" in string_input:
    # Si 'e' est présent, affichons un message indiquant cela de manière professionnelle.
    print("La chaîne de caractères contient la lettre 'e'.")
else:
    # Si 'e' n'est pas présent, informons l'utilisateur de manière formelle.
    print("La chaîne de caractères ne contient pas la lettre 'e'.")
