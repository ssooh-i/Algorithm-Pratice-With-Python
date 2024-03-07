# 최대 수익을 구하는 두 알고리즘의 계산 속도를 비교하기
# 최대 수익 문제를 O(n*n)과 O(n)으로 푸는 알고리즘을 각각 수행하여 걸린 시간을 출력, 비교

import time # 시간 측정을 위한 모듈
import random # test 주가 생성을 위한 모듈

# 최대 수익 : 느린 O(n*n) 알고리즘
def max_profit_slow(prices):
    n = len(prices)
    max_price = 0  # 최대 수익은 항상 0 이상

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            # i날에 사서 j날에 팔았을 때 얻는 수익
            if prices[j] - prices[i] > max_price:  # 최대 수익보다 크면 최대 수익 갱신
                max_price = prices[j] - prices[i]

    return max_price

# 최대 수익 : 빠른 O(n) 알고리즘
def max_profit_fast(prices):
    n = len(prices)
    max_price = 0  # 최대 수익은 항상 0 이상
    min_price = prices[0] # 첫째날의 주가를 주가의 최솟값으로 기억

    for i in range(1, n):
        # 지금까지의 최솟값에 주식을 사서 i날에 팔 때의 수익
        profit = prices[i] - min_price
        if profit > max_price:
            max_price = profit
        if prices[i] < min_price:
            min_price = prices[i]

    return max_price

def test(n):
    # test 자료 만들기 (5000~20000까지의 난수를 주가로 사용)
    a = []
    for i in range (0, n):
        a.append(random.randint(5000, 20000))

    # 느린 알고리즘 테스트
    start = time.time()
    mps = max_profit_slow(a)
    end = time.time()
    time_slow = end - start

    # 빠른 알고리즘 테스트
    start = time.time()
    mpf = max_profit_fast(a)
    end = time.time()
    time_fast = end - start

    # 계산 결과
    print(n, mps, mpf) # 입력 크기, 각각 알고리즘이 계산한 최대 수익 값 (같아야 함)

    # 계산 시간 비교
    m = 0 # 느린 알고리즘과 빠른 알고리즘의 수행 시간 비율을 저장할 변수
    if time_fast > 0: # 컴퓨터 환경에 따라 빠른 알고리즘 시간이 0으로 측정 될 수 있음, 이럴 때는 0을 출력
        m = time_slow / time_fast

    print("%d %.5f %.5f %.2f" % (n, time_slow, time_fast, m))

test(100)