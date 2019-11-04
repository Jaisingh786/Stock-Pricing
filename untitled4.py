# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 18:35:48 2019

@author: user
"""

import numpy as np

final=np.genfromtxt("add_this.csv",delimiter=",")
result=np.genfromtxt("Result_parta__reg_new.csv",delimiter=",")
final=np.add(final,result)