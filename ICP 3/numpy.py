import numpy as np

x = np.random.randint(1,20,15,int)
x = x.reshape((3,5))
print (x)
m = (x.max(axis=1).reshape(-1,1))

z = (np.where(x==m,x,0))
ans = (x-z)
print (ans)



