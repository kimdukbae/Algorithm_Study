import sys

input = sys.stdin.readline

N, K = map(int, input().split())
electricity = list(map(int, input().split()))

plug = [0] * N
answer = 0
change, maximum = 0, 0

while electricity:
    product = electricity[0]

    if product in plug:
        electricity.remove(product)
        continue

    elif 0 in plug:
        plug[plug.index(0)] = product
        electricity.remove(product)

    else:
        for pl in plug:
            if pl not in electricity:
                change = pl
                break

            elif electricity.index(pl) > maximum:
                maximum = electricity.index(pl)
                change = pl

        plug[plug.index(change)] = product
        electricity.remove(product)
        maximum = 0
        answer += 1

print(answer)
