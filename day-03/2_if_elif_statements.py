print("Welcome to the rollercoaster!\n")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster!\n")
  age = int(input("What is your age? "))
  if age < 12:
    print("Please pay $5")
  elif age <= 18:
    print("Please pay $7")
  elif age <= 30: 
    print("Please pay $10")
  else:
    print("Please pay $15")
else:
  print("Sorry, you have to grow taller before you can ride.")
