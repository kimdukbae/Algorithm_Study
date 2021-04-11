import sys

input = sys.stdin.readline
S = input().rstrip()    # 주의! rstrip() 안하면 개행문자 추가되서 길이 + 1이 됨
count = [0] * 2 # 카운팅 배열

# 0 -> 1 or 1 -> 0 으로 바꾸는 부분 체크
for i in range(len(S) - 1):
    if S[i] == '0' and S[i] != S[i + 1]:
        count[0] += 1
    elif S[i] == '1' and S[i] != S[i + 1]:
        count[1] += 1

# 마지막 덩어리가 연속된 0의 덩어리인지 혹은 1의 덩어리인지 확인
if S[len(S) - 1] == '0':
    count[0] += 1
else:
    count[1] += 1

print(min(count))
