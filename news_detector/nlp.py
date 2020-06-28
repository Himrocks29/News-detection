import nltk
import nltk.corpus
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

stop_words = set(stopwords.words('english'))
lst = []
join = " "
def processing(search):
	lst.clear()
	#inp = input("Enter Search String: \n")
	#string = inp 
	#stop = stopwords('string')
	var_token = word_tokenize(search)
	punctuation = re.compile(r'[.,?!,:;()|]')
	for words in var_token:
		if words not in stop_words:
			word = punctuation.sub("",words)
			lst.append(word)
	#print("Tokens: \n",var_token)
	#print("After stop Words: \n",lst)
	#str_join = join.join(lst)
	#print("\n Final String: \n", str_join)
	#return str_join, lst