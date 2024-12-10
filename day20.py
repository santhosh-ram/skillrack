#Daily Challenge
n=int(input())
l=list(map(int,input().split()))
m=int(input())
z=[]
a=1
for i in range(m//2):
    x=[]
    for j in range(2):
        if a in l:
            x.append("#")
        else:
            x.append(a)
        a+=1
    z.append(x)
c=0
for i in z:
    if i[0]!="#" and i[1]!="#":
        c+=1
for i in range((m//2)-1):
    for j in range(2):
        if z[i][j]!="#" and z[i+1][j]!="#":
            c+=1
print(c)            

#Daily Test
def res(i):
    z=[]
    while(i>9):
        z.append(i%10)
        i//=10
    z.append(i)
    return z
l=list(map(int,input().split()))    
z=list(map(int,input().split()))
x=[]
for i in z:
    x.extend(res(i))
c=0
for i in set(x):
    if x.count(i)>l[i]:
        c+=1
        print("NO")
        break
if c==0:
    print("YES")
