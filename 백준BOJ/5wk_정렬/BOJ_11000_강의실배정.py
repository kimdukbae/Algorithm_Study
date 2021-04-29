# N은 최대 200,000이다. N^2 -> 400억이다.
# 4천만번 연산이라고 착각해서 2중 for문 가능하다고 생각함...
# import sys
#
# input = sys.stdin.readline
# N = int(input())
# lesson = {i: input().split() for i in range(N)}
#
# # '수업이 끝나는 시간' 기준으로 오름차순 정렬
# lesson = sorted(lesson.values(), key=lambda x: x[1])
#
# visited = [0] * N
# for i in range(N):
#     if visited[i]:
#         continue
#     end_time = lesson[i][1]
#     for j in range(i + 1, N):
#         if not visited[i] and not visited[j] and end_time <= lesson[j][0]:
#             visited[i] = i + 1
#             visited[j] = i + 1
#             end_time = lesson[j][1]
#
# visited = set(visited)
# print(len(visited))


import sys
import heapq

input = sys.stdin.readline
N = int(input())
lessons = [list(map(int, input().split())) for _ in range(N)]

# '수업 시작 시간' 기준으로 오름차순 정렬
lessons = sorted(lessons, key=lambda x: x[0])

q = []
for lesson in lessons:
    # 이전 수업이 끝나는 시간과 다음 수업이 시작하는 시간을 비교
    if q and q[0] <= lesson[0]:
        heapq.heappop(q)
    heapq.heappush(q, lesson[1])

# 큐의 각각 원소는 한 강의실에서 하나의 수업이 진행중이라고 생각하면 쉽다.
# 즉, 큐의 사이즈가 강의실의 개수가 된다.
print(len(q))
