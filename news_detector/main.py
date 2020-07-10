from . import nlp
#from nlp import token
from . import compare_nlp
#from . import ht_scraper as ht
from django.shortcuts import render
from django.http import HttpResponse
from . import scraping
from . import file_handle as fh


def main(request):
	scraping.content.clear()
	scraping.heading.clear()
	compare_nlp.lst.clear()
	compare_nlp.decision.clear()
	#search = input("Enter Search String: ")
	search = request.POST['search']
	n = nlp.text_processing(search)
	#print("Final Search String: \n", n)
	scraping.it_scraping(n)
	scraping.ie_scraping(n)


	#print("Enter Compare Block in main")
	if len(scraping.heading) == 0:
		return render(request, "Search.html", {'Heading': 'Result Not Found', 'Content': 'Result Not Found', 'Decision': 'Result Not Found'})
	else: 
		for i in range(len(scraping.heading)):
			#nlp.lst.clear
			print("Heading len: ",len(scraping.heading))
			key_out = nlp.text_processing(scraping.heading[i])
			#print("Final Out Put String: \n", key_out)
			compare_nlp.compare(n, key_out)
		print("Exit Compare Block")
	if len(compare_nlp.lst) == 0:
		return render(request, "Search.html", {'Heading': scraping.heading[0], 'Content': scraping.content[0], 'Decision': "News You Searched was not True", 'percent':0})

	else:	
		comp = compare_nlp.avrg()
		fh.handle(search, comp)
		return render(request, "Search.html", {'Heading': scraping.heading[0], 'Content': scraping.content[0], 'Decision': compare_nlp.decision[0], 'percent':comp})
	'''try:
		compare_nlp.avrg()

		return render(request, "result.html", {'Heading': ie.heading[0], 'Content': ie.content[0], 'Decision': compare_nlp.decision[0]})

	except IndexError:
		return render(request, "result.html", {'Heading': 'Result Not Found', 'Content': 'Result Not Found', 'Decision': 'Result Not Found'})
	except ZeroDivisionError:
		return render(request, "result.html", {'Heading': 'Result Not Found', 'Content': 'Result Not Found', 'Decision': 'Result Not Found'})

		#print("Could Not Find Result Search Again")'''
#main()
