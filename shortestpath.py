'''
Constructs the shortest path from a designated starting vertex to all other vertices in the graph using Dijkstra's Algorithm.
This algorithm will work with either a directed or undirected graph.
@date - Dec 2017.
@author: Diwas Poudel
'''
import sys
import heapq
from _heapq import heappop

def main(inputFile, startingVertex, lastVertex):
    '''
    input file containing directed-graph with positive weights
    file contents are [begin vertex] [end vertex] [cost]
    '''
    graph = open(inputFile)

    '''
    an initially empty dictionary containing mapping
    [vertex]:[adjacency list]
    '''
    adjacency = { }

    # priority queue
    heap = [ ]

    # collection of vertices
    vertices = [ ]

    '''
    shortest path graph
    Each dictionary entry contains mapping of [vertex]:(cost,previous vertex)
    '''
    path = { }
    
    result = { }

    '''
    The following reads in the input file
    and constructs an adjacency list of
    the graph.
    '''
    for line in graph:
        entry = line.split()

        # get the vertices
        vertices.append(entry[0])
        vertices.append(entry[1])

        if entry[0] not in adjacency:
            adjacency[entry[0]] = []

        # construct an edge for the adjacency list
        edge = (entry[1], int(entry[2]))
        adjacency[entry[0]].append(edge)

    # construct the set of unknown vertices
    unVisited = set(vertices)

    if startingVertex not in unVisited:
        print 'Starting vertex', startingVertex, 'not present in graph', graph
        quit()

    # initialize path and heap
    
    path[startingVertex] = [0, None]
    heapq.heappush(heap, [0, startingVertex])
    
    while heap:
        current = heapq.heappop(heap)
        unVisited.remove(current[1])
        parent = current
        
        if current[1] in adjacency.keys():
            for i in range(0, len(adjacency[current[1]])):
                if current[0] + adjacency[current[1]][i][1] < lookupDistance(heap,adjacency[current[1]][i][0]):
                    heapupdate(heap, [current[0] + adjacency[current[1]][i][1], adjacency[current[1]][i][0]])
                elif adjacency[current[1]][i][0] in unVisited and not inheap(heap, adjacency[current[1]][i][0]):
                    heapq.heappush(heap, [current[0] + adjacency[current[1]][i][1], adjacency[current[1]][i][0]])
                
                if adjacency[current[1]][i][0] not in path.keys():
                    path[adjacency[current[1]][i][0]] = [current[0] + adjacency[current[1]][i][1], parent[1]]
                elif current[0] + adjacency[current[1]][i][1] < path[adjacency[current[1]][i][0]][0]:
                    path[adjacency[current[1]][i][0]] = [current[0] + adjacency[current[1]][i][1], parent[1]]
    
    
    endVertex = lastVertex
    result = [ ]
    while endVertex != None:
        result.append(endVertex)
        endVertex = path[endVertex][1]
    result.reverse()
    
    print "The shortest cost from ", str(startingVertex), " to ", str(lastVertex), " is: ", path[lastVertex][0]
    print "The shortest path from ", str(startingVertex), " to ", str(lastVertex), " is: ", result    
       
def inheap(heap, node):
    for i in heap:
        if i[1] == node:
            return True

def lookupDistance(heap, node):
    for i in heap:
        if i[1] == node:
            return i[0]

# update distance of one node in the heap
def heapupdate(heap, node):
    d, vertex = node
    for i in range(len(heap)):
        if heap[i][1] == vertex:
            heap[i][0] = d
            break
    heapq.heapify(heap)

if __name__ == '__main__':

    if len(sys.argv) != 4:
        print 'Usage python lab11.py [input file] [starting vertex]'
        quit()

    main(sys.argv[1], sys.argv[2], sys.argv[3])
