#!/usr/bin/env python
# coding: utf-8

# In[23]:


# Task 1

import networkx as nx
F = nx.Graph()
F.add_nodes_from([1,2,3,4,5,6])
F.add_edges_from([(1,2),(1, 3), (1, 4), (1, 6),(2,3),(2,4),(3,6)])
nx.draw(F, with_labels=True,node_color='#ae2012',
        node_size=1500,
        font_color='white')


# In[25]:


def plot_degree_dist(F):
    
    degrees = F.degree()
    degrees = dict(degrees)
    values = sorted(set(degrees.values()))
    print(values)
    histo = [list(degrees.values()).count(x) for x in values]
    P_k = [x / F.order() for x in histo]
    print(len(P_k))
    
    plt.figure()
    plt.bar(values, P_k)
    plt.xlabel("k",fontsize=20)
    plt.ylabel("p(k)", fontsize=20)
    plt.title("Degree Distribution", fontsize=20)
    
    plt.show()
    plt.figure()
    plt.grid(False)
    plt.loglog(values, P_k, "bo")
    plt.xlabel("k", fontsize=20)
    plt.ylabel("log p(k)", fontsize=20)
    plt.title("log Degree Distribution")
    plt.show()
    plt.show()  


# In[73]:


from collections import Counter
degree_sequence = [F.degree(n) for n in F.nodes]
degree_counts = Counter(degree_sequence)
min_degree, max_degree = min(degree_counts.keys()), max(degree_counts.keys())
plt.xlabel("Degree", fontsize=20)
plt.ylabel("Number of Nodes", fontsize=20)
plot_x = list(range(min_degree, max_degree + 1))
plot_y = [degree_counts.get(x, 0) for x in plot_x]
plt.bar(plot_x, plot_y)


# In[68]:


Adj = nx.adjacency_matrix(F) 


# In[69]:


print(Adj.todense())


# In[61]:


# Task 2

g = nx.DiGraph()
g.add_nodes_from([1,2,3,4,5,6])
g.add_edges_from([
    (1,2),
    (2,3),(2,4),
    (3,1), (3,2),
    (4,1),
    (6,1),
    (6,3),
])
nx.draw(g, with_labels=True,node_color='#283618',
        node_size=1000)


# In[62]:


def plot_degree_dist(F):
    
    degrees = g.degree()
    degrees = dict(degrees)
    values = sorted(set(degrees.values()))
    print(values)
    histo = [list(degrees.values()).count(x) for x in values]
    P_k = [x / g.order() for x in histo]
    print(len(P_k))
    
    plt.figure()
    plt.bar(values, P_k)
    plt.xlabel("k",fontsize=20)
    plt.ylabel("p(k)", fontsize=20)
    plt.title("Degree Distribution", fontsize=20)
    
    plt.show()
    plt.figure()
    plt.grid(False)
    plt.loglog(values, P_k, "bo")
    plt.xlabel("k", fontsize=20)
    plt.ylabel("log p(k)", fontsize=20)
    plt.title("log Degree Distribution")
    plt.show()
    plt.show()  


# In[74]:


from collections import Counter
degree_sequence = [g.degree(n) for n in g.nodes]
degree_counts = Counter(degree_sequence)
min_degree, max_degree = min(degree_counts.keys()), max(degree_counts.keys())
plt.xlabel("Degree", fontsize=20)
plt.ylabel("Number of Nodes", fontsize=20)
plot_x = list(range(min_degree, max_degree + 1))
plot_y = [degree_counts.get(x, 0) for x in plot_x]
plt.bar(plot_x, plot_y)


# In[71]:


A = nx.adjacency_matrix(g) 


# In[72]:


print(A.todense())


# In[ ]:




