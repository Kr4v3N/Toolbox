#!/usr/bin/env python3

# # EXPLICATION DU CODE :
# Ce code utilise la bibliothèque "requests" pour envoyer une requête GET au serveur Elasticsearch situé à l'adresse IP
# 192.168.130.8 sur le port 9200.
#
# La requête GET est envoyée au point de terminaison "/_cat/indices" de l'API de Elasticsearch, qui retourne des
# informations sur les indices du cluster.
#
# La réponse du serveur est stockée dans l'objet "response" qui possède plusieurs propriétés, notamment "text", qui contient
# le contenu de la réponse en tant que chaîne de caractères.
# Le code imprime le contenu de la réponse en utilisant la méthode "text" de l'objet "response".

import requests

# On définit le point de terminaison pour l'API "cat.indices"
endpoint = "http://192.168.130.8:9200/_cat/indices?v"

# On envoie une requête GET au point de terminaison
response = requests.get(endpoint)

# On imprime le texte de la réponse
print(response.text)

#######################################################################################################################

# EXPLICATION DU CODE :
# Ce code utilise la bibliothèque elasticsearch pour se connecter à un serveur Elasticsearch situé à l'adresse IP
# 192.168.130.8 sur le port 9200.
# L'objet "client" envoie une requête GET au point de terminaison "/cat/indices" de l'API de Elasticsearch, qui retourne
# des informations sur les indices du cluster.
# Ces informations sont stockées dans la variable "indexes".
# Il affiche la variable "indexes", qui contient une liste de dictionnaires avec des informations sur chaque
# index du cluster.

import elasticsearch

# On instancie un client pour le cluster Elasticsearch
client = elasticsearch.Elasticsearch("http://192.168.130.8:9200")

# On obtient une liste de tous les index du cluster
indexes = client.cat.indices(v=True)

# On affiche la liste
print(indexes)
