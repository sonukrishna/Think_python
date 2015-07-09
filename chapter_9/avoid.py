def avoids(word,str):
    for letter in word:
	if letter in str:
	    return False
    return True

avoids('sonu','ejjhdsklcjjb')
