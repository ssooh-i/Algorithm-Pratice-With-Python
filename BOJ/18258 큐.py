import sys
N = int(sys.stdin.readline())
Queue = []
for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        Queue.append(int(command[1]))
        #print(Queue[-1])

    elif command[0] == "pop":
        if len(Queue) == 0:  # 길이가 0이면 값이 아무것도 없다는 것
            print(-1)
        else:
            print(Queue[0])
            del Queue[0] #list의 0자리 원소 삭제/ 특정 원소를 지우고 싶다면 remove()쓰기

    elif command[0] == "size":
        print(len(Queue))

    elif command[0] == "empty":
        if len(Queue) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == "front":
        if len(Queue) == 0:
            print(-1)
        else:
            print(Queue[0])

    elif command[0] == "back":
        if len(Queue) == 0:
            print(-1)
        else:
            print(Queue[-1])


