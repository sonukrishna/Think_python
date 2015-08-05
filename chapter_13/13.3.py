'''   find no.of words,common words etc from a file using dictionary   '''
import time
import random
import string
start_time=time.time()
def read_file(filename):
    d={}
    with open(filename)as f:
	for line in f:
	    hist(line,d)
	print d
        a=total_words(d)
	print "Total no.of words:",
        print a
	print "Total no.of different words:",
	print diff_words(d)
	print "different words are:",
	wrds=d.keys()
	print wrds
	print 'the most common TEN words:'
	cmn_wrds=most_common(d,10)
	print "most common TEN words are:"
	print cmn_wrds
#	#for i,j in cmn_wrds[0:10]:
	 #   print i, '\t', j
	print "the random word is:",
	print random_word(d)
	print "time taken:",
	print("	%s seconds",(time.time()-start_time))
def hist(line,d):
    for word in line.split():
	word=word.strip(string.punctuation+string.whitespace)
	word=word.lower()
	d[word]=d.get(word,0)+1
def total_words(d):
    return sum(d.values())
def diff_words(d):
    return len(d)
def most_common(d,n):		# FUNCTION FOR SELECTING MOST COMMON WORDS
    lst=[]
    for key,value in d.items():
	lst.append([value,key])
    lst.sort(reverse=True)
    for x,y in lst[0:n]:
	print x,'\t',y
    #return lst
def random_word(d):
    t=[]
    for i,j in d.items():
	t.extend([i]*j)
    return random.choice(t)
read_file('word.txt')
#print total_words(d)
