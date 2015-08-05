'''PRINT THE KEYS OF A DICTIONARY IN ALPHABETICAL ORDER'''


def histogram(word):
    d={}
    for i in word:
	if i not in d:
	    d[i]=1
	else:
	    d[i] += 1
    return d
def print_hist(h):
    x=sorted(h)
    for i in x:
	print i,h[i]
print_hist(histogram('abrakadabra'))
