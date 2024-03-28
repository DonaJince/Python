'''
enter the input:5
*****
*   *
* * *
*   *
*****
'''
n=int(input("enter the input:"))
c=n//2
for i in range(n):
    for j in range(n):
        if i*j==0 or i==n-1 or j==n-1 or (i==n//2 and j==n//2):
            print("*",end='')
        else:
            print(end=" ")
    print()
                
