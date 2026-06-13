graph = {
    1: [2,3],
    2: [4],
    3: [5],
    4: [],
    5: []
}

visited = set()

def dfs(node):
    if node in visited:
        return

    visited.add(node)

    print(node)

    for nxt in graph[node]:
        dfs(nxt)

dfs(1)
