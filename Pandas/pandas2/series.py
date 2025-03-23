import pandas as pd
import numpy as np
#Pandas Series
"""It is a 1-D array holding data of any type and it is a like a column in a table"""

"""------------------Using Lists------------------"""

#<--------string--------->
countries = [
    "United States", "Canada", "Germany", "France", "Japan", 
    "Australia", "India", "Brazil", "South Africa", "China", 
    "United Kingdom", "Mexico"
]
sr=pd.Series(countries)
#print(sr)

#--------integer----------->
runs=np.array([13,34,56,78,89,100],dtype=np.int8)
sr=pd.Series(runs)
#print(sr)

#--------------custom index------------------>
populations = [0.33, 0.04, 0.08, 0.07, 0.12, 0.03, 1.42, 0.21, 0.22, 1.41, 0.07, 0.13]
sr_c=pd.Series(populations,index=countries)
#print(sr)


"""<-----------------------using dictionaty-------------------------------------->"""
populations_dict = {"United States": 0.33, "Canada": 0.04, "Germany": 0.08, "France": 0.07, "Japan": 0.12,  
                    "Australia": 0.03, "India": 1.42, "Brazil": 0.21, "South Africa": 0.22, "China": 1.41,  
                    "United Kingdom": 0.07, "Mexico": 0.13}

sr=pd.Series(populations_dict)
# print(sr)


"""<------------------------Series Attributes------------------------------->"""

#size
# print(sr.size)
# #dtype
# print(sr.dtype)
# #is_unqiue
# print(sr.is_unique)
# #index
# print(sr.index)
# #value
# print(sr.values)


"""<-----------------Series using read_csv-------------->"""
sr=pd.read_csv("OOPs-Numpy-Pandas-in-Python/Pandas/pandas2/subs.csv")['Subscribers gained']
# print(sr)

sr1=pd.read_csv("OOPs-Numpy-Pandas-in-Python/Pandas/pandas2/kohli_ipl.csv",index_col="match_no")['runs']
# print(sr1)
sr2=pd.read_csv("OOPs-Numpy-Pandas-in-Python/Pandas/pandas2/bollywood.csv",index_col="movie")['lead']
# print(sr2)


"""<--------------head,tail,sample-------------------->"""
# print(sr2.head(10))
# print(sr2.tail(10))
# print(sr2.sample(10))
"""value_counts"""
# print(sr2.value_counts())
"""sort_values"""
# print(sr1.sort_values(ascending=False).head(1).values[0])
"""sort_index"""
# print(sr2.sort_index( ascending=True))




"""<-------------Series Maths Method------------------->"""

"""count"""
# print(sr1.count()) 
# the difference between count and size is that count do not count missing values,whereas size count missing values too.

"""sum,product"""
# print(sr.sum())
"""mean,median,mode,std,var"""
# print(sr.mean())
# print(sr1.median())
# print(sr2.mode().values[0])
"""min/max"""
# print(sr.min())
# print(sr.max())
# print(sr1.describe())
# print(sr.describe())

"""<-----------------Series Indexing------------------------>"""
np.random.seed(42)
se=pd.Series(np.random.randint(1,100,15))
# print(se)
# print(se[12])
# negative indexing does not work and throws an error
# print(sr2[0])
# print(sr2['Uri: The Surgical Strike'])
# print(sr2[-1])
# print(sr1[-1]) when custom index is a string negative index will work but if it is a number it will not work
"""slicing"""
# print(sr1[-5:]) #just like python list
# print(sr1[[1,2,5,7]]) # fancy indexing

"""<--------------Editing items in Series------------------->"""
# index
# sr_c['India']=1.1
"""index is not there"""
sr_c["New Zealand"]=0.13
# print(sr_c.tail()) add the new item to the end of the series

#slicng
sr_c[2:4]=[0.06,0.7]
# print(sr_c)

#fancy indexing
sr_c[[12,11,10]]=[0.10,0.13,0.09]
# print(sr_c)

""""<---------------Series with Python Functionality-------------------->"""
#len/type/dir/min/max/
print(len(sr))
print(type(sr))
print(dir(sr))
print(max(sr))
print(min(sr))