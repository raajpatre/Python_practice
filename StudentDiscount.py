age=int(input("Enter your age: "))
hasID=input("Do you have an ID? (yes/no): ").strip().lower()
if age >= 18 or hasID == 'yes':
    print("You are eligible for student discount.")
else:
    print("You are not eligible for student discount.")
