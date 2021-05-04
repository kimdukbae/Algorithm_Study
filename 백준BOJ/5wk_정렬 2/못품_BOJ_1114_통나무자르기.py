import sys

input = sys.stdin.readline
L, K, C = map(int, input().split())
cut = list(map(int, input().split()))

part = [cut[0]]
for i in range(len(cut) - 1):
    part.append(cut[i + 1] - cut[i])
part.append(L - cut[len(cut) - 1])

maximum = max(part)
ans, index = 0, []
for i, p in enumerate(part):
    if p == maximum:
        if i == 0:
            ans = p + part[i + 1]
            index.append(i)
        elif i == len(part) - 1:
            ans = p + part[i - 1]
            index.append(i - 1)
        else:
            if part[i - 1] > part[i + 1]:
                ans = p + part[i - 1]
                index.append(i - 2)
            else:
                ans = p + part[i + 1]
                index.append(i - 1)

index.sort()
print(ans, cut[index[0]])
