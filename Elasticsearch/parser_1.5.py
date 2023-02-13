#!/usr/bin/env python3

# EXPLICATION DU CODE :
# Ce code utilise la bibliothèque Elasticsearch pour se connecter à un cluster Elasticsearch et effectuer une recherche
# dans un index spécifique.
# Il récupère les résultats de la recherche et extrait certaines données de chaque document, comme l'identifiant (_id),
# l'adresse IP reçue (received_from), la date de création (createdAt), le type de document (type) et le titre (title).
# Ces données sont écrites dans un fichier texte avec le timestamp Unix actuel en tant qu'en-tête.
#
# Si un champ n'est pas présent dans un document, une valeur de substitution est utilisée à la place (le champ est introuvable).
# Il utilise également la bibliothèque ipaddress pour convertir la valeur du champ "received_from" en un objet
# ipaddress.IPv4Address ou ipaddress.IPv6Address, selon le type d'adresse IP contenu dans le champ.
# La bibliothèque json est utilisée pour décoder la chaîne JSON contenue dans le champ "received_from".
#
# Enfin, le code utilise l'horodatage actuel (obtenu grâce à l'appel à "time.time()") pour enregistrer un horodatage
# au début de chaque boucle dans le fichier de sortie.

import elasticsearch
import ipaddress
import json
import time

# Créer un client Elasticsearch pour se connecter au cluster
client = elasticsearch.Elasticsearch("http://IP:9200")

# Récupérer le timestamp Unix actuel en secondes
timestamp = int(time.time())

# Effectuer une recherche dans l'index "case-71" avec une taille de 10 résultats
res = client.search(index="case-93", size=10)

# Extraire les données des résultats de recherche
documents = res["hits"]["hits"]

# Définir la liste des champs à extraire
fields = ["_id", "id_case", "received_from", "createdAt", "type", "title"]

# Ouvrir un fichier pour l'écriture
with open("output-" + str(timestamp) + ".txt", "w") as f:
    # Écrire le timestamp Unix actuel dans le fichier
    f.write("Timestamp: " + str(timestamp) + "\n\n")

    # Parcourir chaque document dans les résultats de la recherche
    for doc in documents:
        # Parcourir chaque champ dans la liste des champs à extraire
        for field in fields:
            # Vérifier si le champ existe dans le document
            if field in doc:
                # Récupérer la valeur du champ
                value = doc[field]
            elif field in doc["_source"]:
                # Récupérer la valeur du champ dans les données du document (_source)
                value = doc["_source"][field]
                # Si le champ est "received_from", extraire l'adresse IP
                if field == "received_from":
                    value = json.loads(value)["ip"]
                    # Convertir l'adresse IP en objet ipaddress.IPv4Address ou ipaddress.
                    # Essayer de convertir l'adresse IP en objet ipaddress.IPv4Address
                    try:
                        value = ipaddress.IPv4Address(value)
                    # Si l'adresse IP est invalide pour un objet ipaddress.IPv4Address,
                    # essayer de convertir l'adresse IP en objet ipaddress.IPv6Address
                    except ipaddress.AddressValueError:
                        value = ipaddress.IPv6Address(value)
            else:
                # Si le champ n'existe pas, utiliser une valeur de substitution
                value = "(champ introuvable)"
            # Écrire le champ et sa valeur dans le fichier
            f.write(field + ": " + str(value) + "\n")
            # Ajouter une nouvelle ligne après chaque block de données
