#Daily Challenge
a,b=map(int,input().split())
for i in range(b):
  for j in range(i+1):
    print(chr(((a+j-1)%26)+65),end=" ")
  print()  

n=int(input())
l=[True]*(n+1)
l[0]=l[1]=False
for i in range(2,int(n**0.5)+1):
    if l[i]:
        for j in range(i*i,n+1,i):
            l[j]=False
for i in range(5,len(l)-5):
    if l[i] and l[i+6]:
        print(i,i+6)
