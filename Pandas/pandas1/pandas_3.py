import pandas as pd

countries = [
    "India", "USA", "Canada", "Australia", "Brazil", "South Africa", "Kenya", "Nigeria", 
    "Mexico", "Argentina", "Egypt", "Ghana", "Indonesia", "Vietnam", "Philippines", "Saudi Arabia", "Malaysia", "Algeria",
    "Chile", "Colombia", "Peru", "Ethiopia", "Turkey", "Japan", "South Korea", "North Korea", "Cuba", "Venezuela"
]

independence_years = [
    1947, 1776, 1867, 1901, 1822, 1910, 1963, 1960, 
    1810, 1816, 1922, 1957, 1945, 1945, 1946, 1932, 1957, 1962,
    1818, 1810, 1821, 1941, 1923, 660, 1945, 1945, 1902, 1811
]

myseries=pd.Series(independence_years,countries)
# print(myseries)
# print(myseries['India'])


programming_languages = {
    "Python": 1991,
    "Java": 1995,
    "C": 1972,
    "C++": 1985,
    "JavaScript": 1995,
    "Ruby": 1995,
    "Swift": 2014,
    "Go": 2009,
    "Rust": 2010,
    "Kotlin": 2011
}
# print(pd.Series(programming_languages))

smartphones = {
    "iPhone 13": 3227,
    "Samsung Galaxy S22": 3700,
    "Google Pixel 7": 4355,
    "OnePlus 10 Pro": 5000,
    "Xiaomi 12 Pro": 4600
}
camera_megapixels = {
    "iPhone 13": 12,
    "Samsung Galaxy S22": 50,
    "Google Pixel 7": 50,
    "OnePlus 10 Pro": 48,
    "Xiaomi 12 Pro": 50
}
s1=pd.Series(smartphones)
s2=pd.Series(camera_megapixels)
# print(s1["OnePlus 10 Pro"])
# print(s1.keys())
# print(s1.values)

s1=s1+200 #broadcasted
# print(s1.values)


sales_q1 = {
    "Apple": 120.5,
    "Microsoft": 90.3,
    "Google": 75.2,
    "Amazon": 110.8,
    "Tesla": 45.7,
    "Meta": 35.6,
    "Samsung": 85.4,
    "Intel": 18.9,
    "Netflix": 8.1,
    "Adobe": 5.9,
    "IBM": 15.3,       # Present in Q1, but not in Q2
    "Sony": 22.4,       # Present in Q1, but not in Q2
    "Nvidia": 30.5      # Present in Q1, but not in Q2
}
sales_q2 = {
    "Apple": 130.2,
    "Microsoft": 95.7,
    "Google": 78.9,
    "Amazon": 115.4,
    "Tesla": 50.1,
    "Meta": 38.2,
    "Samsung": 88.6,
    "Intel": 20.5,
    "Netflix": 9.0,
    "Adobe": 6.3,
    "Oracle": 17.8,     # Present in Q2, but not in Q1
    "AMD": 19.6,        # Present in Q2, but not in Q1
    "Salesforce": 25.1  # Present in Q2, but not in Q1
}
q1=pd.Series(sales_q1)
q2=pd.Series(sales_q2)
sum_sales=q1+q2
# print(sum_sales)

all_sum_sales=q1.add(q2,fill_value=0)

# print(all_sum_sales)

#--------- Creating a  dataframe-------------->

import numpy as np
np.random.seed(101)
mydata=np.random.randint(0,101,(4,3))
my_index=["IN",'NZ','SA','IRE']
my_columns=[2008,2011,2019]
df=pd.DataFrame(mydata,my_index,my_columns)
# print(df)


#------------------ Working with csv----------------------->
#bill,tip,sex,smoker,day,time,price_per_person,name
df=pd.read_csv("OOPs-Numpy-Pandas-in-Python/Pandas/tip.csv",index_col="name")
# print(df.head())
# print(df.columns)
# print(df.describe().transpose())

# print(df[['tip','bill']])

df['tip_percentage']=np.round((df['tip']/df['bill'])*100,2)
# print(df.head())

# print(df.drop('tip_percentage',axis=1))
# print(df.head(5))

# to remove a column permanently add attribute inplace=True or df=df.drop('column/row_name',axis=1/0)
# print(df.drop('tip_percentage',axis=1,inplace=True))
# print(df.head(2))
print(df.loc[['John','David','Emma']])