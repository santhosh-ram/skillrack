#Daily challenge
s,k=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(s)]
for i in range(s//2):
    if i%2==0:
        l[i][:k//2],l[-(i+1)][k//2:]=l[-(i+1)][k//2:],l[i][:k//2]
    else:
        l[i][k//2:],l[-(i+1)][:k//2]=l[-(i+1)][:k//2],l[i][k//2:]
for i in l:
    print(*i)

#Daily test
s,k=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(s)]
for i in range(k):
    count=0
    for j in range(s):
        if str(l[j][i]).count("0")>=1:
            count+=1
    if count==1:
        for z in range(s):
            if str(l[z][i]).count("0")==0:
                l[z][i]+=1
for i in l:
    print(*i)
        
