#최소비용 구하기
import heapq
import sys
INF = sys.maxsize

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for i in range(N+1)]
visited = [False] * (N+1)
distance = [INF] * (N+1)

for i in range(M) :
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([v,w])

start, end = map(int, sys.stdin.readline().split())

def dijkstra(start) :
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        for i in graph[now] :
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

print(distance[end])