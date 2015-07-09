'''THE FUNCTION TAKE ALTERNATIVE LETTERS FROM EACH AND FORM A NEW WORD'''


def interlock(word1,word2):
    res=[]
    if len(word1)==len(word2):
	list1=list(word1)
	list2=list(word2)
	for i in range(len(list1)):
	    res.append(list1[i])
	    res.append(list2[i])
	return "".join(res)
    else:
	return None

print interlock('legend','legecy')
print interlock('hello','heck')
