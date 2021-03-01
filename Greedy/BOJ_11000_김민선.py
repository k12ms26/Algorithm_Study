# 강의실 배정
# https://github.com/Rurril/IT-DA-3rd/blob/master/study/Python/Week8/BOJ_11000_%EA%B0%95%EC%9D%98%ED%98%84.py
import heapq
import sys

N=int(sys.stdin.readline())

time=list()
standard=list()

for _ in range(N):
    S,T=map(int,sys.stdin.readline().split())
    time.append((S,T))

time.sort()

for i in range(N):
    if len(standard) != 0 and standard[0]<= time[i][0]:
        heapq.heappop(standard)
    heapq.heappush(standard,time[i][1])
    
print(len(standard))

#import sys

# N = int(sys.stdin.readline())
# time = []
# res = []
# for i in range(N) :
#     S,T = map(int,sys.stdin.readline().split())
#     time.append([S,T])
# time.sort()

# for i in range(N) :
#     if len(res) != 0 and res[0] <= time[i][0] :
#         res.remove(min(res))
#     res.append(time[i][1])

# print(len(res))