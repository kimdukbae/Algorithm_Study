# 내 풀이
N = int(input())
cnt = 0

for hour in range(N + 1):
    for minute in range(60):
        for sec in range(60):
            if '3' in str(hour) + str(minute) + str(sec):
                cnt += 1

print(cnt)
# 풀이와 해답이 같다~