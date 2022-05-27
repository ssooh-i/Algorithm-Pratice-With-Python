import math
class Student():
    def __init__(self, num, total, report):
        self.num = num
        self.total = total
        self.report = report

    def


T = int(input())

grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    g = N // 10

    stu = []
    for i in range(N):
        scores = (list(map(int, input().split())))
        stu.append(Student(i+1, (scores[0]*0.35 + scores[1]*0.45 + scores[2]*0.2)))
        stu[i].calTotal()
    stu.sort(key=lambda s: s.total, reverse=True)

    for i in range(N):
        if stu[i].num == K:
            gRank = int(math.floor(i/g))
            # print(f"{i}등 등급{i/g}")
            print(f"#{tc} {grade[gRank]}")
            break