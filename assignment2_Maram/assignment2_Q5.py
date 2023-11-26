# input: [23, 54, 76, 12, 90]
#output: 23 | 54 | 76 | 12 | 90

list_=[23, 54, 76, 12, 90]
output = '|'.join([str(element) for element in list_])
print(output)