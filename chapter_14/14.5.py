'''	it downloads and prints a secret message from thinkpython.com	'''


import urllib


conn=urllib.urlopen('http://thinkpython.com/secret.html')
for line in conn.fp:
    print line.strip()
