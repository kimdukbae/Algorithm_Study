import time

start_time = time.time()

N, M = map(int, input().split())
ball = [0 for _ in range(N)]
ball = list(map(int, input().split()))

case = []
for i in range(N):
    for j in range(i, N):
        if i == j:
            continue
        case.append([i, j])

count = 0
for i in case:
    if ball[i[0]] != ball[i[1]]:
        count += 1

print(count)

end_time = time.time()
print(end_time - start_time)



# # 책의 코드 (위 코드도 맞는거 같다... 하지만 시간초과가 나는지는 자세히 모르겠음...)
# start_time = time.time()
#
# n, m = map(int, input().split())
# data = list(map(int, input().split()))
#
# arr = [0] * 11
#
# for x in data:
#     arr[x] += 1
#
# result = 0
# # 1부터 m까지의 각 무게에 대하여 처리
# for i in range(1, m + 1):
#     n -= arr[i]             # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
#     result += arr[i] * n    # B가 선택하는 경우의 수와 곱해주기
#
# print(result)
#
# end_time = time.time()
# print(end_time - start_time)