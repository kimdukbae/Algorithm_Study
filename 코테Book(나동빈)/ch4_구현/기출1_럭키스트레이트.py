N = input()
half = len(N) // 2

left = N[:half]
right = N[half:]

res1, res2 = 0, 0
for x, y in zip(left, right):
    res1 += int(x)
    res2 += int(y)

if res1 == res2:
    print("LUCKY")
else:
    print("READY")