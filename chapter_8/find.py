def find_s(word,letter,index):
    while index<len(word):
	if word[index]==letter:
	    print index,
	index=index+1
   # print -1

print find_s('soooonuuu','u',1)

