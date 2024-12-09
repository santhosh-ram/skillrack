#Daily Challenge
n=int(input())
l=list(map(int,input().split()))
m=int(input())
for i in range(m):
    if l[0]<l[1]:
        l.append(l[0])
        l.pop(0)
    else:
        l.append(l[1])
        l.pop(1)
print(*l)        

#Daily Test
n=int(input())
c=0
for i in range(1,n+1):
    if i+bin(i)[2:].count("1")==n:
        c+=1
        print("NO")
        break
if c==0:
    print("YES")
