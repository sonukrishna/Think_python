'''   the function reads a file and made histogram of the words in it    '''

import string
def read_file(filename):
    d={}
    with open(filename)as f:
	for line in f:
	    hist(line,d)
	return d
def hist(line,d):
    for word in line.split():
	word=word.strip(string.punctuation+string.whitespace)
	word=word.lower()

	d[word]=d.get(word,0)+1

print read_file('word1.txt')
