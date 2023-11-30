def binary_search(key, lst):
    li, hi =0, len(lst)-1
    while(li<=hi):
        mid =(hi+li)//2
        if(lst[mid] == key):
            return mid
        elif(lst[mid] < key):
            li = mid + 1
        else:
            hi = mid - 1
    return -1
num = [10,50,20,70,80,40,30]
num.sort()
print(num)
target = int(input("Enter your target : "))
result= print("your target is in index : " , binary_search(target, num))