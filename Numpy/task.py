
import numpy as np
#create a null vector of size 10 but the fifth value which is one
n1=np.array([np.nan]*10)
n1[4]=1
#print(n1)
#ask user to input 2 numbers a and b and wap to generate the random array of shape(a,b) and avg of the array
np.random.seed(42)
def arr_cr(a,b):
    n2=np.ceil(np.random.random((a,b))*10)
    n2_avg=np.average(n2)
    n2_mean=np.mean(n2)
    print(n2)
    print(n2_avg)


def nd_shape(a,b):
    n=np.ones((a,b),dtype=int)
    n[1:a-1,1:b-1]=0
    print(n)
#nd_shape(7,5)

n=np.linspace(0,1,12)
n1=np.linspace(0,1,12)[1:-1]

print(n)
print(n1)