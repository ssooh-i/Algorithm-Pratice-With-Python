# testCase = int(input())
# num_list = []
# prime_number = [2,3,5,7,11]
# for tc in range(testCase):
#     num_list.append(int(input()))
# for tc in range(testCase):
#     prime_number_count = [0,0,0,0,0]
#     num = num_list[tc]
#     for i in range(5):
#         while num % prime_number[i] == 0:
#             prime_number_count[i] += 1
#             num = num//prime_number[i]
#     print("#" + str(tc+1),end=' ')
#     for i in prime_number_count:
#         print(i,end = ' ')
#     print()

t = int(input())
for tc in range(1, t+1):
    A, B = map(int, input().split(" "))
    arr_A = list(map(int, input().split(" ")))
    arr_B = list(map(int, input().split(" ")))
    _max = 0

    if B > A:
        for i in range(0, B-A+1):
            sum = 0
            for j in range(A):
                sum += arr_B[j+i] * arr_A[j]
            _max = max(_max, sum)

        #     sum = 0
        #     sum += arr_A[i] * arr_B[i]
        #     #print(sum)
        #     _max = max(_max, sum)
        # #print(_max)


    elif A > B:
        for i in range(0, A-B+1):
            sum = 0
            for j in range(B):
                sum += arr_A[j+i] * arr_B[j]
            _max = max(_max, sum)

    else: #A == B
        sum = 0
        for i in range(0, A):
            sum += arr_A[i] * arr_B[i]
            _max = sum

    print(f"#{tc} {_max}")