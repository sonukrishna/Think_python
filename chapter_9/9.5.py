'''uses_all that takes a word and a string of required letters,
and that returns True if the word uses all the required letters at least once. '''
def uses_all(word,strn):
    for letter in strn:
	if letter not in word:
	    return False
    return True
uses_all('sonu','sssnnnooouu')
