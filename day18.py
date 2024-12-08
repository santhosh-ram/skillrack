#Daily Challenge
s,k=map(int,input().split())
l=list(map(int,input().split()))
i=1
while(len(set(l))!=1):
    z=[]
    if i%k==0:
        for j in range(s):
            if l[j]==1:
                z.append(j)
    for x in z:
        if x==0:
            l[-1]=1
            l[x+1]=1
        elif x==s-1:
            l[0]=1
            l[x-1]=1
        else:
            l[x+1]=1
            l[x-1]=1
    i+=1
print(-1)    

#Daily Test
def sod(n):
    x=[]
    for i in str(n):
        x.append(int(i))
    if n%sum(x)==0:
        return n
    else:
        return -1
n=int(input())        
if sod(n)!=-1:
    print(-1)
else:
    x=[n]
    a=n-1
    while(a>=1 and sod(n)!=-1):
        x.append(a)
        a-=1
    b=n+1
    while(sod(b)!=-1):
        x.append(b)
        b+=1
    if len(x)>=2:
        print(len(x),sorted(x).index(n)+1)
    else:
        print(-1)
