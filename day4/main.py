#import random
#random_int = random.randint(1, 6)
#print(random_int)
#rand_float = random.random() * 5
#print(rand_float)

#datastructure
states = ["Jammu & Kashmir","Uttar Pradesh" ]
states[1] = "telangana"
states.append("Uttar Pradesh")
states.extend(["Haryana", "Punjab"])
print(states)

#nested list

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
dirty_dozen[1][1] = "lauki"
print(dirty_dozen[1][1])