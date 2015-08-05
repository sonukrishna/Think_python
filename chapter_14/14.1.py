'''	this function prints the files into a list from a directory	'''

import os
def walks(dir):
    res=[]
    for word in os.listdir(dir):
	path=os.path.join(dir,word)
	if os.path.isfile(path):
	  #  print path
	    res.append(word)
	else:
	    walks(path)   
    return res

print walks('ss')


