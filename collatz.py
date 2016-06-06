def collatz(number):
  if number % 2 == 0:
      return number / 2
  elif number %2 == 1:
      return (number * 3) + 1

while True:
    try:
        number = int(input("Please enter a number for the collatz sequence: \n"))
    except:
       print("That's not an integer, doofus!")
       continue
    else:
       break

while number != 1:
    var1 = int(collatz(number))
    print(var1)
    number = var1
