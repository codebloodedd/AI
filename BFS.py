graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}
 
visited = []
queue = []
path = []
closeList = []
parent = {}

def bfs(visited, graph, node, goal):
    parent[node] = None
    visited.append(node)
    queue.append(node)
    m = ""
    while m != goal:
        m = queue.pop(0)
        closeList.append(m)
        print(f"Open List: {queue}\nClosed list: {visited}")
        
        for n in graph[m]:
            if n not in visited:
                visited.append(n)
                queue.append(n)
                parent[n] = m
    
    print(parent)
    i = goal
    while i is not None:
        path.append(i)
        i = parent[i]
    path.reverse()
    print(f"Path: {path}")

bfs(visited, graph, "5", "8")