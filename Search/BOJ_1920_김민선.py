#수 찾기
import sys

N = sys.stdin.readline()
n_number = set(sys.stdin.readline().split())
M = sys.stdin.readline()
m_number = sys.stdin.readline().split()

for i in m_number :
    sys.stdout.write("%d\n" % (1 if i in n_number else 0))