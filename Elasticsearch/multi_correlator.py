#!/usr/bin/env python3

import glob
import json

# Récupère la liste de tous les fichiers qui se nomment 'output-*' dans le répertoire courant
output_files = glob.glob('output-*')

# Dictionnaire pour enregistrer les corrélations trouvées
correlations = {
    "origine": [],
    "action": [],
    "statut": [],
    "cible_impactee": [],
    "technique": [],
    "vulnerabilite": []
}

# Ouvre le fichier 'etsi.json' en mode lecture
with open('etsi.json', 'r') as etsi_file:
    # Charge le contenu du fichier 'etsi.json' en tant qu'objet Python
    etsi_data = json.load(etsi_file)

    # Parcourt chaque fichier qui commence par 'output-'
    for output_file_path in output_files:
        # Ouvre le fichier en mode lecture
        with open(output_file_path, 'r') as output_file:
            # Lit le contenu du fichier
            output_data = output_file.read()

            # Parcourt chaque élément de la liste etsi_data
            for value in etsi_data:
                # Vérifie si la clé "id" est présente dans l'élément courant
                if "id" in value:

                    if any(value["id"].startswith("B.1.1.{}".format(i)) for i in range(1, 5)) and value[
                        "id"] in output_data:
                        # Ajoute la corrélation trouvée dans le dictionnaire
                        correlations["origine"].append(value["description"])

                    # Vérifie si la valeur de la clé "id" commence par "B.1.2" et est présente dans le fichier output
                    elif value["id"].startswith("B.1.2") and value["id"] in output_data:
                        # Ajoute la corrélation trouvée dans le dictionnaire
                        correlations["action"].append(value["description"])
                    # Vérifie si la valeur de la clé "id" commence par "B.1.3" et est présente dans le fichier output
import glob
import json

# Récupère la liste de tous les fichiers qui se nomment 'output-*' dans le répertoire courant
output_files = glob.glob('output-*')

# Dictionnaire pour enregistrer les corrélations trouvées
correlations = {
    "origine": [],
    "action": [],
    "statut": [],
    "cible_impactee": [],
    "technique": [],
    "vulnerabilite": []
}

# Ouvre le fichier 'etsi.json' en mode lecture
with open('etsi.json', 'r') as etsi_file:
    # Charge le contenu du fichier 'etsi.json' en tant qu'objet Python
    etsi_data = json.load(etsi_file)

    # Parcourt chaque fichier qui commence par 'output-'
    for output_file_path in output_files:
        # Ouvre le fichier en mode lecture
        with open(output_file_path, 'r') as output_file:
            # Lit le contenu du fichier
            output_data = output_file.read()

            # Parcourt chaque élément de la liste etsi_data
            for value in etsi_data:
                # Vérifie si la clé "id" est présente dans l'élément courant
                if "id" in value:

                    if any(value["id"].startswith("B.1.1.{}".format(i)) for i in range(1, 5)) and value[
                        "id"] in output_data:
                        # Ajoute la corrélation trouvée dans le dictionnaire
                        correlations["origine"].append(value["description"])

                    # Vérifie si la valeur de la clé "id" commence par "B.1.2" et est présente dans le fichier output
                    elif value["id"].startswith("B.1.2") and value["id"] in output_data:
                        # Ajoute la corrélation trouvée dans le dictionnaire
                        correlations["action"].append(value["description"])
                    # Vérifie si la valeur de la clé "id" commence par "B.1.3" et est présente dans le fichier output
                    elif value["id"].startswith("B.1.3") and value["id"] in output_data:
                        # Ajoute la corrélation trouvée dans le dictionnaire
                        correlations["statut"].append(value["description"])
                    # Vérifie si la valeur de la clé "id" commence par "B.1.4" et est présente dans le fichier output
                    elif value["id"].startswith("B.1.4") and value["id"] in output_data:
                        # Ajoute la corrélation trouvée dans le dictionnaire
                        correlations["cible_impactee"].append(value["description"])
                    # Vérifie si la valeur de la clé "id" commence par "B.1.5" et est présente dans le fichier output
                    elif value["id"].startswith("B.1.5") and value["id"] in output_data:
                        # Ajoute la corrélation trouvée dans le dictionnaire
                        correlations["technique"].append(value["description"])
                    # Vérifie si la valeur de la clé "id" commence par "B.1.6" et est présente dans le fichier output
                    elif value["id"].startswith("B.1.6") and value["id"] in output_data:
                        # Ajoute la corrélation trouvée dans le dictionnaire
                        correlations["vulnerabilite"].append(value["description"])

# Affiche les corrélations trouvées
for origine in correlations["origine"]:
    print("L'origine probable de l'incident est : " + origine)
for action in correlations["action"]:
    print("L'action probable de l'incident est : " + action)
for statut in correlations["statut"]:
    print("Le statut probable de l'incident est : " + statut)