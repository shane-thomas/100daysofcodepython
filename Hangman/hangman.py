#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

L=[]
chosen_word=random.choice(word_list)
for i in range(len(chosen_word)):
  L+=("_")
lives=len(chosen_word)

endofgame = False
while not endofgame:
  if lives!=0:
    print("\n"*2)
    print(L)
    guess = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
      letter = chosen_word[position]
      if guess == letter:
        L[position] = guess
      elif guess not in chosen_word:
        lives-=1

    if "_" not in L:
      print()
      print("You win\n\n", L)
      endofgame=True
  else:
    print("Game over")
