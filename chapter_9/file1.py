fin=open('snu.txt')
for letter in fin:
    word=letter.strip()
    #print word
    string=word.split()
    result=[]
    for words in string:
	if len(words)<=8:
	    continue
	result.append(words)

    print ','.join(result),	
