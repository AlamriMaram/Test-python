n=int(input("Enter a number to reach to 20 :"))

while(n<=20):
    if (n >= 9):
        print("go up")
        break;
    elif (n >= 20):
        print("go down")
        break;
    elif (n == 19):
        print("WIN")
        break;
    else:
        ("try again")
        
        
