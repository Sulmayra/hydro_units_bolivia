# -*- coding: utf-8 -*-
"""
Eexample file showing how to access the Dispa-SET api to read a configuration file, 
and build batch runs in GAMS

@author: K Kavvadias
"""

from itertools import product
import pickle
import logging
import pandas as pd

import numpy as np
# Import Dispa-SET
import dispaset as ds


# Load the configuration file
config = ds.load_config_excel('../ConfigFiles/ConfigBO_2020.xlsx')


for i in range(2020,2021):
    hydro_year = '../HydroData/ScaledInflows/##/' +str(i) + '.csv'
    # scenario_name =  str(i)

    # Load run specific inputs
    # config['ReservoirScaledInflows'] = hydro_year
    sim_folder = config['SimulationDirectory'] + str(i)

    # # Build simulation
    SimData = ds.build_simulation(config) 
    new_profiles = mid_term_scheduling(config, mts_plot=mts_plot, TimeStep=MTSTimeStep)
    # # Solve using GAMS:
    r = ds.solve_GAMS(sim_folder, config['GAMS_folder'])


data = pd.DataFrame(index = range(2020,2021))
for i in range(2020,2021):
    sim_folder = config['SimulationDirectory'] +  str(i)
    # sim_folder = config['SimulationDirectory'] + '/' + str(i)

    # Load inputs and results to memory
    inputs, results = ds.get_sim_results(path=sim_folder, cache=True)
    
    
    # Save inputs and results to a file
    # Analyse the results for each country and provide quantitative indicators:
    r = ds.get_result_analysis(inputs,results)
    data.loc[i,'TotalLoad'] = r['TotalLoad']
    data.loc[i,'Curtailment'] = r['Curtailment']
data.to_excel('data.xlsx')

