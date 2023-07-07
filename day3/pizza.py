#written by me 
"""""
pizza_type = input("which type of pizza do you want? S, M or L?")
if pizza_type == "S":
   bill = 15
   pep_small = input("Do you want peproni? Y or N? ")
   if pep_small == "Y":
      bill+= 2
      extra_cheese= input("Do you want extra cheese? Y or N ")
      if extra_cheese == "Y":
         bill+= 1
         print (f"Your total bill is {bill}")
elif pizza_type=="M":
   bill = 20
   pep_small = input("Do you want peproni? Y or N? ")
   if pep_small == "Y":
      bill+= 3 
      extra_cheese= input("Do you want extra cheese? Y or N ")
      if extra_cheese == "Y":
         bill+= 1
         print (f"Your total bill is {bill}")
elif pizza_type== "L":
   bill = 25
   pep_small = input("Do you want peproni? Y or N? ")
   if pep_small == "Y":
      bill+= 3
      extra_cheese= input("Do you want extra cheese? Y or N ")
      if extra_cheese == "Y":
         bill+= 1
         print (f"Your total bill is {bill}")
"""
# My code is wrong

# ANgelas Code


# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3
    
if extra_cheese == "Y":
  bill += 1
  
print(f"Your final bill is: ${bill}.")

   

         

   
