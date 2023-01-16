#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

print('''

  ______   __    __  ________   ______    ______         ________  __    __  ________        __    __  __    __  __       __  _______   ________  _______  
 /      \ |  \  |  \|        \ /      \  /      \       |        \|  \  |  \|        \      |  \  |  \|  \  |  \|  \     /  \|       \ |        \|       \ 
|  $$$$$$\| $$  | $$| $$$$$$$$|  $$$$$$\|  $$$$$$\       \$$$$$$$$| $$  | $$| $$$$$$$$      | $$\ | $$| $$  | $$| $$\   /  $$| $$$$$$$\| $$$$$$$$| $$$$$$$\
| $$ __\$$| $$  | $$| $$__    | $$___\$$| $$___\$$         | $$   | $$__| $$| $$__          | $$$\| $$| $$  | $$| $$$\ /  $$$| $$__/ $$| $$__    | $$__| $$
| $$|    \| $$  | $$| $$  \    \$$    \  \$$    \          | $$   | $$    $$| $$  \         | $$$$\ $$| $$  | $$| $$$$\  $$$$| $$    $$| $$  \   | $$    $$
| $$ \$$$$| $$  | $$| $$$$$    _\$$$$$$\ _\$$$$$$\         | $$   | $$$$$$$$| $$$$$         | $$\$$ $$| $$  | $$| $$\$$ $$ $$| $$$$$$$\| $$$$$   | $$$$$$$\
| $$__| $$| $$__/ $$| $$_____ |  \__| $$|  \__| $$         | $$   | $$  | $$| $$_____       | $$ \$$$$| $$__/ $$| $$ \$$$| $$| $$__/ $$| $$_____ | $$  | $$
 \$$    $$ \$$    $$| $$     \ \$$    $$ \$$    $$         | $$   | $$  | $$| $$     \      | $$  \$$$ \$$    $$| $$  \$ | $$| $$    $$| $$     \| $$  | $$
  \$$$$$$   \$$$$$$  \$$$$$$$$  \$$$$$$   \$$$$$$           \$$    \$$   \$$ \$$$$$$$$       \$$   \$$  \$$$$$$  \$$      \$$ \$$$$$$$  \$$$$$$$$ \$$   \$$
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
''')

answer = random.randint(1, 100)
tries = 0

print(
    f"Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 to 100. \nPssst, the correct answer is {answer}"
)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
    tries = 10
elif difficulty == 'hard':
    tries = 5

for i in range(tries, 0, -1):
    if i == 0:
        print("You're out of chances, game over!")
        break
    guess = int(
        input(
            f"You have {i} attempts remaining to guess the number.\nMake a guess: "
        ))
    if guess > answer: print("Higher than the answer!")
    elif guess < answer: print("Lower than the answer!")
    elif guess == answer: print("You got the right answer!")
