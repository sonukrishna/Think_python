''' DELETE FIRST AND LAST ELEMENT FROM A LIST AND MODIFIES IT EACH TIME '''
def midle(lst):
    del lst[0]
    del lst[len(lst)-1]
    return lst

nw_lst=[1,2,3,4,5,6,7,8,9]
for i in nw_lst:
    print midle(nw_lst)
