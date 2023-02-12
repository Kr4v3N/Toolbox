import requests
import urllib
from bs4 import BeautifulSoup
import colorama

def perform_xss_scan(url, payloads_file):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Request failed with status code {response.status_code}")

    soup = BeautifulSoup(response.text, "html.parser")
    input_fields = soup.find_all('input')
    data = {}

    colorama.init()
    with open(payloads_file) as file:
        for payload in file:
            encoded_payload = urllib.parse.quote(payload)
            for field in input_fields:
                if field.has_attr('name'):
                    if field['name'].lower() == "submit":
                        data[field['name']] = "submit"
                    else:
                        data[field['name']] = encoded_payload
                        response = requests.post(url, data=data)
                        if response.status_code != 200:
                            raise Exception(f"Request failed with status code {response.status_code}")
                        elif payload in response.text or encoded_payload in response.text:
                            print(f'\033[32mPayload "{payload}" returned in input fields\033[0m')
                        else:
                            soup = BeautifulSoup(response.text, "html.parser")
                            if soup.body and payload in soup.body.get_text() or encoded_payload in soup.body.get_text():
                                print(f'\033[32mPayload "{payload}" returned in body\033[0m')
                        data = {}
    colorama.deinit()

try:
    url = 'http://testphp.vulnweb.com/search.php?test=query'
    payloads_file = '/home/kr4v3n/Documents/Projets divers/PYTHON DJANGO/Toolbox/XSS/XSS-payloads.txt'

    perform_xss_scan(url, payloads_file)
except Exception as e:
    print(f"An error occured: {e}")
