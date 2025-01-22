"! [BuildStatus] (https://github.com/gkim9/HW2-BFS/actions/workflows/test.yml/badge.svg?event=push)"

# BMI203 HW 2
Breadth-first search

# Breadth-First Search
Breadth-first search (bfs) is a graph traversal algorithm. It can be used to find the shortest path between two nodes for unweighted graphs.

As the name suggests, bfs will start at a given source and explore the graph with the nodes directly connected to the source first. It progressively expands through the layers/depth levels, exploring all nodes in each layer before continuing. To achieve this, bfs uses "First In First Out" queue to add neighboring nodes and decide which node to "visit". The specific implementation is detailed below.

# Implementation
This repo contains a module named "search" that contains the main script "graph.py", implementing three main functions:
* solve_bfs(start)
	* Solve input graph from a given start (Pseudcode provided below)
		* Initialize all data structures:
			* Queue is initialized with the source node
			* Initialize an empty visited list (to keep track of the order of visits)
			* Initialize a dictionary that keeps track of each node's "parent"/"predecessor" {node: parent_node (or None if parent does not exist in the traversal) for all nodes in graph}
		* While the queue contains at least one node, "visit" the first node that was added, remove it from queue, and add to visited list
		* Find neighbor(s) of the node currently visiting and add to end of queue if they neighbors have not been visited yet
		* For all the neighbors not yet visited, update the parent node to the node we are currently visiting
	* Builds and returns list of nodes visited in order
	* Builds and returns dictionary of each node's predecessor (will be used by a different function to reconstruct shortest path)
* neighbors(node)
	* Finds and returns the neighbors of a given node so that it can be added to the queue within solve_bfs function
* bfs(start, end=None)
	* Return nodes in order of breadth-first search traversal from the given start node if end = None
	* Return shortest path from start -> end if path exists
		* This function will handle the retrieval of the shortest path
	* Return None if path from start -> end does not exist