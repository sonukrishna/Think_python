def avoids(str):
    print 'the given forbidden string is:',
    a=raw_input()
    print a
    b=str.strip()
    c=b.split()

    for letter in c:
	if letter not in a:
	    print letter,
            print True
    print len(letter.split())
#	else:
#	    print False
    
avoids('sonu is my name dears...')
