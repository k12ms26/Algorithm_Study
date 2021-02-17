#회장 뽑기
#https://qrlagusdn.tistory.com/161 참고
import sys
INF = sys.maxsize

#플로이드 와샬
def floyd(arr):
    for i in range(1, n+1) :
        arr[i][i] = 0
    for k in range(1, n+1) :
        for i in range(1, n+1):
            for j in range(1, n+1):
                if arr[i][j] > arr[i][k] + arr[k][j] :
                        arr[i][j] = arr[i][k] + arr[k][j]

    res = []
    for i in range(1, n+1) :
        res.append(max(arr[i][1:]))
    minimum = min(res)
    print(minimum, res.count(minimum))

    for i in range(n) :
        if res[i] == minimum : print(i+1, end=" ")
    #print(*ans) (나머지를 한번에 빼는 뭐 그런거)
    
n = int(sys.stdin.readline())
member = [[INF]*(n+1) for i in range(n+1)]
#일단 친구인 사람끼리만
while True :
    a, b = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1 : break
    member[a][b] = 1; member[b][a] = 1
    #member(a).append(b) => 이런식으로 넣으면 플로이드 와샬 불가 : len이 배열마다 달라지므로
floyd(member)