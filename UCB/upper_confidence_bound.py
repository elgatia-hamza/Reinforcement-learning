# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 12:08:48 2020

@author: Hamza
"""
# Upper Confidence Bound (UCB)

# importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# importing dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

# implementing UCB
from math import sqrt, log

N = dataset.shape[0]
d = dataset.shape[1]

number_of_selections = [0] * d
sum_of_rewards = [0] * d 
ads_selected = []
total_reward = 0
for n in range(N):
    ad = 0
    max_upper_bound = 0
    for i in range(d):
        if(number_of_selections[i] > 0):
            average_reward_i = sum_of_rewards[i] / number_of_selections[i]
            delta_i = sqrt(3/2 * (log(n + 1)/number_of_selections[i]))
            upper_bound = average_reward_i  + delta_i
        else :
            upper_bound = 1e400
        
        if (upper_bound > max_upper_bound):
            max_upper_bound = upper_bound
            ad = i
    ads_selected.append(ad)
    number_of_selections[ad] = number_of_selections[ad] + 1
    reward = dataset.values[n,ad]
    sum_of_rewards[ad] = sum_of_rewards[ad] + reward
    total_reward = total_reward + reward
    
    
# Visualisation the results
plt.hist(ads_selected)
plt.title('Histogram of the ads selections')
plt.xlabel('ads')
plt.ylabel('Number of times ad was selected')
plt.show()

            
            
            
            
        
