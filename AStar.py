def neighbor(n):
    if n in graph:
        return graph[n]
    else:
        return None

def aStar(start, goal):
    opened = set(start)
    closed = set()
    g = {}
    parent = {}
    g[start] = 0
    parent[start] = start
    while len(opened)>0:
        n = None
        for v in opened:
            if n == None or g[n] + h(n) > g[v] + h(v):
                n = v
        
        if n == goal or graph[n] == None:
            pass
        else:
            for ( m , weight ) in neighbor(n):
                if m not in opened and n not in closed:
                    opened.add(m)
                    parent[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parent[m] = n
                        if m in closed:
                            closed.remove(m)
                            opened.add(m)
        if n == None:
            print("Path does not exist")
            return None
        
        if n == goal:
            path = []
            print(parent)
            while n != parent[n]:
                path.append(n)
                n = parent[n]
            path.append(start)
            path.reverse()
            print("Path Found")
            return path

        closed.add(n)
        opened.remove(n)
    
    print("Path not found")
    return None
                
def h(n):
    dist = {
        'A' : 11,
        'B' : 6,
        'C' : 99,
        'D' : 1,
        'E' : 7,
        'G' : 0
    }
    return dist[n]

graph = {
    'A' : [('B', 2), ('E', 3)],
    'B' : [('C', 1), ('G', 9)],
    'C' : [],
    'D' : [('G', 1)],
    'E' : [('D', 6)],
    'G' : []
}

path = aStar('A', 'G')
print(path)