#Swap


#Using a temporary variable
a=3
b=4
temp=a
a=b
b=temp
print(a,b)

#Without Using Temporary Variable
a=2
b=5
a , b = b , a
print("a:" ,a)
print("b:" ,b)

#Addition and Subtraction
a=11
b=7
a=a+b
b=a-b
a=a-b
print (a,b)