def bfs(g, start):
    qu = []
    v = set()

    qu.append(start)
    v.add(start)

    while qu:
        q = qu.pop(0)
        print(q)
        for x in g[q]:  # 대상 꼭짓점에 연결된 꼭짓점 중에
            if x not in v:  # 아직 집합에 추가된 적없는 꼭짓점을
                qu.append(x)  # 큐에 추가하고
                v.add(q)  # 집합에도 추가


number_list = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}

bfs(number_list, 1)
