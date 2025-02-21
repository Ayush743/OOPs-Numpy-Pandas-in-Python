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
# daily_users=[200,220,250,275]
# print(sum(daily_users)/len(daily_users))
# #--------------------usng loops--------------------------------->
# num_user=0
# sum_user=0
# for i in range(len(daily_users)):
#     num_user+=1
#     sum_user+=daily_users[i]
# print(f"avg users : {sum_user/num_user}")

# #-----------------------Using Vectorization---------------------------->
# np_daily_users=np.array(daily_users)
# print(np.mean(np_daily_users))

# monthly_sales=[200,220,250,275,300,320,350,370,400,420,450,475]
# #--------------Using Loops----------------------->
# updated_monthly_sales=[]
# for sale in monthly_sales:
#     updated_monthly_sales.append(sale-sale*0.1)

# print(updated_monthly_sales)

# #------------------Using Vectorization----------------------------------->
# np_monthly_sales=np.array(monthly_sales)
# updated_np__monthly_sales=np_monthly_sales*0.9
# print(updated_np__monthly_sales)

# np_array=np.arange(10,20)
# print(np_array.reshape(2,5))


#------------------Universal functions------------------------------------>

"""
arithmetic-add,subtract,division,multiply
trignometry and logarithmic- sin,cos,exp,log
less_than,greater

    """
# complete_square=[4,9,16,25,36,49,64]
# sqr_root=np.sqrt(complete_square)
# print(sqr_root)
# import random
# revenues=np.array([1210, 1059, 1177, 1477 ,1173 ,1014, 1358 ,1028 ,1410, 1251 ,1282 ,1436])
# expenses=np.array([1769, 2493 ,1891 ,2290 ,2152 ,2483 ,1997 ,2166 ,1587 ,1639 ,2006 ,1782])
# print(revenues)
# print(expenses)
# print(expenses[np.less_equal(expenses,2000)])
# print(expenses[np.greater(expenses,2000)])

#-------------------Using vectorize------------------------------------->
# def nps(score):
#     if(score>10):
#         return ("promoter")
#     elif(score>=7):
#         return ("refractor")
#     else:
#         return ("defractor")

# scores=np.random.randint(1,15,7)
# print(scores)
# nps_func=np.vectorize(nps)
# print(nps_func(scores))





#-------------------other fucntions----------------------------------->
# scores=np.array([55,57,89,78,70,90,98,97,84,82])
# eligibility=np.where(scores>75,"yes","No")
# print(eligibility)


# l1=np.random.randint(100,150,6)
# l2=np.random.randint(135,167,6)
# print(l1)
# print(l2)
# print(l1[l1>130])

# def is_vote(age):
#     if(age>18):
#       return "Eligible for vote "
#     else:
#       return "Not eligible for vote"
# ufs_score=np.vectorize(is_vote)
age_list=np.array([12,15,18,67,45,12,21,1,12,14,16])
# print(ufs_score(vote_list))


#------------Ternary Operator--------------------->
import random

trf_chr = np.array([
    "Optimus Prime",
    "Alpha Trion",
    "Vector Prime",
    "Solus Prime",
    "Onyx Prime",
    "Megatronus (The Fallen)",
    "Micronus Prime"
    "Megatron",
    "Bumblebee",
    "Arcee",
    "Ratchet",
    "Bulkhead",
    "Wheeljack",
    "Starscream",
    "Soundwave",
    "Knock Out",
    "Shockwave",
    "Grimlock",
    "Blackarachnia",
    "Ultra Magnus",
    " Arcadius Prime"
])

# Shuffle the list
# random.shuffle(trf_chr)
# is_eligible=np.where(age_list>=18,"eligible","not eligible")
# print(is_eligible)
# marks=np.random.randint(40,100,10)
# print(marks)
# is_eligible_marks=np.where((marks>=70)&(marks<=80),"eligible","not eligible")
# print(is_eligible_marks)


# marks_list=np.array([56,78,79,89,90,98,56,34,77,65,76,88,84,81,46,55,69])
jutsu_level=np.random.randint(20,100,16)
# print(jutsu_level)
# bankai_list=np.where((marks_list>=80) & (marks_list<=90) ,"Bankai","Shadow_Clone_Jutsu")
# print(bankai_list)
# #use brackets to differentiate between condition
# print(marks_list[(marks_list>=70) &(marks_list<=80)])

# jutsu_list=np.where(jutsu_level>80,"Infinite_Tsukuyomi",np.where(jutsu_level>40,"Wind_Style_Rasen_Shruiken","Amatersau"))
# print(jutsu_list)
# #--------------Reshaping the arrays---------------------------->
# print(jutsu_level.reshape(4,4))

# jutsu_level=jutsu_level.reshape(2,-1,)
# print(jutsu_level.flatten())
# #syntax array_name.reshape(num_rows,num_cols)
# print(jutsu_level.ravel())
# #------Both returned the flattened array but flatten returns the copy and ravel returns the reference that is it changes the original array

#------------------Transpose of the matrix--------------------------->
matrix=np.random.randint(1,100,25)
# print(matrix)
# transpose_matrix=np.transpose(matrix)
# #or
# transpose_matrix=matrix.T
# print(transpose_matrix)


#-----------Resizing the array-------------------------------->
#it is used to change the size of the array and fill the array with random values
# print(matrix)
# print(matrix.reshape(5,5))
# print(np.resize(matrix,(7,5)))



#-----------Concatenating and splitting array------------------------------->
# matrix2=np.random.randint(100,140,10)
# matrix3=np.random.randint(200,240,10)
# print(np.concatenate((matrix,matrix2)))
# print(np.vstack((matrix3,matrix2)))
# print(np.hstack((matrix3,matrix2)))
"""
what is Numpy ?
it is a python library for creating N dimensional arrays
 
#     """

# my_matrix=[[1,2,23],[2,324,44],[32,42,42]]
# print(np.array(my_matrix))

# arange=np.arange(1,20,4)
# print(arange)

# zeros=np.zeros((5,5))
# print(zeros)

# ones=np.ones((5,3))
# print(ones)


# linspace=np.linspace(1,20,7)
# print(linspace)


# identiy=np.eye(4)
# print(identiy)

# random_arr=np.random.randint(1,10,(5,3))
# print(random_arr)

# np.random.seed(32)
# print(np.random.rand(4))


# random_matrix=np.random.randint(0,20,(4,5))
# print(random_matrix.min())
# print(random_matrix.reshape(5,4))


# #------------ indexing and selection------------------->
# # arr=np.arange(0,11)
# # arr[:5]=23# broadcasting
# # print(arr)


# # arr1=np.arange(20,31)
# # arr2=arr1[:5] # its acts as a reference to original array and any changes made to this array will be reflected in the orignal array
# # arr2[:]=55
# # print(arr2)
# # print(arr1)
# # # to resolve this we create a copy
# # a=np.arange(10)
# # a_copy=a.copy()
# # a_copy[:]=55
# # print(a_copy)
# # print(a)


# array_2d=np.array([[1,2,4],[7,43,3],[424,42,2]])
# # to select a single row
# first_row=array_2d[0]
# print(first_row)
# last_row=array_2d[-1]
# print(last_row)

# print(array_2d[2,1])



# print(array_2d[:2,:2])
# print(array_2d[1:,:2])
# print(array_2d[:2,1:])


# arr=np.arange(11)
# print(arr[arr>5])



#-----------numpy operations and functions----->
arr=np.arange(11)
#print(arr+4)
#mean,mode,sin,log,sum,var,std


# arr_2d=np.arange(10,35).reshape(5,5)
# print(arr_2d.sum(axis=0))
# print(arr_2d.sum(axis=1))
# arr1=np.arange(1,10).reshape(3,3)
# print(arr1.sum(axis=0))
# print(arr1.sum(axis=1))



#------------------Numpy exercise-------------------------------------->

# array_zeroes=np.zeros(10)
# array_ones=np.ones(10)
# print(array_zeroes)
# print(array_ones)
# array_fives=np.ones(10)*5
# print(array_fives)
# array_1_to_50=np.arange(10,51)
# print(array_1_to_50)
# array_even_1_to_50=np.arange(10,51,2)
# print(array_even_1_to_50)

# matrix_3=np.arange(0,9).reshape(3,3)
# print(matrix_3)
# identity_matrix=np.eye(3)
# print(identity_matrix)

# print(np.random.randn(25))
# print(np.arange(0.01,1.01,0.01).reshape(10,10))
# print(np.linspace(0,1,20))

# arr=np.arange(1,26).reshape(5,5)
# print(arr)
# print(arr[2:,1:])
# print(arr[3,4])
# print(arr[:3,1:2])
# print(arr[3:])
# print(arr.sum())
# print(arr.sum(axis=0))
# print(arr.std())