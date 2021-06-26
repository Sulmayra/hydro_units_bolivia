# -*- coding: utf-8 -*-
"""
Created on Sat May 15 07:12:57 2021

@author: Sulmayra.
"""

import pandas as pd

data = pd.read_csv("ScaledInflows_CE.csv")
data.TIMESTAMP = pd.to_datetime(data.TIMESTAMP)
data = data.squeeze()

for i in range(1980,2016):
    startdate = "01-01-"+str(i)+" 00:00" 
    endate = "12-31-"+str(i)+" 23:55"  
    idx = pd.date_range(start=startdate, end=endate,freq="1h") 
    df = pd.DataFrame(idx)
    df.columns= ["TIMESTAMP"]
    df1 = df.set_index("TIMESTAMP").join(data.set_index("TIMESTAMP"))
    filename="../HydroData/ScaledInflows/CE/" + str(i) + ".csv"
    print(filename)
    df1.to_csv(filename)
    

    


    
    


    
  