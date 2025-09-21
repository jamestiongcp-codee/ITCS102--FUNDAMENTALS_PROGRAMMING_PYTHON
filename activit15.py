oddsummation = 0
for j in range (1,11,1):
    num= eval(input("Enter a number-->"))
    if num % 2 == 1:
        oddsummation += num
        
print(f"The summation of all odd numbers is {oddsummation}")
        
    