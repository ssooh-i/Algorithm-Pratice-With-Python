# 순차 탐색으로 특정 값의 위치 알기
# 입력 : 리스트 a, 찾는 값 x
# 출력 : 찾으면 그 값의 위치, 찾지 못하면 -1

# def search_list(a, x):
#     for i in a:
# i가 인덱스가 아니라 리스트 a의 요소 자체, 그래서 이 코드는 오류이다.
# 왜냐하면 i는 리스트 a의 요소가 되고, 따라서 if a[i]에서는 실제 요소 값을 사용하는 것이기 때문
#         if a[i] == x:
#             return i
#
#     return -1

def search_list(a, x):
    n = len(a)
    for i in range(0, n):
        if a[i] == x:
            return i

    return -1


v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search_list(v, 18))
print(search_list(v, 33))
print(search_list(v, 900))
