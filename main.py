def lire_fichier_csv(nom_fichier):
    """Lit un fichier CSV et retourne les données"""
    with open(nom_fichier, 'r', encoding='utf-8') as f:
        lignes = f.readlines()
    return lignes

def ecrire_fichier_csv(nom_fichier, contenu):
    """Écrit des données dans un fichier CSV"""
    with open(nom_fichier, 'w', encoding='utf-8') as f:
        for ligne in contenu:
            f.write(ligne + '\n')

print(" Lecture du fichier ventes.csv...")
lignes = lire_fichier_csv("ventes.csv")

entete = lignes[0].strip()
donnees = lignes[1:]

# Filtrer les lignes vides
donnees = [l for l in donnees if l.strip() != ""]

total_disponible = len(donnees)
print(f" {total_disponible} produits disponibles dans le fichier\n")

# ── SAISIE UTILISATEUR ──────────────────────────────────────
while True:
    try:
        n = int(input(f"Combien de produits voulez-vous analyser ? (1 à {total_disponible}) : "))
        if 1 <= n <= total_disponible:
            break
        else:
            print(f" Veuillez entrer un nombre entre 1 et {total_disponible}.")
    except ValueError:
        print(" Entrée invalide. Veuillez entrer un nombre entier.")

donnees = donnees[:n]
print(f"\n Analyse des {n} premiers produits...\n")
# ────────────────────────────────────────────────────────────

resultats = []
ca_total = 0
meilleur_ca = -1
id_meilleur_produit = None

for ligne in donnees:
    valeurs = ligne.strip().split(',')
    id_produit = int(valeurs[0])
    prix = float(valeurs[1])
    quantite = int(valeurs[2])
    remise = float(valeurs[3])
    
    ca_brut = prix * quantite
    ca_net = ca_brut * (1 - remise / 100)
    tva = ca_net * 0.20
    
    ca_total = ca_total + ca_net
    
    if ca_net > meilleur_ca:
        meilleur_ca = ca_net
        id_meilleur_produit = id_produit
    
    resultats.append([id_produit, prix, quantite, remise, ca_brut, ca_net, tva])

print("=" * 50)
print("RÉSULTATS PAR PRODUIT")
print("=" * 50)
print(f"{'ID':<6} {'Prix':<8} {'Qté':<6} {'Remise':<8} {'CA Brut':<12} {'CA Net':<12} {'TVA':<10}")
print("-" * 65)

for r in resultats:
    print(f"{r[0]:<6} {r[1]:<8.2f} {r[2]:<6} {r[3]:<8.0f} {r[4]:<12.2f} {r[5]:<12.2f} {r[6]:<10.2f}")

print("-" * 65)
print(f"\n CHIFFRE D'AFFAIRES TOTAL : {ca_total:.2f} €")
print(f" PRODUIT LE PLUS RENTABLE : ID {id_meilleur_produit} (CA Net = {meilleur_ca:.2f} €)")

lignes_sortie = ["ID,Prix,Quantité,Remise,CA_Brut,CA_Net,TVA"]
for r in resultats:
    lignes_sortie.append(f"{r[0]},{r[1]},{r[2]},{r[3]},{r[4]:.2f},{r[5]:.2f},{r[6]:.2f}")

ecrire_fichier_csv("resultats_final.csv", lignes_sortie)
print(f"\n Fichier 'resultats_final.csv' créé avec succès !")

try:
    import matplotlib.pyplot as plt
    
    ids = [r[0] for r in resultats]
    ca_nets = [r[5] for r in resultats]
    
    plt.figure(figsize=(10, 6))
    plt.bar(ids, ca_nets, color='skyblue')
    plt.title(f'Chiffre d\'affaires net par produit (top {n})')
    plt.xlabel('ID Produit')
    plt.ylabel('CA Net (€)')
    plt.savefig('graphique.png')
    print(" Graphique sauvegardé dans 'graphique.png'")
    
except:
    print(" Installe matplotlib avec : pip install matplotlib")