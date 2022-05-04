#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import networkx as nx


# In[7]:


G = nx.read_edgelist('ia-enron-only.edges', nodetype=int)
print(nx.info(G))
nx.draw(G,node_color='#d81b60',node_size=250)


# In[11]:


max([1,2,3,4,5,6,7])


# In[14]:


max(['apple', 'grape', 'carrot'])


# In[12]:


max(['marwa', 'ali', 'mohamed'], key=len)


# In[15]:


highest_degree_node = max(G.nodes, key=G.degree)
highest_degree_node


# In[16]:


G.degree(highest_degree_node)


# In[17]:


betweenness = nx.centrality.betweenness_centrality(G)
highest_betweenness_node = max(G.nodes, key=betweenness.get)
highest_betweenness_node


# In[18]:


betweenness[highest_betweenness_node]


# In[20]:


degree_sequence = [G.degree(n) for n in G.nodes]


# In[21]:


import statistics

print('Mean degree:', statistics.mean(degree_sequence))
print('Median degree:', statistics.median(degree_sequence))


# In[22]:


betweenness = nx.centrality.betweenness_centrality(G)
betweenness_sequence = list(betweenness.values())

print('Mean betweenness:', statistics.mean(betweenness_sequence))
print('Median betweenness:', statistics.median(betweenness_sequence))


# In[23]:


from collections import Counter

degree_counts = Counter(degree_sequence)
degree_counts


# In[24]:


min_degree, max_degree = min(degree_counts.keys()), max(degree_counts.keys())

plot_x = list(range(min_degree, max_degree + 1))


# In[25]:


plot_y = [degree_counts.get(x, 0) for x in plot_x]


# In[26]:


import matplotlib.pyplot as plt

plt.bar(plot_x, plot_y)


# In[27]:


counts, bins, patches = plt.hist(betweenness_sequence, bins=10)


# In[28]:


bins


# In[29]:


counts


# In[30]:


nx.connected_components(G)


# In[31]:


core = next(nx.connected_components(G))
core


# In[32]:


len(core)


# In[33]:


components = list(nx.connected_components(G))


# In[34]:


len(components)


# In[35]:


C = G.copy()


# In[36]:


import random

nodes_to_remove = random.sample(list(C.nodes), 2)
C.remove_nodes_from(nodes_to_remove)


# In[37]:


number_of_steps = 25
M = G.number_of_nodes() // number_of_steps
M


# In[38]:


num_nodes_removed = range(0, G.number_of_nodes(), M)


# In[39]:


N = G.number_of_nodes()
C = G.copy()
random_attack_core_proportions = []
for nodes_removed in num_nodes_removed:
    core = next(nx.connected_components(C))
    core_proportion = len(core) / N
    random_attack_core_proportions.append(core_proportion)
    if C.number_of_nodes() > M:
        nodes_to_remove = random.sample(list(C.nodes), M)
        C.remove_nodes_from(nodes_to_remove)


# In[40]:


plt.title('Random failure')
plt.xlabel('Number of nodes removed')
plt.ylabel('Proportion of nodes in core')
plt.plot(num_nodes_removed, random_attack_core_proportions, marker='o')


# In[41]:


nodes_sorted_by_degree = sorted(G.nodes, key=G.degree, reverse=True)
top_degree_nodes = nodes_sorted_by_degree[:M]
top_degree_nodes


# In[42]:


N = G.number_of_nodes()
number_of_steps = 25
M = N // number_of_steps

num_nodes_removed = range(0, N, M)
C = G.copy()
targeted_attack_core_proportions = []
for nodes_removed in num_nodes_removed:
    core = next(nx.connected_components(C))
    core_proportion = len(core) / N
    targeted_attack_core_proportions.append(core_proportion)
    if C.number_of_nodes() > M:
        nodes_sorted_by_degree = sorted(C.nodes, key=C.degree, reverse=True)
        nodes_to_remove = nodes_sorted_by_degree[:M]
        C.remove_nodes_from(nodes_to_remove)


# In[43]:


plt.title('Targeted attack')
plt.xlabel('Number of nodes removed')
plt.ylabel('Proportion of nodes in core')
plt.plot(num_nodes_removed, targeted_attack_core_proportions, marker='o')


# In[44]:


plt.title('Random failure vs. targeted attack')
plt.xlabel('Number of nodes removed')
plt.ylabel('Proportion of nodes in core')
plt.plot(num_nodes_removed, random_attack_core_proportions, marker='o', label='Failures')
plt.plot(num_nodes_removed, targeted_attack_core_proportions, marker='^', label='Attacks')
plt.legend()


# In[ ]:




