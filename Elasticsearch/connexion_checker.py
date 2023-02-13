#!/usr/bin/env python3

# EXPLICATION DU CODE :
# Ce programme utilise la bibliothèque requests pour envoyer une requête GET au serveur Elasticsearch situé à l'adresse
# IP 192.168.130.8 sur le port 9200. La requête GET est utilisée pour obtenir des informations sur le serveur
# Elasticsearch, par exemple les versions des composants et les informations sur les indices.

# La réponse du serveur est stockée dans l'objet response. L'objet response possède plusieurs propriétés, notamment
# "content", qui contient le contenu de la réponse (en bytes). Le contenu de la réponse est converti en chaîne de
# caractères en utilisant la méthode "encode()" de la chaîne de caractères "You Know, for Search", puis stocké dans
# la variable substring.

# Ensuite, le programme vérifie si la chaîne de caractères substring se trouve dans le contenu de la réponse
# en utilisant l'opérateur "in".
# Si substring est présent, cela signifie que la réponse du serveur a été reçue correctement et que Elasticsearch est
# opérationnel.
# Dans ce cas, un message de confirmation est affiché en vert à l'aide de codes de couleur ANSI.
# Si substring n'est pas présent, cela signifie qu'il y a eu un problème lors de la réception de la réponse du serveur,
# et un message d'erreur est affiché en rouge.

import requests

substring = "You Know, for Search".encode()
response = requests.get("http://IP:9200")

if substring in response.content:
   print()
   print('\033[92m' + "Elasticsearch est opérationnel !" + '\033[0m')
else:
   print('\033[91m' + "Une erreur s'est produite, assurez-vous que le cluster est opérationnel !" + '\033[0m')

#####################################################################################################################

# EXPLICATION DU CODE :
# On utilise la bibliothèque elasticsearch pour se connecter à un serveur Elasticsearch situé à l'adresse IP 192.168.130.8
# sur le port 9200.
#
# La méthode "ping()" de l'objet client est utilisée pour envoyer une requête HEAD au serveur Elasticsearch.
# Si la réponse est positive, la méthode retourne "True", sinon elle retourne "False".
#
# Si la méthode "ping()" retourne "True", cela signifie que le serveur Elasticsearch est opérationnel et un message de
# confirmation est affiché en vert.
#
# Si la méthode ping() retourne "False", cela signifie qu'il y a eu un problème lors de la communication avec le serveur
# Elasticsearch, et un message d'erreur est affiché en rouge.

from elasticsearch import Elasticsearch

client = Elasticsearch("http://IP:9200")

if client.ping():
   print()
   print('\033[92m' + "Elasticsearch est opérationnel !" + '\033[0m')
else:
    print('\033[91m' + "Une erreur s'est produite, assurez-vous que le cluster est opérationnel !" + '\033[0m')

# Le code "\033[92m" indique le début de l'affichage en vert et le code "\033[0m" indique la fin de l'affichage
# en couleur.