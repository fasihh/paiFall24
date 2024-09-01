students = {
    "fasih": [69, 71, 82, 96, 86],
    "owais": [98, 84, 85, 88, 82],
    "ali":   [97, 91, 65, 72, 88],
    "abser": [89, 94, 73, 63, 83]
}

def add_student(student, grades=[]):
    students[student] = grades

def add_grade(student, grade):
    if student in students:
        students[student].append(grade)
        return
    print("student does not exist")
    
def get_student_average(student):
    grades = students[student]
    total = 0
    for grade in grades:
        total += grade
    return total/len(grades)

def remove_student(student):
    if student in students:
        students.pop(student)
        return
    print("student does not exist")
    
new_student = input("enter new student name: ")
add_student(new_student)

while True:
    if input("would you like to enter a new grade for the student? (y/n): ").lower() == 'n':
        break
    add_grade(new_student, float(input("enter grade (out of 100): ")))

for student in students:
    print(student, students[student], sep='\n')

average_of = input("find average of student: ")
print("average", get_student_average(average_of))

remove = input("remove student: ")
remove_student(remove)

for student in students:
    print(student, students[student], sep='\n')
