import random
import os
from art import logo

def compare(u, d):
  if u==d:
    return "Draw!"
  elif d == 0 or u>21:
    return "You lose!"
  elif u == 0 or d>21:
    return "You win!"
  else:
    if d>u:
      return "You lose!"
    else:
      return "You win!"
  
  
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card
  
def calculate_score(L):
  score = sum(L)
  if len(L) == 2 and sum(L) == 21:
    return 0
  if 11 in L and score>21:
    L.remove(11)
    L.append(1)
  return score

def play_game():
  print(logo)
  user_cards = []
  dealer_cards = []
  
  for i in range(2):
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())
  
  
  game_over = False
  
  while not game_over:
    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)
    print(f"  Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
    print(f"  Computer's first card: {dealer_cards[0]}")
  
    if user_score == 0 or dealer_score == 0 or user_score > 21:
      game_over = True
    else:
      cont = input("Type 'y' to get another card, type 'n' to pass: ")
      if cont == 'y':
        user_cards.append(deal_card())
      else:
        game_over = True
  
  while dealer_score < 17 and dealer_score != 0:
    dealer_cards.append(deal_card())
    dealer_score=calculate_score(dealer_cards)
  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {dealer_cards}, final score: {dealer_score}")
  print(compare(user_score, dealer_score))
  
  
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  os.system('clear')
  play_game()
