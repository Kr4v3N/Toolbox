from thehive4py.api import TheHiveApi
from thehive4py.query import Eq

api = TheHiveApi("http://212.227.30.1:9000", "N0KIteIEhi6ayx7pV29TshQjpw5WBrfG")
case_id = "~50188336"

ttp_filter = Eq("type", "ttp")

ttps = api.find_observables(query=ttp_filter)

print(ttps.json())