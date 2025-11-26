from activity25_1 import *

name = input("Hello, What is your name?")
print(f"Welcome to my complier {name}")

tuloy = True

while tuloy == True:
    print("Please select a program")
    print("A - greet\nB - Calculator\nC - summation\n D - Exit")

    choice = input("Please enter your choice: ").lower()

    if choice == 'a':
        greeter(name)
        continue
    elif choice == 'b':
        calcu(sum)
        continue
    elif choice == 'c':
        counter()
        continue
    elif choice == 'd':
        print("System exit")
        break
    else:
        print("invalid Choice")