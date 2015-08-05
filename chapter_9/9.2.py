def has_no_e(word):
    for letter in word:
	if 'e' in letter:
	    print letter
	    return False
	   # print letter
    return True
	
	
print has_no_e('seonu')
