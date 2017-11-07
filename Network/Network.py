import networkx as nx
import matplotlib.pyplot as plt
'''
In dev solver for graph problems
It might run slowly
'''
##Main input
##Input for a graph is tricky,
## since I use the networkX library,
## go to their page to check out how to input graphs or follow my example
# G = nx.Graph() if undirected / G = nx.DiGraph() if directed
G = nx.Graph()
# edit the list with 'tuples' ('Origin','Destination','Weight')
# !!! keep source/origin to be 'O' and target/sink to be 'T' in order for the args to compile
elist = [('O','A',2),('O','B',5),('O','C',4),('A','B',2),('C','B',1),('B','E',3),('C','E',4),
         ('B','D',4),('A','D',7),('D','E',1),('D','T',5),('E','T',7)]
G.add_weighted_edges_from(elist)

##Minimum spanning tree problem with Prim's algorithm
##Takes in nx.Graph() G a undireted networkX Graph
##return a nx.Graph() T a subgraph of mst of G
def minimumSpanningTree(G):
    T = nx.Graph()
    elist = list(nx.minimum_spanning_edges(G,data=False))
    sum = 0;
    for i in range(len(elist)):
        data = G.get_edge_data(elist[i][0],elist[i][1])['weight']
        T.add_edge(elist[i][0],elist[i][1],weight=data)
        sum += data
    print("Optimal Objective value is : " + str(sum))
    return nx.minimum_spanning_tree(G)

##Shortest path problem with Dijkstra's algorithm
##Takes in nx.DiGraph() G a directed networkX graph
##return a nx.DiGraph() T a subgraph of sp of G
def shortestpath(G):
    T = nx.DiGraph()
    elist = list(nx.shortest_path(G, source='O', target='T'))
    sum = 0;
    for i in range(len(elist)-1):
        data = G.get_edge_data(elist[i],elist[i+1])['weight']
        T.add_edge(elist[i],elist[i+1],weight=data)
        sum += data
    print("Optimal Objective value is : " + str(sum))
    return T

##Max flow problem
##Takes in nx.Graph() G a undirected networkX graph
##return a nx.Graph() T a subgraph of sp of G
def maxflow(G):
    T = nx.Graph()
    return T
##Main function of the class
##Takes in string args to run with graph G, bool debug(show original graph if true)
##List of args "mst"->min spanning tree/"sp"->shortest path/"mf"->max flow
def NetworkSolve(args,debug):
    if(args == "mst"):
        T = minimumSpanningTree(G)
    elif(args == "sp"):
        T = shortestpath(G)
    elif(args == 'mf'):
        T = maxflow(G)
    else:
        print("Not yet implementated")
    if(debug):
        ##Show original Graph if debug is true
        pos = nx.spring_layout(G)
        nx.draw(G, pos=pos, with_labels=True)
        nx.draw_networkx_edge_labels(G, pos=pos, with_labels=True)
        plt.show()
    ##Show the Graph
    pos = nx.spring_layout(G)
    nx.draw(T, pos=pos, with_labels=True)
    nx.draw_networkx_edge_labels(T, pos=pos, with_labels=True)
    plt.show()

##runit
NetworkSolve("mst",False)
