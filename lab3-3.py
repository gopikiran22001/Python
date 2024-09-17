sal=float(input("Enter Salary:"))
gender=input("Enter M for And F for Female:")
if gender=='M' and sal<10000:
    bonus=sal*(5+2)/100
    print("Bonus + Salary:",bonus+sal)
elif gender=='M' and sal>=10000:
    bonus=sal*5/100
    print("Bonus + Salary:",bonus+sal)
elif gender=='F' and sal<10000:
    bonus=sal*(10+2)/100
    print("Bonus + Salary:",bonus+sal)
elif gender=='F' and sal>=10000:
    bonus=sal*10/100
    print("Bonus + Salary:",bonus+sal)
else:
    print("Enter gender correctly")
