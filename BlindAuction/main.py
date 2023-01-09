from replit import clear
from art import logo

print(logo)
print()

dictionary={}
repeat = True

print("Welcome to the secret Auction program")

while repeat:
  name = input("What is your name? ")
  bid = int(input("What's your bid? $"))
  rep = input("Are there any other bidders? Type 'yes or 'no'. ").lower()
  dictionary[name] = bid
  clear()
  if rep == "no":
    repeat = False

highest = 0
for key in dictionary:
  if highest < dictionary[key]:
    highest = dictionary[key]
    winner = key

print(f"The winner is {winner} with a bid of ${highest}.")
