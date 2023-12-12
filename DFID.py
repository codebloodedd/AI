graph = {
    'A': ['B', 'C'],
    'B': ['D','E'],
    "C": ['G'],
    'D': [],
    'E': ['F'],
    'G': [],
    'F':[]
}

path = list()

# def DFS(currNode, goal, graph, max, currList):
#     print(f"Checking - {currNode}")
#     currList.append(currNode)
#     if currNode == goal:
#         return True
#     if max<= 0:
#         path.append(currList)
#         return False
#     for node in graph[currNode]:
#         if DFS(node, goal, graph, max-1, currList):
#             return True
#         else:
#             currList.pop()
#     return False

# def DFID(currNode, goal, graph, max):
#     for i in range(max):
#         currList = list()
#         if DFS(currNode, goal, graph, i, currList):
#             return True
#     return False


def DFS(currNode, goal, graph, max, currList):
    print(f"Checking: {currNode}")
    currList.append(currNode)
    if currNode == goal: 
        return True
    if max<= 0:
        path.append(currList)
        return False
    for node in graph[currNode]:
        if DFS(node, goal, graph, max-1, currList):
            return True
        else:
            currList.pop()
    return False

def DFID(currNode, goal, graph, max):
    for i in range(max):
        currList = list()
        if DFS(currNode, goal, graph, i, currList):
            return True
    return False

if not DFID("A", "G", graph, 4):
    print("No Path Found")
else:
    print(f"Path found : {path.pop()}")