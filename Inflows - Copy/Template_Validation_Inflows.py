# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 16:38:20 2021

@author: VLIR_energy
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# from matplotlib.patches import Rectangle
# import matplotlib.colors as mcolors

"************************* caudales ******************************"
df = pd.read_csv("./Validation_Inflows/cuenca propia CORANI.csv", index_col=0)
colores = ['#F1E9E5', '#B4B897','#368B85','#464660','#B42B51','#4A47A3','#413C69','#709FB0','#A7C5EB']
df['Modificado'] = df['WEAP']*0.3
df1 = df.cumsum()
df.plot(kind="line",  figsize=(16, 5), stacked=False, alpha=0.8, legend='reverse', fontsize=12, title = 'Cuenca Propia CORANI' )
df1.plot(kind="line",  figsize=(16, 5), stacked=False, alpha=0.8, legend='reverse', fontsize=12, title = 'Cuenca Propia CORANI' )
plt.legend(bbox_to_anchor=(1, 1.0), loc='upper left')
# plt.xticks(rotation=0)
plt.xlabel('Date')
plt.ylabel('[m3/s]')

# List = ['VALLE DE ZONGO - HARCA','VALLE DE ZONGO - HUAJI','VALLE DE ZONGO - CHURURAQUI','VALLE DE ZONGO - CAHUA']
# for z in List:
#     df = pd.read_csv("./Validation_Inflows/"+z+".csv", index_col=0)
#     colores = ['#F1E9E5', '#B4B897','#368B85','#464660','#B42B51','#4A47A3','#413C69','#709FB0','#A7C5EB']
#     df['1980']= df['1980']
#     df.plot(kind="line", linestyle="dashed", marker="o", figsize=(16, 5), stacked=False, alpha=0.8, legend='reverse', fontsize=12, 
#             title = str(z) )
#     plt.legend(bbox_to_anchor=(1, 1.0), loc='upper left')
#     # plt.xticks(rotation=0)
#     plt.xlabel('Month')
#     plt.ylabel('[m3/s]')




'***************************************************************************'

# "************************* BASELINE ******************************"
# df1 = pd.read_csv("./Caudales/Corani_Caudales2.csv", index_col=0)
# colores = ['#F1E9E5', '#B4B897','#368B85','#464660','#B42B51','#4A47A3','#413C69','#709FB0','#A7C5EB']
# plt.plot(df1, linestyle='--', color='#2C2E43')
# plt.legend(bbox_to_anchor=(1, 1.0), loc='upper left')
# # plt.xticks(rotation=0)
# plt.xlabel('Month')
# plt.ylabel('[GWh]')



# "*************************Reservoir levels******************************"

# for z in ['Central','South','North']:
#     df = pd.read_csv("./Figure_Paper/StorageLevel_"+z+".csv", index_col=0)
#     ax=df.plot(kind="line",  figsize=(8, 4), stacked=False, alpha=0.8, legend='reverse', fontsize=9, 
#             title='Storage levels - Zone: ' + str(z) ) # title='Installed capacity per zone (the horizontal lines indicate the peak demand)'
#     plt.xlabel('Date')

"************************************************************************************"

"*************************INFLOWS _BSHB 2018******************************"

# for z in ['Central','South','North']:
#     df = pd.read_csv("./Figure_Paper/Inflows_"+z+".csv", index_col=0)
#     ax=df.plot(kind="line",  figsize=(16, 5), stacked=False, alpha=0.8, legend='reverse', fontsize=12, 
#             title='Inflows - Zone: ' + str(z) ) # title='Installed capacity per zone (the horizontal lines indicate the peak demand)'
#     plt.xlabel('Date')
#     plt.ylabel('Flow [m3/s]')

"************************************************************************************"

# "************************* BASELINE ******************************"
# hh = pd.read_csv("./Figure_Paper/CNDC_North.csv", index_col=0)
# ax=hh.plot(kind="line",  figsize=(7, 7), stacked=False, alpha=0.8, legend='reverse', fontsize=12, 
#             title='Inflows - Zone: North') # title='Installed capacity per zone (the horizontal lines indicate the peak demand)'
#     # plt.xticks([i for i in range()],labels=df.index) 
# plt.xlabel('Date')
# plt.ylabel('Flow [m3/s]')

# hh = pd.read_csv("./Figure_Paper/CNDC_Central.csv", index_col=0)
# ax=hh.plot(kind="line",  figsize=(7, 4), stacked=False, alpha=0.8, legend='reverse', fontsize=9, 
#             title='Inflows - Zone: Central') # title='Installed capacity per zone (the horizontal lines indicate the peak demand)'
#     # plt.xticks([i for i in range()],labels=df.index) 
# plt.xlabel('Date')
# plt.ylabel('Flow [m3/s]')

# hh = pd.read_csv("./Figure_Paper/CNDC_South.csv", index_col=0)
# ax=hh.plot(kind="line",  figsize=(7, 2), stacked=False, alpha=0.8, legend='reverse', fontsize=8, 
#             title='Inflows - Zone: South') # title='Installed capacity per zone (the horizontal lines indicate the peak demand)'
#     # plt.xticks([i for i in range()],labels=df.index) 
# plt.xlabel('Date')
# plt.ylabel('Flow [m3/s]')


"************************************************************************************"

# # ax1=df.plot(kind="line", figsize=(6, 3),color=colores,
# #             stacked=False, alpha=2, legend='reverse',title=' DAM - Corani')   # title='Installed capacity per zone (the horizontal lines indicate the peak demand)'
# # plt.setp(ax1.get_xticklabels(), rotation=0, ha='left')
# # # plt.xticks([i for i in range()],labels=df.index) 
# # plt.xlabel('Date[Day/Month]')
# # # plt.ylabel(' ')  

# colores = ['#DAA520','#FFD700','#FF8C00','#FFA07A','#E9967A','#F08080','#CD5C5C','#FF7F50','#FF0000','#000000']

# plt.figure(1, figsize=(12, 20)) # Crear la primera mesa de trabajo (figura)
# plt.subplot(421) # La primera imagen de la primera mesa de trabajo
# plt.plot(df)
# plt.legend(['1980','1985','1990','1995','2000','2005','2010','2015','2020','Observed'])


# "************************************************************************************"

"*************************comprando evolucion de energia hidroelectrica ******************************"
# data = pd.read_csv("Hydro_units.csv", index_col=0)
# df=pd.DataFrame(data)

# ax=df.plot(kind="bar",width = 0.8,  figsize=(12, 4),color=['#73C6B6','#1F618D'], stacked=False, alpha=0.8, legend='reverse',
#             title=' ')   # title='Installed capacity per zone (the horizontal lines indicate the peak demand)'
# plt.setp(ax.get_xticklabels(), rotation=90, ha='right')
# plt.xticks([i for i in range(23)],labels=df.index) 
# plt.xlabel('Y ear')
# plt.ylabel('Capacity [MW]')  

"************************************************************************************"



"*************************comprando CNDC VS MODELADO ******************************"
# data = pd.read_csv("GeneracionBruta_C2020.csv", index_col=0)
# df=pd.DataFrame(data)
# ax=df.plot(kind="line", linestyle="dashed", marker="o", figsize=(12, 4), stacked=False, alpha=0.8, legend='reverse',
#            title=' ')   # title='Installed capacity per zone (the horizontal lines indicate the peak demand)'
# plt.setp(ax.get_xticklabels(), rotation=90, ha='right')
# plt.xticks([i for i in range(27)],labels=df.index) 
# plt.xlabel('Central Name')
# plt.ylabel('Output Power [MWh]')  


"************************************************************************************"
# df = df.astype({"ENERO": 'str'})
# x=df['CENTRAL']
# y=df['CNDC']
# plt.plot(x, y)        #El gráfico
# plt.title('Pedidos de postres')      #El título
# plt.legend(['Traditional food', 'Western food'], loc=1)
# ax = plt.subplot()                   #Axis
# # ax.set_xticks(x_values)             #Eje x
# # ax.set_xticklabels(x_values)        #Etiquetas del eje x
# ax.set_xlabel('Petición de postre')  #Nombre del eje x
# ax.set_ylabel('Volumen de peticiones')  #Nombre del eje y
# df.plot(figsize=(12, 6), title='Storage levels')
# plt.draw()
# ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha='right')
#plt.xticks(range(len(count)), (year))
 
 




# def storage_levels(inputs, results):
#     """
#     Reads the DispaSET results and provides the difference between the minimum storage profile and the computed storage profile

#     :param inputs:      DispaSET inputs
#     :param results:     DispaSET results
#     """
#     isstorage = pd.Series(index=inputs['units'].index)
#     for u in isstorage.index:
#         isstorage[u] = inputs['units'].Technology[u] in commons['tech_storage']
#     sto_units = inputs['units'][isstorage]
#     results['OutputStorageLevel'].plot(figsize=(12, 6), title='Storage levels')
#     StorageError = ((inputs['param_df']['StorageProfile'] * sto_units.StorageCapacity).subtract(
#         results['OutputStorageLevel'], 'columns')).divide((sto_units.StorageCapacity), 'columns') * (-100)
#     StorageError = StorageError.dropna(1)
#     if not StorageError.empty:
#         ax = StorageError.plot(figsize=(12, 6),
#                                 title='Difference between the calculated storage Levels and the (imposed) minimum level')
#         ax.set_ylabel('%')

#     return True





# print(df.dtypes)
# fig= plt.tight_layout()
# fig = plt.figure(figsize=(10,7))
# plt.plot(df['CENTRAL'], df['CNDC'])
# df.set_dflabel('Output Power (GWh)')
# df.set_dflabel('Central Name')

# plt.show()

# df.plot(kind='scatter', x= str('CENTRALES HIDROELECTRICAS'),y=str('ENERO'))

# # plt.show()


"*************************VARIAS GRAFICAS EN UNA HOJA******************************"

# fig= plt.tight_layout()
# fig = plt.figure(figsize=(15,15))

# colores = ['blue','green','red','cyan','magenta','yellow','black','white']

# for i in range (1,7):
#     x= np.arange(0,16,2)
#     y=pow(x,np.random.randint(0,6))+np.random.randint(0,10)
#     ax=plt.subplot(2,3,i)
#     ax.plot(x,y,color=colores[i])
#     ax.set_xlabel('x')
#     ax.set_ylabel('y')
#     ax.set_title('Grafica'+str(i))
    
    
"***********************************************************************************"