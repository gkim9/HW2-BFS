# write tests for bfs
import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # copied from last week's to allow local testing
from search import graph
import networkx as nx

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    #should raise an exception with empty graph input
    empty_network = graph.Graph('data/empty_network.adjlist')
    with pytest.raises(Exception):
        empty_network.bfs('Start')

    # testing with tiny_network
    tiny_network = graph.Graph('data/tiny_network.adjlist')

    # total number of visited nodes should equal total number of nodes of tiny_network (30)
    assert len(tiny_network.bfs("Luke Gilbert")) == 30, "Wrong number of nodes and/or edges"

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    # testing graph with 1->7 path but no 7->1 path
    no_connected_network = graph.Graph('data/no_connected_node_test.adjlist')
    assert no_connected_network.bfs("1") == ['1', '2', '3', '4', '5', '6', '7'], "Did not traverse graph in correct order"
    assert no_connected_network.bfs("1", "7") == ['1', '2', '3', '4', '5', '6', '7'], "Did not traverse graph in correct order"
    assert no_connected_network.bfs("7", "1") is None #no path should exist from 7 -> 1
    
    network = graph.Graph('data/citation_network.adjlist')
    assert network.bfs("Luke Gilbert", "34858697") is None, "BFS did not work correctly--> expected no path"

    # Using the networkx package to get "ground truth" of shortest path to compare our code

    actual_shortest = nx.shortest_path(network.graph, "Luke Gilbert", "Lani Wu")
    our_shortest = network.bfs("Luke Gilbert", "Lani Wu")
    assert actual_shortest == our_shortest, "Incorrect shortest path"

    different_source = network.bfs("Tony Capra", "Luke Gilbert")
    assert actual_shortest != different_source, "Path not calculated correctly"