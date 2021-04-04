# PyPy3 제출
import sys

input = sys.stdin.readline
sudoku = [list(map(int, input().split())) for _ in range(9)]
empty = [(x, y) for x in range(9) for y in range(9) if sudoku[x][y] == 0]


def make_cases(x, y):
    numbers = [i + 1 for i in range(9)]

    for k in range(9):
        if sudoku[x][k] in numbers:
            numbers.remove(sudoku[x][k])
        if sudoku[k][y] in numbers:
            numbers.remove(sudoku[k][y])

    x1 = (x // 3) * 3
    y1 = (y // 3) * 3
    for r in range(x1, x1 + 3):
        for c in range(y1, y1 + 3):
            if sudoku[r][c] in numbers:
                numbers.remove(sudoku[r][c])

    return numbers


flag = False    # 스도쿠 판을 채우는 방법이 여럿인 경우는 그 중 하나만을 출력해야하기 때문에!!


def dfs(depth):
    global flag
    if flag:
        return

    if depth == len(empty):
        for s in sudoku:
            print(*s)
        flag = True
        return

    r, c = empty[depth]
    cases = make_cases(r, c)

    for case in cases:
        sudoku[r][c] = case
        dfs(depth + 1)
        sudoku[r][c] = 0


dfs(0)
