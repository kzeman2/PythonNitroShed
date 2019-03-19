#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 17:49:23 2018
@author: kzeman2

NitroShed Model

"""

from mesa import Agent, Model
import random
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from schedule import model_schedule
#import matplotlib.pyplot as plt


#Agent Classes used in model
from farmer_agent import *
from bmp_agent import *
from community_agent import *
from farmland_agent import *
from environment_agent import *

######## Model Control ##########
"""
A model with some number of farmer agents. Farmers are influence based on 
the other agents within the model.These are the CommunityAgent, the 
FarmLandAgent, the EnvironmentAgent, and the BMPAgent.

"""
class NitroShedModel(Model):
    """
    Creates the NitroShed Super Class which creates all of the model Agents
    
    classes used in this model are:
        farmer_agent: creates all of the farmers with typology parameters and 
        places them at a location of farmland
        
        farmland_agent: creates the farmland from information givent from the 
        environement agent
        
        bmp_agent: creates the bmps that can be used by the farmer
        
        community_agent: creates the community which acts as all other 
        stakeholders in the model
        environment_agent: creates the environment HRU's and watershed where 
        the model takes place
    
    """
    
    print('initalizing Nitroshed Model')
    
    
    def __init__(self, Num_Farmers, width, height, bmps_available):
        r"""
        Initializes the model and creates the agents
        
        Takes in parameters designated from runModel.py to create the farmer 
        agents, BMP agents, Farmland agents, community agent and environment 
        agent.  
        
        Parameters
        ----------
        
        Num_Farmers: int
            Number of farmer agents which will be created and run in the model. 
            Each farmer has a typology and other inherint traits which can be 
            found in farmer_agent.py
            
        width: int
            designates how wide the model space is
        
        height: int
            designates how tall the model space is 
            
        bmps_available: int
            gives the number of BMP's that are created in the model. Used in
            the creation of bmp_agent.py
            
        %%%%%%%%%%%%%
        
        num_agents: int 
        number of farmers created in the model
        
        grid: matrix 
        
        schedule: class
        function schedule.py that creates the order that the agents in the model are 
        called to take a step 
        
        bmps_available:
        int
            gives the number of BMP's that are created in the model. Used in
            the creation of bmp_agent.py
            
        returns
        -------
        completed model
        
        """
        self.num_agents = Num_Farmers
        #self.schedule = RandomActivation(self)
        self.grid = MultiGrid(width, height, True)
        self.schedule = model_schedule(self)
        self.bmps_available=bmps_available
        
        #Create BMP's
        print('Creating BMPs')
        for i in range(self.bmps_available):   
            bmp= BMPAgent(i, self)
            self.schedule.add(bmp)
            
            
        #Create Environment
        print('Creating EnvironmentAgent')
        env=EnvironmentAgent(self)
        
        #Creat Community
        print('Creating Community Agent')
        community= CommunityAgent(self)
         
        
        # Create agents
        print('Creating Agents')
        for i in range(self.num_agents):
            a = FarmerAgent(i, self)
            self.schedule.add(a)
            b= FarmLandAgent(i, self)
            self.schedule.add(b)
            
            #Add the agent to a random grid cell
            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))
            self.grid.place_agent(b, (x, y))
            print("Farmer:",a.farmer_id,"Capital",a.capital, "location:", a.pos, "Area:", b.area,"Farm Location", b.pos)

      
    def step(self,i):
        '''Advance the model by one step.'''
        print("model step", i)
        self.schedule.step()

        





