# 입력 리스트 안에서 직접 위치를 바꿔 정렬하는 방법

def ins_sort(a):
    n = len(a)
    for i in range(1, n):  # 1번부터 n-1까지
        key = a[i]  # i번 위치에 있는 값을 key에 저장
        # j를 i 바로 왼쪽 위치로 저장
        j = i - 1
        # 리스트의 j번 위치에 있는 값과 key를 비교해 key가 삽입될 적절한 위치를 찾음
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]  # 삽입할 공간이 생기도록 값을 오른쪽으로 한칸 이동시킴
            j -= 1
        a[j + 1] = key  # 찾은 삽입 위치에 key를 저장

def ins_resort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] < key: #부등호 바꾸면 내림차순이 됨
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key

d = [2, 4, 5, 1, 3]
# ins_sort(d)
ins_resort(d)
print(d)
ins_sort(d)
print(d)