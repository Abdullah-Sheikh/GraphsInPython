import matplotlib.pyplot as lib1
import networkx as lib2

G = lib2.Graph()
G.add_edges_from([ ('A','B'),('A','C'),('B','C')])
#G.add_weighted_edges_from([('A','B',4),('B','C',5)])
pos = lib2.planar_layout(G)
lib2.draw_networkx_nodes(G,pos,node_size=500)
lib2.draw_networkx_edges(G,pos,edgelist=G.edges(),edge_color = 'black')
lib2.draw_networkx_edge_labels(G,pos)
lib2.draw_networkx_labels(G,pos)
lib1.show()