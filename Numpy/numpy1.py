'''
Numpy is better than list because of the following reasons :
1) Numpy is much faster than list.
2)Numpy takes less space than list and uses contiguous memory.
'''
import numpy as np
arr=np.array([1,2,"3",4,5,6,7],np.int16)
arr1=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
# print(arr+1)
# print(arr1.shape)
# print(arr.shape)
# print(arr1.shape)
# l=[1,2,3,4,5]
# l=[a*4 for a in l  ]
# print(l)
# print(arr)
# list1=[1,2,3,4,5,6,7]
# l2=[a+1 for a in list1]
# print(l2)
a_np=np.array([[1,2,3,4,5],[4,5,6,7,8],[14,23,23,42,43]],np.int16)
# print("Numpy array :",a_np)
# print(a_np[0][2:4])
# print(a_np.argmax())
# print(a_np)
a1=np.array([a for a in range(7)])
b1=a1[2:5]
b1[0]=34
# print(a1)
#[ 0  1 34  3  4  5  6]
# print(a_np.ndim,a_np.shape,a_np.size,a_np.dtype)


#----------Numpy Creation----------------------------->


# arr_any=np.full((5,5),10)
# ones=np.ones((2,5))
# zeroes=np.zeros((3,5))
# arrange_arr=np.arange(10,30,2)
# print(arrange_arr)
# linspace=np.linspace(1,10,6)
# print(linspace)
# print(np.full((3,5),8))
# # print(np.zeros((1,5)))
# print(np.empty((5,5)))
# print(np.ones((2,5)))
# print(np.arange(10,31,2))
# print(np.linspace(10,31,9))
#--------------------------Numpy Operation------------------------------>

# l1=[23,34,45,56,67,78,4,5,2]
# l2=[45,67,89,44,33,67,4,6,7]
# a1=np.array([l1,l2])
# print(np.sort(a1,axis=0))
# print(np.sqrt(a1))
# a2=np.array(l2)
# a3=a1+a2
# print(a3)
# print(np.array([1,2,4])+np.array([[1],[2]]))


#---------------Broadcasting------------------------------------------>
# a1=np.array([1,2,3])
# a2=np.array([[1],[2],[6]])
# a3=np.array([[1,4,5],[2,6,7],[6,53,4]])
# print(a1+a2)
# print(a1+a3)



#-----------Indexing and slicing--------------------------------------->
# sales_data=np.array([[200,234,256],[190,203,198],[256,245,201]])
# print(sales_data[0][0])
# #or
# print(sales_data[1,2])
# print(sales_data[1][::-1])

#------Some basic slicing operation-------------------------->
# monthly_sales=np.array([200,220,250,275,300,320,350,370,400,420,450,475])
# print(f"January Sales : {monthly_sales[0]} December Sales : {monthly_sales[-1]}")
# print(f"Monthly Sales for each quarter :\n Q1:{monthly_sales[:3]}\n Q2:{monthly_sales[3:6]}\n Q3:{monthly_sales[6:9]}\n Q4:{monthly_sales[9:12]}\n")
# monthly_sales[3]=280
# print(f"Updated Monthly Sales L: {monthly_sales}")
# summer_months=monthly_sales[5:8]
# avg_summer_sales=np.mean(summer_months)
# print(f"Average Sales for Summer month is : {avg_summer_sales}")
# avg_monthly_sales=np.mean(monthly_sales)
# print(f"The average monthly sales for the entire year is : {avg_monthly_sales}")
# print(F"The Months having higher monthly avg sales are : {monthly_sales[monthly_sales>avg_monthly_sales]} ")


#------------------------Loops Vs Vectorization----------------------------------------------------->
#-----------------using built in functions----------------------->
daily_users=[200,220,250,275]
print(sum(daily_users)/len(daily_users))
#--------------------usng loops--------------------------------->
num_user=0
sum_user=0
for i in range(len(daily_users)):
    num_user+=1
    sum_user+=daily_users[i]
print(f"avg users : {sum_user/num_user}")

#-----------------------Using Vectorization---------------------------->
np_daily_users=np.array(daily_users)
print(np.mean(np_daily_users))