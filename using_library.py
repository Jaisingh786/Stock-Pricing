# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 21:16:38 2019

@author: DEVENDRA
"""
#%%
# using sklearn 
import numpy as np
from sklearn.linear_model import LinearRegression
train=np.genfromtxt("train.csv", delimiter=",")
train=train[1:,:]
test=np.genfromtxt("test.csv", delimiter=",")
test=test[1:,:]
attr_relevance=np.genfromtxt("genome_scores.csv", delimiter=",")
attr_relevance=attr_relevance[1:,:]
# above code has removed the label of the data and stored train, test and attributes
#%%
c=test[0][0]
A_test=[]
A_test.append(c)
for row in test:
    if(row[0]==c):
        pass
    else:
        c=row[0]
        A_test.append(c)
A_train=[]
c=train[0][0]
A_train.append(c)
for row in train:
    if(row[0]==c):
        pass
    else:
        c=row[0]
        A_train.append(c)
a=b=c=0
needed_train=[]
only_in_test=[]
C=np.ones((10000,1))
for i in A_train:
    C[int(i)]-=3   
for i in A_test:
    C[int(i)]+=2
for i in range(0,10000):
    if(C[int(i)]==-2):
        a+=1#only in train
    elif(C[int(i)]==3):
        b+=1
        only_in_test.append(i)#only in test
    elif(C[int(i)]==0):
        needed_train.append(i)
        c+=1
needed_train=np.array(needed_train)
only_in_test=np.array(only_in_test)
#%%
# rounding
def rounding(number):
        return round(number * 2) / 2
#%%
result=np.zeros((2304988,2))
#%%
# doing training and testing simultaneously
i=2152574
X=[]
Y=[]

# i refers to the element in train set
# X stores the input of the train 
# Y stores the rating of the train
#while i < train.shape[0]:
while i <3500000:
    if(train[i,0] in needed_train):
        #print(i)
        temp=train[i,0]#tempindicates user name
        count=0
        while(temp==train[i,0]):#this loops store all the movies he rated into X
            if(count<300):
                b=(attr_relevance[attr_relevance[:,0]==train[i,1]])[:,2]
                if(b.shape[0]!=0):
                    X=np.append(X,b)
                    Y=np.append(Y,train[i,2])
                    #print(A.shape[0]/1128,len(y),i)
                    count+=1
            i+=1
        Y=np.transpose(np.matrix(Y))
        X=np.transpose(np.matrix(X).reshape((1128,count)))
        reg=LinearRegression().fit(X,Y)
         # now we have to predict for this user in the test data
        j=0
         # j contains the index of the test data
        counter=0
        while(j<test.shape[0]):
            if(temp!=test[j,0]):
                j+=1
                pass
            else:
                while (temp==test[j,0]):
                    counter=1
                    b=(attr_relevance[attr_relevance[:,0]==test[j,1]])[:,2]
                    if len(b)!=0:
                        result[j,0]=j
                        a=reg.predict(b.reshape(1,-1))
                        result[j,1]=a[0,0]
                        j=j+1
                    else:
                        result[j,0]=j
                         # storing the average rating for that user
                        result[j,1]=np.sum(Y)/count
                        j=j+1
                if(counter==1):
                    break
    i=i+1
    X=[]
    Y=[]

         

    
    
   