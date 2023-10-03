import collections

def bfs(graph , root):
    
    visited = set()
    queue = collections.deque([root])

    while queue:

        vertex = queue.popleft()
        visited.add(vertex)

        for i in graph[vertex]:

            if i not in visited:
                queue.append(i)
    print(visited)


graph = {
    5 : [3 , 7],
    3 : [2 , 4],
    7 : [8],
    2 : [],
    4 : [8],
    8 : []
}

print( bfs( graph , 5 ) )