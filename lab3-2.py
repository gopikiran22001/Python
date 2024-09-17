import math
a=float(input("Enter a value:"))
b=float(input("Enter b value:"))
c=float(input("Enter c value:"))
d=b*b-4*a*c
if d>0:
    print("Roots Are Real:")
    r1=-b+math.sqrt(d)/(2*a)
    r2=-b-math.sqrt(d)/(2*a)
    print("Root 1:",r1," Root 2:",r2)
elif d==0:
    print("Roots Are Real and Equal:")
    r1=-b/(2*a)
    print("Root:",r1)
else:
    print("Roots Are Imaganiary:")
    r1=-b+complex(d)/(2*a)
    r2=-b-complex(d)/(2*a)
    print("Root 1:",r1," Root 2:",r2)
