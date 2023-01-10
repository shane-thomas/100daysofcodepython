import logo from art

#Add
def add(n1, n2):
  return n1+n2

#Subtract
def subtract(n1, n2):
  return n1-n2

#Multiply
def multiply(n1, n2):
  return n1*n2

def divide(n1, n2):
  return n1/n2

operations = {
  "+": add,
  "-": subtract,
  "/": divide,
  "*": multiply
}

def calculator():
  print(logo)
  number1 = float(input("What's the first number? "))
  for symbol in operations:
    print(symbol)

  end = False
  while not end:
        symbol = input("Pick an operation: ")
        number2 = float(input("What's the second number? "))
        calculation = operations[symbol]
        answer = calculation(number1,number2)

        print(f"{number1} {symbol} {number2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to exit: ") == 'y':
              number1 = answer
        else:
              end = True
              calculator()
            
 calculator()           
 
