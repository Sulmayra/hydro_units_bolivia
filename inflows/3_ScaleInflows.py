# -*- coding: utf-8 -*-
"""
Created on Tue May 11 23:03:39 2021

@author: VLIR_energy
"""

import pandas as pd

df1 = pd.read_csv("Inflows_CE.csv", index_col=0)


df2 = pd.read_csv("Data_UH.csv", index_col=0)
# To Convert DataFrame to Series
df2_2 = df2.squeeze()

df3 = (df1*df2_2["Height_of_falling_water"]*3600*2.7E-10*24)/df2_2["Power"]
df4 = df3.dropna(1)

# Converting the index as date
df4.index = pd.to_datetime(df4.index).tz_localize("UTC")

df4.to_csv("ScaledInflows_CE.csv")



