'''is_abecedarian that returns True if the letters in a word
appear in alphabetical order'''

def is_abecedarian(word):
    previous=word[0]
    for letter in word:
	if letter<previous:
	    return False
	previous=letter
    return True

is_abecedarian('abrakadabra')
