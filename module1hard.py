grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = sorted({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'})

#for i in zip(students, grades):
#    print(i)

students_grades = dict(zip(students, grades))

for student in students_grades:
    avg_grade = sum(students_grades[student]) / len(students_grades[student])
    print(f"Average grade for {student} - {avg_grade}")
