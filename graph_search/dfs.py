def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
visited = [False] * 9 # 노드 개수보다 하나 더 많게 해서 1, 2, 3... 순서로

dfs(graph, 1, visited)