import pandas as pd
import numpy as np
import matplotlib.pyplot
"""<-----------------Dataframes Methods-------------------->"""


"""--------------1)value_counts----------"""
# df=pd.read_csv("OOPs-Numpy-Pandas-in-Python/Pandas/pandas2/student_placement_data.csv")
# print(df.head(10))
df=pd.DataFrame([
    [87,1,8.9,1],
    [96,0,9,0],
    [76,0,6.9,1],
    [67,1,7.4,0],
    [89,0,8.2,1],
    [89,0,8.2,1],
    [89,1,5.6,0]
    ],columns=["IQ","Gender","CGPA","Placement"])
# print(df.value_counts()) it gives the number of times each row is repeated
ipl=pd.read_csv("OOPs-Numpy-Pandas-in-Python/Pandas/pandas2/ipl-matches.csv")
# print(ipl[(ipl['MatchNumber'=="Final"]) | (ipl['MatchNumber'=='Semi Final'])][ 'Player_of_Match'].value_counts)
# print(ipl[(ipl['MatchNumber']=='Final') | (ipl["MatchNumber"]=="Semi Final")]['Player_of_Match'].value_counts().index[0])
# print(ipl[~(ipl["MatchNumber"].str.isdigit())]["Player_of_Match"].value_counts())
# print(ipl['TossDecision'].value_counts().plot(kind='pie'))
# print((ipl['Team1'].value_counts()+ipl['Team2'].value_counts()).sort_values(ascending=False))


"""------------2) sort_values---------------"""
movies=pd.read_csv("OOPs-Numpy-Pandas-in-Python/Pandas/pandas2/movies.csv")
# print(movies.sort_values('title_x',ascending=False,na_position='first'))
# if the dataframe contains missing values then we give additional parameter na_position='first' or 'last'
# print(movies.columns)
# print(movies.sort_values(['year_of_release','title_x'],ascending=[True,False]))




"""-------------rank--------------"""
batsman=pd.read_csv("OOPs-Numpy-Pandas-in-Python/Pandas/pandas2/batsman_runs_ipl.csv")
batsman['rank']=batsman["batsman_run"].rank(ascending=False)
# print(batsman.sort_values('rank'))

"""<--------sort_index--------------------->"""
marks=pd.DataFrame([
    ["Ayush",98,79,85],
    ["Optimius Prime",99,75,95],
    ["Zaraki Kenpachi",88,59,65],
    ["Zuko",68,89,89]
],columns=["Name","Science","Maths","English"])
# marks.set_index('Name')
# print(marks.sort_index(ascending=False))


"""set_index"""
batsman.set_index("batter",inplace=True)
# print(batsman)

"""reset_index"""
# batsman.reset_index(inplace=True)
# print(batsman)
batsman.reset_index(inplace=True)
batsman.set_index('rank',inplace=True)
# print(batsman)
movies.set_index('title_x',inplace=True)

"""----------rename--------------"""
movies.rename(columns={
    "title_x" : 'index',
    'poster_path' : 'link',
    'imdb_id' : 'imdb'
},inplace=True)
movies.rename(index={
    "Uri: The Surgical Strike":"URI",
    "Battalion 609":"Bat"

},inplace=True)

# print(movies.head())
"""<-------------unique and nunique------------>"""
np.random.seed(42)
t=pd.Series(np.append(np.random.randint(1,10,15),np.ones(5)*np.nan))
# print(t)
# print(t.unique())
# print(len(t.unique()))
# print(t.nunique()) it does not count the missing values (NaN)

"""<--------------isnull/hasNan/notnull----------------------->"""

# print(t.isnull())
# print(t.notnull())
# print(t.hasnans)
student=pd.read_csv("OOPs-Numpy-Pandas-in-Python/Pandas/pandas2/student_placement_data.csv")
# print(student.isnull())
# print(student.notnull())
"""-----dropna------------"""
# print(len(student))
student.dropna()
# print(len(student))
# print(student.isna().sum())
student.dropna(how="all",inplace=True)# it removes the record which contain all values as NaN
# print(len(student))
student.dropna(subset=['Name'],inplace=True) # use subset to remove the records which contains the missing values of the particular column given in subset

# print(student.isna().sum())


"""<--------------------fillna--------------------------->"""
student['Package']=student['Package'].fillna(student['Package'].mean())
# print(student['Package'][80:])
# print(student['Package'].mean())

"""<---------------drop_duplicates------------------>"""
# print(student.duplicated().sum()) #9
student.drop_duplicates(inplace=True)
# print(student.duplicated().sum()) 
print(ipl.columns)
# print(ipl[(ipl['City']=='Delhi') & ((ipl["Team1Players"].str.contains('V Kohli')) | ((ipl["Team1Players"].str.contains('V Kohli'))))])

vk=ipl[((ipl["Team1Players"].str.contains('V Kohli')) | (ipl["Team2Players"].str.contains('V Kohli')))]


# print(vk[vk['City']=='Delhi'].head(1))

ipl['all_players']=ipl['Team2Players']+ipl['Team1Players']
def did_play(sr):
    return 'V Kohli' in sr
ipl['did_play']=ipl['all_players'].apply(did_play)
# print(ipl[['did_play','all_players']])


# print(ipl[(ipl['City']=='Delhi') & (ipl['did_play']==True)].drop_duplicates(subset=["City","did_play"],keep='first'))

"""<-------drop------------------------->"""
#<----in Series------------->
np.random.seed(42)
n=np.random.randint(10,30,13)
sr=pd.Series(n)
# print(sr)
sr.drop(index=[11,12],inplace=True)
# print(sr)

#dataframe

#to delete the columns

# student.drop("Internships",axis=1,inplace=True) #to delete the single column
student.drop(columns=["Internships","Extra Curricular Score"],axis=1,inplace=True)
# print(student.head())

#to delete the rows
student.drop(index=[1,2,3,4,5],axis=0,inplace=True)
# print(student.head())


"""<---------------apply---------------------------->"""

#for Series
t=np.random.randint(10,20,10)
sr=pd.Series(t)
# print(sr)
def sigmoid(value):
    return 1/(1+np.exp(-value))
sr=pd.Series(t).apply(sigmoid)
# print(sr)
import random
def create_list():
    l=[]
    for i in range(6):
        l.append((random.randint(1,23),(random.randint(1,23))))
    return l
l1=create_list()
l2=create_list()  
d={ "first_points":l1,"second_points":l2}
df=pd.DataFrame(d)
import math
df['All_Points']=df['first_points']+df['second_points']
# print(df.head(5))  
def cal_dis(t):
    d=(((t[0]-t[2])**2)+((t[1]-t[3])**2))**0.5
    return d
df['eucilidean_distance']=df['All_Points'].apply(cal_dis)
print(df.head(5))