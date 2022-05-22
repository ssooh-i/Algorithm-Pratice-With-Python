T = int(input())

# for t in range(1, 1+T):
#     N = input()
#     arr = [0,0,0,0,0,0,0,0,0,0]
#     intN = int(N)
#     count = 1
#     while 0 in arr:
#         for i in N:
#             if arr[int(i)] > 0:
#                 continue
#             else:
#                 arr[int(i)] += 1
#         count += 1
#         result = str(intN*count)
#     count -= 1
#     print(f'#{t} {result}')

for tc in range(1, T +1):
    N = input()
    count = [0 for _ in range(10)]
    N=list(N)
    for i in range(len(N)):
        if (count[i] == 0) & (count[i] == N[i]):
            count[i] = 1
    print(count)