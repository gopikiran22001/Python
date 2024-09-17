x=int(input("Enter a Number:"))
if x%5==0 and x%11==0:
    print(x," is divisible by both 5 and 11")
elif x%5==0 or x%11==0:
    if x%5==0:
        print(x," is divisible by 5 but not 11")
    else:
        print(x," is divisible by 11 but not 5")
else:
    print(x," is divisible not by both 5 and 11")


