#!/usr/bin/env python3
import json

# EXPLICATION DU CODE :
# Ce code utilise la bibliothèque elasticsearch pour se connecter à un serveur Elasticsearch situé à l'adresse IP
# 192.168.130.8 sur le port 9200.
# L'objet "client" envoie une requête de recherche à l'index "case-13" du cluster Elasticsearch.
# Les résultats de la recherche sont stockés dans l'objet "res".
# Il extrait les données des résultats de la recherche et les stocke dans la variable "data".
# Il ouvre un fichier nommé data.json en mode écriture et parcourt la liste des données.
# Les données sont ensuite converties en chaîne de caractères au format JSON et enregistrées dans un fichier
# nommé "data.json", avec une indentation de 4 espaces pour chaque niveau de clé.
# Enfin, le code imprime le message "Done!" pour indiquer la fin de l'écriture dans le fichier.

import elasticsearch
import json

# Créer un client pour le cluster Elasticsearch
client = elasticsearch.Elasticsearch("http://192.168.130.8:9200")

# Récupérer les données de l'index concerné
res = client.search(index="case-13")

# Extraire les données des résultats de recherche
data = res["hits"]

# Ouvre un fichier pour l'écriture
with open("data.json", "w") as f:
    # Parcourir le document
    for doc in data["hits"]:
        # Convertir les données en chaîne de caractères au format JSON
        doc_json = json.dumps(doc, indent=4)
        # Écrire la chaîne de caractères au format JSON dans le fichier
        f.write(doc_json)
        # Ajouter une nouvelle ligne après chaque data
        f.write("\n")

print('\033[92m' + "Done!" + '\033[0m')
