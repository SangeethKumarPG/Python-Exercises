student_scores={
    "Harry":81,
    "Ron":78,
    "Hermoine":99,
    "Draco":74,
    "Neville":62
}
student_grade = {}

for keys in student_scores:
    if student_scores[keys] >=91 and student_scores[keys] <= 100:
        student_grade[keys] = "Outstanding"
    elif student_scores[keys] >=81 and student_scores[keys] <= 90:
        student_grade[keys] = "Exceeds Expectation"
    elif student_scores[keys] >=71 and student_scores[keys] <= 80:
        student_grade[keys] = "Acceptable"
    else:
        student_grade[keys] = "Fail"

for keys in student_grade:
    print(f"{keys} : {student_grade[keys]}")
