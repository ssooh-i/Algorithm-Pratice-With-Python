# 재귀호출을 이용한 이진 탐색 만들기

def binary_search(a, x, start, end):
    # 종료조건 : 남은 탐색 범위가 비었으면 종료
    if start > end:
        return -1

    mid = (start + end) // 2  # 탐색 범위의 중간 위치 (몫만 가져옴)
    if a[mid] == x:
        return mid
    elif a[mid] < x:  # x가 중간 값보다 크다면 시작 범위를 더 미룬다
        return binary_search(a, x, mid+1, end)
    else:  # x가 중간 값보다 작다면 끝 범위를 당긴다
        return binary_search(a, x, start, mid-1)

    return -1


d = [1, 4, 9, 16, 25, 36, 49, 64, 81]

print(binary_search(d, 36, 0, len(d)-1))
print(binary_search(d, 53, 0, len(d)-1))
