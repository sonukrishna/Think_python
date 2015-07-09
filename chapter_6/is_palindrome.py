def pal(word):
    a=word[:]
    b=word[::-1]
    if a==b:
	print 'palindrome'
    else:
	print 'not'

pal('12321')
