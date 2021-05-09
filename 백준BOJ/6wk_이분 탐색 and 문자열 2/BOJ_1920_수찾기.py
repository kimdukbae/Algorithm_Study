import sys

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))
answer = []

A.sort()


def binary_search(arr, left, right, target):
    if left > right:
        return 0
    mid = (left + right) // 2
    if arr[mid] == target:
        return 1
    elif arr[mid] > target:
        return binary_search(arr, left, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, right, target)


for chk in check:
    print(binary_search(A, 0, N - 1, chk))
