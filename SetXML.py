def SetXML(inverted):
	output="<inverted_index> \n"
	for lemma in inverted:
		output += "<lemma name=\"{0}\">\n".format(lemma)
		for doc,idf in inverted[lemma].items():
			output += "<document id=\"{0}\" weight=\"{1}\"/>\n".format(doc,idf)
		output += "</lemma> \n"
	output+="</inverted_index>"	
	return output