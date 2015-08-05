'''fun reads a file breaks each line into words,remove white space and converts to lowercase'''

import string
def foo():
    d=[]
    with open('word1.txt')as f:
	for i in f:
	    i=i.strip().lower()
	    for c in string.punctuation:
		i=i.replace(c,"")
	    print i
	
foo()
