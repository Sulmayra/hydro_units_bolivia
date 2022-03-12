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



"*************************comprando evolucion de energia hidroelectrica ******************************"
data = pd.read_csv("./Figure_Paper/Reservoir_Level/Zongo_Zongo.csv", index_col=0)
df=pd.DataFrame(data)
data = pd.read_csv("./Figure_Paper/Reservoir_Level/Zongo_SantaRosa.csv", index_col=0)
df1=pd.DataFrame(data)
data = pd.read_csv("./Figure_Paper/Reservoir_Level/Zongo_Tiquimani.csv", index_col=0)
df2=pd.DataFrame(data)
data = pd.read_csv("./Figure_Paper/Reservoir_Level/Miguilla.csv", index_col=0)
df3=pd.DataFrame(data)
data = pd.read_csv("./Figure_Paper/Reservoir_Level/Angostura.csv", index_col=0)
df4=pd.DataFrame(data)
data = pd.read_csv("./Figure_Paper/Reservoir_Level/Corani.csv", index_col=0)
df5=pd.DataFrame(data)
data = pd.read_csv("./Figure_Paper/Reservoir_Level/Misicuni.csv", index_col=0)
df6=pd.DataFrame(data)
data = pd.read_csv("./Figure_Paper/Reservoir_Level/San_Jacinto.csv", index_col=0)
df7=pd.DataFrame(data)

# colores = {'#DAA520','#FFD700','#FF8C00','#FFA07A','#E9967A','#F08080','#CD5C5C','#FF7F50','#FF0000','#000000'}
colores = ['#FFE194', '#B4B897','#368B85','#464660','#4A47A3','#709FB0','#0F52BA','#413C69','#B42B51','#000000']

# ax1=df.plot(kind="line", figsize=(5, 2.5),color=colores,fontsize=10,
#             stacked=False, alpha=2, legend='reverse', title='Zongo - Zongo')   # title='Installed capacity per zone (the horizontal lines indicate the peak demand)'
# plt.setp(ax1.get_xticklabels(), rotation=0, ha='left')
# plt.legend(bbox_to_anchor=(1, 1.05), loc='upper left')

ax1=df1.plot(kind="line", figsize=(5, 2.5),color=colores,fontsize=10,
            stacked=False, alpha=2, title='Zongo - Santa Rosa')   # title='Installed capacity per zone (the horizontal lines indicate the peak demand)'
plt.setp(ax1.get_xticklabels(), rotation=0, ha='left')
plt.legend(bbox_to_anchor=(1, 1.05), loc='upper left')


# ax1=df2.plot(kind="line", figsize=(5, 2.5),color=colores,fontsize=8,
#             stacked=False, alpha=2, legend='reverse', title='Zongo - Tiquimani')   # title='Installed capacity per zone (the horizontal lines indicate the peak demand)'
# plt.setp(ax1.get_xticklabels(), rotation=0, ha='left')
# plt.legend(bbox_to_anchor=(1, 1.05), loc='upper left')

ax1=df3.plot(kind="line", figsize=(5, 2.5),color=colores,fontsize=8,
            stacked=False, alpha=2, title='Miguilla')   # title='Installed capacity per zone (the horizontal lines indicate the peak demand)'
plt.setp(ax1.get_xticklabels(), rotation=0, ha='left')
plt.legend(bbox_to_anchor=(1, 1.05), loc='upper left')


# ax1=df4.plot(kind="line", figsize=(5, 2.5),color=colores,fontsize=8,
#             stacked=False, alpha=0.8, legend='reverse', title='Angostura')   # title='Installed capacity per zone (the horizontal lines indicate the peak demand)'
# plt.setp(ax1.get_xticklabels(), rotation=0, ha='left')
# plt.legend(bbox_to_anchor=(1, 1.05), loc='upper left')

ax1=df5.plot(kind="line", figsize=(4.5, 2.5),color=colores,fontsize=8,
            stacked=False, alpha=2, title='Corani')   # title='Installed capacity per zone (the horizontal lines indicate the peak demand)'
plt.setp(ax1.get_xticklabels(), rotation=0, ha='left')
plt.legend(bbox_to_anchor=(1, 1.05), loc='upper left')


# ax1=df6.plot(kind="line", figsize=(5, 2.5),color=colores,fontsize=8,
#             stacked=False, alpha=0.8, legend='reverse', title='Misicuni')   # title='Installed capacity per zone (the horizontal lines indicate the peak demand)'
# plt.setp(ax1.get_xticklabels(), rotation=0, ha='left')
# plt.legend(bbox_to_anchor=(1, 1.05), loc='upper left')

ax1=df7.plot(kind="line", figsize=(5, 2.5),color=colores,fontsize=8,
            stacked=False, alpha=2, title='San Jacinto')   # title='Installed capacity per zone (the horizontal lines indicate the peak demand)'
plt.setp(ax1.get_xticklabels(), rotation=0, ha='left')
plt.legend(bbox_to_anchor=(1, 1.05), loc='upper left')











# plt.figure(1, figsize=(12, 20)) # Crear la primera mesa de trabajo (figura)
# plt.subplot(421) # La primera imagen de la primera mesa de trabajo
# plt.plot(df)
# plt.legend(['1980','1985','1990','1995','2000','2005','2010','2015','2020','Observed'])
# # plt.xlabel('Time Step [Day]')
# # plt.ylabel('Reservoir Level')
# plt.title('Zongo system_Zongo',loc='center')
# plt.subplot(422) # La segunda subimagen de la segunda mesa de trabajo
# plt.plot(df1)
# plt.legend(['1980','1985','1990','1995','2000','2005','2010','2015','2020','Observed'])
# # plt.xlabel('Time Step [Day]')
# # plt.ylabel('Reservoir Level')
# plt.title('Zongo system_Santa Rosa')
# plt.subplot(423) # La segunda subimagen de la segunda mesa de trabajo
# plt.plot(df2)
# plt.legend(['1980','1985','1990','1995','2000','2005','2010','2015','2020','Observed'])
# # plt.xlabel('Time Step [Day]')
# # plt.ylabel('Reservoir Level')
# plt.title('Zongo system_Tiquimani')
# plt.subplot(424) # La segunda subimagen de la segunda mesa de trabajo
# plt.plot(df3)
# plt.legend(['1980','1985','1990','1995','2000','2005','2010','2015','2020','Observed'])
# # plt.xlabel('Time Step [Day]')
# # plt.ylabel('Reservoir Level')
# plt.title('Miguilla')
# plt.subplot(425) # La segunda subimagen de la segunda mesa de trabajo
# plt.plot(df4)
# plt.legend(['1980','1985','1990','1995','2000','2005','2010','2015','2020','Observed'])
# # plt.xlabel('Time Step [Day]')
# # plt.ylabel('Reservoir Level')
# plt.title('Angostura')
# plt.subplot(426) # La segunda subimagen de la segunda mesa de trabajo
# plt.plot(df5)
# plt.legend(['1980','1985','1990','1995','2000','2005','2010','2015','2020','Observed'])
# # plt.xlabel('Time Step [Day]')
# # plt.ylabel('Reservoir Level')
# plt.title('Cornai')
# plt.subplot(427) # La segunda subimagen de la segunda mesa de trabajo
# plt.plot(df6)
# plt.legend(['1980','1985','1990','1995','2000','2005','2010','2015','2020','Observed'])
# plt.xlabel('Time Step [Day]')
# plt.ylabel('Reservoir Level')
# plt.title('Misicuni')
# plt.subplot(428) # La segunda subimagen de la segunda mesa de trabajo
# plt.plot(df7)
# plt.legend(['1980','1985','1990','1995','2000','2005','2010','2015','2020','Observed'])
# plt.xlabel('Time Step [Day]')
# plt.ylabel('Reservoir Level')
# plt.title('San Jacinto')
# plt.show()

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