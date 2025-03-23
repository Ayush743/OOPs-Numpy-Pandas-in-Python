import pandas as pd
import numpy as np
"""--------Creating DataFrames-------------"""
#------using lists--------------->
student_data=[
    ['Ayush',8.5,10],
    ['Guni',9.5,13],
    ['Yashvi',8.5,10],
    ['Aakanksha',8.8,6],
    ['Priyanka',8,7],
    ['Artik',7,3],
    ['Nidhi',6.5,8],
    ['Rohan', 9.2, 12],       
    ['Sneha', 7.5, 5],
    ['Kunal', 8.3, 9],
    ['Kunal', 8.3, 9]
    ]
df1=pd.DataFrame(student_data,columns=["Name","CGPA","Package(LPA)"])
# print(df1.head(5))

#--------Using Dictionaries----->
student_data_dict={
    "Name" : [name[0] for name in student_data],
    "CGPA" : [cgpa[1] for cgpa in student_data],
    "Package(LPA)" : [package[2] for package in student_data],
}
df2=pd.DataFrame(student_data_dict)
# print(df2)

#------using read_csv------------>
movies=pd.read_csv("OOPs-Numpy-Pandas-in-Python/Pandas/pandas2/movies.csv")
# print(movies.head(5))

ipl=pd.read_csv("OOPs-Numpy-Pandas-in-Python/Pandas/pandas2/ipl-matches.csv")
# print(ipl.head(5))

"""<---------------------Dataframe Attributes and Methods----------------->"""
#<---------------------shape---------------------------->

# print(movies.shape)
# print(ipl.shape)

#<-------------------------dtypes---------------------------->
# print(movies.dtypes)
# print(ipl.dtypes)

#<------------------index-------------------------------->
# print(movies.index)

#<------------------------columns------------------------->
# print(movies.columns)
# print(ipl.columns)
# print(df1.columns)

#<---------------values----------------------------->

# print(df1.values)
"""[['Ayush' 8.5 10]
 ['Guni' 9.5 13]
 ['Yashvi' 8.5 10]
 ['Aakanksha' 8.8 6]
 ['Priyanka' 8.0 7]
 ['Artik' 7.0 3]
 ['Nidhi' 6.5 8]
 ['Rohan' 9.2 12]
 ['Sneha' 7.5 5]
 ['Kunal' 8.3 9]]"""
# print(ipl.values)

# <------------------head,tail,sample---------------------->

# print(df1.head(5))
# print(ipl.tail(5))
# print(movies.sample(5)) #use sample when the data is biased


#<----------info----------------->
# print(movies.info())

#<---------------describe------------------->
#gives mathematical summary
# print(df1.describe())
# print(movies.describe())

#<------------isnull------------------>
# print(movies.isna().sum())
# print(ipl.isna().sum())


#<----------------duplicated---------->
# print(movies.duplicated().sum())
# print(df1.duplicated().sum())


#<-----------rename-------------------->
# df1.rename(columns={'Name' : 'name',
#                     "CGPA" : 'cgpa',
#                     'Package(LPA)' : "package"},inplace=True)
# print(df1)