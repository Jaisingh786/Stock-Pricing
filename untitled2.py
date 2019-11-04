# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 11:32:09 2019

@author: user
"""

import numpy as np
from sklearn.linear_model import LinearRegression

test=np.genfromtxt("test.csv", delimiter=",")
test=test[1:,:]
attr_relevance=np.genfromtxt("genome_scores.csv", delimiter=",")
attr_relevance=attr_relevance[1:,:]
#%%
control=1000
X=np.zeros((control,10))
Y=np.zeros((control,1))
#%%
from random import shuffle
train=np.genfromtxt("train.csv", delimiter=",")
train=train[1:,:]
shuffle(train)
#%%
#count=0
i=0
j=0
while i<control:
    b=(attr_relevance[attr_relevance[:,0]==train[i,1]])[:10,2]
    if(b.shape[0]!=0):
        X[j,:]=b
        Y[j,0]=train[i,2]
        j+=1
        #count+=1
        #print(A.shape[0]/1128,len(y),i)
    i+=1
X=X[:j+1,:]
Y=Y[:,j+1,:]   
#Y=np.transpose(np.matrix(Y))
#X=np.transpose(np.matrix(X).reshape((1128,count)))
#%%
reg=LinearRegression().fit(X,Y)
#%%
result=np.zeros((test.shape[0],2))
#%%
i=0
while i<test.shape[0]:
    b=(attr_relevance[attr_relevance[:,0]==test[i,1]])[:10,2]
    if(b.shape[0]!=0):
        result[i,0]=i
        a=reg.predict(b.reshape(1,-1))
        result[i,1]=a[0,0]
        i=i+1
    else:
        result[i,1]=i
        result[i,0]=3.5
        