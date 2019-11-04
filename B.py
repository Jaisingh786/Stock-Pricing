# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 12:39:56 2019

@author: user
"""

import numpy as np
attr_relevance=np.genfromtxt("genome_scores.csv", delimiter=",")
attr_relevance=attr_relevance[1:,:]
#%%
i=0
temp=attr_relevance[0,0]
#%%
B=np.zeros((9998,1128))
#%%
i=0
counter=0
temp=attr_relevance[0,0]
while(counter<9998):
    temp=attr_relevance[i,0]
    j=0
    while(attr_relevance[i,0]==temp):
        B[int(temp),j]=attr_relevance[i,2]
        j+=1
        i+=1
    counter+=1
#%%
np.savetxt("B.csv",B,delimiter=",")