#일루미네이션
import sys
from collections import deque

def bfs():
    q = deque()
    length = 0
    #시작점은 (1,1)
    q.append([0,0]); visit[0][0] = 1
    while q :
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<H and 0<=ny<W and building[nx][ny] == 1 and visit[nx][ny] == 0:
                q.append([nx,ny])
                length += 6
                visit[nx][ny] = 1
                if building[x][y] == 1 and visit[x][y] == 1: length -= 1
    return length

W,H = map(int,sys.stdin.readline().split())
building = [list(map(int,sys.stdin.readline().split())) for i in range(H)]
visit = [[0 for j in range(W)] for i in range(H)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

print(bfs())