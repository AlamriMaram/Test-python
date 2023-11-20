#for loop 

n=5
sum_=0
for i in range(1, n+1):
    result= "2"*i
    sum_+=int(result)
print(sum_)


---------------------

for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
---------------------