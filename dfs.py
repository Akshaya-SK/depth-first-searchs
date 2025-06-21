# DFS using adjacency list and recursion

def dfs(graph, start, visited):
    if start not in visited:
        visited.append(start)
        for neighbor in graph[start]:
            dfs(graph, neighbor, visited)

def main():
    n, e = map(int, input("Enter number of nodes and edges: ").split())
    graph = {}

    print("Enter the edges (one per line):")
    for _ in range(e):
        u, v = input().split()
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)  # Undirected graph

    for node in graph:
        graph[node].sort()

    start_node = input("Enter the start node: ")
    visited = []
    dfs(graph, start_node, visited)

    print("DFS Traversal Output:")
    print(visited)

main()
