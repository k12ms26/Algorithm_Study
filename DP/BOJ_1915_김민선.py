#가장 큰 정사각형
#https://cagongman.tistory.com/18 참고
import sys

n, m = map(int,sys.stdin.readline().split())
square = []
for i in range(n):
    square.append(list(map(int, list(sys.stdin.readline().rstrip('\n')))))

dp = [[0]*(m+1) for i in range(n+1)]
side = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if square[i-1][j-1] == 1:
            dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
 
            if dp[i][j] > side:
                side = dp[i][j]

print(side**2)