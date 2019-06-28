import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import string
import glob
import math
from nltk.stem.snowball import SnowballStemmer

trans = string.maketrans(string.punctuation, "                                ")
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


lemmas = []
idf_dict = {}
texts_count = 0
for filename in glob.glob("texts/*/*[02468]"):
    with open(filename, 'r') as myfile:
        texts_count += 1
        article = str(myfile.read().replace('\n', '  '))
    myfile.close()
    wordnet_lemmatizer = WordNetLemmatizer()  # nltk.download('wordnet')
    stemmer = SnowballStemmer("english")
    article = ''.join([i if ord(i) < 128 else ' ' for i in article])
    article = article.translate(trans)

    tokens = nltk.word_tokenize(article)  # nltk.download('punkt')

    tagged = nltk.pos_tag(tokens)  # PoSTagger embedded, nltk.download('averaged_perceptron_tagger')

    for item in tagged:

        if item[1].startswith('J') or item[1].startswith('N') or item[1].startswith('V') or item[1].startswith('R'):
            if get_wordnet_pos(item[1]) != '':
                temp = wordnet_lemmatizer.lemmatize(item[0], get_wordnet_pos(item[1]))
            else:
                temp = wordnet_lemmatizer.lemmatize(item[0])

            if len(stemmer.stem(str(temp)).encode("utf-8")) <= 1:
                continue
            lemmas.append(stemmer.stem(str(temp)).encode("utf-8"))
            if stemmer.stem(temp.encode("utf-8")) in idf_dict:
                idf_dict[stemmer.stem(temp.encode("utf-8"))] += 1
            else:
                idf_dict[stemmer.stem(temp.encode("utf-8"))] = 1

        else:
            continue

lemma_set = set(lemmas)

occurences = []
for set_item in lemma_set:
    occurences.append((lemmas.count(set_item) * math.log10(texts_count / (int(idf_dict[set_item]) * 1.0)),
                       int(idf_dict[set_item]) * 1.0))
cardinality_list = zip(lemma_set, occurences)

with open("final", "w") as vertex:
    for line in cardinality_list:
        vertex.write(str(line) + "\n")
vertex.close()
