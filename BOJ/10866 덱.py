import sys
N = int(sys.stdin.readline())
Deque = []
for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "push_front":
        Deque.insert(0, int(command[1])) #insert(인덱스번호, 값)

    elif command[0] == "push_back":
        #Deque.insert(len(Deque), int(command[1])) # 맨끝에 요소추가 1
        Deque.append(int(command[1])) #맨끝에 요소추가 2


    elif command[0] == "pop_front":
        if len(Deque) == 0:  # 길이가 0이면 값이 아무것도 없다는 것
            print(-1)
        else:
            print(Deque[0])
            del Deque[0] #list의 0자리 원소 삭제/ 특정 원소를 지우고 싶다면 remove()쓰기

    elif command[0] == "pop_back":
        if len(Deque) == 0:
            print(-1)
        else:
            print(Deque[-1])
            del Deque[-1]

    elif command[0] == "size":
        print(len(Deque))

    elif command[0] == "empty":
        if len(Deque) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == "front":
        if len(Deque) == 0:
            print(-1)
        else:
            print(Deque[0])

    elif command[0] == "back":
        if len(Deque) == 0:
            print(-1)
        else:
            print(Deque[-1])


