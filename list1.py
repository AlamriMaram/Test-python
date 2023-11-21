list1=[8,2,5,4]

for i in range (len(list1)):
    print(i)
        
----------------------

list1=[8,2,5,4]

for i in range (len(list1)):
    print(list1[i])
    
----------------------

list1=[8,2,5,4]
for i in list1:
    print(i)

----------------------

for i in [2,4]:
    print(i)

----------------------


list1=[8,2,5,4]
print (list1[1]+2)

------------------------

list1=[8,2,5,4]
print (list1[1]+[3])

--------------------------

s = "a,b,c"
data =s.split("b")
print(data)

-------------------------

s=[2,4,1,7]
x=s
print(x)

-------------------------

s=[2,5,5,1,7]
x=s
x[4]=5
print(s)

-----------------------------

s=[2,5,5,1,7]
x=s.copy()
print(x)
x[4]=5
print(x)
print(s)

-----------------------------
s=[3,4,6,7]
for i in s:
    print(i, end=" ")
    
-----------------------------

s=[3,4,6,7]
for i in s:
    print(i*2, end=" ")

-------------------------------

s=[-1,5,-5,1,-7]
count = 0
for i in s:
    if(i<0):
        count+=1
print(count)

----------------------------------












