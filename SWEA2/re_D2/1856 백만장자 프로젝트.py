T = int(input())
for tc in range(1, T+1):
    n = int(input())
    N = list(map(int, input().split()))
    _sum = 0
    _max = N[-1]
    for i in range(n-1, -1, -1):
        if _max > N[i]:
            _sum += _max - N[i]
        else: # max_n =< nums[i] 경우
            _max = N[i]
    print(f"#{tc} {_sum}")
