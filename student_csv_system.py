import csv
def calculate_average(marks):
    return sum(marks)/len(marks)

with open("student.csv","w",newline="") as file:
    writer=csv.writer(file)

    writer.writerow(["name","Average"])

    s=int(input("Enter number of student:"))

    for i in range(s):
        print(f"---student{i+1}----")
        name=input("Enter student name:")

        n=int(input("Enter number of subject:"))
        marks=[]

        for j in range(n):
            m=int(input(f"Enter marks{j+1}:")) 
            marks.append(m)

        avg=calculate_average(marks)

        writer.writerow([name,avg])
print("\n Data saved to student.csv")

with open("student.csv","r") as file:

    reader=csv.DictReader(file)

    total_avg=0
    count=0

    for row in reader:
        total_avg+=float(row["Average"])
        count+=1
    if count>0:

        print("class Average:",total_avg/count)
