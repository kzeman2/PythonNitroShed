#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 09:13:40 2018

@author: kzeman2

Control Code for running the NitroShed Model found in model.py
"""
from model import *

#runmodel
#import matplotlib.pyplot as plt
model = NitroShedModel(2,10,10,2)
for i in range(5):
    model.step(i)



"""

Old ways I have run the model


model = NitroShedModel(2,10,10,3)
#model.step()
farmer_capital = [a.capital for a in model.schedule.agents]
plt.hist(farmer_capital)




import matplotlib.pyplot as plt
model = NitroShedModel(10,10,10)
for i in range(10):
    model.step()
    

farmer_capital = [a.capital for a in model.schedule.agents]
plt.hist(farmer_capital)




#run.py
import matplotlib.pyplot as plt

all_capital = []
for j in range(10):
    model = NitroShedModel(10,10,10)
    for i in range(10):
        model.step()
        
        for agent in model.schedule.agents:
            all_capital.append(agent.capital)
    
plt.hist(all_capital, bins=range(max(all_capital)+1))



import numpy as np

model = NitroShedModel(50, 10, 10)
for i in range(20):
    model.step()
    
agent_counts = np.zeros((model.grid.width, model.grid.height))
for cell in model.grid.coord_iter():
    cell_content, x, y = cell
    agent_count = len(cell_content)
    agent_counts[x][y] = agent_count
plt.imshow(agent_counts, interpolation='nearest')
plt.colorbar()


"""
