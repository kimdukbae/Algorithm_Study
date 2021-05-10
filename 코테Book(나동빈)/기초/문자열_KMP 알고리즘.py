# 참고 : https://devbull.xyz/python-kmp-algorijeumeuro-munjayeol-cajgi/
# Longest proper prefix which is suffix
def compute_LPS(string, lps):
    # 접두사와 접미사의 가장 긴 길이
    length = 0

    # 항상 lps[0]은 0이므로 while문은 i=1부터 시작!
    i = 1
    while i < len(string):
        # 이전 인덱스에서 같았다면 다음 인덱스만 비교하면 된다.
        if string[i] == string[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            # 일치하지 않는 경우
            if length != 0:
                # 이전 인덱스에서는 같았으므로 length를 줄여서 다시 검사
                # ?
                length = lps[length - 1]
            else:
                # 이전 인덱스에서도 같지 않았다면 lps[i]는 0이고 i는 1 증가
                lps[i] = 0
                i += 1


def KMP(txt, patt):
    N = len(txt)
    M = len(patt)
    lps = [0] * M

    compute_LPS(patt, lps)

    i = 0  # txt의 index
    j = 0  # pattern의 index
    while i < N:
        # 문자열이 같은 경우 양쪽 인덱스를 모두 증가
        if patt[j] == txt[i]:
            i += 1
            j += 1
        # Pattern 못 찾았으면
        elif patt[j] != txt[i]:
            # j != 0인 경우는 짧은 lps에 대해 재검사
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

        # Pattern 찾은 경우
        if j == M:
            print("Found a pattern at index " + str(i - j))
            j = lps[j - 1]


# text = 'ABXABABABXAB'
# pattern = 'ABXAB'
# text = "ABABDABACDABABCABAB"
# pattern = "ABABCABAB"
text = 'ABABCABABABCABABAB'
pattern = 'ABABCABABAB'
KMP(text, pattern)
