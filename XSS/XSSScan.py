import requests
import urllib
from bs4 import BeautifulSoup
import colorama
import logging

def perform_xss_scan(url, payloads_file):
    # Configure log
    logging.basicConfig(filename='script_debug.log', filemode='w', encoding='utf-8', level=logging.DEBUG,
                        format='%(asctime)s: %(levelname)s: %(message)s')

    response = requests.get(url)
    if response.status_code != 200:
        logging.error(f"Request failed with status code {response.status_code}")
        raise Exception(f"Request failed with status code {response.status_code}")

    soup = BeautifulSoup(response.text, "html.parser")
    input_fields = soup.find_all('input')
    links = soup.find_all('a')
    data = {}

    colorama.init()
    with open(payloads_file) as file:
        for payload in file:
            encoded_payload = urllib.parse.quote(payload)

            for field in input_fields:
                # Check for XSS in hidden field
                if field.has_attr('type') and field['type'] == 'hidden':
                    if field.has_attr('name'):
                        data[field['name']] = encoded_payload
                        response = requests.post(url, data=data)
                        if response.status_code != 200:
                            logging.error(f"Request failed with status code {response.status_code}")
                            raise Exception(f"Request failed with status code {response.status_code}")
                        elif payload in response.text or encoded_payload in response.text:
                            print(f'\033[32mPayload "{payload}" returned in input fields\033[0m')
                            logging.info(f'Payload "{payload}" returned in input fields')
                        else:
                            soup = BeautifulSoup(response.text, "html.parser")
                            if soup.body and payload in soup.body.get_text() or encoded_payload in soup.body.get_text():
                                print(f'\033[32mPayload "{payload}" returned in body\033[0m')
                                logging.info(f'Payload "{payload}" returned in body')
                        data = {}

                elif field.has_attr('name'):
                    if field['name'].lower() == "submit":
                        data[field['name']] = "submit"
                    else:
                        data[field['name']] = encoded_payload
                        response = requests.post(url, data=data)
                        if response.status_code != 200:
                            logging.error(f"Request failed with status code {response.status_code}")
                            raise Exception(f"Request failed with status code {response.status_code}")
                        elif payload in response.text or encoded_payload in response.text:
                            logging.info(f'Payload "{payload}" returned in input fields')
                            print(f'\033[32mPayload "{payload}" returned in input fields\033[0m')
                        else:
                            soup = BeautifulSoup(response.text, "html.parser")
                            if soup.body and payload in soup.body.get_text() or encoded_payload in soup.body.get_text():
                                print(f'\033[32mPayload "{payload}" returned in body\033[0m')
                                logging.info(f'Payload "{payload}" returned in body')
                        data = {}

            # Check for XSS in JavaScript values
            if field.has_attr("onclick") or field.has_attr("onload") or field.has_attr("onsubmit"):
                for attr in ["onclick", "onload", "onsubmit"]:
                    if field.has_attr(attr):
                        original_value = field[attr]
                        field[attr] = encoded_payload
                        response = requests.get(url)
                        if response.status_code != 200:
                            raise Exception(f"Request failed with status code {response.status_code}")
                        elif payload in response.text or encoded_payload in response.text:
                            print(f'\033[32mPayload "{payload}" returned in {attr}\033[0m')
                            logging.info(f'Payload "{payload}" returned in {attr}')
                        field[attr] = original_value

            # Check for XSS in cookies
            for cookie in response.cookies.values():
                if payload in cookie or encoded_payload in cookie:
                    print(f'\033[32mPayload : "{payload}" returned in cookies\033[0m')
                    logging.info(f'Payload : "{payload}" returned in cookies')

            # Check for XSS in HTTP Header
            headers = {'X-XSS-Protection': encoded_payload}
            response = requests.get(url, headers=headers)
            if payload in response.text or encoded_payload in response.text:
                print(f'\033[32mPayload "{payload}" returned in HTTP headers\033[0m')
                logging.info(f'Payload "{payload}" returned in HTTP headers')

            # Check for XSS in URL parameters
            url_with_payload = url + "?" + urllib.parse.urlencode({'param': encoded_payload})
            response = requests.get(url_with_payload)
            if response.status_code != 200:
                raise Exception(f"Request failed with status code {response.status_code}")
            elif payload in response.text or encoded_payload in response.text:
                print(f'\033[32mPayload "{payload}" returned in URL parameters\033[0m')
                logging.info(f'Payload "{payload}" returned in URL parameters')

            # Check for XSS in links
            for link in links:
                if link.has_attr('href'):
                    original_link = link['href']
                    link['href'] = original_link + encoded_payload
                    response = requests.get(url)
                    if response.status_code != 200:
                        raise Exception(f"Request failed with status code {response.status_code}")
                    elif payload in response.text or encoded_payload in response.text:
                        print(f'\033[32mPayload "{payload}" returned in embedded link\033[0m')
                        logging.info(f'Payload "{payload}" returned in embedded link')
                    link['href'] = original_link

        colorama.deinit()

try:
    url = 'http://testphp.vulnweb.com/search.php'
    payloads_file = '/home/kr4v3n/Documents/Projets divers/PYTHON DJANGO/Toolbox/XSS/XSS-payloads.txt'
    perform_xss_scan(url, payloads_file)
except Exception as e:
    print(f"An error occured: {e}")
    logging.info(f"An error occured: {e}")

