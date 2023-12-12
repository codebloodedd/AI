import copy
visited_states = []

def getNeighbor(currState, goal, prevH):
    global visited_states
    state = copy.deepcopy(currState)
    for i in range(len(state)):
        temp = copy.deepcopy(state)
        if len(temp[i]) > 0:
            elem = temp[i].pop()
            for j in range(len(temp)):
                temp1 = copy.deepcopy(temp)
                if j != i:
                    temp1[j] = temp1[j] + [elem]
                    currH = heuristic(temp1, goal)
                    if currH > prevH:
                        child = copy.deepcopy(temp1)
                        return child
    return 0

def heuristic(currState, goal):
    val = 0
    RealGoal = goal[3]
    for i in range(len(currState)):
        if len(currState[i])>0:
            check = currState[i]
            for j in range(len(currState[i])):
                if currState[i][j] != RealGoal[j]:
                    val -= j
                else:
                    val += j
    return val



def sln(initial, goal):
    global visited_states
    if (initial == goal):
        print(goal)
        print("Solution Found")
        return
    
    currState = copy.deepcopy(initial)
    while True: 
        visited_states.append(copy.deepcopy(currState))
        print(currState)
        prevH = heuristic(currState, goal)
        child = getNeighbor(currState, goal, prevH)
        if child == 0:
            print("Final State - ")
            print(currState)
            return
        
        currState = copy.deepcopy(child)


def main():
    global visited_states
    initial = [[],[],[],['B','C','D','A']]
    goal = [[],[],[],['A','B','C','D']]
    sln(initial,goal)

main()