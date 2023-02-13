#!/usr/bin/env python3

import sys
import os
import json
from colorama import Fore, Style


def read_file(file_path):
    """Lit le contenu d'un fichier et le renvoie sous forme d'objet Python.

    Args:
        file_path: Le chemin du fichier à lire.

    Returns:
        Le contenu du fichier sous forme d'objet Python.

    Raises:
        FileNotFoundError: Si le fichier spécifié n'existe pas.
        ValueError: Si le fichier n'est pas valide.
    """

    # Vérifie si le fichier existe
    if not os.path.isfile(file_path):
        raise FileNotFoundError("Le fichier {} n'existe pas.".format(file_path))

    # Récupère l'extension du fichier
    _, file_extension = os.path.splitext(file_path)

    try:
        # Ouvre le fichier en mode lecture
        with open(file_path, 'r') as file:
            # Si c'est un fichier JSON, charge le contenu du fichier en tant qu'objet Python
            if file_extension == '.json':
                return json.load(file)
            # Si c'est un fichier texte, renvoie le contenu du fichier sous forme de chaîne de caractères
            else:
                return file.read()
    except json.JSONDecodeError:
        raise ValueError(f"Le fichier {file_path} n'est pas un fichier JSON valide.")
    except UnicodeDecodeError:
        raise ValueError(f"Le fichier {file_path} n'est pas un fichier valide.")

def print_error(message):
    """Affiche un message d'erreur en rouge.

    Args:
        message: Le message à afficher.
    """
    print(Fore.RED + message + Style.RESET_ALL)

# Vérifie si les fichiers sont des fichiers JSON et texte
etsi_file_path = 'etsi.json'
output_file_path = 'output.txt'

# Ouvre les fichiers etsi.json et output en mode lecture et charge le contenu du fichier etsi.json
try:
    etsi_data = read_file(etsi_file_path)
    output_data = read_file(output_file_path)
except (FileNotFoundError, ValueError) as error:
    print(error)
    sys.exit(1)

# Indicateur pour savoir si une corrélation a été trouvée
correlation_found = False

# DEBUG
# for value in etsi_data:
#     print("id : " + value["id"] + ", description : " + value["description"])

# Parcourt chaque élément de la liste etsi_data
for value in etsi_data:

    # Vérifie si la clé "id" est présente dans l'élément courant
    if "id" in value:
        # Vérifie si la valeur de la clé "id" commence par "B.1.1." et est présente dans le fichier output
        if any(value[int("id")].startswith(f"B.1.1.{i}") for i in range(1, 5)) and value[int("id")] in output_data:
            # Affiche la phrase "L'origine probable de l'incident est : " suivie de la valeur de la clé "description"
            print()
            print(f"L'origine probable de l'incident est : {value['description']}")
            correlation_found = True

        # Vérifie si la valeur de la clé "id" commence par "B.1.2." et est présente dans le fichier output
        elif value["id"].startswith("B.1.2.") and value["id"] in output_data:
            # Affiche la phrase "L'action probable effectuée est la suivante : " suivie de la valeur de la clé "description"
            print()
            print(f"L'action probable effectuée est la suivante : {value['description']}")
            correlation_found = True

        # Vérifie si la valeur de la clé "id" commence par "B.1.3." et est présente dans le fichier output
        elif value["id"].startswith("B.1.3.") and value["id"] in output_data:
            # Affiche la phrase "Le résultat probable est le suivant : " suivie de la valeur de la clé "description"
            print()
            print(f"Le résultat probable est le suivant : {value['description']}")
            correlation_found = True

        # Vérifie si la valeur de la clé "id" commence par "B.1.4" et est présente dans le fichier output
        elif value["id"].startswith("B.1.4.") and value["id"] in output_data:
            # Affiche la phrase "La cible impactée et l'actif sont probablement les suivants :" suivie de la valeur de la clé "description"
            print()
            print(f"La cible impactée et l'actif sont probablement les suivants : {value['description']}")
            correlation_found = True

        # Vérifie si la valeur de la clé "id" comprise entre "B.1.5.1" et "B.1.5.11" et est présente dans le fichier output
        elif value["id"].startswith("B.1.5.") and value["id"] in output_data:
            # Affiche la phrase "La technique utilisée est probablement la suivante : " suivie de la valeur de la clé "description"
            print()
            print(f"La technique utilisée est probablement la suivante : {value['description']}")
            correlation_found = True

        # Vérifie si la valeur de la clé "id" commence par "B.1.6" et est présente dans le fichier output
        elif value["id"].startswith("B.1.6.") and value["id"] in output_data:
            # Affiche la phrase "La vulnérabilité exploitée est probablement la suivante : " suivie de la valeur de la clé "description"
            print()
            print(f"La vulnérabilité exploitée est probablement la suivante: {value['description']}")
            correlation_found = True

        # Vérifie si la valeur de la clé "id" commence par "B.1.7" et est présente dans le fichier output
        elif value[int("id")].startswith("B.1.7.") and value["id"] in output_data:
            # Affiche la phrase "Les conséquences sur la CIA sont les suivantes : " suivie de la valeur de la clé "description"
            print()
            print(f"Les conséquences sur la CIA sont les suivantes: {value['description']}")
            correlation_found = True

        # Vérifie si la valeur de la clé "id" commence par "B.1.8" et est présente dans le fichier output
        elif value["id"].startswith("B.1.8.") and value["id"] in output_data:
            # Affiche la phrase "Les conséquences commerciales sont les suivantes : " suivie de la valeur de la clé "description"
            print()
            print(f"Les conséquences commerciales sont les suivantes: {value['description']}")
            correlation_found = True

# Si aucune corrélation n'a été trouvée, affiche le message "Aucune corrélation trouvée !"
if not correlation_found:
    print()
    print_error("Aucune corrélation trouvée !")
