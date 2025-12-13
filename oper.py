def oper():
    while True:
        print("What would you like to know under this topic?-->")
        print("A - Arithmetic Operators\nB - Assignment Operators\nC - Relational Operators\nD - Logical Operators\nE - Exit sub menu")
        choice = input("Enter choice-->").lower()
                                                            
        if choice == 'a':
            while True:
                print("Please select:\nA - Description\nB - Sample code\nC - Result of sample code\nD - Back")
                choicee = input("Your choice-->").lower()
                                                                            
                if choicee == 'a':
                    print("Python provides a comprehensive set of arithmetic operators for performing mathematical calculations. These operators work with numeric values (integers, floats, etc.) to produce a result.")
                    print('Examples are:\nAddition (+): Adds two operands.\nSubtraction (-): Subtracts the second operand from the first.\nMultiplication (*): Multiplies two operands.\nDivision (/): Divides the first operand by the second, always returning a floating-point result.\nFloor Division (//): Divides the first operand by the second, returning the largest integer less than or equal to the result (effectively discarding the fractional part).\nModulus (%): Returns the remainder of the division of the first operand by the second. ')
                                                                    
                elif choicee == 'b':
                    while True:
                        print('Please select:\n1. Simple Calculator\n2. Deposit Denomination\n3. Back')
                        pick = input("Enter choice-->")
                                    
                        if pick == '1':
                            print('n1 = eval (input("enter the first number"))')
                            print('n2 = eval (input("enter the second number"))')
            
                            print('s = n1+n2\nd = n1-n2\np = n1*n2\nq = n1/ n2\nl = n1%n2\nm = n1//n2')
            
                            print('print("the sum of", n1, "and", n2, "is", s)')
                            print('print("the difference of",n1,"and",n2,"is",d)')
                            print('print("the product of",n1,"and",n2,"is",p)')
                            print('print("the quotient of",n1,"and",n2,"is",q)')
                            print('print(n1,"exponented by",n2,"is",n1**n2)')
                            print('print("the remainder of",n1,"and",n2,"is",l)')
                            print('print("the floor division of",n1,"and",n2,"is",m)')
                                    
                        elif pick == '2':
                            print('n1= eval(input("Enter Amount to Deposit"))')
                            print('print("Here is the breakdown using Ph Denomination")')
                         
                            print('a=n1//1000\nn1= n1%1000\nb=n1//500\nn1=n1%500\nc=n1//200\nn1=n1%200\nd=n1//100\nn1=n1%100\ne=n1//50\nn1= n1%50\nf=n1//20\nn1=n1%20\ng=n1//10\nn1=n1%10\nh=n1//5\nn1=n1%5\ni=n1//1\nn1=n1%1')
            
                            print('print("1000=",a)\nprint("500=",b)\nprint("200=",c)\nprint("100=",d)\nprint("50=",e)\nprint("20=",f)\nprint("10=",g)\nprint("5=",h)\nprint("1=",i)')
                                
                        elif pick == '3':
                            break                            
                        
                        else:
                            print('Invalid Choice')                                    
                elif choicee == 'c':
                    while True:
                        print('Please select:\n1. Simple Calculator\n2. Deposit Denomination\n3. Back')
                        pick = input("Enter choice-->")
                        
                        if pick == '1':
                            n1 = eval (input("enter the first number"))
                            n2 = eval (input("enter the second number"))
            
                            s = n1+n2
                            d = n1-n2
                            p = n1*n2
                            q = n1/ n2
                            l = n1%n2
                            m = n1//n2
            
                            print("the sum of", n1, "and", n2, "is", s)
                            print("the difference of",n1,"and",n2,"is",d)
                            print("the product of",n1,"and",n2,"is",p)
                            print("the quotient of",n1,"and",n2,"is",q)
                            print(n1,"exponented by",n2,"is",n1**n2)
                            print("the remainder of",n1,"and",n2,"is",n1%n2)
                            print("the floor division of",n1,"and",n2,"is",n1//n2)                    
            
                        elif pick == '2':
                            n1= eval(input("Enter Amount to Deposit"))
                            print("Here is the breakdown using Ph Denomination")
            
                            a=n1//1000
                            n1= n1%1000
                            b=n1//500
                            n1=n1%500
                            c=n1//200
                            n1=n1%200
                            d=n1//100
                            n1=n1%100
                            e=n1//50
                            n1= n1%50
                            f=n1//20
                            n1=n1%20
                            g=n1//10
                            n1=n1%10
                            h=n1//5
                            n1=n1%5
                            i=n1//1
                            n1=n1%1
            
            
                            print("1000=",a)
                            print("500=",b)
                            print("200=",c)
                            print("100=",d)
                            print("50=",e)
                            print("20=",f)
                            print("10=",g)
                            print("5=",h)
                            print("1=",i)
     
                        elif pick == '3':
                            break
                        else:
                            print('Invalid Choice')                    
                elif choicee == 'd':
                    break
                
                else:
                    print('Invalid Choice')
               
        elif choice == 'b':
            while True:                             
                print("Please select:\nA - Description\nB - Sample code\nC - Result of sample code\nD - Back")
                choicee = input("Your choice-->").lower()
            
                if choicee == 'a':
                    print("Python assignment operators are used to assign values to variables. The most basic assignment operator is the equal sign (=), but Python also provides augmented assignment operators that combine an arithmetic or bitwise operation with an assignment.")
                    print('Simple Assignment Operator:\n= (Assignment): Assigns the value on the right to the variable on the left.')
                    print('Augmented Assignment Operators:\n+= (Addition Assignment): Adds the right operand to the left operand and assigns the result to the left operand.\n-= (Subtraction Assignment): Subtracts the right operand from the left operand and assigns the result to the left operand.\n*= (Multiplication Assignment): Multiplies the left operand by the right operand and assigns the result to the left operand.\n/= (Division Assignment): Divides the left operand by the right operand and assigns the result to the left operand.\n%= (Modulus Assignment): Divides the left operand by the right operand and assigns the remainder to the left operand.\n//= (Floor Division Assignment): Divides the left operand by the right operand and assigns the integer quotient to the left operand.')
    
                elif choicee == 'b':
                    print('a = 7\n\na += 3\na -= 2\na *= 4\na /= 2')
    
                    print('print("the value of a is", a)')
                
    
                        
                elif choicee == 'c':
                    a = 7
    
                    a += 3
                    a -= 2
                    a *= 4
                    a /= 2
    
                    print("the value of a is", a)
                
                elif choicee == 'd':
                    break                                        
                else:
                    print('Invalid Choice')
                
        elif choice == 'c':
            while True: 
                print("Please select:\nA - Description\nB - Sample code\nC - Result of sample code\nD - Back")
                choicee = input("Your choice-->").lower()
                                
                if choicee == 'a':
                    print('Relational operators in Python, also known as comparison operators, are used to compare two values and determine the relationship between them. The result of a relational operation is always a boolean value: True or False.')
                    print('Here are the six relational operators in Python:\n\nGreater than (>): Checks if the left operand is greater than the right operand.\nLess than (<): Checks if the left operand is less than the right operand.\nGreater than or equal to (>=): Checks if the left operand is greater than or equal to the right operand.\nLess than or equal to (<=): Checks if the left operand is less than or equal to the right operand.\nEqual to (==): Checks if the two operands are equal.\nNot equal to (!=): Checks if the two operands are not equal.')                                                                                                                                                        
                elif choicee == 'b':
                    print('balance = 500')
                    print('withdrawal = 500')
        
                    print('print(balance < withdrawal)\nprint(balance > withdrawal)\nprint(balance >= withdrawal)\nprint(balance <= withdrawal)\nprint(balance == withdrawal)\nprint(balance != withdrawal)')
                        
                elif choicee == 'c':
                    balance = 500
                    withdrawal = 500
        
                    print(balance < withdrawal)
                    print(balance > withdrawal)
                    print(balance >= withdrawal)
                    print(balance <= withdrawal)
                    print(balance == withdrawal)
                    print(balance != withdrawal)

                elif choicee == 'd':
                    break                
                else:
                    print('Invalid choice')                                   
        elif choice == 'd':
            while True:
                print("Please select:\nA - Description\nB - Sample code\nC - Result of sample code\nD - Back")
                choicee = input("Your choice-->").lower()
                                                            
                if choicee == 'a':
                    print('Python utilizes three logical operators: and, or, and not. These operators are used to combine conditional expressions and return a Boolean result (True or False) based on the logical evaluation.')
                    print('\nand operator:\n\nThe and operator returns True only if both of its operands are True.\nIf either or both operands are False, the expression returns False.')
                    print('\nor operator:\n\nThe or operator returns True if at least one of its operands is True.\nThe expression returns False only if both operands are False.')
                    print('\nnot operator:\n\nThe not operator is a unary operator, meaning it operates on a single operand.\nIt reverses the truth value of an expression: if the expression is True, not makes it False, and vice versa.')
                                    
                elif choicee == 'b' :
                    while True:
                        print('Please select:\n1. and\n2. or\n3. not\n4. Back')
                        pick = input("Enter your choice-->")
                        if pick == '1':
                            print(' username ="kyutienicorobin" ')
                            print(' password = "zorohunter"')
                            print('print(( username == "kyutienicorobin") and ( password == "zorohunter"))')
                               
                            print('print(( username == "kyutienicorobin") and ( password == "zorohun"))')                                
                                    
                        elif pick == '2':
                            print(' username ="kyutienicorobin" ')
                            print(' password = "zorohunter"')
                            print('print(( username == "kyutienicorobin") or ( password == "zorohunter"))')
                               
                            print('print(( username == "kyutienicorobin") or ( password == "zorohun"))')                                
                        
                        elif pick == '3':
                            print(' username ="kyutienicorobin" ')
                            print(' password = "zorohunter"')
                            
                           
                            print('print(not((username == "kyutienicorobin") and (password == "zorohunter")))')
                                   
                            print('print(not((username == "kyutienicorobin") and (password == "zorotheblackhunter")))')
                            
                        elif pick == '4':
                            break
    
                        else:
                            print('Invalid Choice')

                elif choicee == 'c' :
                    while True:
                        print('Please select:\n1. and\n2. or\n3. not\n4. Back')
                        pick = input("Enter your choice-->")
                        if pick == '1':
                            username ="kyutienicorobin" 
                            password = "zorohunter"
                            print(( username == "kyutienicorobin") and ( password == "zorohunter"))
                               
                            print(( username == "kyutienicorobin") and ( password == "zorohun"))                             
                                    
                        elif pick == '2':
                            username ="kyutienicorobin" 
                            password = "zorohunter"
                            print(( username == "kyutienicorobin") or ( password == "zorohunter"))
                               
                            print(( username == "kyutienicorobin") or ( password == "zorohun"))                                
                        
                        elif pick == '3':
                            username ="kyutienicorobin" 
                            password = "zorohunter"
                            
                            print(not((username == 'kyutienicorobin') and (password == 'zorohunter')))
                                   
                            print(not((username == 'kyutienicorobin') and (password == 'zorotheblackhunter')))
                            
                        elif pick == '4':
                            break
                    
                        else:
                            print('Invalid Choice')                    
                elif choicee == 'd':
                    break
                else:
                    print('Invalid choice')                                                                                                              
        elif choice == 'e':
            break                                                                            
        else:
            print('Invalid choice')                                                        
                            
    