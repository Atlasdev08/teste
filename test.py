import cfscrape
from bs4 import BeautifulSoup as bs

scraper=cfscrape.create_scraper()
reponse=scraper.get("https://www.vinted.fr/vetements?catalog%5B%5D=76&order=newest_first&price_to=15&currency=EUR&brand_id%5B%5D=304")
print(reponse.text)
