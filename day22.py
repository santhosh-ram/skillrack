#Daily Challenge
def res(s):
    a=-1
    for i in range(len(s)-1):
        if abs(ord(s[i])-ord(s[i+1]))==32:
            a=i
            break
    if a>=0:
        a.pop(a)
        a.pop(a)
    return s    
s=list(input().strip())    
b=True
while(b):
    l=len(s)
    z=res(s)
    if len(z)==l:
        b=False
if len(s)>0:
    print(*s,sep="")
else:
    print(-1)

#Daily Test
s,k=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(s)]
c=0
if s%2==1 and l[(s//2)+1:][::-1]==l[:s//2]:
    c+=1
elif s%2==0 and l[s//2:][::-1]==l[:s//2]:
    c+=1
a=list(zip(*l))
b=0
if k%2==1 and a[(k//2)+1:][::-1]==a[:k//2]:
    b+=1
elif k%2==0 and a[k//2:][::-1]==a[:k//2]:
    b+=1
if c>0 and b>0:
    print("Both")
elif c>0 and b==0:
    print("Horizontally Symmetric")
elif c==0 and b>0:
    print("Vertically Symmetric")
else:
    print(-1)
