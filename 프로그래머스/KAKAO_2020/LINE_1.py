# 2019 상반기 LINE 기출

from collections import deque


def solution(cony, brown):
    time = 0
    visit = [[0] * 2 for _ in range(200001)]
    q = deque()
    q.append((brown, 0))

    while 1:
        cony += time

        if cony > 200000:
            return -1
        if visit[cony][time % 2]:
            return time

        for i in range(0, len(q)):
            current = q.popleft()
            currentPosition = current[0]
            newTime = (current[1] + 1) % 2

            newPosition = currentPosition - 1
            if newPosition >= 0 and not visit[newPosition][newTime]:
                visit[newPosition][newTime] = True
                q.append((newPosition, newTime))

            newPosition = currentPosition + 1
            if newPosition < 200001 and not visit[newPosition][newTime]:
                visit[newPosition][newTime] = True
                q.append((newPosition, newTime))

            newPosition = currentPosition * 2
            if newPosition < 200001 and not visit[newPosition][newTime]:
                visit[newPosition][newTime] = True
                q.append((newPosition, newTime))

        time += 1


print(solution(11, 2))