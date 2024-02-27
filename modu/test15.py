# 친구 리스트에서 자신의 모든 친구를 찾는 알고리즘 - 그래프
# 앞으로 처리해야 할 사람을 넣어두었다가 꺼내기 위한 기억 장소로 큐를 사용한다.
# 이미 처리 대상으로 추가한 사람들을 적어둘 기억 장소로 집합을 이용한다.

def print_all_friends(g, start):
    qu = []  # 앞으로 처리해야 할 사람들을 큐에 저장
    done = set()  # 이미 큐에 추가한 사람들을 집합에 기록 (중복 방지)

    qu.append(start)  # 자신을 큐에 넣고 시작
    done.add(start)  # 집합에도 추가

    while qu:  # 큐에 처리할 사람이 남아있는 동안
        p = qu.pop(0)  # 처리 대상 한명 꺼내기
        print(p)  # 이름 출력
        for x in g[p]:  # 그의 친구들 중에
            if x not in done:  # 아직 큐에 추가된 적이 없는 사람을
                qu.append(x) # 큐에 추가하고
                done.add(x) # 집합에도 추가

# 친구 관계 리스트
# A와 B가 친구이면
# A의 친구 리스트에도 B가 나오고, B의 친구 리스트에 A가 나옴
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

# 그래프에 연결된 모든 꼭짓점을 탐색하는 알고리즘 - 그래프 탐색 알고리즘