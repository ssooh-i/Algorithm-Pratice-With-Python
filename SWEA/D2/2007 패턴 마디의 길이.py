# #문제 케이스가 이상하여 백준 16229번 반복 패턴 문제로 대체함
# n,m = map(int, input().split(" "))
# s = list(input())
# k = s[0]
# if len(s) > n:
#     print('s input Error')
# else:
#     for i in range(0, m):
#         s.append(s[i])
#         print(s)
#
    # for j in range(0, m):
    #     for i in range(len(s), len(s)+m):
    #         s[i].append(s[j])
    #         print(s)

T = int(input())

for tc in range(1, T + 1):

    text = input()
    patten = []
    next_patten = []
    ans = 0
    for i in range(11):  # 마디의 최대 길이가 10이므로 range(11)
        patten = text[:i]  # patten리스트에 패턴 입력
        next_patten = text[i:i * 2]  # 다음 패턴 입력
        # print(patten)
        # print(next_patten)
        if i != 0 and patten == next_patten:  # 다음 패턴과 이번 패턴이 같은경우
            ans = len(patten)  # 길이 출력
            break
    print(f'#{tc} {ans}')