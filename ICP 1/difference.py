l = list(str(input("enter any string")))
from random import randint

a=[]
if len(l)>2:
    del l[randint(0,len(l)-1)]
    del l[randint(0,len(l)-1)]
    for i in l[::-1]:
        a.append(i)

    print("".join(a))
else:
    print ("give longer input")
