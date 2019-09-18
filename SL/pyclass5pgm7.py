#write a python program to count the frequency of words in a given file.

from collections import Counter
def word_count(fname):
	with open(fname) as f:
		return Counter(f.read().split())

print("Number of words in the file: ", word_count("test.txt"))

'''
#Another way to do it is:

f1 = open("test.txt", "r")
l1=f1.readlines()
l2=list()
for i in l1:
	l2.extend(i.split())
l2=list(set(l2))
print(l2)
d1=dict()

d1['word']+=1

'''


