#!/usr/bin/env python
# coding: utf-8

# In[1]:


import itertools
import random

get_ipython().run_line_magic('matplotlib', 'inline')
import networkx as nx


# In[2]:


def barabasi_albert_graph(N, m):
    G = nx.complete_graph(m + 1)
    for i in range(G.number_of_nodes(), N):
        new_neighbors = []
        possible_neighbors = list(G.nodes)
        for _ in range(m):
            degrees = [G.degree(n) for n in possible_neighbors]
            j = random.choices(possible_neighbors, degrees)[0]
            new_neighbors.append(j)
            possible_neighbors.remove(j)
        for j in new_neighbors:
            G.add_edge(i, j)

    return G


# In[5]:


G = barabasi_albert_graph(30, 1)
nx.draw(G, node_size=400)


# In[ ]:




