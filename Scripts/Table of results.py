# -*- coding: utf-8 -*-
"""

@author: 
"""

# Import Dispa-SET
import dispaset as ds
import pandas as pd
import numpy as np
import pickle

# Set the simulation date range
start_year =  1981
end_year = 2016

# Path of the scenarios
Scenario = ["Baseline/bolivia_base_2020",
            "Scenario_1/Demand_1.5_2020",  
            "Scenario_2/Demand_2_2020"]

# Load the configuration file
config = ds.load_config_excel('../ConfigFiles/ConfigTest.xlsx')
config['SimulationDirectory']  = config['SimulationDirectory']+'/'+ Scenario[0]

data= pd.DataFrame(index = range(start_year,end_year))

# Import Name Hydro Units
hp = pd.read_csv('Hydro_unit.csv')
hp = hp.squeeze()


inputs = {}
results = {}
generation = {}
cost = {}
power = {}
for i in range(start_year, end_year):
    config['SimulationDirectory'] = config['SimulationDirectory'][:-4] + str(i)   

    # Load the simulation results:
    inputs[i], results[i] = ds.get_sim_results(config['SimulationDirectory'], cache=False)
    r = ds.get_result_analysis(inputs[i], results[i])
    data.loc[i,'Average electricity cost EUR/MWh']= r['Cost_kwh'] 
    data.loc[i,'Total Generation WAT MW']= r['UnitData']['Generation [TWh]'][hp].sum()
    data.loc[i,'Total Load Shedding MWh'] = r['ShedLoad']*1E6   
    data.loc[i,'Total Curtailed RES TWh']= r['Curtailment']
    data.loc[i,'Total shifted load TWh']= r['ShiftedLoad']
    data.loc[i,'Total hours of congestion (h)']= sum(r['Congestion'].values())    
    data.loc[i,'Peak Load MW']= r['PeakLoad']
    data.loc[i,'Net Importations TWh']= r['NetImports']
    data.loc[i,'Total CO2 emissions (t CO2)']= r['UnitData']['CO2 [t]'].sum()/1E6
    generation[i]= ds.plot_energy_zone_fuel(inputs[i], results[i], ds.get_indicators_powerplant(inputs[i], results[i])) 
    data.to_csv('data.csv')
    
    
####### Generation reliability #######
Reliability= pd.DataFrame()
for i in range(start_year, end_year): 
    Reliability.loc[i,'EENS'] =  results[i]['OutputShedLoad'].sum(axis=1).sum()
    +results[i]['LostLoad_MaxPower'].sum(axis=1).sum()
    + results[i]['LostLoad_MinPower'].sum(axis=1).sum() 
    Reliability.loc[i,'LEOP'] =  Reliability.loc[i,'EENS']*1000/ r['TotalLoad']
    df =  results[i]['OutputShedLoad']
    Reliability.loc[i,'LOLE'] =  df[df != 0].count().sum()
    Reliability.loc[i,'LOLP'] =   Reliability.loc[i,'LOLE']*100/(results[i]['OutputShedLoad']['CE'].count()*4)
    Reliability.loc[i,'XLOL'] =  Reliability.loc[i,'EENS']/Reliability.loc[i,'LOLE']
Reliability.to_csv('Reliability.csv')

