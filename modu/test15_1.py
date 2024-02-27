# 친구 리스트에서 자신의 모든 친구를 찾고 친구들의 친밀도를 계산하는 알고리즘
# 입력 : 친구 관계 그래프 g, 모든 친구를 찾을 자신 start
# 출력 : 모든 친구의 이름과 자신과의 친밀도

def print_all_friends(g, start):
    qu = []  # 앞으로 처리해야 할 사람들을 큐에 저장
    done = set()  # 이미 큐에 추가한 사람들을 집합에 기록 (중복 방지)

    qu.append((start, 0))  # (자신, 친밀도) 정보를 하나의 튜플로 묶어 처리

    done.add(start)  # 집합에도 추가

    while qu:  # 큐에 처리할 사람이 남아있는 동안
        (p, d) = qu.pop(0)  # 처리 대상 한명 꺼내기
        print(p, d)  # 이름 출력
        for x in g[p]:  # 그의 친구들 중에
            if x not in done:  # 아직 큐에 추가된 적이 없는 사람을
                qu.append((x, d+1)) # 큐에 친밀도 +1해서 추가하고
                done.add(x) # 집합에도 추가

fr_info = {
    'Summer': ['John', 'Justin', 'Mike'],
    'John': ['Summer', 'Justin'],
    'Justin': ['John', 'Summer', 'Mike', 'May'],
    'Mike': ['Justin', 'Summer'],
    'May': ['Justin', 'Kim'],
    'Kim': ['May'],
    'Tom': ['Jerry'],
    'Jerry': ['Tom']
}


print_all_friends(fr_info, 'Summer')
print()
print_all_friends(fr_info, 'Jerry')
