class Stage():
    def __init__(self, stage, fail):
        self.stage = stage
        self.fail = fail

def solution(N, stages):
    answer = []
    _count = [0 for _ in range(N+1)]  # 현재 스테이지인 사람
    _stages = []

    for i in stages:
        print(i)
        _count[i-1] += 1
    print(_count)

    passOrChallenge = len(stages)

    for i in range(N):
        _stages.append(Stage(i+1, _count[i] / passOrChallenge))
        passOrChallenge -= _count[i]

    for i in range(len(_stages)):
        print(_stages[i].fail)

    _stages.sort(reverse=True, key=lambda s: s.fail) #[s.fail for s in _stages]
    for i in range(len(_stages)):
        answer.append(_stages[i].stage)

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
