# -*- coding: utf-8 -*-
"""

@author: 
"""

from itertools import product
import pickle
import logging
import pandas as pd

import numpy as np
# Import Dispa-SET
import dispaset as ds

# Load the configuration file
config = ds.load_config_excel('../ConfigFiles/ConfigBO_2020_HU.xlsx')

data = pd.DataFrame(index = range(1980,2016))
for i in range(1980,2016):
    config['SimulationDirectory']  = config['SimulationDirectory']+ '/' + str(i)
    sim_folder = config['SimulationDirectory'] 

    # Load inputs and results to memory
    inputs, results = ds.get_sim_results(path=sim_folder, cache=True)
    
   
    # Save inputs and results to a file
    # Analyse the results for each country and provide quantitative indicators:
    r = ds.get_result_analysis(inputs,results)
    data.loc[i,'TotalLoad'] = r['TotalLoad']
    data.loc[i,'Curtailment'] = r['Curtailment']
data.to_excel('data.xlsx')

