from random import randint
m=randint(1,21)
while randint:
    if (m<19):
        print("Go down",m)
        break
    elif (m>19):
        print("Go up",m)
        break
    elif (m==19):
        print("WIN" ,m)
else:
        print("END",m)