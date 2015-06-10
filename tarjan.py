# downloaded from http://www.logarithmic.net/pfh/blog/01208083168

def strongly_connected_components(graph):

    index_counter = [0]
    stack = []
    lowlink = {}
    index = {}
    result = []
    
    def strongconnect(node):
        index[node] = index_counter[0]
        lowlink[node] = index_counter[0]
        index_counter[0] += 1
        stack.append(node)
    
        successors = graph[node]
        for successor in successors:
            if successor not in index:
                strongconnect(successor)
                lowlink[node] = min(lowlink[node],lowlink[successor])
            elif successor in stack:
                lowlink[node] = min(lowlink[node],index[successor])

        if lowlink[node] == index[node]:
            connected_component = []

            while True:
                successor = stack.pop()
                connected_component.append(successor)
                if successor == node: break
            component = tuple(connected_component)
            result.append(component)
    
    for node in graph:
        if node not in index:
            strongconnect(node)
    
    return result

