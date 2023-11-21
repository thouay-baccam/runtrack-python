# Importe le module string.
import string

# Crée une liste inversée des lettres minuscules.
lower = list(reversed(string.ascii_lowercase))
print("Reversed lowercase:", lower)

# Crée une liste inversée des lettres majuscules.
upper = list(reversed(string.ascii_uppercase))
print("Reversed uppercase:", upper)

# Crée une liste inversée des lettres minuscules et majuscules combinées.
alphabets = list(reversed(string.ascii_letters))
print("Reversed combined:", alphabets)