
i=0
n=int(input("Enter a number "))
sum_=0
while (i<=len(str(n))):
    sum_+=n%10
    n=n//10
    print(n)
    i+=1
print("sum of the numbes is :" +str(sum_))

