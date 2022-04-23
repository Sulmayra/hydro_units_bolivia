# -*- coding: utf-8 -*-
"""

@author: 
"""

# Import Dispa-SET
import dispaset as ds
import pandas as pd
import pickle

# Set the simulation date range
start_year = 1980
end_year = 1983

# Load the configuration file
config = ds.load_config_excel('../ConfigFiles/ConfigTest.xlsx')

inputs = {}
results = {}
for i in range(start_year, end_year):
    config['SimulationDirectory'] = config['SimulationDirectory'][:-4] + str(i)
    config['ReservoirScaledInflows'] = config['ReservoirScaledInflows'][:-8] + str(i) + '.csv'
    config['RenewablesAF'] = config['RenewablesAF'][:-8] + str(i) + '.csv'
    # Limit the simulation period (for testing purposes, comment the line to run the whole year)
    config['StartDate'] = (i, 1, 1, 0, 0, 0)
    config['StopDate'] = (i, 1, 7, 0, 0, 0)

    # Build the simulation environment:
    SimData = ds.build_simulation(config)

    # Solve using GAMS:
    _ = ds.solve_GAMS(config['SimulationDirectory'], config['GAMS_folder'])

    # Load the simulation results:
    inputs[i], results[i] = ds.get_sim_results(config['SimulationDirectory'], cache=False)

# Save inputs and results to a pickle file
with open('results.p', 'wb') as handle:
    pickle.dump(inputs, handle, protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(results, handle, protocol=pickle.HIGHEST_PROTOCOL)

# # Read results from previously saved pickle file
# with open('results.p', 'rb') as handle:
#     inputs = pickle.load(handle)
#     results = pickle.load(handle)
