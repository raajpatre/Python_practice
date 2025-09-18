a,b,c=map(int,input().split())
if(a<b+c and b<c+a and c<a+b):
    if(a==b and b==c):
        print("Equilateral triangle")
        if(a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b):
            print("Right angled Triangle")
    elif(a==b or b==c or c==a):
        print("Isosceles triangle")
        if(a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b):
            print("Right angled Triangle")
    else:
        print("Scalene triangle")
        if(a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b):
            print("Right angled Triangle")
else:
    print("Not a triangle")