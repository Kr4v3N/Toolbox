from thehive4py.api import TheHiveApi
from thehive4py.models import Alert, CaseTemplate

hive_url = 'http://IP:9000'
api_key = 'N0KIteIEhi6ayx7pV29TshQjpw5WBrfG'

thehive = TheHiveApi(hive_url, api_key, version=5,  organisation='Cyrop', cert=False)
data = {
    'title': 'template_title',
    'description': 'template_description',
    'severity': 3,
    'tags': [],
    'status': 'New',
    'type': 'alert_type',
    'source': 'alert_source',
    'sourceRef': 'alert_sourcetRef',
    'artifacts': [],
}
alert = Alert(**data)
print(alert.jsonify())
try:
    response = thehive.create_alert(alert)
    response.raise_for_status()
except Exception as e:
    print(e)
    print(response.json())

