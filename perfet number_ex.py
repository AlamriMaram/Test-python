#Print all perfect number from 1 to 100, if you know that a perfect
#number is a positive integer that is equal to the sum of its
#positive divisors, excluding the number itself. For instance, 6 has
#divisors 1, 2 and 3 (excluding itself), and 1 + 2 + 3 = 6, so 6 is a
#perfect number


sum1=0
for num in range(1,101):
    for i in range(1,num):
        if(num%i ==0):
            #print(i, end =" ")
            sum1 +=i
    print()        
    if(sum1 == num):
        print(num)
    sum1=0
        
print(sum1)
