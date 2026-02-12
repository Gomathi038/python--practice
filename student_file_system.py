def calaculate_average(marks):
    return sum(marks)/len(marks)

file=open("students.txt","w")

s=int(input("Enter number of student:"))

for i in range(s):
    print(f"\n------- students{i+1}")
    name=input("Enter student name:")
    n=int(input("Enter number of subject:"))

    marks=[]
    for j in range(n):
        m=int(input(f"Enter Marks{j+1}:"))
        marks.append(m)

    avg=calaculate_average(marks)

    file.write(f"Name:{name}\n")
    file.write(f"Marks:{marks}\n")
    file.write(f"Average:{avg:.2f}\n")
    file.write("==================\n")

file.close()

print("\n Data saved successfully")

print("\n====== Students Records==========")
file=open("students.txt","r")
content=file.read()
print(content)
file.close()
