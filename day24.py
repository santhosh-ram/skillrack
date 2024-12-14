#Daily Challenge
def res(a,b):
    s=[i for i in range(1,min(a,b)+1) if a%i==0 and b%i==0]
    return s
x,y,z=map(int,input().split())    
l=[]
l.extend(res(x,y))
l.extend(res(y,z))
print(*sorted(l)[::-1])

#Daily Test
s=list(input().strip())
for i in range(len(s)//5):
    z=[]
    for j in "abcde":
        z.append(s.index(j))
    if z==sorted(z):
        for k in "abcde":
            s.remove(k)
    else:
        break
if len(s)>0:
    print("NO")
else:
    print("YES")
            
