'''
enter the input:4
      *       
    * * *     
  * * * * *   
* * * * * * *
'''
n=int(input("enter the input:"))
c=n+1
for i in range(1,n+1):
    for j in range(1,(2*n)):
        if i+j>=n+1 and i+j<=c:
            print("*",end=" ")
        else:
            print(end="  ")
    c+=2
    print()


