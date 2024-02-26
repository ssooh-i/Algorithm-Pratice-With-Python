# 이진 탐색
# 리스트에서 특정 숫자 위치 찾기
# 입력 : 리스트 a, 찾는 값 x
# 출력 : 찾으면 그 값의 위치, 찾지 못하면 -1 출력
def binary_search(a, x):
    # 탐색할 범위를 저장하는 함수 start, end
    # 리스트 전체를 범위로 탐색 시작
    start = 0
    end = len(a) - 1

    while start <= end:  # 탐색할 범위가 남아있는 동안
        mid = (start + end) // 2  # 탐색 범위의 중간 위치 (몫만 가져옴)
        if a[mid] == x:
            return mid
        elif a[mid] < x:  # x가 중간 값보다 크다면 시작 범위를 더 미룬다
            start = mid + 1
        else:  # x가 중간 값보다 작다면 끝범위를 당긴다
            end = mid - 1
    return -1  # 못 찾았을 때


d = [1, 4, 9, 16, 25, 36, 49, 64, 81]

print(binary_search(d, 36))
print(binary_search(d, 53))