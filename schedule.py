#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 15:46:54 2018

@author: kzeman2
"""
from collections import defaultdict
from mesa.time import RandomActivation

class model_schedule(RandomActivation):
    
        
    """
    Scheduler that activates the farmers each step while leaving the 
        
    """
    
    def __init__(self, model):
        super().__init__(model)
        self.agents_by_class = defaultdict(dict)

    def add(self, agent):
        '''
        Add an Agent object to the schedule
        Args:
            agent: An Agent to be added to the schedule.
        '''

        self._agents[agent.unique_id] = agent
        agent_class = type(agent)
        self.agents_by_class[agent_class][agent.unique_id] = agent

    def remove(self, agent):
        '''
        Remove all instances of a given agent from the schedule.
        '''

        del self._agents[agent.unique_id]

        agent_class = type(agent)
        del self.agents_by_class[agent_class][agent.unique_id]

    def step(self, by_class=True):
        '''
        Executes the step of each agent breed, one at a time, in random order.
        Args:
            by_breed: If True, run all agents of a single breed before running
                      the next one.
        '''
        if by_class:
            for agent_class in self.agents_by_class:
                self.step_class(agent_class)
            self.steps += 1
            self.time += 1
        else:
            super().step()

    def step_class(self, class_name):
        '''
        Shuffle order and run all agents of a given breed.
        Args:
            breed: Class object of the breed to run.
        '''
        agent_keys = list(self.agents_by_class[class_name].keys())
        self.model.random.shuffle(agent_keys)
        for agent_key in agent_keys:
            self.agents_by_class[class_name][agent_key].step()

    def get_class_count(self, agent_class):
        '''
        Returns the current number of agents of certain breed in the queue.
        '''
        return len(self.agents_by_class[agent_class].values())


    