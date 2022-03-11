# graph = [[] for _ in range(n)] 이차원 리스트 표현
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    num, ber = map(int, input().split())
    # 양방향으로 연결
    graph[num].append(ber)
    graph[ber].append(num)

# graph 내부 리스트 정렬
for adjacent in graph:
    adjacent.sort()

visited = [False] * (n+1)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

from collections import deque
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(graph, v, visited)
visited = [False] * (n+1)
print()
bfs(graph, v, visited)
