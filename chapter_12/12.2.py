''' THIS FUNCTION RETURNS THE LETTERS IN DECREASING ORDER OF A STRING '''


def most_frequent(word):
    lst1=[]
    for i in word:
	lst1.append((word.count(i),i))
	lst1.sort(reverse=True)
    lst2=[]
    for cnt,lttr in lst1:
	if lttr not in lst2:
	    lst2.append(lttr)
    return lst2


print most_frequent('abrakadabra')
