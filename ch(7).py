#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import networkx as nx

G = nx.gnm_random_graph(20, 50)
nx.draw(G)


# In[2]:


def initial_state(G):
    state = {}
    for node in G.nodes:
        state[node] = 'asleep'
    return state


# In[3]:


initial_state(G)


# In[4]:


import random

P_AWAKEN = 0.2
def state_transition(G, current_state):
    next_state = {}
    for node in G.nodes:
        if current_state[node] == 'asleep':
            if random.random() < P_AWAKEN:
                next_state[node] = 'awake'
    return next_state


# In[5]:


test_state = initial_state(G)
state_transition(G, test_state)


# In[6]:


from simulation import Simulation

sim = Simulation(G, initial_state, state_transition, name='Simple Sim')


# In[7]:


sim.state()


# In[8]:


sim.draw()


# In[9]:


sim.run()


# In[10]:


sim.steps


# In[12]:


sim.draw(with_labels=True,node_size=1000)


# In[13]:


sim.state()


# In[14]:


sim.run(10)


# In[15]:


sim.steps


# In[18]:


sim.draw(with_labels=True,node_size=1000)


# In[19]:


sim.plot()


# In[21]:


sim.draw(4, with_labels=True,node_size=1000)


# In[22]:


sim.state(4)


# In[23]:


sim.plot(min_step=2, max_step=8)


# In[25]:


get_ipython().run_line_magic('matplotlib', 'inline')
import networkx as nx

G = nx.gnm_random_graph(20, 50)
nx.draw(G,node_size=1000)


# In[26]:


import random
import string

def initial_state(G):
    state = {}
    for node in G.nodes:
        state[node] = random.choice('ABCD')
    return state


# In[27]:


initial_state(G)


# In[28]:


def state_transition(G, current_state):
    next_state = {}
    for node in G.nodes:
        if G.degree(node) > 0:
            neighbor = random.choice(list(G.neighbors(node)))
            next_state[node] = current_state[neighbor]
    return next_state


# In[29]:


test_state = initial_state(G)
state_transition(G, test_state)


# In[30]:


import matplotlib.pyplot as plt

sim = Simulation(G, initial_state, state_transition, name='Voter Model')


# In[70]:


sim.draw()


# In[71]:


sim.run(40)


# In[68]:


sim.draw(node_size=1000)


# In[34]:


sim.plot()


# In[35]:


import random

def state_transition(G, current_state):
    next_state = {}
    for node in G.nodes:
        if G.degree(node) > 0:
            neighbor = random.choice(list(G.neighbors(node)))
            next_state[node] = current_state[neighbor]
    return next_state


# In[36]:


def state_transition_async(G, current_state):
    for node in G.nodes:
        if G.degree(node) > 0:
            neighbor = random.choice(list(G.neighbors(node)))
            current_state[node] = current_state[neighbor]
    return current_state


# In[37]:


def state_transition_async(G, current_state):
    nodes_to_update = list(G.nodes)
    random.shuffle(nodes_to_update)
    for node in nodes_to_update:
        if G.degree(node) > 0:
            neighbor = random.choice(list(G.neighbors(node)))
            current_state[node] = current_state[neighbor]
    return current_state


# In[38]:


sim = Simulation(G, initial_state, state_transition_async, name='Async Voter Model')
sim.run(40)
sim.plot()


# In[39]:


def stop_condition(G, current_state):
    unique_state_values = set(current_state.values())
    is_stopped = len(unique_state_values) <= 1
    return is_stopped


# In[40]:


sim = Simulation(G, initial_state, state_transition, stop_condition, name='Voter model')
sim.run(100)


# In[41]:


sim.steps


# In[42]:


sim.plot()


# In[43]:


def state_transition_async_rewiring(G, current_state):
    nodes_to_update = list(G.nodes)
    random.shuffle(nodes_to_update)
    for node in nodes_to_update:
        if G.degree(node) > 0:
            neighbor = random.choice(list(G.neighbors(node)))
            current_state[node] = current_state[neighbor]
            neighbor = random.choice(list(G.neighbors(node)))
            if current_state[node] != current_state[neighbor]:
                G.remove_edge(node, neighbor)
            
    return current_state


# In[72]:


sim = Simulation(G, initial_state, state_transition_async_rewiring, stop_condition,
                 name='Voter Model with rewiring')
sim.draw()


# In[73]:


sim.run(40)
sim.draw(node_size=1000)


# In[74]:


sim.plot()


# In[60]:


get_ipython().run_line_magic('matplotlib', 'inline')
import networkx as nx

G = nx.gnm_random_graph(20, 50)
nx.draw(G,node_size=1000)


# In[49]:


import random

def initial_state(G):
    state = {}
    for node in G.nodes:
        state[node] = 'S'
    
    patient_zero = random.choice(list(G.nodes))
    state[patient_zero] = 'I'
    return state


# In[50]:


initial_state(G)


# In[51]:


MU = 0.1
BETA = 0.1

def state_transition(G, current_state):
    next_state = {}
    for node in G.nodes:
        if current_state[node] == 'I':
            if random.random() < MU:
                next_state[node] = 'S'
        else:
            for neighbor in G.neighbors(node):
                if current_state[neighbor] == 'I':
                    if random.random() < BETA:
                        next_state[node] = 'I'

    return next_state


# In[52]:


test_state = initial_state(G)
state_transition(G, test_state)


# In[53]:


sim = Simulation(G, initial_state, state_transition, name='SIS model')


# In[59]:


sim.draw(node_size=1000)


# In[55]:


sim.run(25)


# In[58]:


sim.draw(node_size=1000)


# In[57]:


sim.plot()


# In[ ]:




