import pandas as pd

df=pd.read_csv("OOPs-Numpy-Pandas-in-Python/Pandas/pokemon.csv",index_col="name")
# print(df["power"].mean())
# #----------Pokemon having power greater than 425----->
# # print(df.loc[df["power"]>500])
# #----------number of pokemons----->
# print((df["power"]>550).sum())
# print(df.loc[df["power"]>550])


# #------------strongest pokemon---------------------->
# print(df.loc[df["power"]==df["power"].max()])


# #---------------speed less or equal to 30------------->
# print(df.loc[df["speed"]<=30])


#----------defence greater than 95--------->
# print(df.loc[df["defense"]>95])

#----------------Legendary---------------->
print(df['legendary'].sum())
print(df.loc[df['legendary']==True])