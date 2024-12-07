#Daily Challenge
n=int(input())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
b=True
while(b):
    c=0
    for i in range(n):
        if l[i]>m[i]:
            c+=1
    if c==0:
        b=False
    else:
        for j in range(n):
            m[j]+=1
output=0
for i in range(n):
    output+=(m[i]-l[i])
print(output)    

#Daily Test
n=int(input())
for i in range(2**n):
    b=bin(i)[2:]
    if len(b)!=n:
        b="0"*(n-len(b))+b
    print(" ".join(b))    
