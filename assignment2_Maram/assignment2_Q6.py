#write a loop that counts how many elements in a list is equal to zero.

list_=[0,1,0,0,4,0,2]
count=0
for i in list_ :
    if i == 0 :
        count+=1
print(count)