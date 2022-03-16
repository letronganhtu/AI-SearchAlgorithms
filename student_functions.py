import numpy as np
import queue
import math

def BFS(matrix, start, end):
    """
    BFS algorithm:
    Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes, each key is a visited node,
        each value is the adjacent node visited before it.
    path: list
        Founded path
    """
    # TODO:

    frontier = queue.Queue(maxsize = 10000000)
    path = []
    visited = {}
    q = []
    haveSolution = False
    
    if start == end:
        visited.update({start: -1})
        path.append(start)
    elif start >= 0 and start < len(matrix):
        frontier.put({start: -1})
        q.append(start)

    while not frontier.empty() and not haveSolution:
        temp = frontier.get()
        visited.update(temp)
        first = next(iter(temp))
        for i in range(len(matrix)):
            if matrix[first][i] != 0 and i not in visited and i not in q and not haveSolution:
                if i == end:
                    path.append(end)
                    path.append(first)
                    haveSolution = True
                    break
                else: 
                    frontier.put({i: first})
                    q.append(i)
    
    if haveSolution:
        while path[len(path) - 1] != start:
            path.append(visited[path[len(path) - 1]])
        path.reverse()

    return visited, path

def DFS(matrix, start, end):
    """
    DFS algorithm
    Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited 
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """

    # TODO: 
    
    frontier = []
    path = [] 
    visited = {}
    stack = []
    haveSolution = False
    
    if start == end:
        visited.update({start: -1})
        path.append(start)
    elif start >= 0 and start < len(matrix):
        frontier.append({start: -1})
        stack.append(start)

    while len(frontier) != 0 and not haveSolution:
        temp = frontier.pop()
        visited.update(temp)
        first = next(iter(temp))
        for i in range(len(matrix)):
            if matrix[first][i] != 0 and i not in visited and i not in stack and not haveSolution:
                if i == end:
                    path.append(end)
                    path.append(first)
                    haveSolution = True
                    break
                else:
                    frontier.append({i: first})
                    stack.append(i)
    
    if haveSolution:
        while path[len(path) - 1] != start:
            path.append(visited[path[len(path) - 1]])
        path.reverse()

    return visited, path

def UCS(matrix, start, end):
    """
    Uniform Cost Search algorithm
    Parameters:visited
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO:

    frontier = queue.PriorityQueue()
    path = []
    visited = {}
    parent = []
    k = len(matrix)
    while k: 
        parent.append(-1)
        k -= 1

    if start == end:
        path.append(start)
        visited.update({start: -1})
    elif start >= 0 and start < len(matrix):
        frontier.put([0, start])
    
    while not frontier.empty():
        temp = frontier.get()
        if temp[1] in visited: continue
        visited.update({temp[1]: parent[temp[1]]})
        if temp[1] == end:
            path.append(end)
            path.append(parent[end])
            break
        for i in range(len(matrix)):
            if matrix[temp[1]][i] != 0 and i not in visited:
                if parent[i] == -1:
                    parent[i] = temp[1]
                    frontier.put([temp[0] + matrix[temp[1]][i], i])
                else:
                    cost = temp[0] + matrix[temp[1]][i]
                    for j in range(len(frontier.queue)):
                        if frontier.queue[j][1] == i: break
                    if cost < frontier.queue[j][0]:
                        frontier.put([cost, i])
                        parent[i] = temp[1]

    if len(path) != 0:
        while path[len(path) - 1] != start:
            path.append(visited[path[len(path) - 1]])
        path.reverse()

    return visited, path

def GBFS(matrix, start, end):
    """
    Greedy Best First Search algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
   
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO:

    path = []
    visited = {}
    h = []
    frontier = queue.PriorityQueue()
    parent = []
    k = len(matrix)
    while k:
        parent.append(-1)
        h.append(-1)
        k -= 1

    if start == end:
        path.append(start)
        visited.update({start: -1})
    elif start >= 0 and start < len(matrix):
        frontier.put([h[start], start])

    while not frontier.empty():
        temp = frontier.get()
        if temp[1] in visited: continue
        visited.update({temp[1]: parent[temp[1]]})
        if temp[1] == end:
            path.append(end)
            path.append(parent[end])
            break
        for i in range(len(matrix)):
            if matrix[temp[1]][i] != 0 and i not in visited and (parent[i] == -1 or h[i] > matrix[temp[1]][i]):
                parent[i] = temp[1]
                h[i] = matrix[temp[1]][i]
                frontier.put([h[i], i])

    if len(path) != 0:
        while path[len(path) - 1] != start:
            path.append(visited[path[len(path) - 1]])
        path.reverse()

    return visited, path

def Astar(matrix, start, end, pos):
    """
    A* Search algorithm
     Parameters:
    ---------------------------
    matrix: np array UCS
        The graph's adjacency matrix
    start: integer 
        starting node
    end: integer
        ending node
    pos: dictionary. keys are nodes, values are positions
        positions of graph nodes
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO:

    path = []
    visited = {}
    frontier = queue.PriorityQueue()
    parent = []
    k = len(matrix)
    while k:
        parent.append(-1)
        k -= 1
    h = []
    for i in range(len(matrix)):
        temp = math.sqrt(math.pow(pos[i][0] - pos[end][0], 2) + math.pow(pos[i][1] - pos[end][1], 2))
        h.append(temp)
    
    if start == end:
        path.append(start)
        visited.update({start: -1})
    elif start >= 0 and start < len(matrix):
        frontier.put([h[start], start])

    while not frontier.empty():
        temp = frontier.get()
        visited.update({temp[1]: parent[temp[1]]})
        if temp[1] == end:
            path.append(end)
            path.append(parent[temp[1]])
            break
        for i in range(len(matrix)):
            if matrix[temp[1]][i] != 0 and i not in visited:
                if parent[i] == -1:
                    parent[i] = temp[1]
                    frontier.put([temp[0] - h[temp[1]] + matrix[temp[1]][i] + h[i], i])
                else:
                    cost = temp[0] - h[temp[1]] + matrix[temp[1]][i] + h[i]
                    for j in range(len(frontier.queue)):
                        if frontier.queue[j][1] == i: break
                    if cost < frontier.queue[j][0]:
                        frontier.put([cost, i])
                        parent[i] = temp[1]

    if len(path) != 0:
        while path[len(path) - 1] != start:
            path.append(visited[path[len(path) - 1]])
        path.reverse()

    return visited, path