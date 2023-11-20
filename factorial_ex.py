#for
n=5
factorial=1
for i in range(1, n+1):
    if( i != n):
        print(i, end = "X")
    else:
        print(i)
    factorial *=i
print()
print(factorial)


