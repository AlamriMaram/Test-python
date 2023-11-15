#write a program that simulates a simple ATM.The pograme should ask the user fo thei PIN:
PIN=int(input("Enter the PIN please :"))
balance = 100

#if coorect ,allow to check balance

if (PIN == 1234):
    number=int(input("Enter a number 1 , 2 , 3:"))

#check balance
    if (number == 1):
        print ("check our balance" ,balance)
    
    elif (number == 2):
        cost=float(input("How much do you want?"))
        avg=(balance - cost)
        print (avg)
    
    elif (number ==3):
        amount = float(input("How much do you want to add ?"))
        avg2 = (amount + balance )
        print ("your balance NOW is : " ,avg2 )
    else:
        print("try again")
    
else:
    print("sorry, try again")
    