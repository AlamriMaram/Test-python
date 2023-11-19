num=int(input("Enter a number"))
def check(num):
    if (num % 2) == 0:
        return( "Even" )
    else:
        return("Odd" )

print(check(num))