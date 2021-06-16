# -*- coding: utf-8 -*-
"""
Created on Tue May 11 23:03:39 2021

@author: VLIR_energy
"""

import pandas as pd

df1 = pd.read_csv("Inflows_OR.csv", index_col=0)


df2 = pd.read_csv("MainData.csv", index_col=0)
# To Convert DataFrame to Series
df2_2 = df2.squeeze()

# ScaledInflows= P / P_diseño
# P= Q*h*g*ρ/1E6
df3 = (df1*df2_2["Falls down (M)"]*9.81*1019/1E6/df2_2["Power (MW)"])
df4 = df3.dropna(1)

# Converting the index as data
df4.index = pd.to_datetime(df4.index)
#df4.index = pd.to_datetime(df4.index,freq='H')


df4.to_csv("ScaledInflows_OR.csv")



