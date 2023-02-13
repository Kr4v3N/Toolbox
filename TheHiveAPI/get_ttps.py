from thehive4py.api import TheHiveApi
from thehive4py.query import Eq

api = TheHiveApi("http://IP:9000", "TOKEN")
case_id = "~50188336"

ttp_filter = Eq("type", "ttp")

ttps = api.find_observables(query=ttp_filter)

print(ttps.json())