#1
year = int(input("Enter the year : "))
 
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("The year is a leap year ")
        else:
            print("The year is not a leap year ")
    else:
        print("The year is a leap year ")
else:
    print("The year is not a leap year ")
       
#2
year=int(input("Enter year:"))

if(year %4 ==0 and year %100 !=0) or (year %400 ==0):
    print(,year "is a leap year")
else:
    print(,year "is not a leap year")