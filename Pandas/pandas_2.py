import pandas as pd

df=pd.read_csv("OOPs-Numpy-Pandas-in-Python/Pandas/pokemon.csv",index_col="name")


# print("The number of pokemons having attack value greater than 150 are :",(df["attack"]>150).sum())
# print(df.loc[df["attack"]>150])
# print(df.loc[df["hp"]==df['hp'].min()])
# print((df['legendary']==False).sum())
# print(df['hp'].mean())
# print(df.loc[df['hp']==df["hp"].max()])
# print(df.loc[df['legendary']==True])


# print(df.loc[(df["type1"]=='Ghost') & (df['type2']=='Poison')])
# print(df.loc[(df["type1"]=='Flying') & (df['type2']=='Fire')])
# print(((df["type1"]=='Ghost') & (df['type2']=='Ghost')).sum())


# print(df.value_counts("type1"))
# print(df['type1'].value_counts())

# # print(df["power"].mean())
# # #----------Pokemon having power greater than 425----->
# # # print(df.loc[df["power"]>500])
# # #----------number of pokemons----->
# # print((df["power"]>550).sum())
# # print(df.loc[df["power"]>550])
print(df.loc[df['type1']=='Fire'].sort_values(by='defense'))

# # #------------strongest pokemon---------------------->
# # print(df.loc[df["power"]==df["power"].max()])
(df['legendary']==True)

# # #---------------speed less or equal to 30------------->
# # print(df.loc[df["speed"]<=30])


# #----------defence greater than 95--------->
# # print(df.loc[df["defense"]>95])

# #----------------Legendary---------------->
# # print("The number of legendary pokemons are",(df["legendary"]==True).sum())
# # print("The legendary pokemons are :")
# # print(df.loc[df['legendary']==True])

# # #--------------------Highest defence with low attack pokemon------->
# print(df.sort_values(by=["defense","attack"],ascending=[False,True]))
# # print(df.loc[(df['attack']==df["attack"].min()) | (df['defense']==df['defense'].max())])
