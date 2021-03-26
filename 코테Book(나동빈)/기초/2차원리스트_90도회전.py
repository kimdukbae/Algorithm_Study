def rotate_matrix_90(board):
    row_length = len(board)
    col_length = len(board[0])

    # 90도 회전할 때마다 행, 열이 서로 바뀐다.
    res = [[0] * row_length for _ in range(col_length)]
    for r in range(row_length):
        for c in range(col_length):
            res[c][row_length - 1 - r] = board[r][c]

    return res


ex = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print(rotate_matrix_90(ex))
