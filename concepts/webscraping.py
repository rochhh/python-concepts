import requests , bs4

res = requests.get("https://nostarch.com")

no_starch_soup = bs4.BeautifulSoup(res.text , 'html.parser')

elems = no_starch_soup.select('div')

print(str(elems[0]))