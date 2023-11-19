#Check whether a number is a Narcissistic number or not in Python,
#you know that Narcissistic numbers are the special type of
#numbers where that number can be formed by sum of its own
#digits raised to the power of no. of digits.

n=input()
m=int(n)
s=0
q=m
while(m! =0):
    p=m10
    s+=p**(len(n))
    m=m//10
if(s==q):
    print('yes')
else:
    print('No')
