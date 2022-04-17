import sys

input = sys.stdin.readline

N = int(input())
K = int(input())
sensors = list(map(int, input().split()))

sensors.sort()

if K >= N:
    print(0)
else:
    explore = []
    for i in range(N - 1):
        explore.append(abs(sensors[i + 1] - sensors[i]))

    explore.sort()
    print(explore)

    for _ in range(K - 1):
        explore.pop()
    print(explore)
