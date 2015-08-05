'''  FUNCTION TAKE A LIST OF WORDS AND SORT THEM FROM LONGEST TO SHORTEST   '''

import random
def sort_by_length(lst):
    res=[]
    for i in lst:
	res.append((len(i),i))
   # res.sort(len(i))
    res.sort(reverse=True)
    res1=[]
    for length,word in res:
	res1.append(word)
    print 'The sorted list is:',
    return res1

print sort_by_length(['srt','defr','pufr','fdddddd'])
	
