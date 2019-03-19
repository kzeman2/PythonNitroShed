#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 16:22:00 2019

@author: kzeman2
"""
import csv

with open('BMPlist.xlsx' , 'rb') as csvfile:
    BMPs= csv.reader(csvfile, deliminater= ' ', quotechar= '|')