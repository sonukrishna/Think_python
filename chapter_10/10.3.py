'''FUNCTION TAKES A LIST AS A PARAMETER AND RETURN TRUE IF IT IS SORTED IN ASCENDING ORDER,FALSE OTHERWISE'''


def is_sorted(lst):
    nw_lst=sorted(lst)
    if lst==nw_lst:
	return True
    else:
	return False

word=list('sonu')
print word        ,
print is_sorted(word)
ss=[1,2,3,4,5,6,7,8,9]
print ss          ,
print is_sorted(ss)
word2=list('abcdefgh')
print word2       ,
print is_sorted(word2)
