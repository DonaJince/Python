'''
enter the input:4
* 
* * 
* * * 
* * * *
'''
n=int(input("enter the input:"))
for i in range(1,n+1):
    for j in range(0,i):
        print("*",end=" ")
    print()
    

