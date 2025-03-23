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
# print(q1)
# print(q2)
# print(q1+q2)
# q3=np.arange(3).reshape(1,3)
# q4=np.arange(3).reshape(3,1)
# # print(q3+q4)
# a1=np.random.randint(10,20,(1,3))
# a2=np.random.randint(10,20,(3,1))
# print(a1+a2)

"""------ user defined mathematical functions"""
def sigmoid(arr):
    print(1/(1+np.exp(-(arr)))) 
#sigmoid(np.arange(1,10))

def mse(act,pred):
    print(np.mean((act-pred)**2))
a=np.random.randint(1,10,10)
b=np.random.randint(1,10,10)
#mse(a,b)


"""----------Handling Missing values---------------------"""
x1=np.array([1,2,3,np.nan,np.nan,np.nan])
print(x1[~(np.isnan(x1))])
# print(x1)
# r_list=np.array([2,4,5,6,3,53,43,43,np.nan,np.nan,np.nan])
# missing_values=np.isnan(r_list)
# print(sum(missing_values))
# print(np.nan_to_num(r_list))
# print(np.nanmean(r_list))
# print(np.nanmedian(r_list))

# np_mean_data=np.where(np.isnan(r_list),np.nanmean(r_list),r_list)
# print(np_mean_data)

# data_without_nan=r_list[~np.isnan(r_list)]
# print(data_without_nan)

# #_____----------Roll function------->
# test_data=np.array([1,2,3,4,np.nan,6,7])
# mask=np.isnan(test_data)
# test_data[mask]=np.roll(test_data,shift=1)[mask]
# print(test_data)

"""plotting"""
import matplotlib.pyplot as plt
x=np.linspace(-10,10,100)
# y=1/(1+np.exp(-(x)))
# y=x**2
# y=np.sin(x)
# y=x*np.log(x)
# print(x)
# print(y)
plt.plot(x,y)
plt.show()