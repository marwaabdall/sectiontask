#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

get_ipython().run_line_magic('matplotlib', 'inline')
import networkx as nx


# In[5]:


G = nx.Graph()
nx.add_cycle(G,[0, 1, 2, 3])
nx.add_cycle(G,[4, 5, 6, 7])
G.add_edge(0, 7)

nx.draw(G, with_labels=True,node_color='#d81b60',node_size=1000)


# In[6]:


partition = [
    {1, 2, 3},
    {4, 5, 6},
    {0, 7},
]


# In[7]:


partition_map = {}
for idx, cluster_nodes in enumerate(partition):
    for node in cluster_nodes:
        partition_map[node] = idx

partition_map


# In[8]:


partition_map[0] == partition_map[7]


# In[11]:


node_colors = [partition_map[n] for n in G.nodes]
        
nx.draw(G, node_color=node_colors, with_labels=True,node_size=1000)


# In[13]:


def modularity(G, partition):
    W = sum(G.edges[v, w].get('weight', 1) for v, w in G.edges)
    summation = 0
    for cluster_nodes in partition:
        s_c = sum(G.degree(n, weight='weight') for n in cluster_nodes)
        # Use subgraph to count only internal links
        C = G.subgraph(cluster_nodes)
        W_c = sum(C.edges[v, w].get('weight', 1) for v, w in C.edges)
        summation += W_c - s_c ** 2 / (4 * W)
    
    return summation / W


# In[14]:


modularity(G, partition)


# In[15]:


partition_2 = [
    {0, 1, 2, 3},
    {4, 5, 6, 7},
]
modularity(G, partition_2)


# In[16]:


nx.community.quality.modularity(G, partition_2)


# In[18]:


K = nx.karate_club_graph()
nx.draw(K, with_labels=True)


# In[19]:


K.nodes[0]


# In[22]:


K.nodes[9]


# In[26]:


K = nx.karate_club_graph()
club_color = {
    'Mr. Hi': 'orange',
    'Officer': 'lightblue',
}
node_colors = [club_color[K.nodes[n]['club']] for n in K.nodes]
nx.draw(K, node_color=node_colors, with_labels=True,node_size=1000)


# In[28]:


groups = {
    'Mr. Hi': set(),
    'Officer': set(),
}

for n in K.nodes:
    club = K.nodes[n]['club']
    groups[club].add(n)
    
groups


# In[29]:


empirical_partition = list(groups.values())
empirical_partition


# In[30]:


nx.community.is_partition(K, empirical_partition)


# In[31]:


nx.community.quality.modularity(K, empirical_partition)


# In[32]:


random_nodes = random.sample(K.nodes, 17)
random_partition = [set(random_nodes),
                    set(K.nodes) - set(random_nodes)]
random_partition


# In[34]:


random_node_colors = ['orange' if n in random_nodes else 'lightblue' for n in K.nodes]
nx.draw(K, node_color=random_node_colors,node_size=1000)


# In[35]:


nx.community.quality.modularity(K, random_partition)


# In[37]:


G = nx.karate_club_graph()
nx.draw(G,node_color='#00c853',node_size=1000)


# In[38]:


nx.edge_betweenness_centrality(G)


# In[39]:


my_edge_betweenness = nx.edge_betweenness_centrality(G)
my_edge_betweenness[0, 1]


# In[40]:


my_edge_betweenness.get((0, 1))


# In[41]:


max(my_edge_betweenness, key=my_edge_betweenness.get)


# In[42]:


max(G.edges(), key=my_edge_betweenness.get)


# In[43]:


my_edge_betweenness = nx.edge_betweenness_centrality(G)
most_valuable_edge = max(G.edges(), key=my_edge_betweenness.get)
G.remove_edge(*most_valuable_edge)


# In[44]:


nx.connected_components(G)


# In[45]:


list(nx.connected_components(G))


# In[46]:


G = nx.karate_club_graph()
partition_sequence = []
for _ in range(G.number_of_edges()):
    my_edge_betweenness = nx.edge_betweenness_centrality(G)
    most_valuable_edge = max(G.edges(), key=my_edge_betweenness.get)
    G.remove_edge(*most_valuable_edge)
    my_partition = list(nx.connected_components(G))
    partition_sequence.append(my_partition)


# In[47]:


len(partition_sequence), nx.karate_club_graph().number_of_edges()


# In[48]:


len(partition_sequence[0])


# In[49]:


len(partition_sequence[-1]), nx.karate_club_graph().number_of_nodes()


# In[50]:


G = nx.karate_club_graph()
modularity_sequence = [modularity(G, p) for p in partition_sequence]
modularity_sequence


# In[52]:


import matplotlib.pyplot as plt
plt.plot(modularity_sequence)
plt.ylabel('Modularity')
plt.xlabel('Algorithm step')


# In[53]:


def my_modularity(partition):
    return nx.community.quality.modularity(G, partition)
best_partition = max(partition_sequence, key=my_modularity)


# In[54]:


best_partition


# In[55]:


def create_partition_map(partition):
    partition_map = {}
    for idx, cluster_nodes in enumerate(partition):
        for node in cluster_nodes:
            partition_map[node] = idx
    return partition_map


# In[57]:


best_partition_map = create_partition_map(best_partition)

node_colors = [best_partition_map[n] for n in G.nodes()]
nx.draw(G, with_labels=True, node_color=node_colors,node_size=1000)


# In[58]:


nx.community.quality.modularity(G, best_partition)


# In[59]:


for partition in partition_sequence:
    if len(partition) == 2:
        two_cluster_partition = partition
        break

two_cluster_partition


# In[60]:


two_cluster_partition_map = create_partition_map(two_cluster_partition)

node_colors = [two_cluster_partition_map[n] for n in G.nodes()]
nx.draw(G, with_labels=True, node_color=node_colors,node_size=1000)


# In[61]:


nx.community.quality.modularity(G, two_cluster_partition)


# In[63]:


import matplotlib.pyplot as plt

pos = nx.layout.spring_layout(G)
fig = plt.figure(figsize=(15, 6))

plt.subplot(1, 2, 1)
two_cluster_partition_map = create_partition_map(two_cluster_partition)
node_colors = [two_cluster_partition_map[n] for n in G.nodes()]
nx.draw(G, with_labels=True, node_color=node_colors, pos=pos,node_size=1000)
plt.title('Predicted communities')

plt.subplot(1, 2, 2)
node_colors = [G.nodes[n]['club'] == 'Officer' for n in G.nodes()]
nx.draw(G, with_labels=True, node_color=node_colors, pos=pos,node_size=1000)
plt.title('Actual communities')


# In[64]:


G.nodes[8]


# In[65]:


list(nx.community.girvan_newman(G))[:5]


# In[ ]:




