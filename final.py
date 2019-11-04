# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 11:06:38 2019

@author: i@am_genius
"""

import numpy as np

train=np.genfromtxt("train.csv", delimiter=",")
train=train[1:,:]
attr_relevance=np.genfromtxt("genome_scores.csv", delimiter=",")
attr_relevance=attr_relevance[1:,:]

i=0;

B=np.genfromtxt("B.csv",delimiter=",")
from sklearn.preprocessing import StandardScaler

scaler=StandardScaler()
scaler.fit(B)
#from sklearn.decomposition import PCA
#pca=PCA(n_components=33)
#pca.fit(B)
#B=pca.transform(B)

avg_data=np.genfromtxt("avg_data.csv")
#%%
from sklearn.linear_model import LinearRegression

#n=5264336
#count_k=0
#Y_result=np.zeros((n,1))
#X=np.zeros((n,33))
#Y=np.zeros((n,1))


linearRegressor = [LinearRegression()  for i in range(10000)]
#spacialRegressor=LinearRegression()

i=0

while i < train.shape[0]:
   count=0
   j=0
   major=train[i,0]
   X=np.zeros((1000,1128))
   Y=np.zeros((1000,1))
   while(train[i,0]==major):    
       b=B[int(train[i,1])]
       if(b[0]!=0 and count<1000):
           X[j,:]=b
           Y[j]=train[i,2]
           j+=1
           count+=1
       i+=1
   X=X[:count,:]
   Y=Y[:count,:]
   (linearRegressor[int(train[i,0])]).fit(X,Y)

#Y_result+=Y
    
#Y_result=Y_result/count_k
    

#%%
       

#%%
#avg_data=np.zeros((1,10000))
#major=1
##%%
#for i in range(0,train.shape[0]):
#    major=train[i,0]
#    sum=0
#    counter=0
#    while(train[i,0]==major):
#        sum+=train[i,2]
#        counter+=1
#        i+=1
#    if(counter!=0):
#        avg_data[0,int(major)]=round(sum/counter,2)
        


#%%
test=np.genfromtxt("test.csv", delimiter=",")
test=test[1:,:]

prediction=[]
result=np.zeros((2304988,2))


for i in range(0,test.shape[0]):
   result[i,0]=i;
   b=B[int(test[i,1])]
   if(b[0]!=0):
       b=b.reshape(-1,1)
       b=np.transpose(b)
       result[i,1]=round((linearRegressor[int(test[i,0])].predict(b))[0][0],2)
   else:
       if(avg_data[int(test[i,0])]!=0):
           result[i,1]=avg_data[int(test[i,0])]
       else:
           result[i,1]=3.36
#%%
import pandas as pd
dummy=pd.read_csv('dummy_submission.csv')
dummy['Prediction']=result[:,1]
dummy.to_csv('Results_new.csv',index=False)

      
#%%



           


