def calculate_result(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average


n = int(input("Enter number of subjects: "))
marks = []

for i in range(n):
    m = int(input(f"Enter marks {i+1}: "))
    marks.append(m)

total, average = calculate_result(marks)

print("Your Total marks:", total)
print("Your Average marks:", average)

if average >= 50:
    print("You are passed in your exam")
else:
    print("You are failed in your exam")
