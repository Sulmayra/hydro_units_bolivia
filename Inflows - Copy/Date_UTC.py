# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 13:40:36 2021

@author: VLIR_energy
"""

import pandas as pd

for z in ['SU']:
    df0 = pd.read_csv("Inflows_"+z+".csv", index_col=0)
    df1 = pd.date_range(start="1979-12-31 00:00", end="2015-12-31 23:55",freq="D")
    # df2 = pd.to_datetime(df1['TIMESTAMP'])
    # df2.tz_localize('UTC')
    
    new_index = df1.tz_localize(tz='UTC')
    df5 = df0.reindex(index=new_index)
    df5.to_csv("fff.csv")