#Daily Challenge
a,b=map(int,input().split())
for i in range(b):
  for j in range(i+1):
    print(chr(((a+j-1)%26)+65),end=" ")
  print()  
