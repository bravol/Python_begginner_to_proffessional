student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key in student_scores:
    # print(key)  names
    # print(student_scores[key])  # scores
    name = key
    score = student_scores[name]

    if score >= 91:
        student_grades[name] = "Outstanding"
    elif score >= 81:
        student_grades[name] = "Exceeds Expectations"
    elif score >= 71:
        student_grades[name] = "Acceptable"
    else:
        student_grades[name] ="Failed"
print(student_grades)