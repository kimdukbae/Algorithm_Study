# 선택 정렬을 사용하여 오름차순 정렬
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(arr)):
    min_idx = i  # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(arr)):
        if arr[min_idx] > arr[j]:
            min_idx = j
    temp = arr[min_idx]
    arr[min_idx] = arr[i]
    arr[i] = temp

print(arr)
