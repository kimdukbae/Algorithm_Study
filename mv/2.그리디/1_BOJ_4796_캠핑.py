import sys

input = sys.stdin.readline
cnt = 1

while True:
    L, P, V = map(int, input().split())
    answer = 0

    if L == 0 and P == 0 and V == 0:
        break

    answer = V // P * L
    answer += min(V % P, L)

    print(f"Case {cnt}: {answer}")
    # print("Case %d: %d" % (cnt, answer))
    cnt += 1
