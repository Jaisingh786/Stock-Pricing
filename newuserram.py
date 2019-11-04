# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 12:22:23 2019

@author: user
"""

import numpy as np
B1=np.genfromtxt("B1.csv",delimiter=",")
#%%
for i in range(0,9970):
    j=0
    sum=0
    while(j<1128):
        sum+=B1[i,j]
        j+=1
    if(sum!=0):
        j=0
        while(j<1128):
            B1[i,j]=B1[i,j]/sum
            j+=1
    i+=1
        
    