import pandas as pd
import numpy as np
movies=pd.read_csv("OOPs-Numpy-Pandas-in-Python/Pandas/pandas2/datasets/imdb-top-1000.csv")
top_gross_genres=movies.groupby("Genre")['Gross'].sum().sort_values(ascending=False).head(3)
# print(top_gross_genres)
# print(genres.min())
#3 genres that produced the maximum gross
# print(movies.sort_values('Gross',ascending=False).drop_duplicates(subset=["Genre"],keep='first')['Genre'].head(3))
top_imdb_genre=movies.groupby('Genre')['IMDB_Rating'].mean().sort_values(ascending=False).index[[0,1,2]]
# print(top_imdb_genre)
top_director_popular=movies.groupby('Director')['No_of_Votes'].sum().sort_values(ascending=False).index[[0,1,2]]
print(movies.columns)
# print(top_director_popular)
# print(movies['Star1'].value_counts())
"""no of groups formed  (len/nunique)"""
# print(len(movies.groupby('Genre')))
# print(movies['Genre'].nunique())
"""no of records/rows in each group  (size/value_counts)"""
# print(movies.groupby('Genre').size())
# print(movies['Genre'].value_counts())
"""to get the first/last/nth record of each group use (first/last)"""
genres=movies.groupby('Genre')
# print(genres.first())
# print(genres.last())
# print(genres.nth(6))

"""<---------------to get all the all records of a particular group-------->"""
# print(genres.get_group('Horror'))
# print(movies[movies['Genre']=='Horror'])

# print(genres.groups)

"""describe/sample/nunique"""
# print(genres.describe())
# print(genres.sample(2,replace=True))
# print(genres.nunique())


"""<---------------agg method (use to specify the operation to be applied on a particular column----------------->"""
#passing dictionary

dict_agg=(genres.agg(
    {
       "Runtime" : ["min","max","mean"],
       "IMDB_Rating" : ["min","max","mean"],
       "Gross" : ["min","max","mean"],
       "Metascore" : ["min","max","mean"],
       "No_of_Votes" : ["min","max","mean"],

    }
))
# print(dict_agg)
#passing list
# list_agg=genres.agg(["min","max","mean"])
# print(list_agg)
df=pd.DataFrame(columns=movies.columns)
for group,data in genres:
    df=df._append(data[data["IMDB_Rating"]==data['IMDB_Rating'].max()])
# highest_rated_movie_genre=movies.groupby("Genre").max()[['IMDB_Rating','Series_Title']]
# print(highest_rated_movie_genre) sorted by alphabets in terms of categorical data
# print(df[['Series_Title','Director']])
print(movies.columns)
genres=movies.groupby("Genre")
# print(genres.agg("min"))
def includes(record):
    c=0
    l=[]
    for i in record:
        if(i[0] in "Aa"):
            l.append(i)
            c+=1
    return c,l
            

# print(pd.DataFrame(genres['Series_Title'].apply(includes)))
for group,data in genres:
    data["rank"]=data["IMDB_Rating"].rank(ascending=False).sort_values()
    # print(data[["Series_Title","rank","IMDB_Rating"]].sort_values("rank"))
def norm(group):
    group["norm_rating"]=(group["IMDB_Rating"]-group["IMDB_Rating"].min())/(group["IMDB_Rating"].max()-group["IMDB_Rating"].min())
    return group

# print(genres.apply(norm)[['Series_Title','norm_rating']].sample(30))


"""groupby on multiple columns"""
act_dir=movies.groupby(["Director","Star1"])
# print(duo.size())
# print(duo.get_group(("Aaron Sorkin","Eddie Redmayne")))
# print(act_dir["Gross"].sum().sort_values(ascending=False).head(1))
act_gen=movies.groupby(["Star1","Genre"])
# print(act_gen["Metascore"].mean().reset_index().sort_values("Metascore",ascending=False).head(1))
# print(act_dir.agg(
#     {
#          'Runtime':  ["min","max","mean"],
#           'IMDB_Rating':  ["min","max","mean"],
#          'No_of_Votes':  ["min","max","mean"],
#         'Gross':  ["min","max","mean"],
#           'Metascore':  ["min","max","mean"],
#     }
#   ))

ipl=pd.read_csv("OOPs-Numpy-Pandas-in-Python/Pandas/pandas2/datasets/deliveries.csv")
print(ipl.columns)
batsman=ipl.groupby("batsman")
# print(batsman["batsman_runs"].sum().reset_index().sort_values("batsman_runs",ascending=False))
ipl_6=ipl[ipl["batsman_runs"]==6]
# print(ipl_6.groupby("batsman")['batsman_runs'].count().sort_values(ascending=False))
ipl_4_6=ipl[(ipl['over']>15) & ((ipl["batsman_runs"]==4) | (ipl["batsman_runs"]==6))]
# print(ipl_4_6[['batsman','over','batsman_runs']])
# print(ipl_4_6.groupby("batsman")["batsman"].count().sort_values(ascending=False))
temp_df=ipl[ipl['batsman']=="AB de Villiers"]
# print(temp_df.groupby('bowling_team')['batsman_runs'].sum().reset_index())

def highscore(player):
    temp_df=ipl[ipl['batsman']==player]
    return temp_df.groupby("match_id")['batsman_runs'].sum().reset_index().sort_values("batsman_runs",ascending=False).head(1).values[0][1]
rec=highscore("AB de Villiers")
print(rec)