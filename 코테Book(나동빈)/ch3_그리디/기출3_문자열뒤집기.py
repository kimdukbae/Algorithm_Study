S = input()
cnt0 = 0
cnt1 = 0

if int(S[0]) == 0:
    cnt0 += 1
elif int(S[0]) == 1:
    cnt1 += 1

for i in range(1, len(S)):
    target = int(S[i])
    if target != int(S[i - 1]):
        if target == 0:
            cnt0 += 1
        elif target == 1:
            cnt1 += 1

print(min(cnt0, cnt1))