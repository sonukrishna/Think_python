'''THE FUNCTION TAKE VALUES FROM A FILE AND STORE THEM AS KEYS'''


def dict_key():
    d={}
    with open('word.txt')as f:
	for line in f:
	    key=line.split()[0]
	    d[key]=None
	return d 
print dict_key()

