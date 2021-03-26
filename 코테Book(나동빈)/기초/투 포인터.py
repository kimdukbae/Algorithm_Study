# 투 포인터 알고리즘이란? 리스트에 순차적으로 접근해야 할 때 2개의 점의 위치를 기록하면서 처리하는 알고리즘
# '특정한 합을 가지는 부분 연속 수열 찾기'와 같은 문제에 적용 가능!


# 1.부분합이 5가 되는 부분 연속 수열의 개수 구하기
n = 5
m = 5
data = [1, 2, 3, 2, 5]

count = 0
interval_sum = 0
end = 0

for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1

    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)


# --------------------------------------------------------
# 2.정렬되어 있는 두 리스트의 합집합 문제
n, m = 3, 4
a = [1, 3, 5]
b = [2, 4, 6, 8]

result = [0] * (n + m)
i = 0
j = 0
k = 0

while i < n or j < m:
    if j >= m or (i < n and a[i] <= b[j]):
        result[k] = a[i]
        i += 1
    else:
        result[k] = b[j]
        j += 1
    k += 1

for i in result:
    print(i, end=' ')
