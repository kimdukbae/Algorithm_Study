def solution(routes):
    answer = 0
    routes = sorted(routes, key=lambda x: x[1])

    minimum = -30001
    for route in routes:
        if minimum < route[0]:
            minimum = route[1]
            answer += 1

    return answer


print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))