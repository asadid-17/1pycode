'''
You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function.

Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name
'''
#import random
#names_string = input("Give everyones names, seprated by a comma.\n")
#name = names_string.split(", ")
#num_items = len(name)
#random_int = random.randint(0,num_items-1)
#if random_int == 0:
 #   print(name[0] + " is going to buy the meal today")
#elif random_int == 1:
 #   print(name[1] + " is going to buy the meal today")
#elif random_int == 2:
 #  print(name[2] + " is going to buy the meal today")
#elif random_int == 3:
 #   print(name[3] + " is going to buy the meal today")
#else:
 #   print(name[4] + " is going to buy the meal today")

import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

#Write your code below this line 👇

#Get the total number of items in list.
num_items = len(names)
#Generate random numbers between 0 and the last index. 
random_choice = random.randint(0, num_items - 1)
#Pick out random person from list of names using the random number.
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")


'''
using choice()

person_paying = random.choice(names)

'''