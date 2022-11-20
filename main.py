# name = input("What's your name? ")
# if name == "David" or name == "david":
#   print("Hello Baldy!")
# else:
#   print("What a beautiful head of hair!")

# name = input("What's your name? ")
# if name.lower() == "david":
#   print("Hello Baldy!")
# else:
#   print("What a beautiful head of hair!")

# name = input("What's your name? ")
# if name.lower().strip() == "mike":
#   print("Hello Baldy!")
# else:
#   print("What a beautiful head of hair!")

# myList = []

# def printList():
#   print()
#   for i in myList:
#     print(i)
#   print()

# while True:
#   addItem = input("Item > ")
#   if addItem not in myList:
#     myList.append(addItem)
#   printList()

# myList = []

# def printList():
#   print()
#   for i in myList:
#     print(i)
#   print()

# while True:
#   addItem = input("Item > ").capitalize().strip()
#   if addItem not in myList:
#     myList.append(addItem)
#   printList()

# myList = []


# def printList():
#   print()
#   for i in myList:
#     print(i)
#   print()


# while True:
#   addItem = input("Item > ").strip().capitalize()
#   if addItem not in myList:
#     myList.append(addItem)
#   printList()


# whatToEat = input("What do you fancy for dinner? ")
# if whatToEat.strip() == "pasta": 
#   print("Get out the pasta maker.")
# elif whatToEat.lower() == "tacos":
#   print("Let's do Taco Tuesday!")
# else: 
#   print("Go search the fridge.")
from termcolor import colored, cprint
rolodex = []

def printList():
  print()
  for name in rolodex:
    print(name)
  print()

while True:
  firstName = input("First Name: ").strip().capitalize()
  lastName = input("Last Name: ").strip().capitalize()
  name = f"{firstName} {lastName}"
  if name not in rolodex:
    rolodex.append(name)
  else:
    cprint(colored("ERROR: Duplicate name", "red"))
  printList()