# 퀵 정렬
# 입력 : 리스트 a
# 출력 : 입력으로 주어진 a
# 리스트a에서 어디부터 어디까지가 정렬 대상인지
# 범위를 지정하여 정렬하는 재귀 호출 함수

def quick_sort_sub(a, start, end):
    # 종료 조건
    if end - start <= 0:
        return

    pivot = a[end]
    i = start

    for j in range(start, end):
        if a[j] <= pivot:
            print('pivot : ', pivot)
            print('바뀌기 전 a[i] = ', a[i], ', a[j] = ', a[j])
            print('바뀌기 전 d:', d)
            a[i], a[j] = a[j], a[i]
            print('바뀐 후 d:', d)
            i += 1
    print('for문 끝남 a[i] = ', a[i], ', a[end] = ', a[end])
    # 왜 끝에 요소와 i번째 요소를 바꿔주는 가?
    # 피벗을 기준으로 리스트를 두 부분으로 나누고 각각 정렬하는 것이 퀵 정렬의 핵심이기 때문에
    # 피벗을 중간으로 이동 시켜주는 것이다.
    a[i], a[end] = a[end], a[i]
    print('for문 끝나고 d : ', d)
    print()

    # 재귀호출
    quick_sort_sub(a, start, i - 1)  # 기준 값보다 작은 그룹을 재귀 호출로 다시 정렬
    quick_sort_sub(a, i + 1, end)  # 기준 값보다 큰 그룹을 재귀 호출로 다시 정렬


# 리스트 전체(0~len(a)-1)를 대상으로 재귀함수 호출
def quick_sort(a):
    quick_sort_sub(a, 0, len(a) - 1)


d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]

quick_sort(d)
print(d)
