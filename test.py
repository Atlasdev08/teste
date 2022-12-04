
import requests

headers = requests.utils.default_headers()
headers.update({'User-agent': 'Mozilla/5.0'})
reponse = requests.get(str("https://www.vinted.fr/vetements?catalog%5B%5D=76&order=newest_first&price_to=15&currency=EUR&brand_id%5B%5D=304"), headers=headers)


print(reponse.content.decode() )
