# -*- coding: utf-8 -*-
"""
Created on Sat May 15 07:12:57 2021

@author: VLIR_energy
"""

import pandas as pd

for z in ['CE','OR','SU','NO',]:
    df1 = pd.read_csv("StorageLevel_"+z+".csv", index_col=0)
    
    df2 = pd.read_csv("MainData_SIN.csv", index_col=0)
    # To Convert DataFrame to Series
    df2_2 = df2.squeeze()
    
    # ScaledInflows= P / P_diseño
    # P= Q*h*g*ρ/1E6
    df3 = (df1*df2_2["Factor"])
    df4 = df3.dropna(1)
    
    # Converting the index as data
    df4.index = pd.to_datetime(df4.index)
    
    new_index0 = pd.date_range(start="2019-12-31 00:00", end="2020-12-31 23:55",freq="1h")
    new_index = new_index0.tz_localize(tz='UTC')
    df5 = df4.reindex(index=new_index)
    data= df5.interpolate(method='polynomial', order=5)  #pad
    
    for i in range(2020,2021):
        startdate = "12-31-"+str(i-1)+" 23:00"+"UTC"
        endate = "12-31-"+str(i)+" 23:55"+"UTC"
        idx = pd.date_range(start=startdate, end=endate,freq="1h") 
        df1  = data.loc[idx,:]    
        # filename="../AvailabilityFactors/"+z+"/" + str(i) +"_HU_SIN.csv"
        filename="../HydroData/ReservoirLevel/"+z+"/" + str(i) + "_HU_SIN.csv"  
        print(filename)
        df1.to_csv(filename)
    
    

    


    
    


    
  