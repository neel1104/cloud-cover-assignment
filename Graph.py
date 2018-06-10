from collections import defaultdict
import heapq


class Graph:
    ''' data structure to store weighted directed graph in the form of 
        adjecency list
    '''
    def __init__(self):        
        self.edges = defaultdict(list)
        self.distances = {}

    def add_edge(self, from_node, to_node, distance):
        "adds weighted directed edges to the graph"
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance


    def dijkstra(self, start, end):
        ''' Returns min distance if there exists a shortest path 
            from start to end; Otherwise, return None '''

        if start == end:
            return float(0)
        Q = []  # priority queue of items; note item is mutable.
        d = {start: 0}  # vertex -> minimal distance
        Qd = {}  # vertex -> [d[v], parent_v, v]
        previous = {}  # previous vertex 
        visited_set = set([start])

        adj = self.edges   # adjecency list
        distances = self.distances   # distances or costs

        # initialize for the starting vertex
        for neighbour in adj.get(start, []):
            distance = distances[start, neighbour]
            item = [distance, start, neighbour]
            d[neighbour] = distance
            heapq.heappush(Q, item)
            Qd[neighbour] = item
            
        while Q:
            distance, parent, cur = heapq.heappop(Q)
            if cur not in visited_set:  # for vertices not visited
                previous[cur] = parent
                visited_set.add(cur)
                if cur == end:  # found destination
                    return d[cur]
                for v in adj.get(cur, []):
                    if d.get(v):
                        if d[v] > distances[cur, v] + d[cur]:
                            d[v] = distances[cur, v] + d[cur]
                            Qd[v][0] = d[v]  # decrease key
                            Qd[v][1] = cur  # update previous
                            heapq._siftdown(Q, 0, Q.index(Qd[v]))
                    else:
                        d[v] = distances[cur, v] + d[cur]
                        item = [d[v], cur, v]
                        heapq.heappush(Q, item)
                        Qd[v] = item

        return None
