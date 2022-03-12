# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 15:51:26 2021

@author: VLIR_energy
"""

import pandas as pd

df0= pd.read_csv("copy.csv", index_col=0)  #usecols=(1,2,3,4)


for i in range(1985,1986):
    df = pd.read_csv("../AvailabilityFactors/CE/" + str(i) + ".csv", index_col=0)
    df1= pd.concat([df, df0], axis=1)
    filename ="../AvailabilityFactors/CE/" + str(i) + ".csv"
    print(filename)
    df1.to_csv(filename)
    # df1.index = pd.RangeIndex(len(df))
    
    

# df1 = pd.read_csv("Inflows_CE.csv", index_col=0)
# df2 = pd.read_csv("MainData_SIN.csv", index_col=0)


# df = df2.drop(df2[(df2['Technology']=='HROR') | (df2['ZONE'] !='CE')].index)
# df5= df.index.tolist()
# # df4= df1.drop(columns= df5,axis=0)
# df6 = df1.drop(df5, axis=1)
# invoices.drop(['invoice', 'client', 'units'], axis=1)