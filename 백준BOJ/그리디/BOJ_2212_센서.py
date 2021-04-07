import sys

input = sys.stdin.readline
N = int(input())
K = int(input())
sensor = list(map(int, input().split()))
sensor.sort()

if K >= N:
    print(0)

else:
    focus = []
    for i in range(N - 1):
        focus.append(abs(sensor[i] - sensor[i + 1]))
    focus.sort()

    for _ in range(K - 1):
        focus.pop()

    print(sum(focus))
