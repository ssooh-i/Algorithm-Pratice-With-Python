#Counter쓰면 안됨
# from collections import Counter
# T = int(input())
# for i in range(1, T+1):
#     num = int(input())
#     test_case = list(map(int, input().split(" ")))
#     if len(test_case) == 1000:
#         bin = Counter(test_case).most_common(1)
#         bin1 = bin[0]
#         bin2 = bin1[0]
#         print("#"+str(i),bin2)
#     else:
#         print(-1)

T = int(input())

for tc in range(1, T+1):
    num = int(input())
    for c in range(num):
        test_case = list(map(int, input().split()))
        score = [0 for _ in range(101)]
        for i in test_case:
            score[i] += 1

        _max = max(score) #17
        for i in range(100, -1, -1):
            if _max == score[i]:
                print(f"#{num} {i}")


            #score.insert(test_case[x], +1) #insert는 원하는 인덱스에 값추가
            #for y in range(0,101):
                # if test_case[x] == score[y]:
                #     score[y] += 1
# t = int(input())
# while t:
#     #반복횟수를 감소시킴(반복문으로 처리해도 무방함)
#     t -= 1
#     #몇번째 케이스인지
#     case = int(input())
#     grade = list(map(int, input().split()))
#     lst = [0]*101
#     #각 자리수마다 카운팅한다.
#     #숫자 1번이 나오면 1번 인덱스에 +1 이런식으로
#     for g in grade:
#         lst[g] += 1
#     #최대값을 찾는다.
#     max_num = max(list)
#     #최대값과 같은값을 뒤에서부터 찾는다.
#     #앞에서 부터 찾으면 정답이 틀릴 수 있다.
#     for i in range(100, -1, -1):
#         if max_num == lst[i]:
#             print(f"#{case} {i}")
#             break