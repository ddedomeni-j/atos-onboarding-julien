# Versions testées : python 3.11, pandas 2.x
import pandas as pd
import matplotlib.pyplot as plt

# Petit dataset bidon
df = pd.DataFrame({
    "ville":   ["Paris", "Lyon", "Paris", "Marseille", "Lyon", "Paris"],
    "age":     [30, 25, 45, 28, 31, 22],
    "salaire": [42000, 38000, 65000, 35000, 41000, 30000],
    "tele":    [True, False, True, False, True, True],
})

# Inspection
print(df.head())
print()
print(df.info())
print()
print(df.describe(include="all"))

# Filtrage + sélection
print()
print(df[df["age"] > 28][["ville", "salaire"]])

# Groupby
print()
print(df.groupby("ville")["salaire"].mean().round(0))

# Petite visualisation (nécessite matplotlib)
df.groupby("ville")["salaire"].mean().plot.bar(title="Salaire moyen par ville")


# Exercice guidé
URL = "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv"
df = pd.read_csv(URL)

print("Exercice -----")
print(df.head)
print()
print(df.isna().sum())
print()
print("nbLignes:{}, nbColonnes:{}".format(df.shape[0], df.shape[1]))
print()
print("Masse moyenne : {}".format(df["body_mass_g"].mean()))
print()
print("Masse moyenne : {}".format(df["body_mass_g"].median()))
print()
print("Masse moyenne par espece : {}".format(df.groupby("species")["body_mass_g"].mean()))
print()
print("Masse moyenne par espece et par sexe : {}".format(df.groupby(["species", "sex"])["body_mass_g"].mean()))
print()
# df["is_large"] = df["body_mass_g"] > 4500
print("nbLignes:{}, nbColonnes:{}".format(df.shape[0], df.shape[1]))
print()
df["is_large"] = df["body_mass_g"].gt(4500)
print(df.head())
df.groupby("species")["body_mass_g"].mean().plot.bar(title="Masse moyenne par espece")
plt.show()