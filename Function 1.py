
#stu=int(input("number of student:"))
def grade_avg(x):
    for i in range(1,x+1):
        sum2=0
        grade=float(input("Enter student grade:"))
        sum2 +=grade
    avg =sum2/x
    return avg

print(grade_avg(2))



