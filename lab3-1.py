sub_1=float(input("Enter Subject 1 marks:"))
sub_2=float(input("Enter Subject 2 marks:"))
sub_3=float(input("Enter Subject 3 marks:"))
sub_4=float(input("Enter Subject 4 marks:"))
avg=(sub_1+sub_2+sub_3+sub_4)/4
if avg>=75:
    print("Grade is Distination")
elif avg>=60 and avg<75:
    print("First Division")
elif avg>=50 and avg<60:
    print("Second Division")
elif avg>=40 and avg<50:
    print("Third Division")
else:
    print("Fail")