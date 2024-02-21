# 일반적인 선택정렬 알고리즘 (버블정렬)

def sel_sort(a):
    n = len(a)
    for i in range(0, n - 1):  # 0부터 n-2까지 반복
        # i번 위치부터 끝까지 자료 값 중 최소값의 위치를 찾음
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        # 찾은 최소값을 i번 위치로 이동
        a[i], a[min_idx] = a[min_idx], a[i]

def sel_resort(a):
    n = len(a)
    for i in range(0, n - 1):  # 0부터 n-2까지 반복
        max_idx = i
        for j in range(i + 1, n):
            if a[j] > a[max_idx]: # 내림차순으로 만들려면, 여길 부등호 바꿔주면 됨
                max_idx = j
        a[i], a[max_idx] = a[max_idx], a[i]

d1 = [2, 4, 5, 1, 3]
d2 = [2, 4, 5, 1, 3]
sel_sort(d1)
sel_resort(d2)
print(d1)
print(d2)