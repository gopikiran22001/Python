x=float(input("Enter how many days Employee 'A' will take to Complete the Job:"))
y=float(input("Enter how many days Employee 'B' will take to Complete the Job:"))
z=float(input("Enter how many days Employee 'C' will take to Complete the Job:"))
avg=x*y*z/(x*y+y*z+z*x)
print("The Number of days they will take to Complete the is:",avg)