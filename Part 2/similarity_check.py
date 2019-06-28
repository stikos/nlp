import numpy
import math
import glob

""" Three similarity functions"""


def cosine_distance(u, v):
	"""
	Returns the cosine of the angle between vectors v and u. This is equal to u.v / |u||v|.
	"""
	i = [x[1] for x in u]
	j = [x[1] for x in v]
	return 1 - numpy.dot(i, j) / (math.sqrt(numpy.dot(i, i)) * math.sqrt(numpy.dot(j, j)))


def jaccard_distance(u, v):
	"""
	Return the Jaccard/Tanimoto similarity by calculating the common stems,
	by calculating the union and intersection of their stems
	"""
	union = 0
	intersection = 0
	for stem1 in list(filter(lambda x: x[1] != 0, u)):
		union += 1
		if v[u.index(stem1)][1] != 0:
			intersection += 1
	for stem2 in list(filter(lambda x: x[1] != 0, v)):
		union += 1
	union -= intersection
	return 1 - intersection / float(union)


def euclidean_distance(u, v):
	""" Returns the Euclidean distance of the two vectors
	"""
	summ = 0
	i = [x[1] for x in u]
	j = [x[1] for x in v]
	summ = math.sqrt(sum([math.pow(a - b, 2) for a, b in zip(i, j)]))
	return summ


def create_vector(file, vector):
	for i in file.readlines():
		temp = i.strip("()\n ").split(",")
		vector.append(((temp[0]), float(temp[1])))


vector1 = []
vector2 = []

for filename in glob.glob("uncategorized/*"):
	cosine = (1.0, '')
	jaccard = (1.0, '')
	eucl = (1.0, '')
	create_vector(filename, vector1)
	for sec_file in glob.glob("categorized/*"):
		create_vector(sec_file, vector2)
		cos = cosine_distance(vector1, vector2)
		if cos < cosine:
			cosine[0] = cos
			cosine[1] = sec_file.partition('/')[2].rpartition('/')[0]
		jac = jaccard_distance(vector1, vector2)
		if jac < jaccard:
			jaccard[0] = jac
			jaccard[1] = sec_file.partition('/')[2].rpartition('/')[0]
		euc = euclidean_distance(vector1, vector2)
		if euc < eucl:
			eucl[0] = euc
			eucl[1] = sec_file.partition('/')[2].rpartition('/')[0]
	res = open("results.txt", "a")
	res.write("File: " + filename + "\ncosine: " + cosine[1] + "\njaccard: " + jaccard[1] + "\neuclidean: " + eucl[
		1] + "\n~~~~~~~~~~~~~\n\n")
