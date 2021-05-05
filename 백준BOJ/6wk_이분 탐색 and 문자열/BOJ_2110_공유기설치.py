import sys

input = sys.stdin.readline
N, C = map(int, input().split())
home = []
for _ in range(N):
    home.append(int(input()))

# 이분 탐색을 위한 오름차순 정렬
home.sort()

# 거리의 최솟값은 시작점의 좌표가 아니다! left = home[0]으로 하면 안됨!
# 우리가 구하고자 하는 것은 '최대 간격'이다.
# 최대 간격은 home[0]보다 작을 수도 있기 때문이다.
# 반례
# 5 3
# 100
# 101
# 102
# 103
# 104
left = 1
right = home[-1]
answer = 0
while left <= right:
    mid = (left + right) // 2  # 간격 설정
    curr_home = home[0]
    cnt = 1
    # 간격에 따른 공유기 설치
    for i in range(1, N):
        if home[i] - curr_home >= mid:
            cnt += 1
            curr_home = home[i]

    # 간격에 따라 공유기 설치했는데 이때 원래 설치하려던 공유기 개수와
    # 같거나 크면 간격을 증가시켜 공유기 다시 설치해본다.
    # --> 간격을 증가시켜 공유기 설치했을 때 두 공유기 사이의 최대 거리가 갱신될 수도 있기 때문에
    # 간격을 증가시킨채로 공유기를 설치해본다.
    if cnt >= C:
        answer = mid
        left = mid + 1

    # 간격을 감소시켜 공유기를 설치하여 C개 이상의 공유기를 설치하게 해본다.
    else:
        right = mid - 1

print(answer)
