'''Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.
Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j].
if s(j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.
Example:
Input: g=[1,2,3], s=[1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. And even though you have 2 cookies, since their size is both 1,
you could only make the child whose greed factor is 1 content.
You need to output 1.'''
def cookie(s,g):
    n,m,i,j=len(s),len(g),0,0
    s.sort()
    g.sort()
    while i<n and j<m:
        if s[i]>=g[j]:
            j+=1
        i+=1
    return j
s=list(map(int,input("enter the greed factors of children").split()))
g=list(map(int,input("enter the greed factors of coookies").split()))
print("output:",cookie(s,g))
