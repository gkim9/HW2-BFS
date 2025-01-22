import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")
    
    def print_graph(self):
        # needed to figure out what nx.read_adjlist did so added a print function
        return self.graph

    def neighbors(self, node):
        # with input of the graph and node, return a list of neighbors (directed for that node)
        # node is cited by the items in the list returned
        return [neighbor for neighbor in self.graph[node]]
    
    def solve_bfs(self, start):
        '''
        'Solving' the graph by getting the "parent" of each node
        (not getting the shortest path from start -> end)
        '''
        prev_node = {} # will contain key, val pair of {node: parent node} for all nodes
        node_list = [] # all nodes
        for node in self.graph:
            prev_node[node] = None # initializing dictionary, the start node should have None
            node_list.append(node)
        print(len(node_list))
        if start not in node_list:
            raise Exception("Either start or end nodes are not found in the graph")

        # based on the pseudocode given in class, added the tracking of the previous/parental node
        Q = []
        visited = []
        Q.append(start)
        visited.append(start)

        while Q != []:
            node = Q.pop(0)
            N_list = self.neighbors(node)
            for neighbor in N_list:
                if neighbor not in visited:
                    visited.append(neighbor)
                    # print(visited)
                    Q.append(neighbor)
                    prev_node[neighbor] = node
        return visited, prev_node

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        Things to raise exception for: if start/end nodes are not in graph

        Will call the solve_bfs function that solves the graph with a given start node
        "BFS" function will determine what outputs to give depending on start/end nodes & compile shortest path if it exists
        """
        visited, prev_node = self.solve_bfs(start)
        shortest_path = []
        input_end = end
        # if no end, just return the "graph" which is the list of the previous node in reference to a specific start
        if end == None:
            return visited
        while end != start:
            shortest_path.append(end)
            end = prev_node[end] # update new end to go up the chain of "parental" nodes until you hit the start
            if end == None: # No path from the start to end node (since it is guaranteed that if the path exists, it'll be less than the path through all nodes)
                return None
        shortest_path.append(end)
       
        return shortest_path[::-1] # since appended from end -> start, reversing order