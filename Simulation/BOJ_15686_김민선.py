#치킨 배달
#https://juhee-maeng.tistory.com/96
import sys
from itertools import combinations
INF = sys.maxsize

N, M = map(int, sys.stdin.readline().split())
cities = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
house = []; chicken = []
distance = INF
for i in range(N) :
    for j in range(N) :
        if cities[i][j] == 1 : house.append([i,j])
        if cities[i][j] == 2 : chicken.append([i,j])

for c in combinations(chicken, M) :
    res = 0
    for h in house :
        res += min([abs(h[0]-i[0])+abs(h[1]-i[1]) for i in c])
        if res >= distance : break
    if res < distance : distance = res
print(distance)