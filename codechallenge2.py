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
