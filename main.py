import sys

N, M = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
mem = []
fd=2
for i in range(len(arr)):
    if i == 0:
        mem.append(arr[i])
    else:
        mem.append(mem[i - 1] + arr[i])
print(mem)
for i in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    if a == 1:
        print(mem[b - 1])
    else:
        print(mem[b - 1] - mem[a - 2])
