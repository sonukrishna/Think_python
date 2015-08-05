'''	FIND ANGRAMS IN A WORD LIST    '''


def anagram():
    dict1={}
    with open('word.txt')as f:
	for i in f:
	    i=i.strip()
	    key=sortd(i)
	    if key in dict1:
		value=dict1.get(key)+","+i
		print value
		dict1[key]=value
	    else:
		dict1[key]=i
	return dict1
def sortd(i):
    char=[x for x in i]
    char.sort()
    return "".join(char)
print anagram()
    
