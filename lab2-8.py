x=int(input("Enter how many elements you want store in List 'A':"))
A=[]
print("Enter elements in List 'A':")
for i in range(x):
    A.append(input())
y=int(input("Enter how many elements you want store in List 'B':"))
B=[]
print("Enter elements in List 'B':")
for i in range(y):
    B.append(input())
print(A,"+",B)
print("Concat:",A+B)