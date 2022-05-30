def solution(participant, completion):
    answer = []
    lst1= participant.split()
    lst2 = completion.split()
    complement = list(set(lst1) - set(lst2))
    print(complement)  # ['B', 'A']
    complement = list(set(lst1).difference(lst2))
    print(complement)
    return answer

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))