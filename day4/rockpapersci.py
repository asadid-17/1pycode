import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
image = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice<0 or user_choice>2:
    print("You selected the wrong number, please choose within the range")
else:
    print(image[user_choice])
    computer_choice = random.randint(0,2)
    print("\nCopmuter choose:\n")
    print(image[computer_choice])
    if user_choice == 0 and computer_choice == 2:
     print("You won!")
    elif computer_choice==0 and user_choice == 2:
     print("You lose!")
    elif computer_choice< user_choice:
     print("You won")
    elif user_choice< computer_choice:
     print("You lose!")
    elif user_choice == computer_choice :
     print("draw, play again")
    






