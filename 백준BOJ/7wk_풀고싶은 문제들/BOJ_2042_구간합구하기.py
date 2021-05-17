# 세그먼트 트리 생성
def init(start, end, index):
    if start == end:
        segment_tree[index] = arr[start]
        return segment_tree[index]
    mid = (start + end) // 2
    segment_tree[index] = init(start, mid, index * 2) + init(mid + 1, end, index * 2 + 1)
    return segment_tree[index]


# 세그먼트 트리에서 조건에 맞는 구간 합 구하기
def interval_sum(start, end, index, left, right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return segment_tree[index]
    mid = (start + end) // 2
    return interval_sum(start, mid, index * 2, left, right) + interval_sum(mid + 1, end, index * 2 + 1, left, right)


# 배열의 원소가 변경되었을 때 세그먼트 트리도 변경하기
def update(start, end, index, what, value):
    if what < start or what > end:
        return
    segment_tree[index] += value
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, index * 2, what, value)
    update(mid + 1, end, index * 2 + 1, what, value)


import sys

input = sys.stdin.readline
N, M, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

segment_tree = [0] * (N * 4)

init(0, N - 1, 1)
for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        b = b - 1
        diff = c - arr[b]
        arr[b] = c
        update(0, N - 1, 1, b, diff)
    elif a == 2:
        print(interval_sum(0, N - 1, 1, b - 1, c - 1))


# 현우
# import sys
#
# input = sys.stdin.readline
# N, M, K = map(int, input().split())
# arr = []
# for _ in range(N):
#     arr.append(int(input()))
#
# segment_tree = [0] * (N * 4)
#
# init(0, N - 1, 1)
# for _ in range(M + K):
#     a, b, c = map(int, input().split())
#     if a == 1:
#         b = b - 1
#         diff = c - arr[b]
#         arr[b] = c
#         update(0, N - 1, 1, b, diff)
#     elif a == 2:
#         print(interval_sum(0, N - 1, 1, b - 1, c - 1))
#
#
# def update(index, start, end, node, value):
#     # 리프 노드를 찾았고, 값의 차이를 리턴
#     if index == start == end:
#         dif = value - tree[node]
#         tree[node] = value
#         return dif
#     mid = (start + end) // 2
#     dif = 0
#     if index <= mid:
#         dif = update(index, start, mid, node * 2, value)
#         tree[node] += dif
#     else:
#         dif = update(index, mid + 1, end, node * 2 + 1, value)
#         tree[node] += dif
#     return dif


# 민서님 코드
# import sys
#
#
# def make_tree(node_num, start, end):
#     global tree, num
#     if start == end:
#         tree[node_num] = num[start]
#     else:
#         mid = (start + end) // 2
#         tree[node_num] = make_tree(node_num * 2, start, mid) + make_tree(node_num * 2 + 1, mid + 1, end)
#     return tree[node_num]
#
#
# def get_sum(node_num, start, end, left, right):
#     if end < left or start > right:
#         return 0
#     if left <= start and end <= right:
#         return tree[node_num]
#     mid = (start + end) // 2
#     return get_sum(node_num * 2, start, mid, left, right) + get_sum(node_num * 2 + 1, mid + 1, end, left, right)
#
#
# def update(node_num, left, right, target, diff):
#     if target < left or right < target:
#         return
#     tree[node_num] += diff
#
#     if left != right:  # not leaf node
#         mid = (left + right) // 2
#         update(node_num * 2, left, mid, target, diff)
#         update(nodenum * 2 + 1, mid + 1, right, target, diff)
#
#
# N, M, K = map(int, sys.stdin.readline().split())
# num = list(int(sys.stdin.readline()) for in range(N))
# tree = [0 for _ in range(N * 4)]
# maketree(1, 0, N - 1)
#
# for in range(M + K):
#     a, b, c = map(int, sys.stdin.readline().split())
#     if a == 1:
#         diff = c - num[b - 1]
#         num[b - 1] = c
#         update(1, 0, N - 1, b - 1, diff)
#     elif a == 2:
#         print(get_sum(1, 0, N - 1, b - 1, c - 1))
