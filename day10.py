#Daily challenge
n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    if l[:i+1].count(l[i])!=l[i]:
        print(l[i],end=" ")
    else:
        print(l[i])
        break


#Daily Test
n=int(input())
l=[]
for i in range(n):
  i=input().split()
  if int(i[1])>=3 and int(i[2])>=8:
    l.append([i[0],int(i[1]),int(i[2])])
l.sort(key=lambda x:(-x[2],-x[1],x[0]))
if len(l)>0:
  for i in l:
    print(i)
else:
  print(-1)
