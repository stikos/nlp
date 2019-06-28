import os
import GetXML
import inverted_idx

inverted_index = {}

def searchen(lemma):
	final={}
	for i in lemma:
		if i in inverted_index:
			
			found = inverted_index[i]
			for j in found:
				if j in final:
					final[j]+=found[j]
				else:
					final[j]=found[j]
	sor = sorted(final.items(), key=lambda x: x[1], reverse = True)
	return sor
	

print("GLOSSIKI TEXNOLOGIA")
print("Enter 1 to extract text and create vertices,\n2 to create inverted index,\n3 to load inverted index\nor 0 to exit: ")
select = int(raw_input())
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
while select != 0:
	if select == 1:
		dir_list = [x for x in os.walk(".", topdown=True)]
		for directory in dir_list[0][1]:
			if directory != "vertices" and directory != "crawls":
				print("Creating vertices for: "+directory)
				os.system("cd "+directory+" && python *scrapy.py && python tokenizer.py")
	elif select == 2:
		inverted_idx.main(inverted_index)
		lemma_list = []
		count = 1
		while True:
			print("Enter search query terms (type \'exit!\' to finish query or exit search)")
			print("Term "+ str(count) + ": ")
			term = str(raw_input())
			if term == "exit!":
				break
			while term != "exit!":
				count = count + 1
				lemma_list.append(term)
				print("Term "+ str(count) + ": ")
				term = str(raw_input())
			if lemma_list:
				results = searchen(lemma_list) 
				for i in results:
					print i
			

	elif select == 3:
		print("Enter filename of inverted index to be loaded (.xml format): ")
		file = str(raw_input())
		inverted_index = GetXML.GetXML(file)
		lemma_list = []
		count = 1
		while True:
			print("Enter search query terms (type \'exit!\' to finish query or exit search)")
			print("Term "+ str(count) + ": ")
			term = str(raw_input())
			if term == "exit!":
				break
			while term != "exit!":
				count = count + 1
				lemma_list.append(term)
				print("Term "+ str(count) + ": ")
				term = str(raw_input())
			if lemma_list:
				results = searchen(lemma_list) 
				for i in results:
					print i

	print("Enter 1 to extract text and create vertices,\n2 to create inverted index,\n3 to load inverted index\nor 0 to exit: ")
	select = int(raw_input())
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("Done!")
