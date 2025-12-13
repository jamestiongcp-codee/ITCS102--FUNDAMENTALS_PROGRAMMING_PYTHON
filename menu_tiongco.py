import os
from print import*
from conditionals import* 
from oper import*
from loops import*
from list import*
from dictionary import*
from function import*

print("Welcome to my Interactive Menu Program")
print("+++++++++++++++++++++++++++++++++++++++++++++++")
ask = input("Hello, What is your name?-->")
print("+++++++++++++++++++++++++++++++++++++++++++++++")
print(f"Hello {ask},what do you want to know?-->")
while True:

    print("Select from the options below:")
    print("A - PRINT STATEMENT\nB - VARIABLES\nC - OPERATORS\nD - CONDITIONALS\nE - LOOPS\nF - LIST\nG - Dictionary\nH - FUNCTONS\nI - EXIT ")

    choice = input("Enter your choice-->").lower()
    
    if choice == 'a':
        choiceA()
        continue
        os.system('cls')
    elif choice == 'b':
        choiceB()
        continue
        os.system('cls')
    elif choice == 'c':
        oper()                
        continue
        os.system('cls')
    elif choice == 'd':
        cond()                
        continue
        os.system('cls')
    elif choice == 'e':
        loops()                                  
        os.system('cls')                              
    elif choice == 'f':
        lists()
        os.system('cls')
    elif choice == 'g':
        dict()
        os.system('cls')
    elif choice == 'h':
        func()
        os.system('cls')
    elif choice == 'i':
        print('Thanks you for visiting my Program!!!;)')
        break 

    else:
        print('Invalid Choice')
        os.system('cls')                        