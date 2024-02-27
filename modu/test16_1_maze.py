# 미로찾기 프로그램 (그래프 탐색)
# 입력: 미로 정보 g, 출발점 start, 도착점 end
# 출력: 미로를 나가기 위한 이동 경로는 문자열, 나갈 수 없으면 ? 출력

def solve_maze(g, start, end):
    qu = []
    visit = set()

    qu.append(start)
    visit.add(start)

    while qu:
        node = qu.pop(0)
        v = node[-1] #큐에 저장된 이동 경로의 마지막 문자가 현재 처리해야 할 꼭짓점
        if v == end: # 종료 조건: 지금 검사하는 꼭짓점이 목적지라면? 종료
            return node #지금까지 전체 이동 경로를 돌려주고 종료
        for x in g[v]: # 대상 꼭짓점에 연결된 꼭짓점들 중에
            if x not in visit: # 아직 방문하지 않은 꼭짓점을
                qu.append(node + x) # 이동 경로에 새꼭짓점으로 큐에 저장
                #print('node: ', node, ' x:', x)
                visit.add(x)
    return "?"

maze = {
    'a': ['e'],
    'b': ['c', 'f'],
    'c': ['b', 'd'],
    'd': ['c'],
    'e': ['a', 'i'],
    'f': ['b', 'g', 'j'],
    'g': ['f', 'h'],
    'h': ['g', 'l'],
    'i': ['e', 'm'],
    'j': ['f', 'k', 'n'],
    'k': ['j', 'o'],
    'l': ['h', 'p'],
    'm': ['i', 'n'],
    'n': ['m', 'j'],
    'o': ['k'],
    'p': ['l'],
}

print(solve_maze(maze, 'a', 'p'))