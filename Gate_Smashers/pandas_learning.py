import pandas as pd

# convert dictionary into a dataframe
stu_data = [{"name": "shamu", "age": 14},
             {"name": "ramu",
             "age": 8
             }]
df = pd.DataFrame(stu_data)
print(df.head(1))
print(df.tail(1))
print(df.shape)
print(df.columns)
print(df['age'])
# print(df.describe())
print(df.size)
print(df.values)
print(df.index)

# # stu_data = [("shamu", 14),
# #             ("ramu",8)]
# df = pd.DataFrame(stu_data).get(["name", "age"])
# df.index = ["student1", "student2"]
# df.columns = ["student_name", "student_age"]
# df["student_rollno"] = [1, 2]
# df["student_age"] = df["student_age"] + 1
#
# # remove row where age is less than 9
# df = df[df["student_age"] > 9]
# print(df)
#
# print(df)
