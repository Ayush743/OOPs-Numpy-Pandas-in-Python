import numpy as np
from time import time
from sys import getsizeof

"""Python Lists vs numpy arrays"""
#-----------------------Execution Speed------------------------->
# start=time()
#l1=[i for i in range(1000000)]
# l2=[i for i in range(1000000)]
# l3=[]
# for i in range(len(l1)):
#     l3.append(l1[i]+l2[i])
# print(time()-start) 
""" python list takes 0.3015482425689697s"""

# np_start=time()
#x1=np.arange(1000000,dtype=np.int8)
# x2=np.arange(1000000,2000000)
# x3=x1+x2
# print(time()-np_start)
"""Numpy takes 0.007079362869262695s for the same operation"""

#numpy is 42.595392853534506 times faster than python list in above example



#<------------------------------Memory----------------------------------------->
# print(getsizeof(l1)) #number of bytes occupied by python list in memory -8448728 Bytes
# print(getsizeof(x1)) #number of bytes occupied by numpy array in memory -1000112 Bytes
# print(8448728-1000112)
""" numpy takes 7448616 bytes less than python lists """



"""--------------------Advanced Indexing------------------------------->"""
k1=np.arange(12).reshape(4,3)
k2=np.arange(35).reshape(7,5)

# print(k1[::2,:])
"""[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]"""
# say if we want to access the 1, and 4 row which is not possible with simple indexing so we use the fancy indexing
"""-----Fancy indexing----------"""
# print(k1[[0,2,3]])
# print(k2)
# print(k2[[0,2,3,6]])
# print(k2[:,[1,3,4]])
"""----Boolean Indexing----------"""
import random
np.random.seed(42)
z1=np.random.randint(10,50,(7,5))
print(z1)
# print(z1>26)
"""[[ True  True False False  True]
 [ True  True  True False False]
 [ True  True  True  True False]
 [ True False  True  True  True]
 [False  True  True False  True]
 [ True  True  True False False]
 [False  True False  True False]]"""
# print(z1[z1>26])
"""[48 38 30 48 28 32 33 45 49 33 31 33 39 47 30 42 31 34 36 37 46 30]"""
even_num_max=z1[(z1%2==0) & (z1>26)]
not_div_7=z1[z1%7!=0]
# print(even_num_max)
# print(not_div_7)



#----------Broadcasting--------------------------------------->
q1=np.arange(12).reshape(3,4)
q2=np.arange(4).reshape(1,4)
print(q1)
print(q2)
print(q1+q2)