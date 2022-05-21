class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []

    def addEdge(self, next):
        self.edges.append(next)

n = int(input())
m = int(input())
nodes = [Node(i) for i in range(0, n+1)]
v = 1
for _ in range(m):
    _from, _to = map(int, input().split())
    nodes[_from].addEdge(_to)
    nodes[_to].addEdge(_from)

visited = [0 for i in range(n)] #false로 안하고 0으로 한 이유는 다하고 나서 sum할꺼라서


def dfs(v):
    visited[v] = 1 #방문하면 1로 바꾸기
    for i in range(n+1):
        if nodes[i][v] == 1 and visited[i] == 0:
            dfs(i)
            #print(dfs(i))
        #print(nodes[i][v],end=" ")

dfs(1) #1번 컴퓨터에 연결된 것만 찾음

print(sum(visited)-1) #몇개인지 세고 시작점인 노드 1번을 삭제한 개수가 정답