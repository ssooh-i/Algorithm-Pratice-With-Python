class Stage():
    def __init__(self, num, fail):
        self.num = num
        self.fail = fail


def solution(N, stages):
    answer = []
    _stage = []

    _count = [0 for _ in range(N + 1)]
    for i in range(len(stages)):
        _count[stages[i] - 1] += 1

    p = len(stages)
    for i in range(0, N):
        fail = 0
        if p != 0:
            fail = _count[i] / p
        _stage.append(Stage(i + 1, fail))
        p -= _count[i]
    _stage.sort(reverse=True, key=lambda s: s.fail)

    for i in range(len(_stage)):
        answer.append(_stage[i].num)

    return answer


print(solution(4, [4, 4, 4, 4, 4]))
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
