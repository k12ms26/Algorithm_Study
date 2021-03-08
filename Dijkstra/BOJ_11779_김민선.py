#최소비용 구하기2
import heapq
import sys
INF = sys.maxsize

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for i in range(N+1)]
visited = [-1] * (N+1)
distance = [INF] * (N+1)
cities = []

for i in range(M) :
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([v,w])

start, end = map(int, sys.stdin.readline().split())

def dijkstra(start) :
    q = []
    cnt = 0
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        for i in graph[now] :
            cost = dist + i[1]
            if cost < distance[i[0]] :
                visited[i[0]] = now
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

def trace(start,end) :
    cities.append(end)
    visited[start] = 0
    while visited[end] != -1 and visited[end] != 0:
        cities.append(visited[end])
        end = visited[end]
    
dijkstra(start)
trace(start, end)
print(distance[end])
print(len(cities))
print(*cities[::-1])