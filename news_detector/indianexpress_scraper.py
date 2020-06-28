import requests
from requests import get 
from bs4 import BeautifulSoup
import time


content = []
heading = []
#cat = []

def scraping(ur):
	url = "https://indianexpress.com/?s={}".format(ur)
	results = requests.get(url)
	print(" Request Response: ",results)
	soup = BeautifulSoup(results.text, "html.parser")
	container_div = soup.find_all('div', class_='search-result')

	for i in container_div:
		res_div = soup.find_all('div', class_='details')
		for h in res_div:
			#head = soup.find_all('h3')
			heading.append(h.h3.text)
			content.append(h.p.text)
	print("Search Scan Complete IE")
	print("IE len in IE_Scraper: ", len(heading))


#scraping(uri[0])