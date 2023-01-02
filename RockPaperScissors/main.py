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

#Write your code below this line 👇
import random
choice = int(input("What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors. \n"))
print()
if choice == 1:
  print(paper)
elif choice == 2:
  print(scissors)
elif choice == 0: print(rock)
print("Computer chose: ")
comp=random.randint(0,2)
if comp == 1:
  print(paper)
elif comp == 2:
  print(scissors)
elif comp == 0: print(rock)

if choice == comp:
  print("Draw")    
elif (choice == 1 and comp == 0) or (choice == 2 and comp == 1) or (choice == 0 and comp == 2) :
  print("You win")
else:
  print("You lose")
