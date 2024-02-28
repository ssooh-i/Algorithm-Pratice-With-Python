# 최대 수익 알고리즘
# 방법 1 : 가능한 모든 경우를 비교하기 (주식을 사는 날이 중심으로 된 생각)
def max_profit(prices):
    n = len(prices)
    max_profit = 0  # 최대 수익은 항상 0 이상

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            # i날에 사서 j날에 팔았을 때 얻는 수익
            if prices[j] - prices[i] > max_profit:  # 최대 수익보다 크면 최대 수익 갱신
                max_profit = prices[j] - prices[i]

    return max_profit


stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]

print(max_profit(stock))
