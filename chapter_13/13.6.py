'''     two file comparing usin SET    '''

import string
def dclare(filename):#,filename2):
    f1=open(filename)
  #  f2=open(filename2)
    s=set()
    s1=set()
    return read_file(f1,s)
   # s2=set()
def read_file(f,s):
    for i in f:
	j=i.strip(string.punctuation+string.whitespace)
	j=j.lower()
#	print i
	s.add(j)
 #       for j in s:
##	    sep=j.split()
#	    for sep1 in sep:
#		s1.add(sep1)
    return s
#def substract(f1,f2,s1,s2):
 #   res=set()
  #  a=read_file(f1,s1)
   # b=read_file(f2,s2)
    #for i in a:
#	if i not in b:
#	    res.add(i)
 #   return res
print dclare('word1.txt')
