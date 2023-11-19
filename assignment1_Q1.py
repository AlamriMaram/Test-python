#Q1
Rockwall=float(input("Ener rokwall hardness :"))
carbon=float(input("Enter the carbon content :"))
tensile=float(input("Enter the stength :"))

if (rockwall >50 and carbon >0.7 and tensile>5600):
    Grade=10
elif(rockwall >50 and tensile>0.7):
    Grade=9
elif(rockwall >50 and tensile>5600):
    Grade=8
elif(rockwall >50 and tensile>5600):
    Grade=7
else:
    Grade=0
print(" steal grade is " ,Grade)