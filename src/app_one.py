import requests

def first_request():
    request = requests.get("https://www.google.com/")
    return print (request.status_code)

first_request()