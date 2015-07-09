'''FUNCTION TAKE TWO STRINGS AND RETURN TRUE IF THEY ARE ANAGRAMS'''


def is_anagram(str1,str2):
    lst1=sorted(list(str1))
    lst2=sorted(list(str2))
    if lst1==lst2:
	return True
    else:
	return False

print is_anagram('arundhathi','anirudh')
print is_anagram('amaze','eamza')
