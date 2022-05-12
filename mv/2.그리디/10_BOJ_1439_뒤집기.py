import sys

input = sys.stdin.readline

S = input()
words = list(S)

zero_block = 0
one_block = 0
explore = [words[0]]

for i in range(1, len(words)):
    if explore[-1] == words[i]:
        explore.append(words[i])
    else:
        if explore[-1] == '0':
            zero_block += 1
            explore = [words[i]]
        elif explore[-1] == '1':
            one_block += 1
            explore = [words[i]]

print(min(zero_block, one_block))
