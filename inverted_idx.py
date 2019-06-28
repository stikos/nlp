import glob
import math
import SetXML


def InvertedFile(file, inverted_index):
    inv_list = []
    f = open(file, "r")
    first_list = f.readlines()
    for item in first_list:
        inv_list.append(item.strip("()\n").replace("\'", "").split(","))
    f.close()
    filename = file.replace("$", "/")
    for word, tf in inv_list:
        if word in inverted_index:
            posting_list = inverted_index[word]
            posting_list[filename[9:-4]] = tf
        else:
            inverted_index[word] = {filename[9:-4]: tf}
    return inverted_index


def main(inverted_index):
    vertex_counter = 0
    for _ in glob.glob("vertices/http*.txt"):
        vertex_counter = vertex_counter + 1
    print("Creating index for " + str(vertex_counter) + " articles...")

    """
    Tha arxisoume na diatrexoume ola ta dianusmata kai gia kathe kainourgio limma
    pou tha sunantame tha kanoume eisagogi sto dictionary, diladi:
    for filename in vertex_files:
    	for line in filename:	
    		if lemma not in inverted_index:
    			kane tin eisagogi tou
    		else:
    			prosthese sta keimena toy limmatos kai to neo keimeno
    tf-idf weighting: to tf to pairno kateutheian apo to dianusma, eno to idf mporo
    na to ypologizo ek neou se kathe eisagogi. arkei na kratao se mia metavliti to plithos
    olon ton keimenon kai na mporoume kai na metrisoume to mikos tou leksikou kathe limmatos,
    diladi se posa keimena summetexei. Etsi se kathe nea eisagogi tha ananeonoume to varos 
    tou limmatos gia olo tou to leksiko.
    """

    for filename in glob.glob("vertices/http*.txt"):
        InvertedFile(filename, inverted_index)
    for word in inverted_index:
        postings_list = inverted_index[word]
        idf = math.log10(vertex_counter / (len(inverted_index[word]) * 1.0))
        for entry, weight in postings_list.iteritems():
            postings_list[entry] = float(weight) * idf

    xmlout = open("inverted_index.xml", "w")
    txtout = open("inverted_index_text.txt", "w")
    xmlout.write(SetXML.SetXML(inverted_index))
    txtout.write(SetXML.SetXML(inverted_index))
    xmlout.close()

    return inverted_index
