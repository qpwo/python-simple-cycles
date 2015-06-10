# Luke Miles, January 2015
# FINDING ALL THE ELEMENTARY CIRCUITS OF A DIRECTED GRAPH DONALD B. JOHNSON
from collections import defaultdict
from tarjan import strongly_connected_components as SCC
from itertools import chain

def grab_cycles(graph): # expects graph to be strongly connected
    cycles = set()
    blocked = defaultdict(bool)
    B = defaultdict(list)
    stack = []

    def find_cycles(v, s):
        f = False
        stack.append(v)
        blocked[v] = True
        for w in graph[v]:
            if w == s:
                cycles.add(tuple(stack))
                f = True
            elif not blocked[w]:
                if find_cycles(w, s):
                    f = True
        if f:
            unblock(v)
        else:
            for w in graph[v]:
                if v not in B[w]:
                    B[w].append(v)
        stack.remove(v)
        return f

    def unblock(node):
        blocked[node] = False
        Bnode = B[node]
        while Bnode:
            w = Bnode.pop(0)
            if blocked[w]:
                unblock(w)

    start = min(graph) # arbitrary
    find_cycles(start, start)
    return tuple(cycles)

def get_subgraph(graph, vertices):
    #returns subgraph induced by vertices
    return {vert : {child
                    for child in graph[vert]
                    if child in vertices}
            for vert in vertices}

def get_elementary_cycles(graph):
    #returns all elementary cycles in a graph
    return tuple(chain.from_iterable(
                     grab_cycles(get_subgraph(graph, scc))
                     for scc in SCC(graph)))
