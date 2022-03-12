# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 06:46:13 2021

@author: VLIR_energy
"""
import logging
import sys

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from ..misc.str_handler import clean_strings
from ..common import commons

 df1 = pd.read_csv("Inflows_"+z+".csv", index_col=0)

# def storage_levels(inputs, results):
#     """
#     Reads the DispaSET results and provides the difference between the minimum storage profile and the computed storage profile

#     :param inputs:      DispaSET inputs
#     :param results:     DispaSET results
    """
    # isstorage = pd.Series(index=inputs['units'].index)
    # for u in isstorage.index:
    #     isstorage[u] = inputs['units'].Technology[u] in commons['tech_storage']
    # sto_units = inputs['units'][isstorage]
    # results['OutputStorageLevel'].plot(figsize=(12, 6), title='Storage levels')
    # StorageError = ((inputs['param_df']['StorageProfile'] * sto_units.StorageCapacity).subtract(
    #     results['OutputStorageLevel'], 'columns')).divide((sto_units.StorageCapacity), 'columns') * (-100)
    # StorageError = StorageError.dropna(1)
    # if not StorageError.empty:
 ax = StorageError.plot(figsize=(12, 6),
        #                         title='Difference between the calculated storage Levels and the (imposed) minimum level')
        # ax.set_ylabel('%')