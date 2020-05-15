import requests
from bs4 import BeautifulSoup
import sys

if len (sys.argv) != 2 :
    print("Usage: python recipe_scraper.py URL")
    sys.exit (1)

headers = {'User-Agent': 'Mozilla/5.0'}
#url = "https://www.bbcgoodfood.com/recipes/orzo-tomato-soup" # sys.argv[1]
url = sys.argv[1]

requested_url = requests.get(url, headers=headers)

soup = BeautifulSoup(requested_url.text, 'html.parser')
results = soup.find(id='recipe-ingredients')

print("\n")
print(url)
print(soup.title.string)
print("\n")
for tag in results.find_all("li", recursive=True):
    print(tag.get('content'))
