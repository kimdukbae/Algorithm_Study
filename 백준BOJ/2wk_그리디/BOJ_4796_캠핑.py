import sys

input = sys.stdin.readline
idx = 1

while True:
    ans = 0
    L, P, V = map(int, input().split())

    if L == 0 and P == 0 and V == 0:
        break
    # min() 을 쓴 이유 -> L:1, P:4, V:7
    ans = ((V // P) * L) + min(V % P, L)

    print("Case %d: %d" % (idx, ans))
    idx += 1
