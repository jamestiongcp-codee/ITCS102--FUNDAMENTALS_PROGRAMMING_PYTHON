def greeter(name):
    print(f"Hello, {name} How are you?")

greeter("james")
greeter("nerio")

def summation(x):
    sum = 0
    for j in range(x,0,-1):
        sum += j
    print(f"The summation of {x} is {sum}")

summation(2)
summation(4)
