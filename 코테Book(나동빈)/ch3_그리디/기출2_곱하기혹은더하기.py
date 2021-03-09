S = input()
result = int(S[0])

for i in range(1, len(S)):
    target = int(S[i - 1])
    addOrPlus = int(S[i])

    if target == 0 or target == 1:
        result += addOrPlus
    elif 2 <= target <= 9:
        result *= addOrPlus

print(result)