from thehive4py.api import TheHiveApi
from thehive4py.query import Eq

# Créez une instance de TheHiveApi en fournissant l'URL de votre instance TheHive et votre clé d'API
api = TheHiveApi("http://212.227.30.1:9000", "N0KIteIEhi6ayx7pV29TshQjpw5WBrfG")

# Récupérez les informations sur le cas en fournissant l'ID du cas
case = api.get_case("~344152")

case_id = "~50188336"
# Récupérez les observables du cas en fournissant l'ID du cas
observables = api.get_case_observables(case_id)

 # TODO: Impossible de récupérer les TTPs
# Créez un filtre pour n'inclure que les TTPs
ttp_filter = Eq("type", "ttp")

# Récupérez les TTPs du cas en utilisant la méthode find_observables avec le filtre ttp_filter
ttps = api.find_observables(query=ttp_filter)

# Récupérez les tâches du cas
tasks = api.get_case_tasks(case_id)

# Créez un dictionnaire vide pour stocker les informations fusionnées
merged_data = {}

# Fusionnez les informations sur le cas dans le dictionnaire merged_data
merged_data.update(case.json())

# Vérifiez si la réponse de l'API contient des observables
if not observables.json():
    # Si la réponse est vide, cela signifie qu'il n'y a pas d'observables pour ce cas
    merged_data["observables"] = "Ce case ne possède pas d'observables"
else:
    # Si la réponse contient des observables, ajoutez-les au dictionnaire merged_data
    merged_data["observables"] = observables.json()

# Vérifiez si la réponse de l'API contient des TTPs
if not ttps.json():
    # Si la réponse est vide, cela signifie qu'il n'y a pas de TTPs pour ce cas
    merged_data["ttps"] = "Ce case ne possède pas de TTPs"
else:
    # Si la réponse contient des TTPs, ajoutez-les au dictionnaire merged_data
    merged_data["ttps"] = ttps.json()

# Vérifiez si la réponse de l'API contient des tâches
if not tasks.json():
    # Si la réponse est vide, cela signifie qu'il n'y a pas de tâches pour ce cas
    merged_data["tasks"] = "Ce cas ne possède pas encore de tâches"
else:
    # Si la réponse contient des tâches, ajoutez-les au dictionnaire merged_data
    merged_data["tasks"] = tasks.json()

# Affichez le dictionnaire merged_data
print(merged_data)
