str=[1,5,2,6,4,8,2,4,5,8]
print str
def cumulative(lst):
    #print 'the input list is:'
   # lst=[1,5,6,8,3,8,2,7,2,6]
   # print lst
    res=[]
    i=0
    for num in lst:
	i=i+num
	res.append(i)
    print 'the cumulative lst'
    print res
cumulative(str)
