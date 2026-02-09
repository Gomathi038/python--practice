def calculate_result(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average


s = int(input("Enter number of students: "))

for i in range(s):
    print(f"\n--- Student {i+1} ---")
    
    name = input("Enter student name: ")
    
    n = int(input("Enter number of subjects: "))
    marks = []
    
    for j in range(n):
        m = int(input(f"Enter marks {j+1}: "))
        marks.append(m)
    
    total, average = calculate_result(marks)
    
    print("Student Name:", name)
    print("Total Marks:", total)
    print("Average Marks:", average)
    
    if average >= 90:
        print("Your Grade is: O")
    elif average >= 70:
        print(" your Grade is: A")
    elif average >= 50:
        print(" your Grade is: B")
    else:
        print(" your Grade is : F")
