salary=float(input("Enter the salary:"))
if(salary>50000):
   if(salary>100000):
         deduction=salary*0.15
   else:
         deduction=salary*0.10
elif(salary>=20000 and salary<=50000):
    deduction=salary*0.05   
else:
    deduction=0
print("The net salary is:",salary-deduction)
