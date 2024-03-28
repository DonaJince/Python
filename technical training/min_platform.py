'''Given the arrival and departure times of all trains that reach a railway station, the task is to find the minimum number of platforms required for the railway station
so that no train waits. We are given two arrays that represent the arrival and departure times of trains that stop.
Example:
Input: arr = (9:00, 9:40, 9:50, 11:00, 15:00, 18:00)
dep = (9:10, 12:00, 11:20, 11:30, 19:00, 20:00)
Output: 3
Explanation: There are at-most three trains at a time (time between 9:40 to 12:00)'''


def platforms(a,d):
    i,j,c=0,0,0
    new=[]
    while i<len(a) and j<len(d):
        if a[i]<=d[j]:
            i+=1
            c=i
        else:
            p=0
            while d[p]<d[j]:
                c-=1
                p+=1
            new.append(c)
            j+=1
            i=0
    if new:
        return(max(new))
    else:
        return len(a)
a=list(map(int,input("arrival time:").split()))
d=list(map(int,input("arrival time:").split()))
print("minimum platforms:",platforms(a,d))
