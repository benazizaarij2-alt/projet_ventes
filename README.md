# Analyse des ventes CSV

## 1. Description

Ce projet est un programme Python permettant de lire un fichier CSV contenant des informations sur des produits (identifiant, prix, quantité, remise).
Il calcule pour chaque produit :

* le chiffre d’affaires brut
* le chiffre d’affaires net après remise
* la TVA (20%)

Le programme affiche ensuite les résultats sous forme de tableau, calcule le chiffre d’affaires total, identifie le produit le plus rentable, génère un fichier de sortie CSV et crée un graphique.

---

## 2. Prérequis

Avant d’exécuter le projet, il est nécessaire d’installer :

* Python 3.x
* La bibliothèque matplotlib (pour le graphique)

Installation de matplotlib :

```bash
pip install matplotlib
```

---

## 3. Installation

1. Télécharger ou cloner le projet depuis le dépôt GitHub :

```bash
git clone <lien_du_projet>
```

2. Accéder au dossier du projet :

```bash
cd nom_du_projet
```

3. **Créer un environnement virtuel** :

**Sur Windows :**
```bash
python -m venv venv
venv\Scripts\activate
```

**Sur macOS/Linux :**
```bash
python3 -m venv venv
source venv/bin/activate
```

4. **Installer les dépendances** :

```bash
pip install -r requirements.txt
```

5. Vérifier que le fichier `ventes.csv` est présent dans le dossier.

---

## 4. Utilisation

1. Lancer le programme avec la commande :

```bash
python main.py
```

2. Saisir le nombre de produits à analyser lorsque demandé.

3. Le programme :

* affiche les résultats dans la console
* calcule le chiffre d’affaires total
* indique le produit le plus rentable
* génère un fichier `resultats_final.csv`
* crée un graphique enregistré sous le nom `graphique.png`

---

## 5. Auteurs

Projet réalisé par :

* Arij Ben aziza
Rami bra
Issam ammouri
