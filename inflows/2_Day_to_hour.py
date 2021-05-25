# -*- coding: utf,-8 -*-
"""
Created on Tue May 11 14:59:35 2021

@author: VLIR_energy
"""

import pandas as pd

data = pd.read_excel("Inflows_NO.xlsx",index_col=0)

new_index = pd.date_range(start="01-01-1980 00:00", end="12-31-2015 23:55",freq="1h")

data_newindex = data.reindex(index=new_index)

data_fill= data_newindex.fillna(method="pad")

data_fill.to_csv("hr_Inflows.csv")
















