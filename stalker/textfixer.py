import re
f=open("linker.txt","r")
string= f.read()
l=(string.replace('http',"\nhttp"))
l.sort()
q=open("linker_fixed.txt", "w")
q.write(l)
