'''    select random words from a file   '''


import time
import random
import string
start_time=time.time()
def read_file(filename):
    d={}
    with open(filename)as f:
        for line in f:
            hist(line,d)
       # print d
	#print "the random word is:",
	print random_word(d)
	a= cum(d)
	n=random.choice(a)
	print "the random no is:",
	print bisct(a,n)
	lst1=random_word(d)
	rand=bisct(a,n)
	print "the random word for the index is:",
	print random_word1(lst1,rand)
	print("time in seconds %s",(time.time()-start_time))
def hist(line,d):
    for word in line.split():
        word=word.strip(string.punctuation+string.whitespace)
        word=word.lower()
        d[word]=d.get(word,0)+1
def random_word(d):
    t=[]
    for i in d.keys():
	t.append(i)
  #  print random.choice(t)
    return t
def cum(d):
    t1=[]
    count=0
    for i in d.values():
	count=count+i
	t1.append(count)
    return t1
def bisct(b,n):
   # n=random.choice(d)
    beg=0
    end=len(b)-1
    while(beg<=end):
	mid=(beg+end)/2
	if b[mid]==n:
	    return mid
	    break
	elif n>b[mid]:
	    beg=mid+1
	else:
	    end=mid-1
    if beg<=end:
	print 'The indx of the obj:',
	return mid+1
   # else:
#	return 'nothing found!'
def random_word1(a,n):
    for i in a:
	if n==a.index(i):
    		return i
   

read_file('word1.txt')
