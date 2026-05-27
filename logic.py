import requests

def harvest_html(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text
