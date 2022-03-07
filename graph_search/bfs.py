from collections import deque

graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
visited = [False] * 9

def bfs(graph, start, visited):
    # deque는 안에 리스트 필요
    queue = deque([start])
    visited[start] = True
    
    # popleft()를 반복해서 queue가 비면 종료
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph, 1, visited)