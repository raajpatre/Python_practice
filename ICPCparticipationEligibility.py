cfr=int(input("Enter your CodeForces rating:"))
ccr=int(input("Enter your CodeChef rating:"))
tps=int(input("Enter total problems solved:"))
a="Not eligible for ICPC participation because"
if(cfr>=1200 and ccr>=1600 and tps>400):
    print("Eligible for ICPC participation")
else:
    if(cfr<1200):
        a=a+" CodeForces rating is less than 1200."
    if(ccr<1600):
        a=a+" CodeChef rating is less than 1600."
    if(tps<=400):
        a=a+" Total problems solved is not more than 400."
    print(a)