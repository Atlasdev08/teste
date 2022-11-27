import requests


headers = requests.utils.default_headers()

reponse = requests.get(str("http://httpbin.org/ip'"))


print(reponse.texte )

