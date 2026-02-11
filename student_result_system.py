def calculate_average(marks):
    return sum(marks) / len(marks)

def calculate_grade(avg):
    if avg >= 90:
        return "O"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "F"

students = [] 
s = int(input("Enter the number of students: "))

for i in range(s):
    print(f"\nStudent details {i+1}")
    student = {}

    student["name"] = input("Enter the student name: ")
    n = int(input("Enter the number of subjects: "))

    marks = []
    for j in range(n):
        m = int(input(f"Enter the marks {j+1}: "))
        marks.append(m)

    avg = calculate_average(marks)

    student["marks"] = marks
    student["average"] = avg
    student["grade"] = calculate_grade(avg)

    students.append(student)

print("\n=== Student Report ===")
for st in students:
    print("\nName =", st["name"])
    print("Marks =", st["marks"])
    print("Average =", st["average"])
    print("Grade =", st["grade"])

topper = max(students, key=lambda x: x["average"])

print("\nTopper =", topper["name"])
print("With average of:", topper["average"])
