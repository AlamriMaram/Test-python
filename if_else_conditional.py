#if else conditional

#Activity1: EVEN and ODD :

number=int(input("Enter your number :"))
 
if ((number %2) == 0):
    print("your number is EVEN ")
else:
    print("your naumber i odd")

--------------------------------------------------

#Activity2: Discoun for total amount greater than $100

price=float(input("Enter the total price:"))
if ( price > 100 ):
    Discount=price*(10/100)
    T_Discount=(price-Discount)
    print ("your Discout is :" ,T_Discount)
else:
    Discount=price*(5 /100)
    T_Discount=(price-Discount)
    print ("your Discout is :" ,T_Discount)
    
----------------------------------------------

#Activity 3:
num =int(input("Enter number :"))
if (num>0):
    if (num % 7 ==0):
        print("positive and divided by 7")
    else:
        print("positive and divided by 7")
    else:
 print("Nagative")
 
-----------------------------------------------

#Activity4: GENDER AND AGE :
g=input("Enter your Gender:")
if (g.lower() =='m' ):
    age=int(input("Enter your age"))
    if (24<=age<30):
        print("accepted")
    else:
        print("Not accepted")
   
else:
    print("OUT")
-------------------------------------------    




    
    

    
    
 
    
