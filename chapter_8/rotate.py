def rotate(str,index):
    for letter in str:
	rot=chr(ord(letter)+index)
	print rot,

rotate('sonu',-10)
