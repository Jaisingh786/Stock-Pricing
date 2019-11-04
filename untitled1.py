# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 10:29:40 2019

@author: user
"""

import numpy as np
import pandas as pd
iro=np.genfromtxt('Final_result_sub_1.csv',delimiter=',')
#%%
a = iro[1:,0]
b=iro[1:,1]
df = pd.DataFrame({'Id' : a, 'Prediction' : b})
df['Id'] =df['Id'].astype(int)
df.to_csv("finalk.csv", index=False)
#%%
#np.savetxt('finalk.csv',iro[1:,:],delimiter=',',fmt='%0.1f')