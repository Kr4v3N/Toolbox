#!/usr/bin/env python3

# EXPLICATION DU CODE :
# On utilise la bibliothèque elasticsearch pour se connecter à un serveur Elasticsearch situé à l'adresse IP
# 192.168.130.8 sur le port 9200.
#
# L'objet "client" envoie une requête GET au serveur Elasticsearch pour récupérer les informations sur le cluster.
# Ces informations sont stockées dans l'objet "res".
#
# On crée un nouveau dictionnaire data qui contient un sous-ensemble des informations stockées dans res.
# Enfin, le code utilise la bibliothèque json pour formater le dictionnaire data en chaîne de caractères au format JSON
# et l'affiche en bleu.

from elasticsearch import Elasticsearch
import json

print()
print('\033[92m' + "Voici les informations concernant le cluster :" + '\033[0m')
print()

# Se connecte et récupère les informations sur le cluster
client = Elasticsearch("http://192.168.130.8:9200")
res = client.info()

# Créer un nouveau dictionnaire avec les informations que l'on souhaite afficher
data = {
    'name': res['name'],
    'cluster_name': res['cluster_name'],
    'version': res['version'],
    'tagline': res['tagline'],
}

# Affiche la sortie
print('\033[34m' + json.dumps(data, indent=2) + '\033[0m')

