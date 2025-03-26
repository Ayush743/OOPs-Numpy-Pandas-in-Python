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



"""---------------------------"""