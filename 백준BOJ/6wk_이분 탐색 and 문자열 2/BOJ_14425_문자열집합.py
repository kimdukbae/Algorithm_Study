import sys

input = sys.stdin.readline
N, M = map(int, input().split())
S = list(input().rstrip() for _ in range(N))
check = list(input().rstrip() for _ in range(M))

answer = 0
for chk in check:
    if chk in S:
        answer += 1

print(answer)


# https://alpyrithm.tistory.com/74
# https://hooongs.tistory.com/313