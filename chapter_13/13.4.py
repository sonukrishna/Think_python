'''   compare the words in a book and in a word list  '''

import string
def foo(filename1,filename2):
    d1=[]
    d2=[]
    d3=[]
    d4=[]
    f1=open(filename1)
    f2=open(filename2)
    print "The words not in common:\n"
    return foo2(f1,f2,d1,d2,d3,d4)
def foo1(f,d,d1):
        for i in f:
            i=i.strip().lower()
            for c in string.punctuation:
                i=i.replace(c,"")
	 #   print "the sentences without punctuation:"
          #  print i
            d.append(i)
            for j in d:
                sep=j.split()
                #s=s+len(sep)
                for sep1 in sep:
                    if sep1 not in d1:
                        d1.append(sep1)
	return d1
def foo2(f1,f2,d1,d2,d3,d4):
    a=foo1(f1,d1,d3)
    b=foo1(f2,d2,d4)
    for i in a:
	if i not in b:
	   # print "the words not in common:\n"
	    print i

foo('word1.txt','word2.txt')
