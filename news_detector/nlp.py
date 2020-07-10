import spacy 
from spacy.tokenizer import Tokenizer
def text_processing(search):
	nlp = spacy.load("en_core_web_sm")
	toeknizer = Tokenizer(nlp.vocab)
	all_stopwords = nlp.Defaults.stop_words
	text_tokens = nlp(search)
	#print(text_tokens)
	tokens_without_sw= [word for word in text_tokens if not word in all_stopwords]
	#print(tokens_without_sw)
	tokens = []
	for i in tokens_without_sw:
		#print(i.pos_)
		if i.pos_ == "VERB":
			tokens.append(i)
		elif i.pos_ == "NOUN":
			tokens.append(i)			
		elif i.pos_ == "ADJ":
			tokens.append(i)
		elif i.pos_ == "PROPN":
			tokens.append(i)
		else:
			pass
	#print("Tokens: {}".format(tokens))
	return " ".join([str(i) for i in tokens])


'''st = "China Shake Hands with Pakistan"
a = text_processing(st)
print(a)'''
#stn = " ".join([str(i) for i in a])
