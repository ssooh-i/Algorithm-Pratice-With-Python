# 하노이의 탑
# 입력 : 옮기려는 원반의 개수 n
# 옮길 원반이 현재 있는 출발점 기둥 from_pos
# 원반을 옮길 도착점 기둥 to_pos
# 옮기는 과정에서 사용할 보조 기둥 aux_pos
# 출력 : 원반을 옮기는 순서

def hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1:  # 종료 조건, 원반 한개를 옮기는 문제면 그냥 옮기면 된다.
        print(from_pos, " -> ", to_pos)
        return
    # 원반 n-1개를 aux_pos로 이동 (to_pos를 보조 기둥으로 사용)
    hanoi(n - 1, from_pos, aux_pos, to_pos)
    # 가장 큰 원반을 목적지로 이동
    print(from_pos, " -> ", to_pos)

    # aux_pos에 있는 원반 n-1개를 목적지로 이동(from_pos를 보조 기둥으로 사용)
    hanoi(n - 1, aux_pos, to_pos, from_pos)


# print("n = 1")
# #원반 1개를 1번 기둥에서 3번기둥으로 이동
# hanoi(1, 1, 3, 2)
# print("n = 2")
# #원반 2개를 1번 기둥에서 3번기둥으로 이동
# hanoi(2, 1, 3, 2)
# print("n = 3")
# #원반 3개를 1번 기둥에서 3번기둥으로 이동
# hanoi(3, 1, 3, 2)


print("n = 4")
hanoi(4, 1, 3, 2)
