import sys
from collections import deque

# 1. 문서의 중요도 높은 순서대로 정렬한다.
# 2. 궁금한 문서가 언제 인쇄되는지 출력한다.

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    doc_cnt, target = map(int, input().split())
    important = list(map(int, input().split()))
    docs = []
    for i in range(len(important)):
        docs.append((important[i], i))

    important.sort(reverse=True)

    order = 0
    while True:
        if docs[0][0] == max(important):
            order += 1
            if docs[0][1] == target:
                print(order)
                break
            else:
                docs.pop(0)
                important.pop(0)
        else:
            docs.append(docs[0])
            docs.pop(0)
