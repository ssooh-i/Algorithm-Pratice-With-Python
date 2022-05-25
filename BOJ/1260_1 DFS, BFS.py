from queue import Queue

class Node:
    def __init__(self, value): #초기화
        self.value = value
        self.edges = [] #간선들을 저장할 공간

    def addEdge(self, next): #다음으로 갈 곳 추가
        self.edges.append(next)

def dfs(now): #지금있는 위치를 받아옴
    print(now, end=" ")
    for next in nodes[now].edges:
        if visited[next] is False: #방문했는지 여부가 false면 실행
            visited[next] = True #방문했으니 True로 바뀌줌
            dfs(next) #next 인자를 함수로 보냄/재귀

#main
N, M, V = map(int, input().split())
nodes = [Node(i) for i in range(0, N+1)] #노드의 개수를 받아서 n개 노드 초기화
visited = [False for _ in range(0, N+1)] #방문 여부를 알려주기 위함, n개의 노드를 방문하기 때문에 n개가 있어야함

for _ in range(M): #간선 추가 할 곳
    _from, _to = map(int, input().split())
    nodes[_from].addEdge(_to) #양방향이라서 반대로도 추가함
    nodes[_to].addEdge(_from)

for now in range(1, N+1):
    nodes[now].edges.sort() #정점 번호가 작은 것부터 먼저 방문하기 때문에 정렬

visited[V] = True #탐색할 번호 V가 True면
dfs(V)
print()

visited = [False for _ in range(0, N+1)]
q = Queue()
q.put(V) #put은 값을 넣는거(push), get은 pop(꺼내고 삭제)
visited[V] = True #처음 시작할 때부터 True로 바꿔줌, 1부터 시작하니까
while q.empty() is False: #q가 비어있지 않다면 실행하자
    now = q.get() #지금 노드를 꺼내서 출력
    print(now, end =" ")
    for next in nodes[now].edges: #nodes[now].edges에 다음이 있는지 확인
        if visited[next] is False: #다음이 없다면
            visited[next] = True
            q.put(next)