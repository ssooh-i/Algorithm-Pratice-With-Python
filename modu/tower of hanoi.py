MSG_FORMAT = "{}번 원반을 {}에서 {}로 이동"

def move(N, start, to):
    print(MSG_FORMAT.format(N, start, to))

def hanoi(N, start, to, aux):
    if N == 1:
        move(1, start, to)
    else:
        hanoi(N-1, start, to, aux)
        move(N-1, start, to) #얘를 내리게되면 순서가 달라진다, 답이 아님
        hanoi(N-1, aux, to, start)

def honoiCount(N):
    return (2**N) - 1



hanoi(3, 'A', 'C', 'B')
print(honoiCount(3))

hanoi(5, 'A', 'C', 'B')
print(honoiCount(5))