'''THE FUNCTION TAKE A STRING AND COUNT HOW MANY TIME A LETTER APPEARS USING DICTIONARY'''


def histogram(strng):
    d={}
    for i in strng:
	if i not in d:
	    d[i]=1
	else:
	    d[i] += 1
    return d

print histogram('abrakadabra')

