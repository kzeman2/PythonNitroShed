#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 09:30:28 2018

@author: kzeman2
"""
from mesa import Agent
from mesa.time import RandomActivation
import CSV 
import random
####### Community Agent ########
class CommunityAgent(Agent):
    
    def __init__(self, model):
        self.TotalFundsAvailable= []
        self.NitrogenTax=.1
        self.CostShare= 1000
        #self.education
        self.loans=1
        print("Communtiy Agent created: Cost Share Available:", self.CostShare)
        
        


    def step(self):
        with open('BMPlist' , 'rb') as csvfile:
                BMPs= csv.reader(csvfile, deliminater= ' ', quotechar= '|')
        print("Community Step")
        pass    