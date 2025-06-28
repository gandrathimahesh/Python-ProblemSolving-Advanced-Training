#GRAPHS

# undirected graph

""" graphs=((5,2),(5,7),(5,8),(2,7),(2,8),(8,7),(8,3),(2,3))
d={}
for i,j in graphs:
    if i not in d:
        d[i]=[j]
    else:
        d[i].append(j)
    if j not in d:
        d[j]=[i]
    else:
        d[j].append(i)
print(d)
 """
#Directed graph

""" graphs=((5,2),(5,7),(5,8),(2,7),(2,8),(8,7),(8,3),(2,3))
d={}
for i,j in graphs:
    if i not in d:
        d[i]=[j]
    else:
        d[i].append(j)
print(d) """

#print all the paths


from collections import defaultdict
def print_all_parts(u,v,path=[]):
    path.append(u)
    if (u==v):
        print(path)
        path.pop()
        return
    for i in d[u]:
        if i not in path:
            print_all_parts(i,v,path)
    path.pop()
    return
graph=((5,2),(5,7),(5,8),(2,7),(2,8),(8,7),(8,3),(2,3))
d=defaultdict(list)
for i,j in graph:
    d[i].append(j)
    d[j].append(i)
print_all_parts(5,3)
 



#give path is exit or not
'''
from collections import defaultdict

def path_exists(u, v, path=[]):
    path.append(u)
    if u == v:
        return True
    for i in d[u]:
        if i not in path:
            if path_exists(i, v, path):
                return True
    path.pop()
    return False

graph = ((5,2),(5,7),(5,8),(2,7),(2,8),(8,7),(8,3),(2,3))
d = defaultdict(list)
for i,j in graph:
    d[i].append(j)
    d[j].append(i)

# Example: Check if path from 5 to 3 exists'

found = path_exists(5, 3)
print("Path exists:", found)'''


#shortest path
'''
from collections import defaultdict, deque

def shortest_path(u, v):
    visited = set()
    queue = deque([[u]])  # queue stores paths

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == v:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in d[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return None  # if no path exists

# Graph
graph = ((5,2),(5,7),(5,8),(2,7),(2,8),(8,7),(8,3),(2,3))
d = defaultdict(list)
for i, j in graph:
    d[i].append(j)
    d[j].append(i)

# Find shortest path from 5 to 3
print("Shortest path:", shortest_path(5, 3))'''

#shortest sum

'''from collections import defaultdict, deque

def sum_of_shortest_path(u, v):
    visited = set()
    queue = deque([[u]])  # store paths as lists

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == v:
            print("Shortest path:", path)
            return sum(path)

        if node not in visited:
            visited.add(node)
            for neighbor in d[node]:
                if neighbor not in path:  # avoid cycles
                    new_path = path + [neighbor]
                    queue.append(new_path)
    return -1  # no path found

# Graph
graph = ((5,2),(5,7),(5,8),(2,7),(2,8),(8,7),(8,3),(2,3))
d = defaultdict(list)
for i, j in graph:
    d[i].append(j)
    d[j].append(i)

# Example: sum of shortest path from 5 to 3
print("Sum of shortest path:", sum_of_shortest_path(5, 3))'''


