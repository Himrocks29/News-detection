import textdistance
import spacy 
  
lst = []
decision = []
def compare(s_inp, s_out):
	'''nlp = spacy.load("en_core_web_sm")
	str_inp = nlp(s_inp)
	srt_inp = " ".join([token.lemma_ for token in str_inp])
	#print(str_inp)
	#inp_lower = str_inp.lower()
	print("Lower String Input: {}".format(str_inp))
	str_out = nlp(s_out)
	srt_out = " ".join([token.lemma_ for token in str_out])
	#print(str_out)
	#out_lower = str_out.lower()
	print("Lower String Output: {}".format(str_out))
	#print("Inside Compare")
	#print("Str1: ", s_inp)
	#print("Str2: ", s_out)'''
	

	#Jaccard Index
	jacc = textdistance.jaccard(s_inp, s_out)
	print("jaccard: ", jacc)
	
	#Sorens
	soren = textdistance.sorensen(s_inp, s_out)
	print("Sorensen: ", soren)
	
	#TVR Value
	tvr = textdistance.tversky(s_inp, s_out)
	print("Tversky: ", tvr)
	
	#Over Lap Index
	overlap = textdistance.overlap(s_inp, s_out)
	print("overlap_cofficient: ", overlap)
	
	#Tanimoto Distance
	#tanimoto_distance = textdistance.tanimoto(str_inp, str_out)
	#print("Tanimoto: ", tanimoto_distance)

	res = (jacc+soren+tvr+overlap)/4
	if res == 0:
		pass
	else:
		lst.append(res)
	print("Result: {}".format(res))
	'''if (res >= 0.6):
		print("News Your Searched was True")
	else:
		print("News Your Searched was fake")'''


def avrg():
	
	#print("Enter Average Block")
	print("List Length: ",len(lst))
	#print("content of list: ",lst)
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
	#print("Exit Average Block")
	return avg

