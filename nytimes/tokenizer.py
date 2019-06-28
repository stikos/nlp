import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import string
import glob

"""I parakato sunartisi metatrepei ta treebank tags se wordnet tags gia na mporoun na 
xrisimopoiithoun apo ton lemmatizer"""
def get_wordnet_pos(treebank_tag):

    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return ''

for filename in glob.glob("http*.txt"):
	with open(filename, 'r') as myfile:
	    article=str(myfile.read().replace('\n', '')).replace(".", " ").replace("-", " ")
	wordnet_lemmatizer = WordNetLemmatizer() #nltk.download('wordnet')
	article = article.translate(None, string.punctuation)

	tokens = nltk.word_tokenize(article) #nltk.download('punkt')
	tagged = nltk.pos_tag(tokens) #PoSTagger embedded, nltk.download('averaged_perceptron_tagger')



	lemmas = []
	for item in tagged:
		if (item[1].startswith('J') or item[1].startswith('N') or item[1].startswith('V') or item[1].startswith('R')):
			if (get_wordnet_pos(item[1]) != ''):
				temp = wordnet_lemmatizer.lemmatize(item[0], get_wordnet_pos(item[1]))
			else:
				temp = wordnet_lemmatizer.lemmatize(item[0])
			lemmas.append(temp.encode("utf-8"))
			#print(item[0]+"__________"+temp)
		else:
			continue

	lemma_set = set(lemmas)

	occurences = []
	for set_item in lemma_set:
		occurences.append(lemmas.count(set_item))
	cardinality_list = zip(lemma_set, occurences)

	with open("../vertices/"+filename, "w") as vertex:
		for line in cardinality_list:
			#print(token)
			vertex.write(str(line)+"\n")

	with open("tokens_"+filename, "wb") as tokensfile:
		for token in tagged:
			#print(token)
			tokensfile.write(str(token)+"\n")
