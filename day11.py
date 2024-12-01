#Daily Test
n=int(input())
l=[]
for i in range(n):
    i=input().split()
    l.append(i[1])
print(len(set(l)))    
z=[]
for i in set(l):
    z.append([i,l.count(i)])
z.sort(key=lambda x:(x[0],-x[1]))
for i in z:
    print(i)
  
#Daily Challenge
s=input().strip()
l=[]
n=""
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        n+=s[i]
    else:
        l.append(n+s[i])
        n=""
l.append(s[-1]+n)
for i in l:
    if len(i)%2==0:
        print(i[:len(i)//2])
        print(i[len(i)//2:],end="")
    else:
        print(i,end="")
