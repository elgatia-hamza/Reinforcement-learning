# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 12:46:19 2020

@author: Hamza
"""
# Multi-Armed bandit problem (Naive version)

# importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# importing dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

# implementing Random selection
import random 
N = dataset.shape[0]
d = dataset.shape[1]

ads_selected = []
total_reward = 0
for n in range(N):
    ad = random.randrange(d)
    ads_selected.append(ad)
    reward = dataset.values[n,ad]
    total_reward = total_reward + reward
    
    
# Visualisation the results
plt.hist(ads_selected)
plt.title('Histogram of the ads selections')
plt.xlabel('ads')
plt.ylabel('Number of times ad was selected')
plt.show()

            
            
            
            
        

