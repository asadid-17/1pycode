print("simple rollercoaster code by ash:")

height = int(input("Enter Your height:"))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster.")
    age = int((input("What is your age?")))
    if age <12:
        bill = 5
        print("You have to pay $5.")
    elif age <= 18:
        bill = 7
        print ("You have to pay $7")
    elif age>= 45 and age <=55:
        bill = 0
        print ("You have to pay $0")
    else:
        bill = 12
        print ("You have to pay $12")
    wants_pic = input("Do you want photos? Y or N ")
    if wants_pic == "Y":
        bill +=3
        print(f"your total bill is ${bill}")
    
else:
    print("sorry, we can't allow you.")