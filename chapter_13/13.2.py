''' count the no.of words used in a book'''


import string
def foo():
    d=[]
    s=0
    d1=[]
    with open('word1.txt')as f:
        for i in f:
            i=i.strip().lower()
	   # ss=len(i.split())
            for c in string.punctuation:
                i=i.replace(c,"")
	    print i
	    d.append(i)
	    for j in d:
		sep=j.split()
		s=s+len(sep)
		for sep1 in sep:
	            if sep1 not in d1:	
		        d1.append(sep1)
        print 'total no of words:',
	print s
	print 'The words used in the Book are:',
	return d1
		
#	for i in f:
#	    s=len(i.split())
#	    print s
print foo()
