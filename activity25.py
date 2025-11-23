from activity25_1 import *

name = input("Hello, What is your name?")
print(f"Welcome to my complier {name}")

tuloy = True

while tuloy == True:
    print("Please select a program")
    print("A - greet\nB - Calculator\nC - summation\n D - Exit")

    choice = input("Please enter your choice: ").lower()

    if choice == 'a':
        greeter()
        continue
    elif choice == 'b':
        calcu()
        continue
    elif choice == 'c':
        summation()
        continue
    elif choice == 'd':
        print("System exit")
        break
    else:
        print("invalid Choice")