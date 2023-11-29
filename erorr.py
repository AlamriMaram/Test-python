try:
    x= 4/0
    print(x)
except ZeroDivisionError:
    print("can not divid by zero")
except:
    print("somthing going wrong")