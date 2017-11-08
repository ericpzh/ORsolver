import networkx as nx
import matplotlib.pyplot as plt
'''
Solver for graph problems
It might run slowly
'''
##Main input
##Input for a graph is tricky,
## since I use the networkX library,
## go to their page to check out how to input graphs or follow my example
# G = nx.Graph() if undirected / G = nx.DiGraph() if directed
G = nx.DiGraph()
# edit the list with 'tuples' ('Origin','Destination','Weight')
# !!! keep source/origin to be 'O' and target/sink to be 'T' in order for the args to compile
elist = [('O','A',5),('O','B',7),('O','C',4),('A','B',1),('B','C',2),('B','E',5),('C','E',4),('B','D',4),('A','D',3),('E','D',1),('D','T',9),('E','T',6)]
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
    elist = nx.dijkstra_path(G,'O','T')
    sum = 0;
    for i in range(len(elist)-1):
        data = G.get_edge_data(elist[i],elist[i+1])['weight']
        T.add_edge(elist[i],elist[i+1],weight=data)
        sum += data
    print("Optimal Objective value is : " + str(sum))
    return T

##Max flow problem with augmenting path algorithm
##Takes in nx.Graph() G a directed networkX graph
##return a nx.Graph() T a subgraph of sp of G
def maxflow(G):
    # turn weight into capacity
    T = nx.DiGraph()
    elist = list(nx.edge_dfs(G))
    for i in range(len(elist)):
        data = G.get_edge_data(elist[i][0], elist[i][1])['weight']
        T.add_edge(elist[i][0],elist[i][1],capacity = data)
    #calculate max flow
    flow_value, flow_dict = nx.maximum_flow(T, 'O', 'T')
    elist = [(key, subkey, value) for key, subdict in flow_dict.items() for subkey, value in subdict.items()]
    #subgraph containing only flow
    R = nx.DiGraph()
    for i in elist:
        R.add_edge(i[0],i[1],weight = i[2])
    print("Optimal Objective value is : " + str(flow_value))
    return R

##Main function of the class
##Takes in string args to run with graph G, bool debug(show original graph if true)
##List of args "mst"->min spanning tree/"sp"->shortest path/"mf"->max flow
def NetworkSolve(args,debug):
    if(args == "mst"): #min spanning tree
        T = minimumSpanningTree(G)
    elif(args == "sp"): #shortest path
        T = shortestpath(G)
    elif(args == 'mf'): #max flow
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
NetworkSolve("mf",False)
