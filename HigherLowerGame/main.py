from art import logo, vs
from game_data import data
import random
import os

game_over = False
score = 0
print(logo)
while not game_over:
  s = set()
  for i in range(2):
    s.add(random.randint(1,len(data)+1))
  a = list(s)[0]
  na = data[a]['name']
  desa = data[a]['description']
  couna = data[a]['country']
  b = list(s)[1]
  nb = data[b]['name']
  desb = data[b]['description']
  counb = data[b]['country']
  print(f'Compare A: {na}, a {desa}, from {couna}.')
  print(f'\n{vs}')
  print(f'Against B: {nb}, a {desb}, from {counb}.')
  choice = input("Who has more followers? Type 'A' or 'B': ").lower()
  if data[a]['follower_count'] > data[b]['follower_count']:
    answer = 'a'  
  else:
    answer = 'b'
  if answer == choice:
    score+=1
    os.system('clear')
    print(logo)    
    print(f"That's the right answer! Current score: {score}")
  else:
    os.system('clear')
    print(logo)
    print(f"Sorry that's wrong... Final score: {score}")
    game_over = True
