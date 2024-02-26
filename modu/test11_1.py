# 쉽게 설명한 퀵정렬
# 입력 : 리스트 a
# 출력 : 정렬된 새 리스트

def quick_sort(a):
    n = len(a)

    # 퀵 정렬 함수는 재귀 호출 함수이므로 병합 정렬과 마찬가지로 종료조건이 필요하다
    # 종료 조건: 정렬할 리스트의 자료개수가 1개 이하면 정렬할 필요가 없음
    if n <= 1:
        return a

    # 기준 값을 정하고 기준에 맞춰 그룹을 나누는 과정
    pivot = a[-1]  # 편의상 마지막 요소를 기준으로 둠
    g1 = []  # 기준보다 작은 값
    g2 = []  # 기준보다 큰 값

    for i in range(0, n - 1):  # 기준이 맨 마지막 값이니까 제외한다
        if a[i] < pivot:
            g1.append(a[i])
        else:
            g2.append(a[i])

    # 각 그룹에 대해 재귀 호출로 퀵 정렬을 한 후
    # 기준 값과 합쳐 하나의 리스트로 결곽값 반환
    return quick_sort(g1) + [pivot] + quick_sort(g2)


d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(quick_sort(d))
