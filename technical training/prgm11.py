n=int(input("enter a number1:"))
m=int(input("enter the number2:"))
temp=m
while m>0:
    n*=10
    m//=10
n+=temp
print("new number:",n)
    

