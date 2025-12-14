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
    print("A - PRINT STATEMENT\nB - VARIABLES\nC - OPERATORS\nD - CONDITIONALS\nE - LOOPS\nF - LIST\nG - Dictionary\nH - FUNCTONS\nI - EXIT")

    choice = input("Enter your choice-->").lower()
    
    if choice == 'a':
        print('\n')
        print(f'Welcome {ask}')
        print('\n')
        choiceA()
        os.system('cls')
        continue
        
    elif choice == 'b':
        print('\n')
        print(f'Welcome {ask}')
        print('\n')
        choiceB()
        os.system('cls')
        continue
        
    elif choice == 'c':
        print('\n')
        print(f'Welcome {ask}')
        print('\n')
        oper()
        os.system('cls')                
        continue
        
    elif choice == 'd':
        print('\n')
        print(f'Welcome {ask}')
        print('\n')
        cond()
        os.system('cls')                
        continue
        
    elif choice == 'e':
        print('\n')
        print(f'Welcome {ask}')
        print('\n')
        loops()                                  
        os.system('cls')                              
    elif choice == 'f':
        print('\n')
        print(f'Welcome {ask}')
        print('\n')
        lists()
        os.system('cls')
    elif choice == 'g':
        print('\n')
        print(f'Welcome {ask}')
        print('\n')
        dict()
        os.system('cls')
    elif choice == 'h':
        print('\n')
        print(f'Welcome {ask}')
        print('\n')
        func()
        os.system('cls')
    elif choice == 'i':
        print('Thank you for visiting my Program!!!;)')
        break 

    else:
        print('Invalid Choice')
        os.system('cls')                        