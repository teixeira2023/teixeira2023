import cloudscraper
from bs4 import BeautifulSoup

scraper = cloudscraper.create_scraper()
r = scraper.get('https://bdjogos.com.br/index.php')
print("Status", r.status_code)
print(r.text[:500])
