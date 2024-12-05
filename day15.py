#Daily Challenge
s,k=map(int,input().split())
l=list(map(int,input().split()))
a=[0]*k
for i in l:
  for j in range(k):
    if j>=i-1:
      if a[j]==0:
        a[j]=1
      else:
        a[j]=0
a=a[::-1]
z=[a[i]*(2**i) for i in range(k)]
print(sum(z))
