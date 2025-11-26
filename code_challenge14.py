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
        