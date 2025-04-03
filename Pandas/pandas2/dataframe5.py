import numpy as np
import pandas as pd
import random
#To fetch a single item we need only one thing that is it corresponding index (Series) (1d)
#To fetch a single item we need two things  that is it corresponding index and the  specific column name (Dataframe) (2d)
"""no of items required to fetch a particular data is the dimension of the data for series 1 is required that is index,for dataframe 2 is required that is index and column and for 3 3 things are required that is indexes and 1 column for multi_indexing dataframe"""
index=[]
random.seed(42)
for i in range(10):
    index.append((random.choice(["computer_science","mechanical","electrical","electronics","information_technology"]),random.randint(2020,2025)))
index=list(set(index))
# print(index)
l=[('information_technology', 2025), ('electrical', 2020), ('electrical', 2023), ('mechanical', 2025), ('electrical', 2022), ('computer_science', 2023), ('electrical', 2025), ('information_technology', 2020), ('electrical', 2024)]
no_of_students=np.random.randint(120,300,len(l))
sr=pd.Series(no_of_students,index=l)
# print(sr)
# print(sr[('electrical', 2023) ])
"""<------------multiindex object------------------->"""
#1) using from_tuple
multi_index=pd.MultiIndex.from_tuples(l)
# print(multi_index)
# print(multi_index.levels)

#2) using from_product
multi_index_2=pd.MultiIndex.from_product([["cse","me","ece","b.ph","mba"],[2020,2021,2022]])
# print(multi_index_2)

"""multi_index series"""
np.random.seed(42)
sr=pd.Series(np.random.randint(200,400,len(multi_index_2)),index=multi_index_2)
# print(sr)
# print(sr['ece',2021])
# print(sr['ece'])

"""unstack (to convert the multi_index series to dataframe)"""
df=sr.unstack()

"""stack (do the vice-versa of unstack)"""
# print(df.stack())


"""<-------------multi_index_dataframe---------------------->"""
d=[('computer_science', 2020), ('electrical', 2021), ('information_technology', 2020), ('mechanical', 2021), ('computer_science', 2025), ('information_technology', 2023), ('mechanical', 2024), ('computer_science', 2021)]
multi_index=pd.MultiIndex.from_tuples(d)
multi_index_2=pd.MultiIndex.from_product([["CSE","IT"],[2020,2021,2022,2023]])
# print(len(multi_index))
x2=np.random.randint(200,500,(len(multi_index_2),2))
x2[:,0]=np.random.randint(2,15,len(multi_index_2))
# print(x2)
df=pd.DataFrame(x2,index=multi_index_2,columns=["avg_package","no_of_students"])
# print(df)
# print(df.loc["CSE"])
# print(df.loc["CSE",2023])
# print(df.loc["CSE"]["avg_package"])
np.random.seed(42)
x5=np.random.randint(200,500,(10,4))

x5[:,::2]=np.random.randint(2,17,(10,2))
multi_columns=pd.MultiIndex.from_product([["CSE","IT"],["Avg_Package","No_of_students"]])
df=pd.DataFrame(x5,columns=multi_columns,index=np.arange(2015,2025))

print(df.loc[2018]["CSE","Avg_Package"])