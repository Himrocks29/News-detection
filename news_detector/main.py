from . import nlp
#from nlp import token
from . import compare_nlp
#from . import ht_scraper as ht
from . import indiatoday_scraper as it
from . import indianexpress_scraper as ie
from django.shortcuts import render
from django.http import HttpResponse


def main(request):

	it.content.clear()
	it.heading.clear()
	ie.content.clear()
	ie.heading.clear()
	compare_nlp.lst.clear()
	compare_nlp.decision.clear()
	#search = input("Enter Search String: ")
	search = request.POST['search']
	n = nlp.processing(search)
	key_inp = " "
	key_inp = key_inp.join(nlp.lst)
	#print("Final Search String: \n", key_inp)
	it.scraping(key_inp)
	ie.scraping(key_inp)


	#print("Enter Compare Block in main")
	if it.heading == '/0':
		return
	else: 
		for i in range(len(it.heading)):
			#nlp.lst.clear
			print("IT heading len: ",len(it.heading))
			n = nlp.processing(it.heading[i])
			key_out = " "
			key_out = key_out.join(nlp.lst)
			#print("Final Out Put String: \n", key_out)
			c = compare_nlp.compare(key_inp, key_out)
	if ie.heading == '/0':
		return
	else:
		for j in range(len(ie.heading)):
			print("IE heading len: ",len(it.heading))
			n = nlp.processing(ie.heading[j])
			key_out = " "
			key_out = key_out.join(nlp.lst)
			#print("Final Out Put String: \n", key_out)
			c = compare_nlp.compare(key_inp, key_out)
	
	
	try:
		compare_nlp.avrg()
		if ie.heading == '/0':
			return
		else:
			return render(request, "result.html", {'Heading': ie.heading[0], 'Content': ie.content[0], 'Decision': compare_nlp.decision[0]})
		
		if it.heading == '/0':
			return
		else:
			return render(request, "result.html", {'Heading': it.heading[0], 'Content': it.content[0], 'Decision': compare_nlp.decision[0]})
		
	except IndexError:
		return render(request, "result.html", {'Heading': 'Result Not Found', 'Content': 'Result Not Found', 'Decision': 'Result Not Found'})
	except ZeroDivisionError:
		return render(request, "result.html", {'Heading': 'Result Not Found', 'Content': 'Result Not Found', 'Decision': 'Result Not Found'})

		print("Could Not Find Result Search Again")
#main()
