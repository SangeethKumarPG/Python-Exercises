import pandas

student_score = {
    "student" : ["Maine", "Alex", "Arun"],
    "score" : [79,60,88]
}

#looping over dictionary items

# for (key, value) in student_score.items():
#     print(f"{key} : {value}")

student_data_frame = pandas.DataFrame(student_score)

# print(student_data_frame)

#looping over the data frame traditional way

# for (key,values) in student_data_frame.items():
#     print(key)
#     print(values)

#iterating over dataframe through iterrow() method

for (index,row) in student_data_frame.iterrows():
    # print(row)
    # print(index)
    # print(row.student)
    # print(row.score)
    print(f"{row.student}   {row.score}")