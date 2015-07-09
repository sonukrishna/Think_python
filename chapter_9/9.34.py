def uses_only(word,available):
    for letter in word:
	if letter not in available:
	    print False
    return True
uses_only('sonu','psdkrozjnhku')
