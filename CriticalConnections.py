# Critical Connections



def criticalConnections(n, connections):
    
    graph = {
                'Vertices' : [i for i in range(n)],
                'Edges': {

                         }
            }

    #connections=  [[1,2],[2,0],[1,3]]

    for src,dest in connections:
        if src not in graph['Edges']:
            graph['Edges'][src] = [dest]
        else:
            if dest not in graph['Edges'][src]:
                graph['Edges'][src].append(dest)
        
        if dest not in graph['Edges']:
            graph['Edges'][dest] = [src]
        else:
            if src not in graph['Edges'][dest]:
                graph['Edges'][dest].append(src)

    # print(graph['Edges'])


    vertices = graph['Vertices']
    print(vertices)
    edges = graph['Edges']
    visited = set()
    cycle = set()
    cycleList = []
    Ncycles = 0
    critical_connections = set()

    for vertex in vertices:
        queue = [vertex]
        while queue:
            vert = queue.pop(0)
            if vert not in visited:
                vert_edges = edges[vert]
                formsCycle = []
                #if any-neighbor of the-current-node is in visited-set AND also in queue, then there is a cycle
                print('visited: ', visited)
                print('queue: ',queue)
                print('vert: ',vert, 'vertedges: ', vert_edges)
                print('edges n visited: ',set(vert_edges).intersection(visited))
                print('edges n queue: ', set(vert_edges).intersection(set(queue)))
                if len(set(vert_edges).intersection(visited)) > 0 and len(set(vert_edges).intersection(set(queue))) > 0:
                    #There is a cycle
                    #Now function for what forms the cycle - the neighbor and the children
                    for each in set(vert_edges).intersection(visited):
                        formsCycle.append(each)
                        #formsCycle.extend(edges[each])
                    for each in set(vert_edges).intersection(set(queue)):
                        formsCycle.append(each)
                        #formsCycle.extend(edges[each])

                    formsCycle = set(formsCycle)
                    print('forms Cycle: ', formsCycle)
                    cycle = cycle.union(formsCycle)
                    if len(cycle) >= 3:
                        Ncycles += 1
                        cycleList.append(cycle)
                        print('cycleSoFar: ',cycle)
                        print('N. cycles: ',Ncycles)
                        print('cycleList: ', cycleList)
                        cycle = set()
                        
                        
                
                visited.add(vert)
                queue.extend(vert_edges)
                print('visited: ', visited)
                print('queue: ',queue)

                print('\n')

    criticalNodes = set(vertices)-cycle
    print('nodes with cycle: ',cycle)
    print('nodes without cycle: ',criticalNodes)
    print('Nycles: ',Ncycles)
    print('cycleList: ', cycleList)

    for node in criticalNodes:
        for each in edges[node]:
            critical_connections.add((min(node,each),max(node,each)))

    critical_connections = list(critical_connections)
    critical_connections = [[x,y] for x,y in critical_connections]
    return critical_connections




# n = 4
# connections=  [[0,1],[1,2],[2,0],[1,3]]

# n = 6
# connections = [[0,1],[0,2],[1,2],[1,3],[3,4],[3,5],[4,5]]

n = 9
connections = [[0,1],[0,2],[1,2],[1,3],[3,4],[3,5],[4,6],[6,7],[6,8]]

print(criticalConnections(n,connections))