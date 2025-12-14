def func():
    while True:
        print("Please select:\nA - Description\nB - Sample code\nC - Result of sample code\nD - Back")
        choicee = input("Your choice-->").lower()

        if choicee == 'a':
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
            print('Functions in Python are reusable blocks of code that perform a specific, related action when called. They are a fundamental part of Python programming, used to organize code, make it more readable, and avoid repetition. ')
            print("\nThere are two main types of functions in Python:\nUser-defined functions: Functions created by programmers for specific tasks within their code.\nBuilt-in functions: Pre-defined functions that are always available in Python, such as print(), len(), int(), and input()")
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
        elif choicee == 'b':
            while True:
                print("Please select:\n1. Built-in functions\n2. User-defined functions\n3. Back")
                ask = input("Enter choice-->")
                if ask == '1':
                    while True:
                        print('Choose:\n1. print function\n2. input function\n3. len function\n4. Back')
                        askk = input('Enter choice-->')
                        if askk == '1':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            print('print("HELLO WORLD")')
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                        elif askk == '2':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            print("""name = input(" What is your name")
print("Hello", name, "Welcome to the matrix")""")
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 

                        elif askk == '3':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            print("""name= input("Enter a string ->")
print("Your name has", len(name), "characters")""")
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 


                        elif askk == '4':
                            break

                        else:
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            print("Invalid choice")
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                elif ask == '2':
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                    print("""def greeter(name):
    print(f"Hi {name}, how do you do?")

greeter('james')
greeter('kent')
greeter('cruz')
greeter('acie')
greeter('sumagop')

def summation(x):
    sum = 0
    for y in range(x,0,-1):
        sum += y
    print(f"The summation of {x} is {sum}")
    
summation(14)
summation(13)""")
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                elif ask == '3':
                    break
                else:
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                    print('Invalid Choice')
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 


        elif choicee == 'c':           
            while True:
                print("Please select:\n1. Built-in functions\n2. User-defined functions\n3. Back")
                ask = input("Enter choice-->")
                if ask == '1':          
                    while True:
                        print('Choose:\n1. print function\n2. input function\n3. len function\n4. Back')
                        askk = input('Enter choice-->')
                        if askk == '1':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            print("HELLO WORLD")
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                        elif askk == '2':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            name = input(" What is your name")
                            print("Hello", name, "Welcome to the matrix")
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 

                        elif askk == '3':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            name= input("Enter a string ->")
                            print("Your name has", len(name), "characters")
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 

                        elif askk == '4':
                            break

                        else:
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            print("Invalid choice")
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 

                elif ask == '2':
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                    def greeter(name):
                        print(f"Hi {name}, how do you do?")

                    greeter('james')
                    greeter('kent')
                    greeter('cruz')
                    greeter('acie')
                    greeter('sumagop')

                    def summation(x):
                        sum = 0
                        for y in range(x,0,-1):
                            sum += y
                        print(f"The summation of {x} is {sum}")
    
                    summation(14)
                    summation(13)
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")            
                elif ask == '3':
                    break

                else:
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                    print('Invalid Choice')
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 

        elif choicee == 'd':
            break
        else:
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
            print("Invalid Choice")
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")   

