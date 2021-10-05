
def avgPerStudent(studentGrades):
    student1 = studentGrades[0]
    ansStudent1 = 0
    for number in student1:
        ansStudent1 += number
    ansStudent1 = ansStudent1 / 3

    student2 = studentGrades[1]
    ansStudent2 = 0
    for number in student1:
        ansStudent2 += number
    ansStudent2 = ansStudent2 / 3

    student3 = studentGrades[2]
    ansStudent3 = 0
    for number in student3:
        ansStudent3 += number
    ansStudent3 = ansStudent3 / 3

    student4 = studentGrades[3]
    ansStudent4 = 0
    for number in student4:
        ansStudent4 += number
    ansStudent4 = ansStudent4 / 3

    return round(ansStudent1, 2), round(ansStudent2, 2), round(ansStudent3, 2), round(ansStudent4, 2)


def avgAllStudents(studentGrades):
    ans = 0
    for lst in studentGrades:
        for number in lst:
            ans += number
        ans = ans / 3
    return round(ans, 2)


studentGrades = [[95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0]]
print(avgPerStudent(studentGrades))
print(avgAllStudents(studentGrades))
