qty=int(input("Enter the Quantity of items Sold:"))
price=float(input("Enter the Price Single item:"))
grand_Total=qty*price
disc=grand_Total*10/100
tax=grand_Total*12/100
print("Grand Total:\t",grand_Total)
print("Discount:\t-",disc)
print("Tax:\t\t+",tax)
print("FInal Total:\t",(grand_Total+tax-disc))