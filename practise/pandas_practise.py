# Series is a one dimensional labeled array.

import pandas as pd
from pandas.core.methods.selectn import DataFrame

# marks = pd.Series([80,90,100,110])
# print(marks)
# datatype:int64

student_marks = pd.Series([80, 90, 100, 110], index=['rajiv', 'riya', 'mohit', 'shweta'])
print(student_marks)
print(student_marks.get("rajiv"))

########################## DATAFRAME #######################################
data = {
    "Name": ["Raj", "Amit", "Riya"],
    "Age": [35, 30, 28],
    "City": ["Chandigarh", "Delhi", "Mumbai"]
}

df = pd.DataFrame(data)
print(df)

####################################### READING DATA FROM CSV ##################################
df = pd.read_csv("C:/Users/admin/PycharmProjects/PythonProject1/employees.csv")
print(df) # print all the data
print(df["Name"])
# print(df.head(1)) # print only 1st row of data
# print(df.tail(1)) # print only last row of data
# print(df.info()) # print the information about the data

############### Filter data ############
result = df[df['Age'] < 30]
print(result)
# ########### Add a new colum ###########
# df["Bonus"] = df["Salary"] * 0.10
# print(df)
#
# ########### update values ##############
# df.loc[df["Name"] == "Raj", "Salary"] = 60000
# print(df)

