n=int(input("Enter number of subject:"))
marks=[]
for i in range(n):
    m=int(input(f"Enter your Marks{i+1}:"))
    marks.append(m)
total=sum(marks)
average=total/n
print("Total mark:",total)
print("Average mark:",average)
if(average>=50):
    print("Result:Pass")
else:
    print("Result:Need inprovement")
