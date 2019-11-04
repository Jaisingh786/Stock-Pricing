# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 10:05:25 2019

@author: user
"""

import pandas as pd
import numpy as np
taged=pd.read_csv("tags.csv")
I=np.genfromtxt("I.csv",delimiter=",")
#%%
exist=[]
for i in range(0,282648):
    if taged.iloc[i,0] in I:
        exist.append(taged.iloc[i,0])
#%%
exist=np.array(exist)
exist.sort()
unique = np.unique(exist, axis=0)
#%%
B1=np.genfromtxt("B.csv",delimiter=",")
#%%
gen_attr=pd.read_csv("genome_attributes.csv")
ARR=[]
IND=[]
for i in range(0,9998):
    if(B1[i,0]==0):
        j=0
        #counter=0
        while(j<327):
            counter=0
            if(i==unique[j]):
                #counter1=1
                arr=[]
                counter=1
                k=0
                while(k<282648):
                    count=0
                    if(taged.iloc[k,0]==i):
                        count=1
                        while(taged.iloc[k,0]==i):
                            arr.append(taged.iloc[k,1])
                            k+=1
                    if(count==1):
                        break
                    k+=1
            if(counter==1):
                ARR.append(arr)
                IND.append(i)
                break
            j+=1
            #if(counter1==1):
               # ARR.append(arr)
              #  IND.append(i)
              #  break
#%%
for i in range(0,327):
    j=0
    while(j<len(ARR[i])):
        k=0
        while(k<1128):
            if(ARR[i][j]==gen_attr.iloc[k,1]):
                B1[IND[i],k]=1
                print(i)
            k+=1
        j+=1
        
#%%
for i in range(0,327):
    k=0
    while(k<1128):
        if(B1[IND[i],k]==0):
            B1[IND[i],k]=0.001
        k+=1
            
#%%
np.savetxt("B1.csv",B1,delimiter=",")
#%%
#np.savetxt("ARR.csv",ARR,delimiter=",")
np.savetxt("IND.csv",IND,delimiter=",")
#%%

              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
        
           