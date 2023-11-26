#Write a Python program to find the list of words that are longer than n from a given
#list of words.
#Hint: take n from user

def cal(word_list, n):
    result =[]
    for word in word_list:
        if len(word) > n:
            result.append(word)
    return result

word_list = input("Enter a list of words : " ).split()
n = int(input("Enter the minimum length (n) "))

f = cal(word_list, n)

print("words longer than" ,n,":")
print(f)

            