#function

def sum_num(*args):
    sum1=0
    for n in args:
        sum1+=n
    return sum1

result=sum_num(1,2,3)
print(result)

-----------------------
def main():
    result=sum_num(1,2,3)
    print(result)
    
def sum_num(*args):
    sum1=0
    for n in args:
        sum1+=n
    return sum1
main()                #main : No args , No return 
------------------------
num=5
def main():
    print(func1(2), func2(1))
    
def func1(x):
    num = 5
    return x*num

def func2(x):
    i=4
    y=3
    return i*x+y-num
main()

