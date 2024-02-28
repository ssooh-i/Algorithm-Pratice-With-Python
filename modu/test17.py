# 가짜 동전 찾기 알고리즘 (가짜 동전은 1개이고 무게가 다른 동전보다 가볍다)
# 방법 1 : 하나씩 비교하기

# a에서 b까지 놓인 동전과 c에서 d까지에 놓인 동전의 무게를 비교
# a에서 b까지에 놓인 동전 중에 가짜 동전이 있으면 -1
# c에서 d까지에 놓인 동전 중에 가짜 동전이 있으면 1
# 양쪽에 가짜 동전이 없으면 0
def weigh(a, b, c, d):
    #print('a:', a,' b:', b,' c:', c,' d:', d)
    fake = 100
    if a <= fake and fake <= b:
        return -1
    elif c <= fake and fake <= d:
        return 1
    else:
        return 0


# weigh()함수(저울질)를 이용하여 left, right까지에 놓인 가짜 동전의 위치를 알아내기
def find_fakecoin(left, right):
    for i in range(left + 1, right+1):  # left+1 ~right까지 반복
        # 가장 왼쪽 동전과 나머지 동전을 차례로 비교
        result = weigh(left, left, i, i)
        if result == -1:  # left 동전이 가벼움
            return left
        elif result == 1:  # right 동전이 가벼움
            return i
    return -1  # 모든 동전의 무게가 같으면, 가짜동전이 없는 예외 경우


n = 100 # 전체 동전 개수
print(find_fakecoin(0, n - 1))