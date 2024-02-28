# 최대 수익 알고리즘
# 방법 2 : 한번 반복으로 최대 수익 찾기 (주식을 파는 날을 중점으로 고려)
def max_profit(prices):
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


stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]

print(max_profit(stock))
