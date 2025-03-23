import pandas as pd
df=pd.read_csv("OOPs-Numpy-Pandas-in-Python/Pandas/words_values.csv",index_col='Word')
# print(df.head(10))

""" How many elements does the dataframe have"""

# print(df.shape)
# print(df.info())

""" what is the value of the word apple """

# print(df.loc["apple","Word Value"])
# print(df.loc["elephant","Number of Characters"])
#it takes two argument and we can specify the column name


""" what is the  highest possible value of the word """
# print(df.max())
# print(df.min())
# print(df.describe())
# chr_5=df[df["Number of Characters"]>5]
# print(chr_5.head())
print(df.loc[(df["Number of Characters"]==3) & (df["Word Value"]==17)])
print(df.loc[df["Number of Characters"]>5,"Number of Characters"])
# print(df[df["Word Value"]==50])

#---------sorting the specific column------->
# print(df.sort_values(by="Number of Characters",ascending=False))

df=pd.read_csv("OOPs-Numpy-Pandas-in-Python/Pandas/words_1932.csv",index_col="Word")
df1=pd.read_csv("OOPs-Numpy-Pandas-in-Python/Pandas/words_values.csv",index_col="Word")
print(df.head(10))
print(df.info())
print(df.shape)
print(df.loc["ufwakokc","value"])
print(df.loc[df["value"]==193])
print(df.describe())

print(df.sort_values(by="value",ascending=False).head(5))

print(df1["value"].mode())
print(df["value"].value_counts())
print(df.loc[df["value"]==80].head(20))
print(df.loc[df["value"]==66].sort_values(by="chr"))

print(df.loc[(df["value"]==66)  & (df['chr']==df.loc[df["value"]==66,'chr'].min())])


df["ratio"]=df['value']/df["chr"]
# # print(df.head())

#print(df.sort_values(by='ratio',ascending=False).head(1))
print(df.loc[df['ratio']==df["ratio"].max()])
print(df.loc[(df["value"]==78) & (df["chr"]==df.loc[df["value"]==78,'chr'].min())])

print(df.loc[df['ratio']==13].shape)

print(df.loc[(df["ratio"]==13) & (df["value"]==df.loc[df["ratio"]==13,"value"].max())].shape)
# print(df.loc[df['ratio']==])
print(df.loc[df["ratio"]==13,'value'].max())

print(df.loc[df["value"]==80,'chr'].min())
print(df.loc[(df["value"]==80) & (df["chr"]==df.loc[df["value"]==80,'chr'].min())])

print(df.loc[df["chr"]> 6.512422 ].shape)


