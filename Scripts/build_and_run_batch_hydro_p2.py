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


data = pd.DataFrame(index = range(1980,1981))
for i in range(1980,1981):
    sim_folder = config['SimulationDirectory'] + '/' + str(i)

    # Load inputs and results to memory
    inputs, results = ds.get_sim_results(path=sim_folder, cache=True)
    
    
    # Save inputs and results to a file
    # Analyse the results for each country and provide quantitative indicators:
    r = ds.get_result_analysis(inputs,results)
    data.loc[i,'TotalLoad'] = r['TotalLoad']
    data.loc[i,'Curtailment'] = r['Curtailment']
data.to_excel('data.xlsx')

