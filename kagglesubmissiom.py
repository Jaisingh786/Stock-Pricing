# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 11:53:07 2019

@author: user
"""

import numpy as np

train=np.genfromtxt("train.csv", delimiter=",")
train=train[1:,:]
test=np.genfromtxt("test.csv", delimiter=",")
test=test[1:,:]
attr_relevance=np.genfromtxt("genome_scores.csv", delimiter=",")
attr_relevance=attr_relevance[1:,:]
#W_trained_users=[]
#rating =[]
#movie=[]
#tag=[]
#%%
#c=test[0][0]
#A_test=[]
#A_test.append(c)
#for row in test:
#    if(row[0]==c):
#        pass
#    else:
#        c=row[0]
#        A_test.append(c)
#A_train=[]
#c=train[0][0]
#A_train.append(c)
#for row in train:
#    if(row[0]==c):
#        pass
#    else:
#        c=row[0]
#        A_train.append(c)
#a=b=c=0
#needed_train=[]
#only_in_test=[]
#C=np.ones((10000,1))
#for i in A_train:
#    C[int(i)]-=3   
#for i in A_test:
#    C[int(i)]+=2
#for i in range(0,10000):
#    if(C[int(i)]==-2):
#        a+=1#only in train
#    elif(C[int(i)]==3):
#        b+=1
#        only_in_test.append(i)#only in test
#    elif(C[int(i)]==0):
#        needed_train.append(i)
#        c+=1
#needed_train=np.array(needed_train)
#only_in_test=np.array(only_in_test)
#%%
#findout how many movies have tags
#import pandas as pd
#tags= pd.read_csv("tags.csv")
#tags=tags.sort_values('movieId') 
#for row in train:
#    if(row[0]==1):#a givrn user
#        movie.append(int(row[1]))
#        rating.append(row[2])
#        taged=[]
#        for j in range(0,tags.shape[0]):
#            temp=j
#            if(tags.iloc[temp,0]==movie[-1]):
#                while(tags.iloc[temp,1]==movie[-1]):
#                    taged.append(tags[temp,1])
#                    temp+=1
#                #print(i)
#                if(len(taged)!=0):
#                    #print(len(taged))
#                    break
#        if(len(taged)!=0):
#           tag.append(taged)
#           break
#    else:
#         break
#%%
#weights=[]
#y=[]
#A=[]
#store_train=[]
#lam=0.01
#i=2407717
#while i<3333124:
#    #i_counter=0
#    if(train[i,0] in needed_train):
#        #print(i)
#        temp=train[i,0]#tempindicates user name
#        store_train.append(temp)
#        count=0
#        while(temp==train[i,0]):#this loops store all the movies he rated into A
#            if(count<300):
#                b=(attr_relevance[attr_relevance[:,0]==train[i,1]])[:,2]
#                if(b.shape[0]!=0):
#                    A=np.append(A,b)
#                    y=np.append(y,train[i,2])
#                    #print(A.shape[0]/1128,len(y),i)
#                    count+=1
#            i+=1
#            #i_counter+=1    
#       # if(count>=301):
#        #    count=301
#        y=np.transpose(np.matrix(y))
#    #A=np.transpose(A)
#        #i=i-1
#        #print(i)
#        A=np.transpose(np.matrix(A).reshape((1128,count)))
#        c=np.ones((A.shape[0],1))
#        A=np.hstack((A,c))
#        res=(np.linalg.inv((np.transpose(A))*A+2*lam*(np.identity(A.shape[1]))))*(np.transpose(A))*y
#        weights.append(res)
#        A=[]
#        y=[]
#    else:
#        i+=1
    #i=i+i_counter 
        #break#train.shape[0]  
#store_train=np.array(store_train)
#%%
#weights_468=np.zeros((468,1129))
#for i in range(0,468):
#    for j in range(0,1129):
#        weights_468[i,j]=(weights[i])[j]
#%%        
#np.savetxt("weights_final.csv",weight_final, delimiter=",")
#%%
#np.savetxt("store_527.csv",store_train, delimiter=",")
#%%
weight_final=np.genfromtxt("weights_final.csv",delimiter=",")
store_final=np.genfromtxt("store_final.csv",delimiter=",")
#%%
#weight_final=np.append(weight_final,weights_468)
#%%
#weight_final=np.reshape(weight_final,(2724,1129))
#store_final=np.genfromtxt("store_final.csv",delimiter=",")
#store_final=np.append(store_final,store_train)

#%%
def rounding(number):
        return round((number * 2)) / 2
#%%
def new_movie_avg_rating(j):
    for k in range(0,len(user_store)):
        if(user_store[k]==store_final[j]):
            return user_store_rating[k]
    counter=0
    i=0
    su=0
    for i in range(train.shape[0]):
        if train[i,0]==store_final[j]:
            su=su+train[i,2]
            counter+=1
    if counter!=0:
        return (rounding(su/counter))
#%%
def new_user_rating(i):
    for k in range(0,len(movie_store)):
        if(movie_store[k]==test[i,1]):
            return movie_store_rating[k]
    counter=0
    j=0
    su=0
    for j in range(train.shape[0]):
        if test[i,1]==train[j,1]:
            su=su+train[j,2]
            counter+=1  
    if counter!=0:
        return (rounding(su/counter))
#%%
# prediction       
result=np.zeros((2304988,2))
movie_store=[]#for storing new movie
movie_store_rating=[]
user_store=[]
user_store_rating=[]
#%%
for i in range(0,test.shape[0]):
    #if(i%1000==0):
       # print(1)
    counter=0
    for j in range(0,2724):
        length=0
        if(test[i,0]==store_final[j]):
            counter=1
            length=0
            while test[i,0]==store_final[j]:
                length+=1
                b=(attr_relevance[attr_relevance[:,0]==test[i,1]])[:,2]
                if(len(b)!=0):     
                    weight=weight_final[j]
                    predict=rounding(weight[:1128].dot(b)+weight[1128])
                    result[i,1]=predict
                    result[i,0]=i
                    i+=1
                else:
                    result[i,0]=i
                    result[i,1]=(new_movie_avg_rating(j))
                    movie_store.append(test[i,1])
                    movie_store_rating.append(rounding(result[i,1]))
                    #result[i,1]=rounding(result[i,1])
                    #result[i,1]=np.NaN
                    i+=1
        #print(length)
        if(length!=0):
            break
        #print(length,j)           
    if counter==0:
        result[i,0]=i
        result[i,1]=(new_user_rating(i))
        user_store.append(test[i,0])
        user_store_rating.append(rounding(result[i,1]))
        #result[i,1]=np.NaN
        #result[i,1]=rounding(result[i,1])
    if(result[i,1]==np.nan):
        result[i,1]=3.5
        
#%%
#weight_avg=np.array(1129)
#for i in range(0,2256):
#    weight_avg=weight_avg+weight_final[i]
#weight_avg/=2256
##%%
#for i in range(0,test.shape[0]):
#    result[i]=i
#    b=(attr_relevance[attr_relevance[:,0]==test[i,1]])[:,2]
#    if(len(b)!=0):
#        result[i,1]=rounding(weight_avg[:1128].dot(b)+weight_avg[1128])
#    else:
#        result[i,1]=3.5
        





















    
    
            
        
                
                
                
        
    