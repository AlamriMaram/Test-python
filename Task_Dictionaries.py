dic = {1:{"name": "John" , "age":27 , "sex":"male"},
       2:{"name" : "marie" , "age":22 , "sex":"female"},
       3:{"name" : "slai" , "age":23 , "sex":"femal"}}

for key in dic:
        if ( dic[key]['age'] >  22):
            
            print(dic[key]["name"])