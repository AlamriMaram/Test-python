dic = {1:"A" , 2:"b"}
print( dic.get(4,"x"))

----------------------------

dic = {1:"A" , 2:"b"}
print( dic.pop(1))
print(dic)

---------------------------

dic = {1:"A" , 2:"b"}
for key in dic:
    print(key)
--------------------------

dic = {1:"A" , 2:"b"}
for x in dic.items():
    print(x)
    
--------------------------

dic = {1:"A" , 2:"b"}
print (dic.values())

--------------------------
dic = {1:{"name": "maram" , "age":25},
       2:{"name" : "maryam" , "age":22}}
for key in dic:
    print(dic[key]["name"])
    
-----------------------------

dic = {1:{"name": "maram" , "age":25},
       2:{"name" : "maryam" , "age":22}}
for key in dic:
    for key1 in dic[key]:
        print(dic[key][key1])
        
-----------------------------








        