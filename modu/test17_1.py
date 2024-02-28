# 가짜 동전 찾기 알고리즘 (가짜 동전은 1개이고 무게가 다른 동전보다 가볍다)
# 방법 2 : 반씩 그룹으로 나눠서 비교하기

# a에서 b까지 놓인 동전과 c에서 d까지에 놓인 동전의 무게를 비교
# a에서 b까지에 놓인 동전 중에 가짜 동전이 있으면 -1
# c에서 d까지에 놓인 동전 중에 가짜 동전이 있으면 1
# 양쪽에 가짜 동전이 없으면 0
def weigh(a, b, c, d):
    print('a:', a, ' b:', b, ' c:', c, ' d:', d)
    fake = 100
    if a <= fake and fake <= b:
        return -1
    elif c <= fake and fake <= d:
        return 1
    else:
        return 0


def find_fakecoin(left, right):
    # 종료조건 : 가짜 동전이 있을 범위 안에 동전이 한개뿐이면 그 동전이 가짜동전이다.
    if left == right:
        return left
    # left에서 right까지에 놓인 동전을 두 그룹(g1_left ~ g1_right, g2_left ~ g2_right)으로 나눔
    half = (right - left + 1) // 2
    # 동전 수가 홀수면 2그룹으로 나누고 1개가 남음
    g1_left = left
    g1_right = left + half - 1
    g2_left = left + half
    g2_right = g2_left + half - 1

    # 나눈 두 그룹을 weigh()함수를 이용해 저울질 함
    result = weigh(g1_left, g1_right, g2_left, g2_right)

    if result == -1:  # left 동전이 가벼움
        return find_fakecoin(g1_left, g1_right)
    elif result == 1:  # right 동전이 가벼움
        return find_fakecoin(g2_left, g2_right)
    else:
        return right  # 두 그룹으로 나눠지지 않고 남은 한개의 동전이 가짜동전임


n = 100
print(find_fakecoin(1, n))
