# -*- coding: utf-8 -*-
"""
Eexample file showing how to access the Dispa-SET api to read a configuration file, 
and build batch runs in GAMS

@author: K Kavvadias
"""

from itertools import product
import pickle
import logging

# Add the root folder of Dispa-SET to the path so that the library can be loaded:
import sys,os
sys.path.append(os.path.abspath('../../Dispa-SET'))

# Import Dispa-SET
import dispaset as ds

# Define path to save results. Each run will be a pickled tuple: (inputs, results)
path_to_save = r'./scenario_runs'

# Load the configuration file
config = ds.load_config_excel('../ConfigFiles/ConfigBO_2020.xlsx')
                             #'../ConfigFiles/ConfigCY.xlsx'
# Define your different input files as a list. The number of total runs will be the product of the length of the defined lists.
heat_demand_scen = ['../HydroData/ScaledInflows/##/2020.csv',
                    '../HydroData/ScaledInflows/##/2015.csv',
'../HydroData/ScaledInflows/##/2014.csv',
'../HydroData/ScaledInflows/##/2013.csv',
'../HydroData/ScaledInflows/##/2012.csv',
'../HydroData/ScaledInflows/##/2011.csv',
'../HydroData/ScaledInflows/##/2010.csv',
'../HydroData/ScaledInflows/##/2009.csv']
# '../HydroData/ScaledInflows/##/2008.csv',
# '../HydroData/ScaledInflows/##/2007.csv',
# '../HydroData/ScaledInflows/##/2006.csv',
# '../HydroData/ScaledInflows/##/2005.csv',
# '../HydroData/ScaledInflows/##/2004.csv',
# '../HydroData/ScaledInflows/##/2003.csv',
# '../HydroData/ScaledInflows/##/2002.csv',
# '../HydroData/ScaledInflows/##/2001.csv',
# '../HydroData/ScaledInflows/##/2000.csv',
# '../HydroData/ScaledInflows/##/1999.csv',
# '../HydroData/ScaledInflows/##/1998.csv',
# '../HydroData/ScaledInflows/##/1997.csv',
# '../HydroData/ScaledInflows/##/1996.csv',
# '../HydroData/ScaledInflows/##/1995.csv',
# '../HydroData/ScaledInflows/##/1994.csv',
# '../HydroData/ScaledInflows/##/1993.csv',
# '../HydroData/ScaledInflows/##/1992.csv',
# '../HydroData/ScaledInflows/##/1991.csv',
# '../HydroData/ScaledInflows/##/1990.csv',
# '../HydroData/ScaledInflows/##/1989.csv',
# '../HydroData/ScaledInflows/##/1988.csv',
# '../HydroData/ScaledInflows/##/1987.csv',
# '../HydroData/ScaledInflows/##/1986.csv',
# '../HydroData/ScaledInflows/##/1985.csv',
# '../HydroData/ScaledInflows/##/1984.csv',
# '../HydroData/ScaledInflows/##/1983.csv',
# '../HydroData/ScaledInflows/##/1982.csv',
# '../HydroData/ScaledInflows/##/1981.csv',
# '../HydroData/ScaledInflows/##/1980.csv'


power_scen = ['../PowerPlants/##/2020.csv']

cost_heat_slack_scen = [20.0, 51.0, 100.0]
res_mod_scen = [0.8,1.0,1.2]

all_combinations = list(product(heat_demand_scen, power_scen, cost_heat_slack_scen, res_mod_scen))
logging.info(str(len(all_combinations)) + ' runs will be made')  # 36 for this case

i = 0

for iheat, ipower, icost_heat, iresmod in all_combinations:
    i += 1
    scenario_name = "run_1_" + str(i)

    # Load run specific inputs
    config['HeatDemand'] = iheat
    config['PowerPlantData'] = ipower
    config['default']['CostHeatSlack'] = icost_heat
    config['modifiers']['Solar'] = config['modifiers']['wind'] = iresmod

    # Build simulation
    SimData = ds.build_simulation(config)
    # Solve using GAMS:
    r = ds.solve_GAMS(config['SimulationDirectory'], config['GAMS_folder'])

    # Load inputs and results to memory
    inputs, results = ds.get_sim_results(path=config['SimulationDirectory'], cache=True)
    # Save inputs and results to a file
    filename = os.path.join("../prueba/", scenario_name+".p")
    with open(filename, "wb") as f:
        pickle.dump((inputs, results), f, protocol=pickle.HIGHEST_PROTOCOL)
    logging.info('Saved {} to pickle file'.format(scenario_name))
