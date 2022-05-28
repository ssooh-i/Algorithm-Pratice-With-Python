def solution(lottos, win_nums):
    answer = []
    count = 0
    zero_count = 0
    for i in range(6):
        for j in range(6):
            if win_nums[i] == lottos[j]:
                count += 1
    for i in range(6):
        if lottos[i] == 0:
            zero_count += 1
    if (count+zero_count) == 0:
        answer.append(6)
    else:
        answer.append(7-(count+zero_count))

    if count == 0:
        answer.append(6)
    else:
        answer.append(7-count)

    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))

print(solution([14, 12, 13,15, 5, 1], [20, 9, 3, 45, 4, 35]))