import networkx as nx
import matplotlib.pyplot as plot

file = open("C:/Users/knich/Documents/Python Workplace/NetworkProblem/E_Coli/100/ecoli_transcriptional_network_regulonDB_6_7-1.tsv", "r")

graph = nx.Graph()

for line in file:
    this_line = line.split()
    graph.add_edge(this_line[0], this_line[1])

nx.draw(graph, with_labels=True)
plot.show()
