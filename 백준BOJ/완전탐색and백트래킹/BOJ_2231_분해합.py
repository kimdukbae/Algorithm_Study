import sys

input = sys.stdin.readline
N = int(input())
ans = 0

for num in range(N):
    distribute = 0
    itos = str(num)
    for i in range(len(itos)):
        distribute += int(itos[i])
    if num + distribute == N:
        ans = num
        break

print(ans)
