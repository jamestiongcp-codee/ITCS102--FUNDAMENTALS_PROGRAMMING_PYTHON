def choiceA():
    while True:
        print("Please select:\nA - Description\nB - Sample code\nC - Result of sample code\nD - Exit sub menu")
        choice = input("Your choice-->").lower()
    
        if choice == 'a':
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print('\n\n')
            print("The print() function in Python is a built-in function used to display output to the console or a specified file stream. It is fundamental for debugging, providing user feedback, and displaying program results.")
            print('\n\n')
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        elif choice == 'b':
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print('\n\n')  
            print('print("HELLO WORLD")')
            print('\n\n')
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        elif choice == 'c':
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print('\n\n')  
            print("HELLO WORLD")
            print('\n\n')
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        elif choice == 'd':
            print('\n\n')
            print("Exiting")
            print('\n\n')
            break
        
        else:
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print('\n\n')
            print("Invalid choice")
            print('\n\n')
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")



def choiceB():
    while True:   
        print("Please select:\nA - Description\nB - Sample code\nC - Result of sample code\nD - Exit sub menu")
        choice = input("Your choice-->").lower()
        
        if choice == 'a':
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print('\n\n')
            print('In Python, a variable acts as a named storage location, or container, for a value. Variables are fundamental to programming, allowing you to store and manipulate data throughout your code.')
            print('\n\n')
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        elif choice == 'b':
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print('\n\n') 
            print('name = james') #the variable (name) holds the value james
            print('print(name)')
            print('\n\n')
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        elif choice == 'c':
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print('\n\n')
            print('james')
            print('\n\n')
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        elif choice == 'd':
            break        
        
        else:
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print('\n\n')
            print('Invalid Choice')
            print('\n\n')
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

            
        
        
        
       
       
    