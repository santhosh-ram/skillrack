#Daily Challenge
import math
def check_coprime(a, b):
    return math.gcd(a, b) == 1
def process_matrix(R, C, matrix):
    for row in matrix:
        adjacent_coprimes = []
        for i in range(C - 1):
            if check_coprime(row[i], row[i + 1]):
                adjacent_coprimes.append(row[i])
                adjacent_coprimes.append(row[i + 1])
        if adjacent_coprimes:
            print(" ".join(map(str, sorted(set(adjacent_coprimes)))))
        else:
            print(-1)
R, C = map(int, input().split()) 
matrix = []
for _ in range(R):
    row = list(map(int, input().split()))
    matrix.append(row)
process_matrix(R, C, matrix)

#Daily Test
n=int(input())
l=[]
for i in range(n):
    i=(input().strip()).split(".")
    l.append(i)
s=input().strip()
if s=="n" or s=="N":
    l.sort(key=lambda x:x[0])
    for i in l:
        print(i[0]+"."+i[1])
else:
    l.sort(key=lambda x:x[1])
    for i in l:
        print(i[0]+"."+i[1])
