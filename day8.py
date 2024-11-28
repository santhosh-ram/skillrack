#Daily Challenge
s=input().strip()
n=int(input())
count=0
for i in range(len(s)-3):
  if (str(int(s[i:i+4))==s[i:i+4]) and int(s[i:i+4])%n==0:
    count+=1
print(count)

#Daily test
s=input().strip()
c=""
while(s!="1" and s!=""):
  if s[:2]=="11" or s[:2]=="10":
    c+="b"
    s=s[2:]
  else:
    c+="a"
    s=s[1:]
print(-1 if s=="1" else c)    
