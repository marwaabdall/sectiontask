#!/usr/bin/env python
# coding: utf-8

# In[2]:


import networkx as nx
g=nx.Graph()
nodes=[1,2,3,4,6]
g.add_nodes_from(nodes)
edges=[(1, 2),(1,3),(1,4),(2,3),(2,4),(3,4),(4,6)]
g.add_edges_from(edges)
nx.draw(g, with_labels=True,node_color='#d81b60',node_size=1000,font_color='white',font_size=30)


# In[6]:


print("marwa")


# In[13]:


nx.has_path(g,4,6)


# In[15]:


list(nx.all_simple_paths(g,3,4))


# In[16]:


nx.shortest_path(g,3,4)
nx.shortest_path_length(g, 3, 4)
nx.is_connected(g)


# In[11]:


nx.is_connected(G)


# In[19]:


c=nx.Graph()
nx.add_cycle(c,[1,2,3])
c.add_edge(4,5)
nx.draw(c,with_labels=True,node_size=1000,font_color='white',font_size=30,node_color='#f50057')
nx.is_connected(c)
nx.has_path(c,4,3)


# In[20]:


nx.number_connected_components(c)


# In[21]:


list(nx.connected_components(c))


# In[22]:


components=list(nx.connected_components(c))
len(components[0])


# In[23]:


max(nx.connected_components(c),key=len)


# In[26]:


core_nodes=max(nx.connected_components(c),key=len)
core=c.subgraph(core_nodes)
nx.draw(core, with_labels=True,node_color='#f50057',node_size=1000)


# In[27]:


d=nx.DiGraph()
d.add_edges_from([(1,2),(2,3),(3,4),(3,5),(4,5)])
nx.draw(d, with_labels=True,node_color='#00c853',node_size=1000,font_color='white',font_size=20)


# In[28]:


nx.has_path(d, 1, 4)


# In[29]:


nx.shortest_path(d, 2, 5)


# In[31]:


nx.shortest_path(d, 4, 5)
nx.is_strongly_connected(d)
nx.is_weakly_connected(d)
list(nx.weakly_connected_components(d))


# In[32]:


nx.shortest_path(d, 4, 5)


# In[33]:


nx.is_strongly_connected(d)


# In[34]:


list(nx.strongly_connected_components(d))


# In[4]:


r = nx.read_graphml('openflights_usa.graphml (1).txt')


# In[5]:


r.nodes['IND']


# In[6]:


r.nodes['IND']['name']


# In[7]:


#EX 1..........................

lofn=list(nx.shortest_path(r,'IND','FAI'))
if len(lofn)==2:
    print('Yes,there is a direct flight between Indianapolis and Fairbanks')
else:
    print('No,there is not a direct flight between Indianapolis and Fairbanks')


# In[8]:


#EX 2.......................................
nx.shortest_path(r,'IND','FAI')


# In[9]:


#EX 3.........................................

def connecting_flights(r):
    list1=[]
    flag=0
    for node in r.nodes:
        list1.append(node)
    for i in range(len(list1)):
        for j in range(len(list1)):
            if nx.has_path(r,list1[i],list1[j]):
                continue
            else:
                flag=1
                break
    if flag==0:
        print('YES,there is a path in the network between every possible pair of airports')
    else:
         print('NO,there is not a path in the network between every possible pair of airports')

connecting_flights(r)       


# In[ ]:




