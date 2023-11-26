#If you have the following list as an input:
#[‘red’, ‘yellow’, ‘pink’, ‘black’]
#And the following list is the output of it:
#[‘red’, ‘purple’, ‘yellow’, ’Black’, ‘green’]
#Find how we got the output

i = ['red', 'yellow', 'pink', 'black']
i.insert(1,"purple")
i.pop(3)
i.append('green')
i[3]=i[3].capitalize()
print(i)