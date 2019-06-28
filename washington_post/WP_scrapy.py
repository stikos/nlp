from bs4 import BeautifulSoup
import glob

for filename in glob.glob('*.html'):
	f = open(filename)
	raw = f.read()
	soup = BeautifulSoup(raw, "lxml")
	for anchor in soup.find_all("a"):
				anchor.replaceWith(" "+anchor.get_text()+" ") #getting anchor text embedded in paragraphs
	with open(filename[:-5]+".txt", 'wb') as f:

		for final in soup.find_all(id="article-body"):
			temp = final.get_text()
			temp = ''.join([i if ord(i) < 128 else '' for i in temp])
			f.write(temp)
			"""print(final.get_text(strip=True))"""
	f.close()
