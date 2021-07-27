# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 23:55:27 2021

@author: VLIR_energy
"""

import pandas as pd

data = pd.read_csv("ScaledInflows_OR.csv", index_col=0)


for i in range(1980,1982):
    startdate = "01-01-"+str(i)+" 00:00" 
    endate = "31-12-"+str(i)+" 23:55"  
    idx = pd.date_range(start=startdate, end=endate,freq="1h") 
    df = pd.DataFrame(range(len(idx)), index=idx)
    df1 = df + data.copy(deep=False)
    filename="../HydroData/ScaledInflows/OR/" + str(i) + ".csv"
    print(filename)
    df1.to_csv(filename)
