import random
def histogram(strng):
    d={}
    for i in strng:
        if i not in d:
            d[random.choice(i)]=1
        else:
            d[random.choice(i)] += 1
    return d

print histogram('abrakadabra')


