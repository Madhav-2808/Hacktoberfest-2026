import operations

def calculator():
  print(" ")
  print("Welcome to the Simple Calculator")
  print("--------------------------------")
  print("Select operation:")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Exit")
  print(" ")

  while True:

    choice = input("Enter choice: ")
    if choice in ('1', '2', '3', '4'):
      try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
      except ValueError:
        print("Invalid input. Please enter numbers only.")
        continue 

      if choice == '1':
        print(num1, "+", num2, "=", operations.add(num1, num2))

      elif choice == '2':
        print(num1, "-", num2, "=", operations.subtract(num1, num2))

      elif choice == '3':
        print(num1, "*", num2, "=", operations.multiply(num1, num2))

      elif choice == '4':
        print(num1, "/", num2, "=", operations.divide(num1, num2))
    
    elif choice == '5':
        Print("Exiting ...")
        break
    else:
        print("Invalid Input")
        continue
    
if __name__ == "__main__":
  calculator()