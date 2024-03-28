'''
enter the input:4
      * 
    * * 
  * * * 
* * * *
'''
n=int(input("enter the input:"))
for i in range(n):
    for j in range(n):
        if i+j>=n-1:
            print("*",end=" ")
        else:
            print(end="  ")
    print()


