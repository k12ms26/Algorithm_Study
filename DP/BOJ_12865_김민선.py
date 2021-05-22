#평범한 배낭
#https://claude-u.tistory.com/208
import sys

N, K = map(int, sys.stdin.readline().split())
things = [[0,0]]
for i in range(N) :
    W, V = map(int, sys.stdin.readline().split())
    things.append([W,V])

dp =[[0]*(K+1) for i in range(N+1)]
for i in range(1,N+1) :
    for j in range(1,K+1) :
        weight = things[i][0]
        value = things[i][1]
        if j < weight :
            dp[i][j] = dp[i-1][j]
        else :
            dp[i][j] = max(value + dp[i-1][j-weight], dp[i-1][j])
print(dp[N][K])