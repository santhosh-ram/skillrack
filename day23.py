#Daily challenge
s=input().strip()
n=int(input())
l=[]
for i in range(n):
    a=input().strip()
    z=[]
    for j in a:
        z.append(s.index(j)+1)
    l.append([sum(z),a])
m=sorted(l)[-1][0]
for i in l:
    if i[0]==m:
        print(i[-1])
        break
    
#Daily Test
n=int(input())
a=n
while(True):
    a+=1
    if bin(a).count("1")==bin(n).count("1") and a>n:
        break
print(a)    
