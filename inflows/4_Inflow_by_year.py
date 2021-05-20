# -*- coding: utf-8 -*-
"""
Created on Sat May 15 07:12:57 2021

@author: Sulmayra.
"""

import pandas as pd

data = pd.read_csv("Inflows_NO.csv", index_col=0)


for i in range(1980,2016):
    startdate = "01-01-"+str(i)+" 00:00" 
    endate = "12-31-"+str(i)+" 23:55"  
    idx = pd.date_range(start=startdate, end=endate,freq="1h") 
    df = pd.DataFrame(range(len(idx)), index=idx)
    df = data.copy()
    filename="./export_dataframe/" + str(i) + ".csv"
    print(filename)
    df.to_csv(filename)
    

    


    


    
  