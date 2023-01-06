import random
word_list = ["aardvark", "baboon", "camel"]

L=[]
chosen_word=str(random.choice(word_list))
for i in range(len(chosen_word)):
  L+=("_")
lives=len(chosen_word)

endofgame = False
while not endofgame:
  while lives>0:
    print("\n"*2)
    print(L)
    guess = input("Guess a letter: ").lower()
    if guess not in list(chosen_word):
          lives=lives-1
    else:
      for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
          L[position] = guess
        

    if "_" not in L:
      print()
      print("You win\n\n", L)
      endofgame=True
  else:
    print("Game over")
    break
