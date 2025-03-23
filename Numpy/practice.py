
import numpy as np
import random
np.random.seed(42)
a=np.random.randint(10,60,10)
b=np.random.randint(10,40,(3,5))
c=np.random.randint(10,70,(2,2,2))
# print(a)

y1=np.sort(b,axis=0)
y2=np.sort(b,axis=1)
y3=np.sort(a)
# print(y1)
# print(y2)

print(a)
print()
print()
print(b)
c=np.random.randint(120,220,(3,5))
d=np.random.randint(1000,1200,(3,1))

# print(np.append(a,400))
# print(np.append(b,np.ones((3,5)),axis=0))
# print(np.append(b,np.zeros((3,1)),axis=1))

# print(np.concatenate((b,c),axis=0))
# print(np.concatenate((b,d),axis=1))
e=np.random.randint(1,5,15)
# print(e)
# print(np.unique(e))

"""expand_dims"""
#a=np.arange(12)
# print(np.expand_dims(a,axis=0))
# print(np.where(a>30,a,'less'))
# print(np.where(a%2==0,"even",'odd'))
# arc=np.random.choice(np.array(["male","female"]*13),size=13)
# print(arc)
# print(np.where(arc=="male",1,0))

# print(np.argmax(a))
# print(np.cumsum(a))