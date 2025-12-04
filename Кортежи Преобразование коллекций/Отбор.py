n = int(input())

students = []
for _ in range(n):
    student_info = input()
    students.append(student_info)

for student in students:
    print(student)

print()

for student in students:
    name, grade = student.split('\t')
    if int(grade) >= 4:
        print(student)
