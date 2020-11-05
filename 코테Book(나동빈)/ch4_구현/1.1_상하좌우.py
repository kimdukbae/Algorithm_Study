# 내 풀이
N = int(input())
route = list(map(str, input().split()))
x, y = 1, 1

dir = [[0, -1], [0, 1], [-1, 0], [1, 0]]
word = ['L', 'R', 'U', 'D']

for r in route:
    for i in range(len(word)):
        if r == word[i]:
            nx = x + dir[i][0]
            ny = y + dir[i][1]

    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
    x, y = nx, ny

print(x, y)
# 풀이와 해답이 같다~