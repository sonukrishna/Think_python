'''	FIND THE DUPLICATES  USING DICTIONARY	'''

def has_duplicate2(lst):
    count=0
    dict1={}
    for key in lst:
	if key in dict1:
	    dict1[key]=count
	    print True
	    break
        else:
	    dict1[key]=count
	   

has_duplicate2([1,3,2,4,3,5,1,5])
has_duplicate2([1,2,3,4,5,65])
