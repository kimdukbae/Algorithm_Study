def solution(s):
    length = len(s)
    cand = [length]

    for size in range(1, length):
        compressed = ""
        splited = [s[i:i+size] for i in range(0, length, size)]
        count = 1

        for j in range(1, len(splited)):
            prev, cur = splited[j-1], splited[j]
            if prev == cur:
                count += 1
            else:
                compressed += (str(count) + prev) if count > 1 else prev
                count = 1

        compressed += (str(count) + splited[-1]) if count > 1 else splited[-1]
        cand.append(len(compressed))

    return min(cand)

print(solution("aabbaccc"))