import sys
N = int(sys.stdin.readline()) #input() 시간초과 에러뜸
Q = []
for i in range(N):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        Q.append(command[1])

    elif command[0] == 'pop':
        if len(Q) == 0: #길이가 0이면 값이 아무것도 없다는 것
            print(-1)
        else:
            print(Q.pop()) #pop은 값 꺼내오고 삭제됨

    elif command[0] == 'size':
        print(len(Q))

    elif command[0] == 'empty':
        if len(Q) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == 'top':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q[-1]) #스택에 젤 마지막부분 가져오기
