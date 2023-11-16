num1=float(input("Enter the first: "))
num2=float(input("Enter the second: "))
num3=float(input("Enter the third: "))


if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3
print("the largest number is " ,largest)
