import copy
s = 'sample1.txt';
d = 'sample2.txt';

def swapfiles(a,b):
    with open (a,'r') as f1:
        dataA= f1.read()
    with open (b,'r') as f2:
        dataB= f2.read()

    with open (a,'w') as f1:
        f1.write(dataB)
    with open (b,'w') as f2:
        f2.write(dataA)

swapfiles(s,d)