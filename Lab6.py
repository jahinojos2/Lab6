from Graphs import Vertex, Graph
from Edges import EdgeWeight, VertexSetCollection
import heapq
import time

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 19:27:26 2018
@author: jaimeahinojos
"""

def get_incoming_edge_count(list, vertex):
    count = 0
    for (vertex_first, vertex_last) in list:
        if vertex_last is vertex:
            count = count + 1
    return count


def topological_sort(graph):
    result_list = []

    no_incoming = []
    for vertex in graph.adjacency_list.keys():
        if get_incoming_edge_count(graph.edge_weights.keys(), vertex) == 0:
            no_incoming.append(vertex)

    remaining_edges = set(graph.edge_weights.keys())
    while len(no_incoming) != 0:

        current_vertex = no_incoming.pop()
        result_list.append(current_vertex)
        outgoing_edges = []

        for to_vertex in graph.adjacency_list[current_vertex]:
            outgoing_edge = (current_vertex, to_vertex)
            if outgoing_edge in remaining_edges:
                outgoing_edges.append(outgoing_edge)
                remaining_edges.remove(outgoing_edge)

        for (from_vertex, to_vertex) in outgoing_edges:
            in_count = get_incoming_edge_count(remaining_edges, to_vertex)
            if in_count == 0:
                no_incoming.append(to_vertex)

    return result_list

def minimum_spanning_tree(graph):

    edge_list = []
    for edge in graph.edge_weights:
        edge_weight = EdgeWeight(edge[0], edge[1], graph.edge_weights[edge])
        edge_list.append(edge_weight)
    heapq.heapify(edge_list)


    vertex_sets = VertexSetCollection(graph.adjacency_list)

    result_list = []

    while len(vertex_sets) > 1 and len(edge_list) > 0:

        next_edge = heapq.heappop(edge_list)

        set1 = vertex_sets.get_set(next_edge.from_vertex)

        set2 = vertex_sets.get_set(next_edge.to_vertex)

        if set1 is not set2:

            result_list.append(next_edge)

            vertex_sets.merge(set1, set2)
    return result_list



g = Graph()

vertex_A = Vertex('New York')
vertex_B = Vertex('Atlanta')
vertex_C = Vertex('Philadelphia')
vertex_D = Vertex('Chicago')
vertex_E = Vertex('Venice')
vertex_F = Vertex('Italy')
vertex_G = Vertex('Moscow')
vertex_H = Vertex('Barcelona')
vertex_I = Vertex('Madrid')
vertex_J = Vertex('Vienna')

g.add_vertex(vertex_A)
g.add_vertex(vertex_B)
g.add_vertex(vertex_C)
g.add_vertex(vertex_D)
g.add_vertex(vertex_E)
g.add_vertex(vertex_F)
g.add_vertex(vertex_G)
g.add_vertex(vertex_H)
g.add_vertex(vertex_I)
g.add_vertex(vertex_J)


g.add_directed_edge(vertex_A, vertex_B)
g.add_directed_edge(vertex_A, vertex_D)
g.add_directed_edge(vertex_B, vertex_F)
g.add_directed_edge(vertex_C, vertex_A)
g.add_directed_edge(vertex_D, vertex_F)
g.add_directed_edge(vertex_E, vertex_I)
g.add_directed_edge(vertex_E, vertex_G)
g.add_directed_edge(vertex_F, vertex_J)
g.add_directed_edge(vertex_H, vertex_I)
g.add_directed_edge(vertex_I, vertex_G)
g.add_directed_edge(vertex_J, vertex_B)

start_time = time.time()
result_list = topological_sort(g)
print('Time to Topological Sort: ')
print("--- %s seconds ---" % (time.time() - start_time))
print
    # display sorted list
first = True
for vertex in result_list:
    if first:
        first = False
    else:
        print(vertex.label)
print
# Main program 1
graph1 = Graph()

# Add vertices A through H
vertex_names = ["New York", "Atlanta", "Philadelphia", "Chicago", "Italy", "Madrid", "Barcelona", "Vienna", "Moscow", "Venice"]
for vertex_name in vertex_names:
    graph1.add_vertex(Vertex(vertex_name))

# Add edges
graph1.add_undirected_edge(graph1.get_vertex("New York"), graph1.get_vertex("Atlanta"), 351)
graph1.add_undirected_edge(graph1.get_vertex("New York"), graph1.get_vertex("Chicago"), 231)
graph1.add_undirected_edge(graph1.get_vertex("Atlanta"), graph1.get_vertex("Philadelphia"), 436)
graph1.add_undirected_edge(graph1.get_vertex("Atlanta"), graph1.get_vertex("Chicago"), 398)
graph1.add_undirected_edge(graph1.get_vertex("Atlanta"), graph1.get_vertex("Barcelona"), 1021)
graph1.add_undirected_edge(graph1.get_vertex("Atlanta"), graph1.get_vertex("Vienna"), 243)
graph1.add_undirected_edge(graph1.get_vertex("Philadelphia"), graph1.get_vertex("Italy"), 743)
graph1.add_undirected_edge(graph1.get_vertex("Chicago"), graph1.get_vertex("Italy"), 876)
graph1.add_undirected_edge(graph1.get_vertex("Italy"), graph1.get_vertex("Madrid"), 545)
graph1.add_undirected_edge(graph1.get_vertex("Venice"), graph1.get_vertex("Vienna"), 160)
graph1.add_undirected_edge(graph1.get_vertex("Barcelona"), graph1.get_vertex("Madrid"), 45)
graph1.add_undirected_edge(graph1.get_vertex("Italy"), graph1.get_vertex("Moscow"), 231)


start_time = time.time()
tree_edges = minimum_spanning_tree(graph1)
print('Time to find minimum spanning tree: ')
print("--- %s seconds ---" % (time.time() - start_time))
print

print("Edges in minimum spanning tree (graph 1):")
for edge in tree_edges:
    print(edge.from_vertex.label + " to " + edge.to_vertex.label + ", weight = " + str(edge.weight))



