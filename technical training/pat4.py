'''
enter the input:4
* * * * 
* * * 
* * 
*
'''
n=int(input("enter the input:"))
for i in range(0,n):
    for j in range(n-i):
        print("*",end=" ")
    print()
    

