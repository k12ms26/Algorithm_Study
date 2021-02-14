#구슬 찾기
import sys
from collections import deque

#중간인 구슬이 될 수 없는 구슬의 개수 -> N개 중 N/2개보다 더 가볍거나 무거우면 정답으로
def bfs():
    q = deque()
    #다른 인덱스와 연결시키기 위한 루프 : 현재 인덱스의 원소+원소의 인덱스의 원소 = N/2개보다 크면 현재 인덱스는 answer

N,M = map(int,sys.stdin.readline().split())
heavier = [[] for i in range(N+1)]
lighter = [[] for i in range(N+1)]
for i in range(M) :
    a, b = map(int,sys.stdin.readline().split())
    lighter[a].append(b)
    heavier[b].append(a)

bfs()
