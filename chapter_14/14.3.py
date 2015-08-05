'''	anagrams---using database modules	'''
import anydbm
import pickle
def ana(filename):
    db=anydbm.open('dbase.db','c')
    with open(filename)as f:
	for i in f:
#	    i=i.strip()
	    key=srted(i)
	    if key in db:
	        value=db.get(key)+","+i
	   	#	print value
		t=pickle.dumps(value)
		t1=pickle.loads(t)
	#	print t1
		db[key]=t1
	    else:
		db[key]=i
	return db
def srted(i):
    char=[x for x in i]
    char.sort()
    return "".join(char)

print ana('ss/word.txt')
