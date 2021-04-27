import sys
import collections

input = sys.stdin.readline
N = int(input())
books = list(input().rstrip() for _ in range(N))

# 오늘 책이 몇 개씩 판매됐는지 정산해준다고 이해하면 쉽다.
counter = collections.Counter(books)

# 가장 많이 팔린 책 권수
maximum = max(counter.values())
ans = []
for key, value in counter.items():
    # 가장 많이 팔린 책이 여러 개일 수도 있기에 조건문 작성
    if value >= maximum:
        maximum = value
        ans.append(key)

ans.sort()
print(ans[0])
