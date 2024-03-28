
'''
enter the input:7
   *   
  ***  
 ***** 
*******
 ***** 
  ***  
   *
   '''
n=int(input("enter the input:"))
c=n//2
for i in range(n):
    for j in range(n):
        if not( i-j>c or  i-j<-c or i+j<c or i+j>3*c ):
            print("*",end='')
        else:
            print(end=' ')
    print()
    


'''n=int(input('number?'))
for i in range(n):
    for j in range(n):
        if i+j>=n//2 and i-j>=-(n//2) and i-j<=n//2 and i+j<=3*(n//2):
            print('*',end='')
        else:
            print(end=' ')
    print()'''

'''n=int(input('number?'))
for i in range(n):
    for j in range(n):
        if (j<=n//4 and i+j>=n-1) or (i>=3*n//4 and j>=n//2 and i+j<=3*(n//2)) :
            print('*',end='')
        else:
            print(end=' ')
    print()'''





