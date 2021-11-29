#시험 감독
import sys

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())

count = N
for tester in A:
    if tester >= B :
        tester -= B
        count += tester // C
        if tester % C != 0: count += 1
    
print(count)