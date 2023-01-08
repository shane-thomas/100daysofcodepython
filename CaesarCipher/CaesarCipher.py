from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cipher(text, shift, direction):
  endtext = ''
  if direction == 'decode':
    shift*=-1
  for letter in text:
    if letter.isalpha():
      position = alphabet.index(letter)
      endtext += alphabet[position + shift]
    else:
      endtext+=letter
  print(f"The {direction}d text is {endtext}")
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'").lower()
  if restart == 'yes':
    restart()
  else:
    print("No\n Goodbye")

def restart():
  print(logo)
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower().strip(" ")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))%26
  cipher(text = text, shift=shift, direction=direction)
  
restart()
