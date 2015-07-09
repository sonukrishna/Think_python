def pal(word1,word2):
    if len(word1)==len(word2):
	if word1[:]==word2[::-1]:
	    return 'given two are palindrome:',word1,word2
	else:
	    return 'they are NOT'
    else:
	return 'not in same length'

print pal('sonu','unos')
print pal('sonu','sasi')
print pal('sonu','ssssssss')
