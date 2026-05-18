import numpy as np

# Creation tableau de temperature
rng = np.random.default_rng(seed=42)
temperatures = rng.uniform(15, 30, size=(30))

print(temperatures)

# Calcul de la moyenne/mediane/ecart-type
mean_temp = np.mean(temperatures)
median_temp = np.median(temperatures)
std_temp = np.std(temperatures)

print(f"Moyenne: {mean_temp:.2f}°C")
print(f"Médiane: {median_temp:.2f}°C")
print(f"Écart-type: {std_temp:.2f}°C")

# Trouver les jours où la température était supérieure à 25°C
hot_days = np.where(temperatures > 25)[0]
print(f"Jours avec température > 25°C: {len(hot_days)}") 

# Remplacer les jours > à 28 degres par des nan
temperatures[temperatures > 28] = np.nan
print("Températures après remplacement des valeurs > 28°C par NaN:", temperatures)

# Calcul de la moyenne en ignorant les NaN
mean_temp_ignore_nan = np.nanmean(temperatures)
print(f"Moyenne en ignorant les NaN: {mean_temp_ignore_nan:.2f}°C")

# Matrice d'entiers
matrice_int = rng.uniform(0, 100, size=(5, 6)).astype(int)
print("Matrice d'entiers:\n", matrice_int)

colonne3 = matrice_int[:, 2]
print("Colonne 3 de la matrice:\n", colonne3)

lignes_paires = matrice_int[::2, :]

print("Lignes paires de la matrice:\n", lignes_paires)
