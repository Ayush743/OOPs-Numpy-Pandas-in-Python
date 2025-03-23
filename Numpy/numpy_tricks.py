import numpy as np

"""Sort"""
x1=np.random.randint(34,65,10)
x2=np.sort(x1) #ascending
x3=np.sort(x1)[::-1] #descending
x4=np.random.randint(12,30,(6,3))
# print(x4)
# print(np.sort(x4,axis=0)) #axis-0 for column wise and axis=1 for row wise default is row wise

"""Append"""
# print(np.append(x1,300))
# print(np.append(x4,np.ones((1,x4.shape[1])),axis=0)) #0 for rowwise and 1 for column wise and make sure to keep the size same 
a1=np.arange(10).reshape(5,2)
a2=np.arange(10,20).reshape(5,2)
# print(np.concatenate((a1,a2),axis=0)) #row wise
# print(np.concatenate((a1,a2),axis=1)) # column wise
np.random.seed(42)
z1=np.random.randint(1,6,15)
# print(z1)
# print(np.unique(z1))

"""where"""
w=np.random.randint(20,100,15)
# print(w)
# print(np.where(w>50)) #return the indices
# print(np.where(w>63,0,w)) # can be used as the ternary operator

"""argmax and argmin"""

# print(np.argmax(w)) #return the index of the maximum number
# print(np.argmin(w)) #return the index of the minimum number

"""cumsum and cumprod"""
print(np.cumsum(w))
#[49 57 21 83 79 40 52 95 77 41 68 78 61 79 99]
#[ 49 106 127 210 289 329 381 476 553 594 662 740 801 880 979]

"""percentile"""
a=np.random.randint(1,100,30)
# print(a)
# print(np.percentile(a,50))
"""histogram"""
# print(np.histogram(a,bins=[0,10,20,30,40,50,60,70,80,90,100]))
# (array([6, 3, 1, 1, 3, 4, 6, 2, 2, 2]), array([  0,  10,  20,  30,  40,  50,  60,  70,  80,  90, 100]))

"""isin"""
q=np.arange(20,30).reshape(5,2)
items=[10,21,23,12,34]
print(q)
print(q[np.isin(q,items)])
"""[[20 21]
 [22 23]
 [24 25]
 [26 27]
 [28 29]]
[21 23]"""

"""put"""
np.put(q,[0,1],[110,349])
#print(q) # first name of array,indexes you want to change,value you want to put on the repective indices
"""clip"""
print(a)
print(np.clip(a,a_max=28,a_min=23))