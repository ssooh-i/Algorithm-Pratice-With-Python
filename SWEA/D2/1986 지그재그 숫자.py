T = int(input())
for tc in range(1, T+1):
    N = int(input())
    temp = []
    result = 0
    for i in range(0, N+1):
        temp.append(i)
        if i == N:
            pass
        else:
            if (i+1)%2 == 0:
                temp.append('-')
            else:
                temp.append('+')

    #print(*temp)
    for i in range(1, len(temp),2):
        if temp[i] == '+':
            result += temp[i+1]
        else:
            result -= temp[i+1]
    print(f"#{tc} {result}")


# T = int(input())
# for tc in range(1, T+1):
# N = int(input())
#
# isPlus = False
# _sum = 1
# for i in range(2, N+1):
#     if (isPlus): # 더해주겠따.
#         _sum += i
#         isPlus = False
#     else: # 뺴주겠따.
#         _sum -= i
#         isPlus = True
# print(_sum)