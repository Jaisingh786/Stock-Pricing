# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 00:04:14 2019

@author: DEVENDRA
"""

import numpy as np
submission_initial=np.genfromtxt("edit_it_in_notepad6.csv",delimiter=",")
#%%
sub_part_a=np.genfromtxt("Result_parta__full.csv",delimiter=",")
Adding_first_col=np.zeros((1,2))
sub_part_a=np.append(Adding_first_col,sub_part_a)
sub_part_a=np.reshape(sub_part_a,(2304989,2))
#%%
new_file=submission_initial
new_file=submission_initial-sub_part_a
np.savetxt("Without_user_data.csv",new_file,delimiter=",")
#%%
sub_new=np.genfromtxt("Result_parta__svm_1.csv",delimiter=",")
Adding_first_col=np.zeros((1,2))
sub_new=np.append(Adding_first_col,sub_new)

sub_new=np.reshape(sub_new,(2304989,2))
sub_new=sub_new+new_file
np.savetxt("edit_it_in_notepad8.csv",sub_new,delimiter=",")
#%%
# after editing the above save file in notepad
import pandas as pd
sub1=pd.read_csv("edit_it_in_notepad8.csv")
sub1 = sub1.astype({"Id": int, "Prediction": float})
sub1.to_csv("Submit_this_8.csv",mode = 'w', index=False)