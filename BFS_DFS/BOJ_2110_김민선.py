#공유기 설치
#이분 탐색/이진 탐색 : left, right, mid(중간값) 하나를 기준으로 이것보다 크면 left = mid+1, 아니면 right=mid-1
#https://claude-u.tistory.com/448
import sys

def check(mid, arr):
    current = 0; cnt = 1
    for i in range(1,len(arr)):
        if arr[i] >= arr[current]+mid :
            cnt += 1
            current = i
    return cnt

def search(arr,c):
    # left = 0; right = len(arr)-1; mid = int((left+right)/2)
    left = 1; right = arr[-1]-arr[0]
    res = 0
    while left<=right :
        mid = (left+right)//2
        if check(mid, arr) >= c :
            res = mid
            left = mid + 1
        else :
            right = mid - 1
    print(res)
    # while left<right:
    #     if abs(arr[mid]-arr[left]) >= abs(arr[right]-arr[mid]) :
    #         res = abs(arr[right]-arr[mid])
    #         left = mid + 1
    #     else :
    #         res = abs(arr[mid]-arr[left])
    #         right = mid - 1
    # print(res)
N,C = map(int,sys.stdin.readline().split())
home = list()
for i in range(N):
    home.append(int(sys.stdin.readline()))
home.sort()
search(home,C)