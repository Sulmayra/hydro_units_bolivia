# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 15:55:34 2021

@author: VLIR_energy
"""

import pandas as pd

#data = pd.read_excel("MainData.xlsx", index_col=0)

df1 = pd.read_csv("ScaledInflows_NO.csv")
df1.TIMESTAMP = pd.to_datetime(df1.TIMESTAMP)
df1 = df1.squeeze()

df2 = pd.read_csv("../HydroData/ScaledInflows/NO/1980.csv")
#df1 = pd.merge(left=data, right=data1, left_on="TIMESTAMP", right_on="TIMESTAMP")
df3 = df2.set_index("TIMESTAMP").join(df1.set_index("TIMESTAMP"))
#df3 = pd.merge(left=df1, right=df2, left_on="TIMESTAMP", right_on="TIMESTAMP")
#df.set_index("TIMESTAMP").join(data.set_index("TIMESTAMP"))


#df1.TIMESTAMP.astype('datetime64[ns]')
#df2.TIMESTAMP.astype('datetime64[ns]')
#df3=df2.merge(df1, on='TIMESTAMP')  
#df3 = df2.merge(df1)