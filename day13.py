#Daily Challenge
n=int(input())
a=list(hex(n)[2:])
for i in range(len(a)):
    if a[i]=="0":
        a[i]="O"
    elif a[i]=="1":
        a[i]="L"
    elif a[i].isalpha():
        a[i]=a[i].upper()
c=0
for i in a:
    if i.isdigit():
        c+=1
        print(-1)
        break
if c==0:
    print(*a,sep="")

#Daily Test
from datetime import datetime, timedelta
s="%d-%m-%Y"
d=input("Enter a date (DD-MM-YYYY): ")
x=datetime.strptime(d, s)
f=x.replace(day=1)
n=x+timedelta(days=1)
c=f
while c <= n:
    print(c.strftime(s))
    c += timedelta(days=1)
