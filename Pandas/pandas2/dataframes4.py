import pandas as pd
import numpy as np
courses=pd.read_csv("OOPs-Numpy-Pandas-in-Python/Pandas/pandas2/datasets/courses.csv")
students=pd.read_csv("OOPs-Numpy-Pandas-in-Python/Pandas/pandas2/datasets/students.csv")
nov=pd.read_csv("OOPs-Numpy-Pandas-in-Python/Pandas/pandas2/datasets/reg-month1.csv")
dec=pd.read_csv("OOPs-Numpy-Pandas-in-Python/Pandas/pandas2/datasets/reg-month2.csv")
matches=pd.read_csv("OOPs-Numpy-Pandas-in-Python/Pandas/pandas2/datasets/matches.csv")
ipl=pd.read_csv("OOPs-Numpy-Pandas-in-Python/Pandas/pandas2/datasets/deliveries.csv")


#<-------------To vertically stack 2 dataframes---------->
reg=pd.concat([nov,dec],ignore_index=True) 
# or
nov._append(dec,ignore_index=True)
# to differentiate between 2 dataframes 
reg2=pd.concat([nov,dec],keys=['nov','dec'])
# print(reg2)
# print(reg2.loc["nov"])
# print(reg2.loc[("nov",3)])
# print(pd.concat([nov,dec],axis=1))#to stack horizontally axis=1
# courses=courses.merge(reg,how="inner",on="course_id")
# df=students.merge(courses,how="inner",on="student_id")
# print(df[['name','course_name']])
"""<-----inner_join----->"""
df1=students.merge(reg,how="inner",on="student_id")
# print(df1)

"""<-----left_join----->"""
df2=courses.merge(reg,how="left",on="course_id")
# print(df2)

"""<----right_join--------->"""
temp=pd.DataFrame({
    "student_id" :[26,27,28],
    "name" :["Ayush","Hinata","Kanao"],
    "partner" :[15,17,21],
})
students=pd.concat([students,temp],ignore_index=True)
# print(students)
df3=students.merge(reg,how="right",on="student_id")
# print(df3)
reg=pd.concat([nov,dec],ignore_index=True)
df=reg.merge(courses,how="inner",on="course_id")
# print(df)
# print("Total Revenue : ₹",df["price"].sum())

# reg=pd.concat([nov,dec],keys=["nov",'dec'])
nov_rev=nov.merge(courses,on="course_id")['price'].sum()
dec_rev=dec.merge(courses,on="course_id")['price'].sum()
# print("The revenue in november is ₹",nov_rev)
# print("The revenue in november is ₹",dec_rev)
import matplotlib.pyplot as plt
registration=reg.merge(courses,on="course_id").merge(students,on="student_id")
reg.merge(courses,on="course_id").groupby("course_name")['price'].sum().plot(kind="bar")
# plt.show()
arr_id=np.intersect1d(nov["student_id"],dec["student_id"])
# print(students[students["student_id"].isin(arr_id)])
diff_arr=np.setdiff1d(courses['course_id'],reg["course_id"])
# print(courses[courses["course_id"].isin(diff_arr)])

# df=pd.read_csv("OOPs-Numpy-Pandas-in-Python/Pandas/pandas2/datasets/imdb-top-1000.csv")
# print(df.columns)
reg=pd.concat([nov,dec],ignore_index=True)
# print(df[df["Genre"]=="Horror"].sort_values("IMDB_Rating",ascending=False)[["Series_Title","IMDB_Rating","No_of_Votes","Released_Year"]])
total_revenue=reg.merge(courses,on="course_id")["price"].sum()
# print(total_revenue)
# print("november month revenue :",nov.merge(courses,on="course_id")["price"].sum())
# print("december month revenue :",dec.merge(courses,on="course_id")["price"].sum())
temp_df=pd.concat([nov,dec],keys=["nov","dec"]).reset_index()
# print(temp_df.merge(courses,on="course_id").groupby("level_0")["price"].sum())
# print(reg.merge(courses,on="course_id").merge(students,on="student_id")[["name","course_name","price"]])

reg.merge(courses,on="course_id").groupby("course_name")["price"].sum().plot(kind="bar")
# plt.show()
# print(students[students["student_id"].isin(np.intersect1d(nov["student_id"],dec["student_id"]))])

df=reg.merge(courses,on="course_id")
# print(courses[courses["course_id"].isin(np.setdiff1d(courses["course_id"],reg["course_id"]))])
# print(students[students["student_id"].isin(np.setdiff1d(students["student_id"],reg["student_id"]))])
"""self_join"""
# print(students.merge(students,how="inner",left_on="partner",right_on="student_id")[["name_x","name_y"]])
df=reg.merge(students,on="student_id").reset_index()
print(df.groupby(["student_id","name"])["name"].count().sort_values(ascending=False).head(3))
df=reg.merge(courses,on="course_id").merge(students,on="student_id").groupby(["student_id","name"])["price"].sum().sort_values(ascending=False)
# print(df)