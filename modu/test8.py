# 선택 정렬을 사용해서 주어진 리스트의 자료를 오름차순으로 정렬하는 알고리즘을 만드시오
# 입력 : 리스트 a
# 출력 : 정렬된 새 리스트
# 주어진 리스트에서 최솟값의 위치를 돌려주는 함수

# def find_min_idx(a): #내가 짠 코드
#     n = len(a)
#     min_idx = 0
#     for i in range(1, n):  # 0번째랑 비교할 꺼니까 1부터 시작
#         if a[i - 1] < a[i]:  # a[i]번째가 더 클때
#             min_idx = i - 1
#         if a[i - 1] > a[i]:  # a[i-1]번째가 더 클때
#             min_idx = i
#
#     return min_idx

def find_min_idx2(a): #책 코드
    n = len(a)
    min_idx = 0
    for i in range(1, n):
        if a[min_idx] > a[i]:  # a[i-1]번째가 더 클때
            min_idx = i

    return min_idx


#d = [2, 4, 5, 1, 3]
v = [2, 3, 4, 5, 1]
#print(find_min_idx(d))
print(find_min_idx2(v))
