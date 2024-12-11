#Daily Challenge
s=input().strip()
z=[]
for i in range(len(s)-1):
    a=str(s[:i+1].count("0"))+str(s[i+1:].count("1"))
    z.append([int(a),s[:i+1],s[i+1:]])
print(*sorted(z)[-1][1:])    

#Daily Test
s=list(input().strip())
while(len(s)!=0):
    print(*sorted(list(set(s))))
    for i in set(s):
        s.remove(i)
