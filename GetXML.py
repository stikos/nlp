def GetXML(file):
	inverted_index={}
	f = open(file, "r")
	first_list = f.readlines()
	print(first_list[0])
	if first_list[0].strip() != "<inverted_index>":
		print("Wrong input")
		return False
	for line in first_list:
		if line[:8]=="<lemma n":
			word = line[14:-2]
		elif line[:8]== "<documen":
			line = line.replace(" ", "$", 1)
			print(line)
			doc1, doc2 = line.split()
			document=doc1[14:-1]
			weight=doc2[8:-2]
			if word in inverted_index:
				posting_list = inverted_index[word]
				posting_list[document] = weight
			else:
				inverted_index[word]={document: weight}
		elif line[:8]=="</lemma>":
			continue
		elif line[:8]=="</invert":
			return inverted_index