#! python3

import bs4, requests

res = requests.get('https://yts.lt/')

soup = bs4.BeautifulSoup(res.text,'html.parser')

le = soup.select('#popular-downloads .browse-movie-title')

for el in le:
	resi = requests.get(el.get('href'))
	soupi = bs4.BeautifulSoup(resi.text,'html.parser')
	eli = soupi.select('#movie-info a')
	print(el.getText())
	for elii in eli:
		x = elii.getText()
		if len(x)==2:
			break
		else:
			print(x)
	print("")
