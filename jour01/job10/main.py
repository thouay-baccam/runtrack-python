# On initialise le montant initial et le rendement annuel.
montant_initial = 4391
rendement_annuel = 30

# Affiche les informations pour l'année 2024.
print("2024:",
    "\nMontant Initial: €", montant_initial,
    "\nTaux de Rendement Annuel: ", rendement_annuel, "%",
    "\nGain Annuel: €", montant_initial * rendement_annuel / 100,
    "\n")

# Met à jour les valeurs pour l'année 2025 et affiche les informations.
montant_initial += 5000
rendement_annuel += 2
print("2025:",
    "\nMontant Initial: €", montant_initial,
    "\nTaux de Rendement Annuel: ", rendement_annuel, "%",
    "\nGain Annuel: €", montant_initial * rendement_annuel / 100,
    "\n")

# Modifie les valeurs pour l'année 2026 et affiche les informations.
montant_initial *= 0.9
rendement_annuel -= 1
print("2026:",
    "\nMontant Initial: €", montant_initial,
    "\nTaux de Rendement Annuel: ", rendement_annuel, "%",
    "\nGain Annuel: €", montant_initial * rendement_annuel / 100,
    "\n")
