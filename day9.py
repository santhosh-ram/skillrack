#Daily challenge
s,k=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(s)]
n=int(input())
x=[]
for i in range(0,s,2):
    z=[]
    for j in range(k//2):
        z.extend(l[i][j*2:(j+1)*2])
        z.extend(l[i+1][j*2:(j+1)*2])
        x.append([sum(z),z])
        z=[]
print(*max(z[-n:])[1][:2])        
print(*max(z[-n:])[1][2:])

#Daily test
n=int(input())
l=list(map(int,input().split()))
for i in l:
    c=0
    x=i
    while(i!=1):
        if i%2==0:
            i=i//2
        else:
            i=(i*3)+1
        c+=1
    z.append([c,x])    
for i in sorted(z)[::-1]:
    print(i[1],end=" ")
