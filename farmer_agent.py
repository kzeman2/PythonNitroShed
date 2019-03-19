#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 17:50:27 2018

@author: kzeman2
"""

##### Farmer Agent ##############
from mesa import Agent
import random


class FarmerAgent(Agent):
    """ A Farmer Agent with initial amount of captial and a unique ID.  the farmer makes deciscions based on 
    five factors: economic, social, environemntal, riskaversion, and innovation. """
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)           #### Super class  used for creating agents from Model Control####
        #Demographics
        self.capital = random.randint(500,1000)
        self.farmer_id=unique_id+1
        self.age=60
        self.education=2
        self.decision= []
        
        #Typology characteritics
        self.economic = random.random()               #Economic factor influencinging decision-making
        self.social = random.random()                 #Social factor influencinging decision-making
        self.environmental= random.random()           #Environmental factor influencinging decision-making
        self.riskaversion= random.random()            #Risk Aversion factor influencinging decision-making
        self.innovation=random.random()               #Innovation factor influencinging decision-making
        print("Farmer:",self.unique_id, "economic:", self.economic)
        
    def step(self):
        print('farmer:',self.unique_id, 'step')
        #other_agent = random.choice(self.model.schedule.agents)
        #other_agent.capital += 100
        #self.capital -= 100
        self.decision= self.economic*1+self.social*1+self.environmental*1+self.riskaversion*1+self.innovation*1
        print('Farmer decision:', self.decision)


    

    

        
    
    



