# 다우기술 소용돌이 배열!!
def check(a, b, arr, n):
    if 0 <= a < n and 0 <= b < n and arr[a][b] == 0:
        return True
    else:
        return False


def print_arr(arr):
    for a in arr:
        print(*a)
    print()


def solution(n):
    answer = 0
    board = [[0] * n for _ in range(n)]

    dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    sx = sy = 0
    cnt = 1
    idx = 0

    # 소용돌이 수 생성
    while cnt <= n ** 2:
        board[sx][sy] = cnt
        nx = sx + dir[idx][0]
        ny = sy + dir[idx][1]
        if check(nx, ny, board, n):
            sx = nx
            sy = ny
        else:
            idx = (idx + 1) % 4
            sx += dir[idx][0]
            sy += dir[idx][1]
        cnt += 1
        print_arr(board)


print(solution(5))
