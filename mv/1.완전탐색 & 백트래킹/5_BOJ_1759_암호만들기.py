import sys

input = sys.stdin.readline

L, C = map(int, input().split())
words = list(map(str, input().split()))

words.sort()
visited = [0] * C


def checkAlphabet(crypto):
    count = 0
    for word in crypto:
        if word == 'a' or word == 'e' or word == 'i' or word == 'o' or word == 'u':
            count += 1
    return count


def backtracking(depth, explore, idx):
    if depth == L:
        length = checkAlphabet(explore)
        if length >= 1 and len(explore) - length >= 2:
            print(''.join(explore))
            return
        return

    for i in range(C):
        # 바로 직전에 뽑은 것을 제외한 그 다음 것(오른쪽 순)부터 뽑아야하기 위한 조건
        if idx < i:
            if not visited[i]:
                visited[i] = 1
                explore.append(words[i])
                backtracking(depth + 1, explore, i)
                visited[i] = 0
                explore.pop()


backtracking(0, [], -1)
