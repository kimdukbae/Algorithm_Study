import sys

input = sys.stdin.readline
N = int(input())
dist = list(map(int, input().split()))
won = list(map(int, input().split()))
won.pop()  # 맨 마지막 도시의 주유소 리터당 가격 필요없음

ans = 0
part = won[0]   # 주유소 가격
ans = part * dist[0]

# 무조건 리터당 가격이 싼 도시에서 주유해야 개이득임
for i in range(1, len(won)):
    if part > won[i]:
        part = won[i]
        ans += part * dist[i]
    else:
        ans += part * dist[i]

print(ans)
