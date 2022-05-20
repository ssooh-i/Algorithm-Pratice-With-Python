T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    all = ''
    for i in range(0, n):
        char, _loop = input().split(" ")
        for _ in range(int(_loop)):
            all += char

    i = 0
    print(f"#{tc}")
    while i<len(all):
        print(all[i],end="")
        i+=1
        if i%10 == 0:
            print()

    # answer = ""
    # for i in range(0, len(all)):
    #     if (i != 0) & (i % 10 == 0):
    #         answer += '\n'
    #     answer += all[i]
    #
    # print(answer.strip())

    # i = 10
    # while i<len(all):
    #     print(all[i-10:i])
    #     i+=10
    # print(all[i-10:])

    # for j in range(0, len(all)):
    #     for i in range(0,10):
    #         print(all[i], end="")
    #     print()
# T = int(input())
# for tc in range(1, T+1):
#     n = int(input())
#     document = {}
#     result = []
#     all = []
#     for i in range(0, n):
#         s, num = input().split(" ")
#         document[s] = int(num)
#         #print(document) #딕셔너리에 값추가 확인
#     _key = list(document.keys())
#     _valuse = list(document.values())
#     for j in range(0, n):
#         result.append(_key[j]*_valuse[j])
#     for i in range(0, len(result)):
#         all += list(result[i])
#     #print(all)
#
#     i = 0
#
#     print(f"#{tc} ")
#     while i < len(all):
#         print(all[i], end="")
#         i += 1
#         if i % 10 == 0:
#             print()