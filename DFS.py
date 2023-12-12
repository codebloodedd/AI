graph = {
's' : ['a', 'b', 'c'],
'a' : ['s', 'b', 'd'],
'b' : ['s', 'a', 'd'],
'c' : ['s', 'g'],
'd' : ['a', 'b', 'e'],
'e' : ['d', 'g'],
'g' : ['c', 'e']
}

closed = []
opened = []

def DFS(closed, graph, start, opened, goal):
    node = start
    while node != goal:
        closed.append(node)
        temp = []
        child = graph[node]
        for n in child:
            if n not in opened and n not in closed:
                temp.append(n)
        opened = temp + opened
        node = opened.pop(0)
    
    if node == 'g':
        print(f"The goal node {node} has been found")
    closed.append(node)
    return opened, closed

opened, closed = DFS(closed, graph, "s", opened, "g")
print('\nThe opened list is - ')
for element in opened:
    print(element, end = ' ')
print('\nThe closed list is - ')
for element in closed:
    print(element, end = ' ')