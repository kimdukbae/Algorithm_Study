# 내 풀이
start = input()

dir = [[-2, -1], [-2, 1], [2, 1], [2, -1], [-1, -2], [1, -2], [-1, 2], [1, 2]]
row = int(start[1])
col = int(ord(start[0]) - ord('a') + 1)
cnt = 0

for i in range(len(dir)):
    nr = row + dir[i][0]
    nc = col + dir[i][1]

    # if nr < 1 or nr > 8 or nc < 1 or nc > 8:
    #     continue
    # cnt += 1
    if nr >= 1 and nr <= 8 and nc >= 1 and nc <= 8:
        cnt += 1

print(cnt)
# 풀이와 해답이 같다~