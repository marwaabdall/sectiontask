#!/usr/bin/env python
# coding: utf-8

# In[3]:


import networkx as nx
G = nx.Graph()
G.add_node(1)
nodes = [2, 3, 4]
G.add_nodes_from(nodes)


# In[7]:


G.add_edge(1, 2)
edges_to_add = [(1,3),(2,3),(3,4),(2,4)]
G.add_edges_from(edges_to_add)
nx.draw(G, with_labels=True,node_color='red',node_size=1200)


# In[8]:


G.nodes()


# In[9]:


G.edges()


# In[10]:


for node in G.nodes:
    print(node)


# In[12]:


for edge in G.edges:
    print(edge)


# In[13]:


G.number_of_nodes()


# In[14]:


G.number_of_edges()


# In[31]:


G.neighbors(2)


# In[27]:


for neighbor in G.neighbors(1):
    print(neighbor)


# In[28]:


list(G.neighbors(2))


# In[32]:


G.has_node(2)


# In[34]:


G.has_node(5)


# In[35]:


1 in G.nodes


# In[41]:


len(list(G.neighbors(2)))


# In[43]:


G.degree(1)


# In[45]:


items =['marwa','y','red']
[item.upper() for item in items]


# In[48]:


print(G.nodes()) 
print([G.degree(n)for n in G.nodes()])


# In[50]:


M = (len(item) for item in items)
list(M)


# In[52]:


min(len(item) for item in items)


# In[59]:


G=nx.DiGraph()
G.add_nodes_from(['red','marwa','cat',15])
G.add_edge('red','cat')
nx.draw(G,with_labels=True,node_size=1000)


# In[11]:


#.....ex 1.......
import networkx as nx
G = nx.Graph()
nodes=[('a','b','c','d')]
G.add_nodes_from(nodes)
G.add_edges_from([
        ('a', 'b'),
        ('a', 'd'),
        ('c', 'd'),
    ])
    
nx.draw(G,with_labels=True,node_size=1500)


# In[15]:


def get_leaves(G):
    liste=[]
    for i in G.nodes():
        if G.degree(i)==1:
            liste.append(i)
    return liste


# In[16]:


get_leaves(G)


# In[23]:


print(open('friends.adjlist.txt').read())


# In[29]:


SG = nx.read_adjlist('friends.adjlist.txt')
nx.draw(SG, node_size=2000, node_color='red', with_labels=True)


# In[36]:


# .....ex2.....

def max_degree(m):
    list1=[]
    mx=0
    for node in m.nodes:
        if m.degree(node)>mx:
            mx=m.degree(node)
            s=node
            
    list1.append(s)
    list1.append(mx)
    print(list1)
max_degree(SG)   


# In[37]:


#.......ex3.......
def mutual_friends(n, node_1, node_2):
    liste=[]
    list1=list(n.neighbors(node_1))
    list2=list(n.neighbors(node_2))
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i]==list2[j]:
                liste.append(list1[i])
    print(liste)
(mutual_friends(SG,'Claire', 'George'))


# In[ ]:





# In[ ]:




