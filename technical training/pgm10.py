def leng(n):
    c=0
    while n>0:
        n//=10
        c+=1
    return c
def zfill(n):
    i,m=1,1
    while i<=n:
        m*=10
        i+=1  
    return m
def q1(n):
    print("answer 1 :",n%10)
    
def q2(n):
    print("answer 2:",n//10)
    
def q3(n,m):
    temp=m
    b=10
    while m>0:
        n*=b
        m//=10
    n+=temp
    print("answer 3:",n)
    
def q4(n,m):
    temp=m
    b=10
    while m>0:
        n-=n%b
        m//=10
        b*=10
    n+=temp
    print("answer 4:",n)
    
def q5(n):
    while n//10:
        n//=10
    print("answer 5:",n)
    
def q6(n):
    t=1
    m=0
    while n//10:
        q=n%10
        m=q*t+m
        n//=10
        t*=10
    print("answer 6:",m)
    
def q7(n,m):
    temp=n
    while n>0:
        m*=10
        n//=10
    m+=temp
    print("answer 7:",m)
    
def q8(n,m):
    p=n
    d=1
    while leng(n)>leng(m):
        n//=10
        d*=10
    q=p-(n*d)
    print("answer 8:",m*d+q)
def q9(n,m):
    c1,c2,t,p=0,0,1,0
    l1=leng(n)//2
    l2=leng(m)
    if not leng(n)%2:
        while leng(n)>l1:
            q=n%10
            p=q*t+p
            n//=10
            t*=10
        n=n*zfill(l1+l2)+(m*zfill(l1))+p
        print("answer 9:",n)
    else:
        x=n
        y=m
        while leng(n)>l1:
            q=n%10
            p=q*t+p
            n//=10
            t*=10
        print("answer9:")
        print(n*zfill(l1+l2+1)+m*zfill(l1+1)+p)
        p,t=0,1
        while leng(x)>l1+1:
            q=x%10
            p=q*t+p
            x//=10
            t*=10
        print(x*zfill(l1+l2)+y*zfill(l1)+p)
n=int(input("enter a number1:"))
m=int(input("enter the number2 to concatinate:"))
q1(n)
q2(n)
q3(n,m)
q4(n,m)
q5(n)
q6(n)
q7(n,m)
q8(n,m)
q9(n,m)




    
