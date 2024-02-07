# def solution(participant, completion):
#     answer = []
#     lst1= participant.split()
#     lst2 = completion.split()
#     complement = list(set(lst1) - set(lst2))
#     print(complement)  # ['B', 'A']
#     complement = list(set(lst1).difference(lst2))
#     print(complement)
#     return answer
#
# print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))

#다시풀기
def solution(participant, completion):
    participant.sort()
    completion.sort()

    for part, com in zip(participant, completion):
        if part != com:
            return part
    return participant[-1]