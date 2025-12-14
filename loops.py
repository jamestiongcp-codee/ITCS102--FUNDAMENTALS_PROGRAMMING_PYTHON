def loops():
    while True: 
        print("Please select:\nA - Description\nB - Sample code\nC - Result of sample code\nD - Back")
        choicee = input("Your choice-->").lower()
                        
        if choicee == 'a':
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print('Python has two primary types of loops, for loops and while loops, which are used to execute a block of code repeatedly. ')
            print('\nfor Loops:\nA for loop is used to iterate over a sequence (such as a list, tuple, string, or range). The code block within the loop is executed once for each item in the sequence. This is useful when you know the number of iterations in advance.')
            print('\nwhile Loops:\nA while loop repeatedly executes a block of statements as long as a given condition is true. This is useful when the number of iterations is unknown and depends on when a condition changes.')
            print("\nLoop Control Statements:\nYou can alter the normal execution flow of loops using control statements:\nbreak: Exits the loop entirely, even if the condition is still true or the iterable hasn't been exhausted.\ncontinue: Skips the current iteration of the loop and moves to the next iteration")
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")        
        elif choicee == 'b':
            while True:
                print("Please select:\n1. for loops\n2. while loops\n3. Back")
                ask = input("Enter choice-->")
                if ask == '1':
                    while True:
                        print('Please select:\n1. looping statements\n2. adding inputted numbers\n3. for loop in reverse\n4. adding odd numbers\n5. for loop, horizontal\n6. for loop increasing numbers\n7. for loop increasing numbers.1\n8. for loop triangles\n9. for loop triangles.1\n10. For loop factorial\n11. for loop adding odd numbers\n12. Multiplication Table\n13. Countdown\n14. for loop triangle.2\n15. for loop triangle.3\n16. for loop triangle with numbers\n17. For loop Christmas tree\n18. Back')              
                        pick = input('Enter choice -->')
                                                                        
                        if pick == '1':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")    
                            print("""for loop in range (1,11,1) :
            print(loop, "Hello World")""")             
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                        elif pick == '2':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            print("""no = 0
        for james in range (1,11,1):
            num = eval(input("Enter number-->"))
            no += num
            print("ang bagong value ay", no)
        print(no)
            """)
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
        
                        elif pick == '3':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            print("""for james in range(20, 0, -1):
            print(james)""")
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                        elif pick == '4':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            print("""oddsummation = 0
        for j in range (1,11,1):
            num= eval(input("Enter a number-->"))
            if num % 2 == 1:
                oddsummation += num
                
        print(f"The summation of all odd numbers is {oddsummation}")
                """)
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                        elif pick == '5':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            print("""for j in range(1,11,1):
            print(j,end="")""")
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                        elif pick =='6':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            print("""for j in range (1,11):
            for jj in range (1,j + 1):
                print(jj,end=" ")
            print()""")
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                        elif pick =='7':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            print("""for j in range (1,11,1):
            for jj in range (1,j,1):
                print(jj,end="")
            print ( )""")
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                        elif pick =='8':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            print("""for j in range (1,11,1):
            for jj in range (1,j,1):
                print("*",end="")
            print ( )""")
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                        elif pick =='9':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            print("""for j in range (1,11,1):
            for jj in range (1,j,1):
                print(" ",end=" ")
            for jjj in range (10,j,-1):
                print("*",end=" ")
            print ( )""")
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                        elif pick =='10':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            print("""result = 1
        num = eval(input("Enter a number-->"))
        for loop in range(num,0,-1):
            result *= loop
        print(result)""")
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                        elif pick =='11':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            print("""result = 0
        for j in range(1,11,1):
            num= eval(input("Enter number"))
            if num %2 != 0:
                result += num
        print("The summation of all odd numbers is", result)
                """)
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                        elif pick =='12':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            print("""result = 1
        print("Multiplication Table Maker")
        num = eval(input("Enter a number:" ))
        print("\nMultiplication Table for",num,":")
        for j in range(1,11,1):
                result = num * j
                print(num,"×", j,"=", result) """)
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                        elif pick =='13':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            print("""print("COUNTDOWN TIMER SIMULATOR")
        num = eval(input("Enter the starting number for countdown:"))
        print("\nCountdown started:")
        for j in range (num,0,-1):
            print(j)
        print("Liftoff!!!")
        """)
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            
                        elif pick =='14':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            print("""for j in range (1,11,1):
            for jj in range (10,j,-1):
                print(" ",end=" ")
            for jjj in range(1,j,1):
                print("*",end=" ")
            for jjjj in range (1,j,1):
                print("*",end=" ")
            print()""")
                            
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                        elif pick =='15':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            print("""for j in range (1,11,1):
            for jj in range (10,j,-1):
                print(" ",end=" ")
            for jjj in range(1,j,1):
                print("*",end=" ")
            for jjjj in range (1,j,1):
                print("*",end=" ")
            print()
        for a in range (1,11,1):
            for aa in range (1,a,1):
                print(" ",end=" ")
            for aaa in range(10,a,-1):
                print("*", end=" ")
            for aaaa in range(10,a,-1):
                print("*", end=" ")
            print()""")
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            
                        elif pick =='16':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            print("""for j in range (1,7,1):
            for jj in range (6,j,-1):
                print(" ",end=" ")
            for jjj in range(j,0,-1):
                print(jjj, end=" ")
            for jjjj in range(2,j+1,1):
                print(jjjj, end=" ")
            print()
               """)
                            
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                        elif pick =='17':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            print("""result= input("Wanna see a Christmas tree?, (yes/no)")
        
        if result.lower()== "yes":
            print("Here ya go:")
            print("\n\t  *")
            print("\t*","*","*")
            print("\t  *")
        
            for j in range (1,7,1):
                for jj in range (6,j,-1):
                    print(" ",end=" ")
                for jjj in range(j,0,-1):
                    print("*", end=" ")
                for jjjj in range(2,j+1,1):
                    print("*", end=" ")
                print()
            for j in range (1,7,1):
                for jj in range (6,j,-1):
                    print(" ",end=" ")
                for jjj in range(j,0,-1):
                    print("*", end=" ")
                for jjjj in range(2,j+1,1):
                    print("*", end=" ")
                print()
            for j in range (1,7,1):
                for jj in range (6,j,-1):
                    print(" ",end=" ")
                for jjj in range(j,0,-1):
                    print("*", end=" ")
                for jjjj in range(2,j+1,1):
                    print("*", end=" ")
                print()
            for b in range (1,8,1):
                for bb in range (3,0,-1):
                    print(" ",end=" ")
                for bbb in range (1,6,1):
                    print("*",end=" ")
                print()
         
        else: 
            print("I'll still let you see it:")
            print("\n\t  *")
            print("\t*","*","*")
            print("\t  *")
        
            for j in range (1,7,1):
                for jj in range (6,j,-1):
                    print(" ",end=" ")
                for jjj in range(j,0,-1):
                    print("*", end=" ")
                for jjjj in range(2,j+1,1):
                    print("*", end=" ")
                print()
            for j in range (1,7,1):
                for jj in range (6,j,-1):
                    print(" ",end=" ")
                for jjj in range(j,0,-1):
                    print("*", end=" ")
                for jjjj in range(2,j+1,1):
                    print("*", end=" ")
                print()
            for j in range (1,7,1):
                for jj in range (6,j,-1):
                    print(" ",end=" ")
                for jjj in range(j,0,-1):
                    print("*", end=" ")
                for jjjj in range(2,j+1,1):
                    print("*", end=" ")
                print()
            for b in range (1,8,1):
                for bb in range (3,0,-1):
                    print(" ",end=" ")
                for bbb in range (1,6,1):
                    print("*",end=" ")
                print()""")
                            
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                        elif pick =='18':
                            break
                            
                                                                                                
                        else:
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            print('Invalid Choice')
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                elif ask == '2':
                    while True:
                        print('Please select:\n1. Washing Machine\n2. Odd-number Compiler\n3. Back')
                        askk = input("Enter choice-->")
                        if askk == '1':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            print("""dirty = True 
askk= input("type yes to start").lower()
if askk == "yes":
    while dirty == True:
        ask = input(" do you want to continue? (yes/no)").lower()
        if ask == "yes":
            print("Continue cycle")
            continue
        
        elif ask == "no":
            print("End cycle")
            break
    
        else:
            print("invalid input")
            continue
else: 
    print("edi don't")""")
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")                 
                        elif askk == '2':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            print("""ask = input("Hi!, what is your name?")
print("+++++++++++++++++++++++++++")
print("Odd number compiler, type '0' to terminate the loop")
sum = 0
odds = ""

Odd = True

while Odd== True:    
    askk = eval(input("Enter a number"))
    if askk % 2 == 1:
        print("odd number detected")
        odds += str(askk) + "," 
        sum += askk
        continue
    elif askk == 0:
        print("loop terminated")
        break
    else:
        if askk % 2 == 0:
            print("even number detected, skipping...")
            continue
        else:
            print("invalid number")
            continue
            
print(f"Hi {ask}, The sum of all odd numbers is {sum}")
print(f"The odd numbers that you inputted are {odds} ")""")       
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                        elif askk == '3':
                            break
                            
                        else:
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            print('Invalid Choice')
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")                     
                elif ask == '3':
                    break                                                                         
                else:
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                    print('Invalid Choice')
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")                                                                                                        
        elif choicee == 'c':
            while True:
                print("Please select:\n1. for loops\n2. while loops\n3. Back")
                ask = input("Enter choice-->")
                if ask == '1':
                    while True:
                        
                        print('Please select:\n1. looping statements\n2. adding inputted numbers\n3. for loop in reverse\n4. adding odd numbers\n5. for loop, horizontal\n6. for loop increasing numbers\n7. for loop increasing numbers.1\n8. for loop triangles\n9. for loop triangles.1\n10. For loop factorial\n11. for loop adding odd numbers\n12. Multiplication Table\n13. Countdown\n14. for loop triangle.2\n15. for loop triangle.3\n16. for loop triangle with numbers\n17. For loop Christmas tree\n18. Back')              
                        pick = input('Enter choice -->')
                        
                        if pick == '1':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            for loop in range (1,11,1) :
                                print(loop, "Hello World")             
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                        elif pick == '2':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            no = 0
                            for james in range (1,11,1):
                                num = eval(input("Enter number-->"))
                                no += num
                                print("ang bagong value ay", no)
                            print(no)
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
            
        
                        elif pick == '3':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            for james in range(20, 0, -1):
                                print(james)
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                        elif pick == '4':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            oddsummation = 0
                            for j in range (1,11,1):
                                num= eval(input("Enter a number-->"))
                                if num % 2 == 1:
                                    oddsummation += num
                
                            print(f"The summation of all odd numbers is {oddsummation}")
                
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                        elif pick == '5':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            for j in range(1,11,1):
                                print(j,end="")
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                        elif pick =='6':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            for j in range (1,11):
                                for jj in range (1,j + 1):
                                    print(jj,end=" ")
                                print()
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                        elif pick =='7':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            for j in range (1,11,1):
                                for jj in range (1,j,1):
                                    print(jj,end="")
                                print ( )
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
            
                        elif pick =='8':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            for j in range (1,11,1):
                                for jj in range (1,j,1):
                                    print("*",end="")
                                print ( )
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                        elif pick =='9':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            for j in range (1,11,1):
                                for jj in range (1,j,1):
                                    print(" ",end=" ")
                                for jjj in range (10,j,-1):
                                    print("*",end=" ")
                                print ( )
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                        elif pick =='10':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            result = 1
                            num = eval(input("Enter a number-->"))
                            for loop in range(num,0,-1):
                                result *= loop
                            print(result)
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                        elif pick =='11':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            result = 0
                            for j in range(1,11,1):
                                num= eval(input("Enter number"))
                                if num %2 != 0:
                                    result += num
                            print("The summation of all odd numbers is", result)
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                
                        elif pick =='12':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            result = 1
                            print("Multiplication Table Maker")
                            num = eval(input("Enter a number:" ))
                            print("\nMultiplication Table for",num,":")
                            for j in range(1,11,1):
                                result = num * j
                                print(num,"×", j,"=", result) 
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                        elif pick =='13':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            print("COUNTDOWN TIMER SIMULATOR")
                            num = eval(input("Enter the starting number for countdown:"))
                            print("\nCountdown started:")
                            for j in range (num,0,-1):
                                print(j)
                            print("Liftoff!!!")
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            
                            
                        elif pick =='14':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            for j in range (1,11,1):
                                for jj in range (10,j,-1):
                                    print(" ",end=" ")
                                for jjj in range(1,j,1):
                                    print("*",end=" ")
                                for jjjj in range (1,j,1):
                                    print("*",end=" ")
                                print()
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            
                        elif pick =='15':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            for j in range (1,11,1):
                                for jj in range (10,j,-1):
                                    print(" ",end=" ")
                                for jjj in range(1,j,1):
                                    print("*",end=" ")
                                for jjjj in range (1,j,1):
                                    print("*",end=" ")
                                print()
                            for a in range (1,11,1):
                                for aa in range (1,a,1):
                                    print(" ",end=" ")
                                for aaa in range(10,a,-1):
                                    print("*", end=" ")
                                for aaaa in range(10,a,-1):
                                    print("*", end=" ")
                                print()
                            
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                        elif pick =='16':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            for j in range (1,7,1):
                                for jj in range (6,j,-1):
                                    print(" ",end=" ")
                                for jjj in range(j,0,-1):
                                    print(jjj, end=" ")
                                for jjjj in range(2,j+1,1):
                                    print(jjjj, end=" ")
                                print()
               
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            
                        elif pick =='17':
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            result= input("Wanna see a Christmas tree?, (yes/no)")
        
                            if result.lower()== "yes":
                                print("Here ya go:")
                                print("\n\t  *")
                                print("\t*","*","*")
                                print("\t  *")
        
                                for j in range (1,7,1):
                                    for jj in range (6,j,-1):
                                        print(" ",end=" ")
                                    for jjj in range(j,0,-1):
                                        print("*", end=" ")
                                    for jjjj in range(2,j+1,1):
                                        print("*", end=" ")
                                    print()
                                for j in range (1,7,1):
                                    for jj in range (6,j,-1):
                                        print(" ",end=" ")
                                    for jjj in range(j,0,-1):
                                        print("*", end=" ")
                                    for jjjj in range(2,j+1,1):
                                        print("*", end=" ")
                                    print()
                                for j in range (1,7,1):
                                    for jj in range (6,j,-1):
                                        print(" ",end=" ")
                                    for jjj in range(j,0,-1):
                                        print("*", end=" ")
                                    for jjjj in range(2,j+1,1):
                                        print("*", end=" ")
                                    print()
                                for b in range (1,8,1):
                                    for bb in range (3,0,-1):
                                        print(" ",end=" ")
                                    for bbb in range (1,6,1):
                                        print("*",end=" ")
                                    print()
                             
                            else: 
                                print("I'll still let you see it:")
                                print("\n\t  *")
                                print("\t*","*","*")
                                print("\t  *")
                            
                                for j in range (1,7,1):
                                    for jj in range (6,j,-1):
                                        print(" ",end=" ")
                                    for jjj in range(j,0,-1):
                                        print("*", end=" ")
                                    for jjjj in range(2,j+1,1):
                                        print("*", end=" ")
                                    print()
                                for j in range (1,7,1):
                                    for jj in range (6,j,-1):
                                        print(" ",end=" ")
                                    for jjj in range(j,0,-1):
                                        print("*", end=" ")
                                    for jjjj in range(2,j+1,1):
                                        print("*", end=" ")
                                    print()
                                for j in range (1,7,1):
                                    for jj in range (6,j,-1):
                                        print(" ",end=" ")
                                    for jjj in range(j,0,-1):
                                        print("*", end=" ")
                                    for jjjj in range(2,j+1,1):
                                        print("*", end=" ")
                                    print()
                                for b in range (1,8,1):
                                    for bb in range (3,0,-1):
                                        print(" ",end=" ")
                                    for bbb in range (1,6,1):
                                        print("*",end=" ")
                                    print()
                                                
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")                   
                        elif pick =='18':
                            break
                            
                            
                        else:
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            print('Invalid Choice')
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")                                                                                                         
                elif ask == '2':
                    while True:
                        print('Please select:\n1. Washing Machine\n2. Odd-number Compiler\n3. Back')
                        askk = input("Enter choice-->")
                        if askk == '1':
                                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                                dirty = True 
                                askk= input("type yes to start").lower()
                                if askk == "yes":
                                    while dirty == True:
                                        ask = input(" do you want to continue? (yes/no)").lower()
                                        if ask == "yes":
                                            print("Continue cycle")
                                            continue
                                        
                                        elif ask == "no":
                                            print("End cycle")
                                            break
                                    
                                        else:
                                            print("invalid input")
                                            continue
                                else: 
                                    print("edi don't")
                                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                                                                                                                
                        elif askk == '2':
                                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                                ask = input("Hi!, what is your name?")
                                print("+++++++++++++++++++++++++++")
                                print("Odd number compiler, type '0' to terminate the loop")
                                sum = 0
                                odds = ""
                                
                                Odd = True
                                
                                while Odd== True:    
                                    askk = eval(input("Enter a number"))
                                    if askk % 2 == 1:
                                        print("odd number detected")
                                        odds += str(askk) + "," 
                                        sum += askk
                                        continue
                                    elif askk == 0:
                                        print("loop terminated")
                                        break
                                    else:
                                        if askk % 2 == 0:
                                            print("even number detected, skipping...")
                                            continue
                                        else:
                                            print("invalid number")
                                            continue
                                            
                                print(f"Hi {ask}, The sum of all odd numbers is {sum}")
                                print(f"The odd numbers that you inputted are {odds} ")
                                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")                            
                        elif askk == '3':
                            break                                                                                                                                         
                        else:
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                            print('Invalid choice')
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")                         
    
                elif ask == '3' :
                    break
                else:
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                    print('Invalid Choice')
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")                                                                                                                                                            
        elif choicee == 'd':
            break

        else:
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
            print('Invalid Choice')
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
        