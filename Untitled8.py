#!/usr/bin/env python
# coding: utf-8

# In[5]:


import networkx as nx
G = nx.Graph()
G.add_node(1)
nodes = [2, 3, 4,5]
G.add_nodes_from(nodes)


# In[9]:


G.add_edge(1, 2)
edges_to_add = [(1,4), (1,5), (2,1),(2,3),(2,5),(5,1),(5,2),(5,3),(5,4),(3,2),(3,5),(3,4),(4,1),(4,3),(4,5)]
G.add_edges_from(edges_to_add)
nx.draw(G, with_labels=True)


# In[ ]:




