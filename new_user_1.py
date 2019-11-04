# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 14:16:04 2019

@author: DEVENDRA
"""
#%%
import numpy as np
final_result=np.genfromtxt("Result_parta__full.csv",delimiter=",")
#%%
train=np.genfromtxt("train.csv", delimiter=",")
train=train[1:,:]
test=np.genfromtxt("test.csv", delimiter=",")
test=test[1:,:]
#%%
train1=train[:,1:]
#train1 does not contain the user id also
#%%
#final_result=result
#%%
movie=[]
train1=train1[train1[:,0].argsort()]
#%%
# getting the average rating for all the movies in the train set
i=0
temp=train1[0,0]
sum=0
counter=0
while(i<train1.shape[0]):
    temp=train1[i,0]
    sum=0
    counter=0
    while(train1[i,0]==temp):
        sum+=train1[i,1]
        counter+=1
        i+=1
    movie.append(temp)
    movie.append(round((sum/counter),1))
#%%
movie=np.array(movie)
movie=movie.reshape(7822,2)
#%%
# this will take time 
i=0
while i<test.shape[0]:
    if i%40000==0:
        print(i)
    #if final_result[i,0]==0 and final_result[i,1]==0:
    # because for the first user we are not predicting anything 0,0 case can excluded
    if final_result[i,0]==0:
        j=0
        counter=0
        while j<7822:
            if test[i,1]==movie[j,0]:
                final_result[i,0]=i
                final_result[i,1]=movie[j,1]
                counter=1
            if(counter==1):
                break
            j=j+1
        if counter==0:
            final_result[i,0]=i
            #final_result[i,1]=3.4 +np.random.normal(0,0.5,1)[0]
            final_result[i,1]=10
    i=i+1
#%%
np.savetxt("Result_partb__full1.csv",final_result,delimiter=",")
#%%
submission=np.genfromtxt("Result_partb__a2.csv",delimiter=",")
#%%
Adding_first_col=np.zeros((1,2))
submission=np.append(Adding_first_col,submission)
submission=np.reshape(submission,(2304989,2))
#%%
np.savetxt("edit_it_in_notepad7.csv",submission,delimiter=",")
#%%
# after editing the above save file in notepad
import pandas as pd
sub1=pd.read_csv("edit_it_in_notepad7.csv")
sub1 = sub1.astype({"Id": int, "Prediction": float})
sub1.to_csv("Submit_this_7.csv",mode = 'w', index=False)







