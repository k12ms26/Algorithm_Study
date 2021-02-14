#구슬 찾기
#https://deok2kim.tistory.com/142
import sys
from collections import deque

#중간인 구슬이 될 수 없는 구슬의 개수 -> N개 중 N/2개보다 더 가볍거나 무거우면 정답으로
def bfs():
    answer = 0
    for i in range(1,N+1):
        answer += check(i, heavier)
        answer += check(i, lighter)
    return answer

def check(start, arr):
    visited = [0]*(N+1)
    q = deque()
    q.append(start)
    cnt = 0; ans = 0
    while q:
        c = q.popleft()
        for i in arr[c] :
            if visited[i] == 0 :
                visited[i] = 1
                q.append(i)
                cnt += 1
    if cnt > N//2 :
        ans += 1
    return ans

N,M = map(int,sys.stdin.readline().split())
heavier = [[] for i in range(N+1)]
lighter = [[] for i in range(N+1)]

for i in range(M) :
    a, b = map(int,sys.stdin.readline().split())
    lighter[a].append(b)
    heavier[b].append(a)
print(bfs())