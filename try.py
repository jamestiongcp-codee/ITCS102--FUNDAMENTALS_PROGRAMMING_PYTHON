import os 

print("Welcome to my Interactive Menu Program")
print("+++++++++++++++++++++++++++++++++++++++++++++++")
ask = input("Hello, What is your name?-->")

while True:

    print(f"Hello {ask},what do you want to do?-->")
    print("Select from the options below:")
    print("A - PRINT STATEMENT, VARIABLES\nB - OPERATORS\nC - CONDITIONALS\nD - LOOPS\nE - LIST\nF - FUNCTONS\nG - EXIT ")

    choice = input("Enter your choice-->").lower()

    if choice == 'a':
        print("PRINT STATEMENT")
        print("What would you like to know under this topic-->")
        print("1. VARIABLE AND PRINTING OUTPUT\n2. INPUT FUNCTION\n\n3. LEN()FUNCTION\n5. TYPE()FUNCTION  ")
        choicee = input("Please enter your choice-->")

        
        if choicee == '1':
            print("A - Definition\nB - Application")
            ask = input("Enter Choice-->").lower()
            if choice == 'a':
                print("A variable serves as a named storage location for data values.To create and use a variable in Python, simply assign a value to it. The print() function in Python is a built-in function used to display output to the console or a specified file. It is a fundamental tool for debugging, providing feedback to the user, and visualizing program execution.")
            elif choice == 'b':
                print("Code:")
                print('print("Hello World")')
                print("Output:")
                print(" Hello World")
            else:
                print("Invalid Input")

        elif choicee == '2':
            print("A - Definition\nB - Application")
            ask = input("Enter Choice-->").lower()
            if choicee == 'a':
                print("The input() function is used to accept input from the console. The input() return a string value.")
            elif choicee == 'b':
                print("Code:")
                print('input("Enter something")') # the user can type something, example "ONE"
                print("Output:")
                print("ONE")
            else:
                print("Invalid Input")

        elif choicee == '3':
            print("A - Definition\nB - Application")
            ask = input("Enter Choice-->").lower()
            if choicee == 'a':
                print("The len() function in Python is a built-in function used to determine the length or number of items in an object.")
            elif choice == 'b':
                print("")




