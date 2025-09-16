num=int(input("Enter a number: "))
rem=num%10
if(num%7==0 or rem==7):
    print("Lucky Number")
else:
    print("Unlucky Number")