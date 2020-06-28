import textdistance
from textblob import TextBlob
from django.shortcuts import render
from django.http import HttpResponse
from nltk.stem import WordNetLemmatizer 
  
lst = []
decision = []
def compare(s_inp, s_out):
	lem_inp = []
	lem_out = []
	lem_inp.clear()
	lem_out.clear()
	#print("Inside Compare")
	#print("Str1: ", s_inp)
	#print("Str2: ", s_out)
	lemma = WordNetLemmatizer() 
	token_inp = s_inp.split()
	
	token_out = s_out.split()

	for i in range(len(token_inp)):
		lem = lemma.lemmatize(token_inp[i])
		lem_inp.append(lem)
	for j in range(len(token_out)):
		lem = lemma.lemmatize(token_out[j])
		lem_out.append(lem)
	#Jaccard Index
	jacc = textdistance.jaccard(lem_inp, lem_out)
	#print("jaccard: ", jacc)
	
	#Sorens
	soren = textdistance.sorensen(lem_inp, lem_out)
	#print("Sorensen: ", soren)
	
	#TVR Value
	tvr = textdistance.tversky(lem_inp, lem_out)
	#print("Tversky: ", tvr)
	
	#Over Lap Index
	overlap = textdistance.overlap(lem_inp, lem_out)
	#print("overlap_cofficient: ", overlap)
	
	#Tanimoto Distance
	tanimoto_distance = textdistance.tanimoto(lem_inp, lem_out)
	#print("Tanimoto: ", tanimoto_distance)

	res = (jacc+soren+tvr+overlap)/4
	lst.append(res)
	print("Result: {}".format(res))
	'''if (res >= 0.6):
		print("News Your Searched was True")
	else:
		print("News Your Searched was fake")'''


def avrg():
	
	print("Enter Average Block")
	print("List Length: ",len(lst))
	print("content of list: ",lst)
	add = 0
	for i in range(len(lst)):
		add = add + lst[i]
	avg = ((add / len(lst))*10)
	print(avg)	

	if ((int(avg) >= 5) and (int(avg) <= 7)):
		#print(int(avg))
		#print("News You Searched was Likely to be True")
		decision.append("News You Searched was Likely to be True")

	elif ((int(avg) > 7) and (int(avg) <= 10)):
		#print(int(avg))
		#print("News You Searched was True")
		decision.append("News You Searched was True")
	elif (int(avg)<5 and int(avg)>=3):
		#print(int(avg))
		#print("News You Searched was fake")
		decision.append("News You Searched was likely fake")
	else:
		decision.append("News You Search Was Fake")	
	print("Exit Average Block")
	