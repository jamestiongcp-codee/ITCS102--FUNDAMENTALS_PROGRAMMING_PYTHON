def choiceA():
    while True:
       
        print("Please select:\nA - Description\nB - Sample code\nC - Result of sample code\nD - Exit sub menu")
        choice = input("Your choice-->").lower()
    
        if choice == 'a':
            print("The print() function in Python is a built-in function used to display output to the console or a specified file stream. It is fundamental for debugging, providing user feedback, and displaying program results.")
    
        elif choice == 'b':
            print('print("HELLO WORLD")')
        
        elif choice == 'c':
            print("HELLO WORLD")
        
        elif choice == 'd':
            print("Exiting")
            break
        
        else:
            print("Invalid choice")
        

def choice2():
    print("Please select:\nA - Description\nB - Sample code\nC - Result of sample code")
    choice = input("Your choice-->").lower()
    
    if choice == 'a':
        print(f"In Python, an escape sequence is a series of characters beginning with a backslash that allows you to represent special characters or actions within a string.")
        print(r"Examples are \t (Horizontal Tab),\n to move to the next line, and \r moves to the beginning of the current line.")

 
    elif choice == 'b':

        print('name = input("Type your name")')
        print(r'print ("\t\t\t\t*\n\n\t\t\t*\t\t\n\n\t\t*\t\t\t\t*\n\n\t*\t\t\t\t\t\t*\n\n*\t\t\t","Hello", name, "\t\t\t\t\t*\n\n\t*\t\t\t\t\t\t*\n\n\t\t*\t\t\t\t*\n\n\t\t\t*\t\t*\n\n\t\t\t\t*")')
    
    elif choice == 'c':
        name = input ("Type your name")
        print ("\t\t\t\t*\n\n\t\t\t*\t\t*\n\n\t\t*\t\t\t\t*\n\n\t*\t\t\t\t\t\t*\n\n*\t\t\t","Hello", name, "\t\t\t\t\t*\n\n\t*\t\t\t\t\t\t*\n\n\t\t*\t\t\t\t*\n\n\t\t\t*\t\t*\n\n\t\t\t\t*")

    else:
        print("Invalid choice")

def choiceB():
    while True:   
        print("Please select:\nA - Description\nB - Sample code\nC - Result of sample code\nD - Exit sub menu")
        choice = input("Your choice-->").lower()
        
        if choice == 'a':
            print('In Python, a variable acts as a named storage location, or container, for a value. Variables are fundamental to programming, allowing you to store and manipulate data throughout your code.')
        
        elif choice == 'b':
            print('name = james') #the variable (name) holds the value james
            print('print(name)')
            
        elif choice == 'c':
            print('james')
        
        elif choice == 'd':
            break        
        
        else:
            print('Invalid Choice')
        

            
        
        
        
       
       
    