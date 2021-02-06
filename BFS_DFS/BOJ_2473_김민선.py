#세 용액
#https://hellya.tistory.com/32
#https://data-bank.tistory.com/30
import sys

def search(solution):
    left = 0; right = len(solution)-1
    s = solution[0]+solution[left]+solution[right]
    res = [abs(s),solution[0],solution[left],solution[right]]
    for i in range(N-2):
        if i > 0 and solution[i] == solution[i -1]:
            continue
        left, right = i + 1, N - 1
        while left<right :
            s = solution[i]+solution[left]+solution[right]
            if abs(s) < res[0] :
                res[0] = abs(s)
                res[1] = solution[i]
                res[2] = solution[left]
                res[3] = solution[right]
            if s > 0 : right -= 1
            elif s < 0 : left += 1
            else :
                return res
    return res

N = int(sys.stdin.readline())
sol = list(map(int, sys.stdin.readline().split()))
sol.sort()
#둘의 차이의 절대값이 가장 작은 두 수여야 한다
result = search(sol)
print("%d %d %d"%(result[1],result[2],result[3]))