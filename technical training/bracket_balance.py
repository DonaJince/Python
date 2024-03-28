'''Program to implement check for bracket balancing'''
def check(s):
    stack=[]
    for i in s:
        if i in ('(','[','{'):
            stack.append(i)
        else:
            if i==']' and stack.pop()!='[':
                return False
            elif i=='}' and stack.pop()!='{':
                return False 
            elif i==')' and stack.pop()!='(':
                return False
    if stack==[]:
        return True
    else:
        return False
s=input("enter the string")
print("brackets are balanced",check(s))
        
