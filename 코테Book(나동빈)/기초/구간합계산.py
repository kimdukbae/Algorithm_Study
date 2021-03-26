# 시간복잡도를 줄이기 위한 핵심은 ★접두사 합(prefix_sum)★을 이용하는 것이다!!

n = 5
data = [10, 20, 30, 40, 50]

sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

# [1, 3] 구간 합
print(prefix_sum[3] - prefix_sum[0])

# [2, 5] 구간 합 
print(prefix_sum[5] - prefix_sum[1])

# [3, 4] 구간 합
print(prefix_sum[4] - prefix_sum[2])
