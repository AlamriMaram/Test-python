answer ="abaacb"
mark=0
user_answer=(input("Enter your answer : "))
for i in range(len(answer)):
    if(user_answer[i] == answer[i]):
        mark+=1
print( mark, "your Gade is out of 6  is ",len(answer))