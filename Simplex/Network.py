import networkx as nx
import matplotlib.pyplot as plt
'''
In dev solver for graph problems
'''
##Main input
##Input for a graph is tricky,
## since I use the networkX library,
## go to their page to check out how to input graphs or follow my example
# G = nx.Graph() if undirected / G = nx.DiGraph() if directed
G = nx.Graph()
# edit the list with 'tuples' ('Origin','Destination','Weight')
elist = [('O','A', 2 ),('O','B',  5 ),('O','C',  4 ),('A','B',  2 ),('C','B',  1 ),('B','E',3),('C','E',  4 ),('B','D',  4 ),('A','D',  7 ),('D','E',  1 ),('D','T',  5 ),('E','T',  7 )]
G.add_weighted_edges_from(elist)

##Show the Graph
pos = nx.spring_layout(G)
nx.draw(G,pos=pos,with_labels = True)
nx.draw_networkx_edge_labels(G,pos=pos,with_labels = True)
plt.show()