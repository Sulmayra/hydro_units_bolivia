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


for i in range(1980,2016):
    hydro_year = '../HydroData/ScaledInflows/##/' + str(i) + '.csv'
    hydro_year_HROR = '../AvailabilityFactors/##/' + str(i) + '.csv'
    # scenario_name =  str(i)

    # Load run specific inputs
    config['ReservoirScaledInflows'] = hydro_year
    config['RenewablesAF'] = hydro_year_HROR
    config['SimulationDirectory']  = config['SimulationDirectory']+ '/' + str(i)
    sim_folder = config['SimulationDirectory'] 

    # Build simulation
    SimData = ds.build_simulation(config) 
   
    # Solve using GAMS:
    r = ds.solve_GAMS(sim_folder, config['GAMS_folder'])




