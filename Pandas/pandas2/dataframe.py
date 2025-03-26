import pandas as pd
import numpy as np
"""--------Creating DataFrames-------------"""
#------using lists--------------->
student_data=[
    ['Ayush',8.5,10],
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


"""Selecting cols from a Dataframe"""
# print(df1['Name'])
# print(movies[['actors','year_of_release','title_x']]) # choosing multiple columns
# print(ipl[["Team1","Team2","WinningTeam"]])
student_dict = {
    'Name': ['Ayush','Priyanka', 'Artik', 'Nidhi', 'Rohan', 'Sneha', 'Kunal'],
    'CGPA': [8.5, 8, 7, 6.5, 9.2, 7.5, 8.3],
    'Package(LPA)': [10,  7, 3, 8, 12, 5, 9],
    'Department': ['CS',  'HR', 'ECE', 'CS', 'IT', 'Finance', 'CS'],
    'Internship(LPA)': [2, 1, 1, 1.2, 2.5, 1.2, 2],
    'Placed': [True,  True, False, True, True, True, True],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male']
}

df=pd.DataFrame(student_dict,index=student_dict['Name'])
"""There are two ways to fetch the rows 
1) using iloc[] which always works whether the index is label or not,include only the starting index not the end
2) using loc[] used when the index is label and include both the passed values 
"""
# using iloc ie with index
# print(df.iloc[0]['Name'])
# print(df.iloc[0:7]['Name'])
# print(df.iloc[[0,5,3,2]]['Name']) fancing indexing
# print(df.loc['Ayush':'Priyanka'])


"<-------------Selecting both rows and columns---------->"
# print(movies.iloc[:3,:3])
# print(movies.loc[:2,'title_x':'poster_path'])

"""<-------------From the DataFrame ipl------------->"""

#<-------final winners----------->
# print(ipl[ipl['MatchNumber']=='Final'][['Season','WinningTeam']])

# <---no of superover-------------->
# print(f"the number of superovers are : {ipl[ipl['SuperOver']=='Y'].shape[0]}")


# <------number of matches srh won in kolkata------>
# print(ipl[(ipl['WinningTeam']=='Chennai Super Kings') & (ipl['City']=='Kolkata')].shape[0])

#<-------------percentage of toss winners winning the team------->
# print(ipl.columns)
# print((ipl[ipl['TossWinner']==ipl['WinningTeam']].shape[0])/len(ipl))

"""<------------From the DataFrame movies----------------->"""
print(movies.columns)

# print(movies[(movies['imdb_rating']>8) & (movies['imdb_votes']>10000)].shape[0])
def format(text):
    return text.split("|")
a=movies['genres'].str.contains('Action')
b=movies['imdb_rating']>8
# print(movies[a&b])

# print(movies[['year_of_release', 'runtime', 'genres']])

movies['actors']=movies['actors'].fillna("None")
movies['Lead_Actor']=movies['actors'].str.split("|").apply(lambda x : x[0])
print(movies[['Lead_Actor','actors']])