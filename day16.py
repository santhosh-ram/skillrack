#Daily Test
s=input().split()
l=[0]*len(s)
for i in s:
    x='';a=''
    for j in i:
        if j.isdigit():
            x+=j
        else:
            a+=j
    l[int(x)-1]=a
print(*l)    

#Daily Challenge
n=int(input())
l=list(map(int,input().split()))
m=int(input())
for i in range(m):
    z=l[(n//2)-1:(n//2)+2]
    a=max(z)
    if z.index(a)==0:
        l.remove(a)
        l.insert(0,a)
    elif(z.index(a)==2):
        l.remove(a)
        l.append(a)
    else:
        l.remove(a)
        if l[0]>l[-1]:
            l.insert(0,a)
        else:
            l.append(a)
print(*l)            
