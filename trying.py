import os 
from print import*
from conditionals import* 
from oper import*

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
        
    elif choice == 'b':
        choiceB()
        continue

    elif choice == 'c':
        oper()                
        continue
    
    #elif choice == 'd':
#        cond()                
#        continue
#    
#    elif choice == 'e':
#        print('')                                  
#                                  
#    elif choice == 'f':
#        print('')                                           
#    elif choice == 'g':
#        print('')                                
#    elif choice == 'h':
#        print('')        
#    elif choice == 'i':
#        print('')        
#    else:
#        print('Invalid Choice')                        