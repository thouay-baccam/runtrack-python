# Fonction pour vérifier si un nombre est premier
def est_premier(nombre):
    if nombre < 2:
        return False
    for i in range(2, int(nombre**0.5) + 1):
        if nombre % i == 0:
            return False
    return True

# Afficher les nombres premiers jusqu'à 1000
print("Nombres premiers jusqu'à 1000 :")
for num in range(2, 1001):
    if est_premier(num):
        print(num)