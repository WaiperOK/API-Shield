import requests

def send_request(method, url, **kwargs):
    response = requests.request(method, url, **kwargs)
    return response
