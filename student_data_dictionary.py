def calculate_average(marks):
    return sum(marks) / len(marks)

students = []

s = int(input("Enter number of students: "))

for i in range(s):
    print(f"\n---------- Student {i+1} ----------")

    student = {}
    student["name"] = input("Enter student name: ")

    n = int(input("Enter number of subjects: "))
    marks = []

    for j in range(n):
        m = int(input(f"Enter marks {j+1}: "))
        marks.append(m)

    student["marks"] = marks
    student["average"] = calculate_average(marks)

    avg = student["average"]

    if avg >= 90:
        student["grade"] = "O"
    elif avg >= 70:
        student["grade"] = "A"
    elif avg >= 50:
        student["grade"] = "B"
    else:
        student["grade"] = "F"

    students.append(student)

print("\n--- Student Details ---")
for st in students:
    print(st)
