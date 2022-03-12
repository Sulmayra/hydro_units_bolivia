# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 14:01:50 2022

@author: VLIR_energy
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("PLOTS1.xlsx", index_col=0)
df=pd.DataFrame(data)
#df['manipulado'] = df['SANTA ROSA I']/2
df.plot()

