import networkx as nx
import os

directory = "D:/E_Coli/"

for subdirectory in os.listdir(directory):
    final_directory = directory + subdirectory + "/"
    for file in os.listdir(final_directory):
        graph = nx.Graph()
        file_to_read = open(final_directory + file, "r")

        for line in file_to_read:
            this_line = line.split()
            graph.add_edge(this_line[0], this_line[1])

        nx.to_undirected(graph)

        if nx.number_connected_components(graph) > 1:
            print("Not connected.")
