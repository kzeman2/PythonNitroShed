#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 09:32:04 2018

@author: kzeman2
"""
from mesa import Agent
from mesa.time import RandomActivation
import random

######## Farm Land Agent ########
class FarmLandAgent(Agent):
    
    def __init__(self,unique_id, model):
        super().__init__(unique_id, model)
        self.unique_id=unique_id
        self.area=random.randint(5000,10000)
        
        
    def step(self):
        print("Farmland Step")
        pass