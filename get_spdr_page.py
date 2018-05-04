import requests, os, bs4

url = 'https://us.spdrs.com/en/product/index.seam'
os.makedirs('spdr_pages', exist_ok=True)

res = requests.get(url)
res.raise_for_status()
