
import requests
session = requests.session()
r = session.get("http://httpbin.org/ip")
print(r.text)

