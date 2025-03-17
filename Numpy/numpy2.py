#Numpy is a lib used in scientific computing and used for fast operation on arrrays including mathematical,statisitcal and logical.The core of numpy is ndarray object and create homogenous arrays.

""" 
Numpy arrays has fixed size at creation,elements must be of the same datatype,complex operations can be applied easily on numpy,numpy is fast and use less storage
"""
#<----creating numpy arrays----------------------->
import numpy as np
l1=np.array([1,2,3,4,5]) # 1-d array or vector
#print(type(l1))

l2=np.array([[1,2,3],[4,5,6]])
#print(l2) 2-d array or matrix

l3=np.array([[[1,2,3]],[[4,5,6]]])
#print(l3.ndim) 3-d array or tensor

l4=np.array([[1,2,3],[5,6,7],[7,8,9],[0,8,0]],dtype=bool)
#print(l4)

l5=np.arange(1,16,2).reshape(4,2) # the product of arguments provided in reshape should be equal to the the numberof elements in the array
#print(l5)

l6=np.ones((4,5)) # provide a tuple of shapes and used in deep learning for initializing the weights or values
#print(l6)
l7=np.zeros((2,2),dtype=int)
#print(l7)
import random
l8=np.random.randint(2,20,(4,5))
#print(l8) for testing and creating numpy array of random numbers
l9=np.random.random((3,4))
#print(l9)
l10=np.linspace(12,34,8).reshape(4,2)
#print(l10)
l11=np.identity(3)
#print(l11) # for creating the identity matrix

"""-------------- Attributes of numpy Array ---------------"""

l12=np.arange(10)
l13=np.arange(12,dtype=np.int16).reshape(3,4)
l14=np.arange(27).reshape(3,3,3)


""" ndim """

# print(l12.ndim)
# print(l13.ndim) gives the dimension of the given array
# print(l14.ndim)

"""shape"""

# print(l12.shape)
# print(l13.shape)
# print(l14.shape) # it returns the number of the elements in each dimension basically the number of  rows and columns and how are they arranged

"""size"""

# print(l12.size)
# print(l13.size)
# print(l14.size) # it returns the number of elements that is the size

"""itemsize"""

# print(l12.itemsize)
# print(l13.itemsize)
# print(l14.itemsize) # it returns hom much memory each element of array is taken


"""dtype"""

# print(l12.dtype)
# print(l13.dtype)
# print(l14.dtype) # tell the datatype of the array

#-----------------------------------------------------------------------------------------------------------

""" Changing the datatype"""
# astype
np.random.seed(42)
a1=np.random.randint(1,18,(3,3),dtype=np.int16)
# print(a1.astype(np.int16))
# print(a1.dtype)
a2=np.random.randint(20,40,(3,3),dtype=np.int16)

"""<------------Scaler operation------------------------------->"""
#1) Arithmetic Operation
a1=a1+10
a1=a1*10
a1=a1-10
a1=a1/10
#print(a1) we can apply all arithemtic operations


# 2) Relation Operation-
b1=np.arange(12).reshape(3,4)
b2=np.arange(10,22).reshape(3,4)
# print([b2>15])
# print([b2==15])
# print(b2[b2>15])


"""<------------------Vector Operations------------------------->"""
# print(b1)
# print(b2)
# b3=b2+b2
# b3=b2-b2
b3=b1*b2
#print(b3)



"""--------------------Some Numpy Functions---------------"""
#1) min/max/sum/prod
m=np.max(b2,axis=1)
n=np.min(b1,axis=0)
s=np.sum(b2,axis=1)
p=np.prod(b1,axis=1)
#print(m,n,s,p)

#2)mean/median/std/var
mn=np.mean(b2,axis=1)
md=np.median(b2,axis=0)
std=np.std(b2,axis=0)
var=np.var(b2,axis=1)
k1=np.arange(12).reshape(3,4)
# print(k1)
# print(np.mean(k1[0,:]))
#print(mn,md,std,var)


#3) dot product
x1=np.random.randint(0,20,(4,5))
x2=np.random.randint(30,50,(5,4))
# print(x1)
# print(x2)
# print(np.dot(x1,x2))


#4) round/floor/ceil
z1=np.random.random((3,3))*100
# print(z1)
# print(np.round(z1,2))
# print(np.ceil(z1))
# print(np.floor(z1))


"""<-------------------------Indexing and Slicing---------------------------------------------->"""

l1=np.arange(10)
l2=np.arange(12,dtype=np.int16).reshape(3,4)
l3=np.arange(27).reshape(3,3,3)

#indexing
# print(l1)
# print()
# print(l2)
# print()
# print(l3)


last_item=l1[-1] 
"""indexing in 1d array"""
#print(last_item)# works in exact similar way as that of python lists
"""indexing in the 2d array"""
# print(l2[1,2])
# print(l2[2,3]) # just give the row number and column number in square brackets
# print(l2[1,0])
"""indexing in the 3d array"""
# print(l3[2,1,1])
# print(l3[0,1,0]) # first choose the position of the 2d matrix  and then in the other argument just proivde the row and column number as that of 2d matrix
# print(l3[0,0,0])
# print(l3[2,2,0])
"""In indexing we fetch only single item but in slicing we can fetch multiple items"""
# print(l1[2:5])
# print(l2[0,:])
# print(l2[:,2])
# print(l2[1:,1:3])
# print(l2[1:,1:3])

"""some unique"""
# print(l2[::2,::3])
# print()
# print(l2[::2,1::2])
# print(l2[1,::3])
# print(l2[:2,1:])
# print(l3[1,:,:])
print("some interesting slicing of 3d arrays")
# print(l3[::2])
# print(l3[0,1,:])
# print(l3[1,:,1])
# print(l3[2,1:,1:])
# print(l3[::2,0,::2])

"""-----------------Iterating-----------------"""
# for i in l1:
#     print(i,end=" ")
# print()
# for i in l2:
#     print(i,end=" ")
# print()
# for i in l3:
#     print(i)
"""---------------------np.nditer---------------------------"""
# for i in np.nditer(l3):
#     print(i,end=" ")

#1 2 3 4 5 6 7--------------------26

""" -------------Transpose and ravel--------------"""

# print(l2.T) simpple code to determine the transpose of the matrix or 2d array

"""-----------ravel->convert the any dimensional array to 1d array------------------"""
# print(l3.ravel())
# [1 2 3 4 5 6 7 8 9------26]


"""-------------------- stacking and splitting------------------------------"""
x1=np.arange(12).reshape(3,4)
x2=np.arange(12,24).reshape(3,4)
print(np.hstack((x1,x2))) # stack the arrays with same shape horizontally the number of rows remain same but the number of columns is increased
print(np.vstack((x1,x2))) # stack the arrays with same shape vertically the number of columns remain same but the number of rows is increased

y1=np.hstack((x1,x2))
y2=np.vstack((x1,x2))

print(np.hsplit(y1,2))
print(np.vsplit(y1,3))