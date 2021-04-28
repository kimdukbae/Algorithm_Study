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
# 왜 '수업 시작 시간'을 기준으로 오름차순 정렬해야하나??
# 반례
# 4
# 1 2
# 1 4
# 2 6
# 4 5

# '시작 시간' 기준 오름차순 정렬 --> (1 2) (1 4) (2 6) (4 5)
# (1 2) -> (2 6) // (1 4) -> (4 5) 이다. 정답은 2임

# '끝나는 시간' 기준 오름차순 정렬 --> (1 2) (1 4) (4 5) (2 6)
# (1 2) -> (4 5) // (1 4) // (2 6) 이다.
# q = [4, 5, 6] 이 남아서 정답이 3이 됨. (오답!!)
# 왜 그럴까?
lessons = sorted(lessons, key=lambda x: x[0])

q = []
for lesson in lessons:
    if q and q[0] <= lesson[0]:
        heapq.heappop(q)
    # '수업 끝나는 시간'만 큐에 넣어줘야함
    # '수업 시작하는 시간`도 같이 넣어주면 안됨!!
    # 왜 그럴까? '끝나는 시간'이 더 빠른 수업을 알아야함. 해당 수업의 '시작 시간'을 비교하여 최적의 강의실을 구해야한다.

    # 하지만, (시작 시간, 끝나는 시간)을 큐에 삽입하면 '시작 시간'이 더 빠른 수업이 큐에 앞쪽에 오게된다.
    # 이렇게 되면 강의실이 비는 타임에 수업을 들을 수 있음에도 불구하고, 해당 수업을 강의실에 배치하지 않고 그냥 넘어가게 된다.
    heapq.heappush(q, lesson[1])

print(len(q))
