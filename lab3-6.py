x=float(input("Enter first number:"))
y=float(input("Enter second number:"))
symb=input("Enter the Operation from '+','-','*','/':")
if symb=='+':
    print(x,"+",y,'=',x+y)
elif symb=='-':
    print(x,"-",y,'=',x-y)
elif symb=='*':
    print(x,"*",y,'=',x*y)
elif symb=='/':
    print(x,"/",y,'=',x/y)
else:
    print("Enter Correct Operation")
