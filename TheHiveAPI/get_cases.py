import json
from thehive4py.api import TheHiveApi

hive_url = 'http://IP:9000'
token = "TOKEN"
organisation = "Cyrop"

api = TheHiveApi(
    hive_url,
    token,
    organisation=organisation,
    version=5,
    cert=False)

# case = api.get_case("~344152")
#alert = api.get_alert("~81924248")
observable = api.get_case_observable("~41300096")
#all_observables = api.find_observables()
#all_case = api.find_cases()
# all_alerts = api.find_alerts()
# all_tasks = api.find_tasks()

# print(json.dumps(case.json()))
#print(json.dumps(alert.json()))
print(json.dumps(observable.json()))
#print(json.dumps(all_observables.json()))
#print(json.dumps(all_case.json()))
# print(json.dumps(all_alerts.json()))
# print(json.dumps(all_tasks.json()))



