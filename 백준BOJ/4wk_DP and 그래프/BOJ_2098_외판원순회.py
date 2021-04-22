# https://shoark7.github.io/programming/algorithm/introduction-to-tsp-and-solve-with-exhasutive-search
# https://shoark7.github.io/programming/algorithm/solve-tsp-with-dynamic-programming
# https://developmentdiary.tistory.com/406
import sys

input = sys.stdin.readline
n = int(input())
cities = [list(map(int, input().split())) for _ in range(n)]


# DP
def tsp(dists):
    N = len(dists)

    # (1 << N) - 1 ==> 'N개의 비트를 모두 켠다'와 같음
    VISITED_ALL = (1 << N) - 1

    # DP를 위한 캐시 초기화
    # 도시의 개수(N)에 대응하고 (1 << N)을 통해 방문한 도시 집합(visited)에 대응
    cache = [[None] * (1 << N) for _ in range(N)]
    INF = float('inf')

    def find_path(last, visited):
        if visited == VISITED_ALL:
            # 마지막 방문 도시 출발 - 0번째 (출발 도시) 사이에 경로가 존재하면
            # 경로 값을 반환.
            # 경로가 존재하지 않는다면 무한값을 반환해서 답이 안되게 한다.
            return dists[last][0] or INF

        # cache 값이 None이 아니라는 것은 last와 visited의 계산이 이미 수행됬고,
        # 지금은 중복호출 되었다는 뜻임 -> 다시 계산하지 않고 값만 바로 반환하도록
        # 중복계산을 없애 효율성 높임 --> DP 사용하는 이유
        if cache[last][visited] is not None:
            return cache[last][visited]

        tmp = INF
        for city in range(N):
            if visited & (1 << city) == 0 and dists[last][city] != 0:
                tmp = min(tmp, find_path(city, visited | (1 << city)) + dists[last][city])
        cache[last][visited] = tmp
        return tmp

    return find_path(0, 1 << 0)


print(tsp(cities))


# 완전탐색
# def tsp(D):
#     N = len(D)
#     inf = float('inf')
#     ans = inf
#     # (1 << N) - 1 ==> 'N개의 비트를 모두 켠다'와 같음
#     VISITED_ALL = (1 << N) - 1
#
#     def find_path(start, last, visited, tmp_dist):
#         nonlocal ans
#         if visited == VISITED_ALL:
#             return_home_dist = D[last][start] or inf
#             ans = min(ans, tmp_dist + return_home_dist)
#             return
#
#         for city in range(N):
#             # visited & (1 << city) != 0 은
#             # visited의 city번째 비트가 켜져있는지?
#             # 여기서는 city번째 비트가 안켜져있으면 (=방문 안했으면)
#             if visited & (1 << city) == 0 and D[last][city] != 0:
#                 find_path(start, city, visited | (1 << city), tmp_dist + D[last][city])
#
#     for c in range(N):
#         find_path(c, c, 1 << c, 0)
#
#     return ans
#
#
# print(tsp(city))
