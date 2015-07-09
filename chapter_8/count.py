def count(word):
    count =0
    print 'the element to be checked:',
    a=raw_input()
    print a
    for letter in word:
	if letter==a:
	    count=count+1
   
    print count
count('ooooosonu')
