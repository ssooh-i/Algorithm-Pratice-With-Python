# t = int(input())
# for tc in range(1, t+1):
#     _list = list(map(int, input().split()))
#     _list.sort()
#     sum = 0
#     for i in range(1,9):
#         sum += _list[i]
#     avg = int(sum/8)
#     print(f"#{tc} {round(avg)}")

    # _max = max(_list)
    # _min = min(_list)
    # for i in range(0, 10):
    #
    #     if _min == _list[i]:
    #         _list.remove(_min)
    #     elif _max == _list[i]:
    #         _list.remove(_max)
    #     else:
    #         break
    # print(_list)

T = int(input())
for tc in range(1, T+1):
    nums = list(map(int, input().split()))
    nums.sort()
    min_n = min(nums)
    max_n = max(nums)
    nums.remove(min_n)
    nums.remove(max_n)

    avg = sum(nums)/8

    print(f'#{tc} {round(avg)}')