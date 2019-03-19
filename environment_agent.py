#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 09:32:54 2018

@author: kzeman2
"""
from mesa import Agent
from mesa.time import RandomActivation
import random

######### Environment Agent #########
class EnvironmentAgent(Agent):
    def __init__(self, model):
        self.soiltype=1
        self.precitipation=1
        self.temperature=1
        self.gis=1
        print("Environment Agent created: soil type:", self.soiltype)
        
        
    def step(self):
        print("Environment Step")
        pass