M = int(input())

students_on_all_lessons = set(input() for _ in range(int(input())))

for _ in range(M - 1):
    students_on_current_lesson = set(input() for _ in range(int(input())))

    students_on_all_lessons &= students_on_current_lesson

for student in students_on_all_lessons:
    print(student)
