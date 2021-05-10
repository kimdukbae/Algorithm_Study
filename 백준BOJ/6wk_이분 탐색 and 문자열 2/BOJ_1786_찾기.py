import sys

input = sys.stdin.readline
text = input().rstrip()
pattern = input().rstrip()

answer = 0
idx = []


# Longest proper prefix which is suffix
def compute_LPS(string, lps):
    length = 0

    i = 1
    while i < len(string):
        if string[i] == string[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1


def KMP(txt, patt):
    global answer, idx
    N = len(txt)
    M = len(patt)
    lps = [0] * M

    compute_LPS(patt, lps)

    i = 0
    j = 0
    while i < N:
        if patt[j] == txt[i]:
            i += 1
            j += 1
        elif patt[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
        if j == M:
            idx.append(i - j + 1)
            answer += 1
            j = lps[j - 1]


KMP(text, pattern)
print(answer)
print(*idx)
