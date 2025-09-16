result = 0
for j in range(1,11,1):
    num= eval(input("Enter number"))
    if num %2 != 0:
        result += num
print("The summation of all odd numbers is", result)
        