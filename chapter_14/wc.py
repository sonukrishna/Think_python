
'''		module		'''


def linecount(filename):
    #f _name_=='_main_':
	count=0
	for line in open(filename):
	    count=count+1
	return count
if __name__=="__main__":
    print linecount('wc.py')
