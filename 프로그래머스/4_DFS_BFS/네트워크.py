def dfs(computers, visited, start):
    record = [start]
    while record:
        j = record.pop()
        if visited[j] == 0:
            visited[j] = 1
        for i in range(len(computers)):
            if computers[j][i] == 1 and visited[i] == 0:
                record.append(i)

def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]
    start = 0
    while 0 in visited:
        if visited[start] == 0:
            dfs(computers, visited, start)
            answer += 1
        start += 1
    return answer

print(solution(3, [[1,1,0], [1,1,1], [0,1,1]]))
