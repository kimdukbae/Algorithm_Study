def solution(people, limit):
    people.sort()
    answer = 0
    start, end = 0, len(people) - 1

    # 반복문 돌 때 마다 1명 혹은 2명 태우는 과정
    while start <= end:
        answer += 1
        if people[start] + people[end] <= limit:    # if문 만족하면 2명 태움 아니면 1명 태움
            start += 1
        end -= 1

    return answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 50, 80], 100))