import requests
from requests import get 
from bs4 import BeautifulSoup
import time


content = []
heading = []

def ie_scraping(ur):
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


def it_scraping(ur):
	url = "https://www.indiatoday.in/topic/{}".format(ur)
	results = requests.get(url)
	#print(" Request Response: ",results)
	soup = BeautifulSoup(results.text, "html.parser")
	container_div = soup.find_all('div', class_='view-content')
	for i in container_div:
		head_div = soup.find_all('div', class_='views-field views-field-label front-label')
		cont_div = soup.find_all('div', class_='views-field views-field-php-2')
		for tag in head_div:
			heading.append(tag.span.h2.a.text)
		for s in cont_div:
			content.append(s.span.text)
	print("Search Scan Complete IT")
	print("IE len in IT_Scraper: ", len(heading))
