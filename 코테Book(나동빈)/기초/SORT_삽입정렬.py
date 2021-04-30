# 삽입 정렬을 사용하여 오름차순 정렬
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(arr)):
    # 인덱스 i부터 1까지 감소하며 반복
    for j in range(i, 0, -1):
        # 한 칸씩 왼쪽으로 이동
        if arr[j] < arr[j - 1]:
            temp = arr[j]
            arr[j] = arr[j - 1]
            arr[j - 1] = temp
        # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
        else:
            break

print(arr)
