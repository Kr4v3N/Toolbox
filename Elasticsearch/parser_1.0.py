#!/usr/bin/env python3

import elasticsearch
import ipaddress
import json
import time

# Créer un client pour le cluster Elasticsearch
client = elasticsearch.Elasticsearch("http://192.168.0.33:9200")
# Si le cluster est joignable
if client.ping():
   # Obtenir le timestamp Unix actuel en secondes
   timestamp = int(time.time())
   # Rechercher tous les index qui correspondent au modèle "case-*"
   res = client.search(index="case-96", size=10)
   # Extraire les données des résultats de recherche
   datas = res["hits"]["hits"]

   # Ouvrir un fichier pour l'écriture
   with open("output-" + str(timestamp) + ".txt", "w") as f:
       # Obtenir l'horodatage actuel au format Unix
       timestamp = int(time.time())
       # Écrire l'horodatage dans le fichier
       f.write("Timestamp: " + str(timestamp) + "\n")
       f.write("\n")

       # Parcourir les données
       for doc in datas:
           # Vérifier si le champ "_id" existe
           if "_id" in doc:
               # Écrire le champ "_id" dans le fichier
               f.write("_id: " + doc["_id"] + "\n")
           else:
               # Écrivez un message si le champ n'existe pas
               f.write("_id: (champ introuvable)\n")
           if "id_case" in doc["_source"]:
               f.write("id_case: {}\n".format(doc["_source"]["id_case"]))
           else:
               f.write("id_case: (champ introuvable)\n")
           if "received_from" in doc["_source"]:
               # Récupérer la valeur du champ "received_from"
               received_from_string = doc["_source"]["received_from"]
               # Décoder la chaîne JSON
               received_from_dict = json.loads(received_from_string)
               # Récupérer l'adresse IP
               received_from_ip = received_from_dict["ip"]
               # Convertir la valeur en un objet ipaddress.IPv4Address ou ipaddress.IPv6Address
               try:
                   ip_address = ipaddress.IPv4Address(received_from_ip)
               except ipaddress.AddressValueError:
                   ip_address = ipaddress.IPv6Address(received_from_ip)
               # Écrire le champ "received_from" dans le fichier
               f.write("received_from: " + str(ip_address) + "\n")
           else:
               # Écrire un message si le champ n'existe pas
               f.write("received_from: (champ introuvable)\n")
           if "createdAt" in doc["_source"]:
               f.write("createdAt: {}\n".format(doc["_source"]["createdAt"]))
           else:
               f.write("createdAt: (champ introuvable)\n")
           if "type" in doc["_source"]:
               f.write("type: {}\n".format(doc["_source"]["type"]))
           else:
               f.write("type: (champ introuvable)\n")
           if "title" in doc["_source"]:
               f.write("title: " + doc["_source"]["title"] + "\n")
           else:
               f.write("Title: (champ introuvable)\n")
           # Vérifier si le champ "description" existe
           if "description" in doc["_source"]:
               # Écrire le champ 'description' dans le fichier
               f.write("description: " + doc["_source"]["description"] + "\n")
           else:
               # Écrire un message si le champ n'existe pas
               f.write("description: (champ introuvable)\n")
           if "tags" in doc["_source"]:
               f.write("tags: " + "\n")
               for tag in doc["_source"]["tags"]:
                   f.write("- " + tag + "\n")
           else:
               f.write("Tags: (champ introuvable)\n")
           if "impactedTarget" in doc["_source"]:
               f.write("impactedTarget: " + doc["_source"]["impactedTarget"] + "\n")
           else:
               f.write("impactedTarget: (champ introuvable)\n")
           if "actionPerformed" in doc["_source"]:
               f.write("actionPerformed: " + doc["_source"]["actionPerformed"] + "\n")
           else:
               f.write("actionPerformed: (champ introuvable)\n")
           if "status" in doc["_source"]:
               f.write("status: " + doc["_source"]["status"] + "\n")
           else:
               f.write("status: (champ introuvable)\n")
           if "origin" in doc["_source"]:
               f.write("origin: " + doc["_source"]["origin"] + "\n")
           else:
               f.write("origin: (champ introuvable)\n")
           # Ajouter une nouvelle ligne après chaque block de données
           f.write("\n")
   print('\033[92m' + "Done!" + '\033[0m')
else:
    print('\033[91m' + "Une erreur s'est produite, assurez-vous que le cluster est opérationnel !" + '\033[0m')


