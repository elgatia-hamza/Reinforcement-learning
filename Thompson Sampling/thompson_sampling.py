# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 10:30:54 2020

@author: Hamza
"""
# Thompson Sampling 

# Importing libraries
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import random
 
# Importing dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

# Implementing Thompson Sampling
N = dataset.values.shape[0]
d = dataset.values.shape[1]

ad_selected = []
number_reward_1 = [0] * d
number_reward_0 = [0] * d
total_rewards = 0

for n in range(N):
    max_random = 0
    ad = 0
    for i  in range(d):
        random_betat = random.betavariate(number_reward_1[i] + 1, number_reward_0[i]+1)
        if random_betat > max_random:
            max_random = random_betat
            ad = i
    ad_selected.append(ad)
    reward = dataset.values[n,ad]
    if reward == 1 :
        number_reward_1[ad] = number_reward_1[ad] + 1
        total_rewards = total_rewards + 1
    else:
        number_reward_0[ad] = number_reward_0[ad] + 1
        
        
# Visualisation the results
plt.hist(ad_selected)
plt.title('Histogram of ads selection')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()

