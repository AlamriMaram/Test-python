#Q2
tuition =10000
year_inc=0.05 #5%
i=0
years=10
current_year = 1
while (current_year <= years):
    tuition= tuition * (1 +year_inc)
    print("Tuition in year" +str(current_year)+": "+ "$" +str(tuition))
    
    if current_year <= 4:
        i+=tuition
    current_year += 1
    
print("the total is " +str(i))
---------------------------------------
T=10000
year_inc=0.05 #5%
Tyear=0
Fyear=0
year=0
while (year<15):
    year=year+1
    tuition=tuition*1.05
    
    if(year==10):
        Tyear=tuition
print("Tuition is ten yeas is " ,Tyear)

for year in range(10,14,1):
    tuition+=tuition
    
print("the total is " ,tuition)


