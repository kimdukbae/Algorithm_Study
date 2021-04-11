import sys

input = sys.stdin.readline
N, M = map(int, input().split())
boxes = list(map(int, input().split()))
books = list(map(int, input().split()))

# 장난치나 이게 문제냐
print(sum(boxes) - sum(books))

