


def eval_loop():
    print 'enter the word:',
   # word=raw_input()
    while True:
	word=raw_input()
	if word =='done':
	    break
        else:
	    print word
	    res=eval(word)
	print res

eval_loop()
