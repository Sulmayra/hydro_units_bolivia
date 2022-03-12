# -*- coding: utf-8 -*-
"""
Created on Sat May 15 07:12:57 2021

@author: VLIR_energy
"""

import pandas as pd

for z in ['SU','NO','OR','CE']:
    df1 = pd.read_csv("Inflows_"+z+".csv", index_col=0)  
    df2 = pd.read_csv("MainData_SIN.csv", index_col=0)
    # To Convert DataFrame to Series
    # df2_2 = df2.squeeze()
    
    # ScaledInflows= P / P_diseño
    # P= Q*h*g*ρ/1E6
    df3 = (df1*df2["Falls down (M)"]*9.81*1019/1E6/df2["Power (MW)"])
    df4 = df3.dropna(1)
    
    # Converting the index as data
    df4.index = pd.to_datetime(df4.index)
    
    new_index0 = pd.date_range(start="1979-12-31 00:00", end="2015-12-31 23:55",freq="1h")
    new_index = new_index0.tz_localize(tz='UTC')
    df5 = df4.reindex(index=new_index)
    data= df5.fillna(method="pad")

    df = df2.drop(df2[(df2['Technology']=='HROR') | (df2['ZONE'] !=str(z))].index)
    df_A= df.index.tolist()
    df = df2.drop(df2[(df2['Technology']=='HDAM') | (df2['ZONE'] !=str(z))].index)
    df_B= df.index.tolist()
    
    
    for i in range(1980,1982):
        startdate = "12-31-"+str(i-1)+" 23:00"+"UTC"
        endate = "12-31-"+str(i)+" 23:55"+"UTC"
        idx = pd.date_range(start=startdate, end=endate,freq="1h") 
        df1  = data.loc[idx,:]    
        df1 = df1.drop(df_A, axis=1)
        filename="../HydroData/ScaledInflows/"+z+"/" + str(i) + ".csv"  
        print(filename)
        df1.to_csv(filename)                
        df1 = df1.drop(df_B, axis=1)
        filename="../AvailabilityFactors/"+z+"/" + str(i) + ".csv"
        print(filename)
        df1.to_csv(filename)
        
    
   

    


    
    


    
  